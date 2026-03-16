"""
Notes API Routes
Handles note creation, retrieval, update, and deletion for authenticated users
Stores data in Supabase database
"""
from flask import Blueprint, request, jsonify
from datetime import datetime
import os
from supabase import create_client, Client
import uuid

notes_bp = Blueprint('notes', __name__, url_prefix='/api/notes')

# Initialize Supabase client
SUPABASE_URL = os.environ.get('SUPABASE_URL') or os.environ.get('PROJECT_URL')
SUPABASE_KEY = os.environ.get('SUPABASE_KEY') or os.environ.get('PROJECT_KEY')

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("SUPABASE_URL and SUPABASE_KEY environment variables are required")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def get_user_id():
    """Get user ID from request headers"""
    return request.headers.get('X-User-ID', 'anonymous')

@notes_bp.route('/', methods=['GET'])
def get_notes():
    """Get all notes for the current user"""
    user_id = get_user_id()
    
    try:
        response = supabase.table('notes').select('*').eq('user_id', user_id).execute()
        notes = response.data if response.data else []
        
        return jsonify({
            'success': True,
            'notes': notes,
            'count': len(notes)
        })
    except Exception as e:
        print(f"Error fetching notes: {e}")
        return jsonify({'error': f'Failed to fetch notes: {str(e)}'}), 500

@notes_bp.route('/<note_id>', methods=['GET'])
def get_note(note_id):
    """Get a specific note"""
    user_id = get_user_id()
    
    try:
        response = supabase.table('notes').select('*').eq('id', note_id).eq('user_id', user_id).execute()
        
        if not response.data:
            return jsonify({'error': 'Note not found'}), 404
        
        return jsonify({
            'success': True,
            'note': response.data[0]
        })
    except Exception as e:
        print(f"Error fetching note: {e}")
        return jsonify({'error': f'Failed to fetch note: {str(e)}'}), 500

@notes_bp.route('/', methods=['POST'])
def create_note():
    """Create a new note"""
    user_id = get_user_id()
    data = request.json
    
    if not data or 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400
    
    try:
        new_note = {
            'id': str(uuid.uuid4()),
            'user_id': user_id,
            'title': data.get('title', 'Untitled'),
            'content': data.get('content', ''),
            'category': data.get('category', 'general'),
            'color': data.get('color', '#FFE5B4'),
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat(),
            'pinned': False,
            'tags': data.get('tags', [])
        }
        
        print(f"Attempting to create note for user: {user_id}")
        print(f"Supabase URL: {SUPABASE_URL}")
        print(f"API Key present: {bool(SUPABASE_KEY)}")
        
        response = supabase.table('notes').insert(new_note).execute()
        
        return jsonify({
            'success': True,
            'note': response.data[0] if response.data else new_note
        }), 201
    except Exception as e:
        print(f"Error creating note: {e}")
        print(f"Error type: {type(e)}")
        return jsonify({'error': f'Failed to create note: {str(e)}'}), 500

@notes_bp.route('/<note_id>', methods=['PUT'])
def update_note(note_id):
    """Update a note"""
    user_id = get_user_id()
    data = request.json
    
    try:
        # Verify note belongs to user
        response = supabase.table('notes').select('*').eq('id', note_id).eq('user_id', user_id).execute()
        
        if not response.data:
            return jsonify({'error': 'Note not found'}), 404
        
        # Prepare update data
        update_data = {}
        if 'title' in data:
            update_data['title'] = data['title']
        if 'content' in data:
            update_data['content'] = data['content']
        if 'category' in data:
            update_data['category'] = data['category']
        if 'color' in data:
            update_data['color'] = data['color']
        if 'pinned' in data:
            update_data['pinned'] = data['pinned']
        if 'tags' in data:
            update_data['tags'] = data['tags']
        
        update_data['updated_at'] = datetime.now().isoformat()
        
        response = supabase.table('notes').update(update_data).eq('id', note_id).eq('user_id', user_id).execute()
        
        return jsonify({
            'success': True,
            'note': response.data[0] if response.data else update_data
        })
    except Exception as e:
        print(f"Error updating note: {e}")
        return jsonify({'error': f'Failed to update note: {str(e)}'}), 500

@notes_bp.route('/<note_id>', methods=['DELETE'])
def delete_note(note_id):
    """Delete a note"""
    user_id = get_user_id()
    
    try:
        # Verify note belongs to user
        response = supabase.table('notes').select('*').eq('id', note_id).eq('user_id', user_id).execute()
        
        if not response.data:
            return jsonify({'error': 'Note not found'}), 404
        
        supabase.table('notes').delete().eq('id', note_id).eq('user_id', user_id).execute()
        
        return jsonify({
            'success': True,
            'message': 'Note deleted'
        })
    except Exception as e:
        print(f"Error deleting note: {e}")
        return jsonify({'error': f'Failed to delete note: {str(e)}'}), 500

@notes_bp.route('/search', methods=['GET'])
def search_notes():
    """Search notes by title or content"""
    user_id = get_user_id()
    query = request.args.get('q', '').lower()
    
    try:
        response = supabase.table('notes').select('*').eq('user_id', user_id).execute()
        user_notes = response.data if response.data else []
        
        results = [
            n for n in user_notes
            if query in n['title'].lower() or query in n['content'].lower()
        ]
        
        return jsonify({
            'success': True,
            'results': results,
            'count': len(results)
        })
    except Exception as e:
        print(f"Error searching notes: {e}")
        return jsonify({'error': f'Failed to search notes: {str(e)}'}), 500

@notes_bp.route('/category/<category>', methods=['GET'])
def get_notes_by_category(category):
    """Get notes by category"""
    user_id = get_user_id()
    
    try:
        response = supabase.table('notes').select('*').eq('user_id', user_id).eq('category', category).execute()
        category_notes = response.data if response.data else []
        
        return jsonify({
            'success': True,
            'notes': category_notes,
            'count': len(category_notes)
        })
    except Exception as e:
        print(f"Error fetching notes by category: {e}")
        return jsonify({'error': f'Failed to fetch notes: {str(e)}'}), 500

@notes_bp.route('/pinned', methods=['GET'])
def get_pinned_notes():
    """Get pinned notes"""
    user_id = get_user_id()
    
    try:
        response = supabase.table('notes').select('*').eq('user_id', user_id).eq('pinned', True).execute()
        pinned = response.data if response.data else []
        
        return jsonify({
            'success': True,
            'notes': pinned,
            'count': len(pinned)
        })
    except Exception as e:
        print(f"Error fetching pinned notes: {e}")
        return jsonify({'error': f'Failed to fetch pinned notes: {str(e)}'}), 500

@notes_bp.route('/stats', methods=['GET'])
def get_notes_stats():
    """Get notes statistics"""
    user_id = get_user_id()
    
    try:
        response = supabase.table('notes').select('*').eq('user_id', user_id).execute()
        user_notes = response.data if response.data else []
        
        categories = {}
        for note in user_notes:
            cat = note.get('category', 'general')
            categories[cat] = categories.get(cat, 0) + 1
        
        return jsonify({
            'success': True,
            'total_notes': len(user_notes),
            'pinned_notes': len([n for n in user_notes if n.get('pinned', False)]),
            'categories': categories
        })
    except Exception as e:
        print(f"Error fetching notes stats: {e}")
        return jsonify({'error': f'Failed to fetch stats: {str(e)}'}), 500
