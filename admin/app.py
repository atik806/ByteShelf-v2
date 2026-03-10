from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, send_from_directory
import os
import json
from datetime import datetime
from werkzeug.utils import secure_filename
import uuid

app = Flask(__name__)
app.secret_key = 'admin-secret-key-change-in-production'

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'txt', 'doc', 'docx', 'ppt', 'pptx'}
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

# Ensure upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Data storage (in production, use a proper database)
DATA_FILE = 'data.json'

def load_data():
    """Load data from JSON file"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {
        'books': [],
        'categories': [
            {'id': 'algorithms', 'name': 'Algorithms & DSA', 'icon': '⚡', 'color': 'default'},
            {'id': 'ml', 'name': 'AI & Machine Learning', 'icon': '🧠', 'color': 'purple'},
            {'id': 'security', 'name': 'Cybersecurity', 'icon': '🔒', 'color': 'red'},
            {'id': 'system', 'name': 'System Design', 'icon': '🌐', 'color': 'yellow'}
        ],
        'stats': {
            'total_books': 0,
            'total_students': 12000,
            'total_categories': 40
        }
    }

def save_data(data):
    """Save data to JSON file"""
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def dashboard():
    """Admin dashboard"""
    data = load_data()
    return render_template('dashboard.html', data=data)

@app.route('/books')
def books():
    """Books management page"""
    data = load_data()
    return render_template('books.html', books=data['books'], categories=data['categories'])

@app.route('/books/add', methods=['GET', 'POST'])
def add_book():
    """Add new book"""
    if request.method == 'POST':
        data = load_data()
        
        # Handle file upload
        file = request.files.get('file')
        filename = None
        if file and file.filename and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            # Add unique prefix to avoid conflicts
            filename = f"{uuid.uuid4().hex[:8]}_{filename}"
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        # Create book entry
        book = {
            'id': str(uuid.uuid4()),
            'title': request.form['title'],
            'author': request.form['author'],
            'category': request.form['category'],
            'price': float(request.form['price']),
            'pages': int(request.form['pages']),
            'description': request.form['description'],
            'badge': request.form.get('badge', ''),
            'filename': filename,
            'created_at': datetime.now().isoformat(),
            'featured': request.form.get('featured') == 'on'
        }
        
        data['books'].append(book)
        data['stats']['total_books'] = len(data['books'])
        save_data(data)
        
        flash('Book added successfully!', 'success')
        return redirect(url_for('books'))
    
    data = load_data()
    return render_template('add_book.html', categories=data['categories'])

@app.route('/books/edit/<book_id>', methods=['GET', 'POST'])
def edit_book(book_id):
    """Edit existing book"""
    data = load_data()
    book = next((b for b in data['books'] if b['id'] == book_id), None)
    
    if not book:
        flash('Book not found!', 'error')
        return redirect(url_for('books'))
    
    if request.method == 'POST':
        # Handle file upload
        file = request.files.get('file')
        if file and file.filename and allowed_file(file.filename):
            # Delete old file if exists
            if book.get('filename'):
                old_path = os.path.join(app.config['UPLOAD_FOLDER'], book['filename'])
                if os.path.exists(old_path):
                    os.remove(old_path)
            
            filename = secure_filename(file.filename)
            filename = f"{uuid.uuid4().hex[:8]}_{filename}"
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            book['filename'] = filename
        
        # Update book data
        book.update({
            'title': request.form['title'],
            'author': request.form['author'],
            'category': request.form['category'],
            'price': float(request.form['price']),
            'pages': int(request.form['pages']),
            'description': request.form['description'],
            'badge': request.form.get('badge', ''),
            'featured': request.form.get('featured') == 'on',
            'updated_at': datetime.now().isoformat()
        })
        
        save_data(data)
        flash('Book updated successfully!', 'success')
        return redirect(url_for('books'))
    
    return render_template('edit_book.html', book=book, categories=data['categories'])

@app.route('/books/delete/<book_id>')
def delete_book(book_id):
    """Delete book"""
    data = load_data()
    book = next((b for b in data['books'] if b['id'] == book_id), None)
    
    if book:
        # Delete file if exists
        if book.get('filename'):
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], book['filename'])
            if os.path.exists(file_path):
                os.remove(file_path)
        
        data['books'] = [b for b in data['books'] if b['id'] != book_id]
        data['stats']['total_books'] = len(data['books'])
        save_data(data)
        flash('Book deleted successfully!', 'success')
    else:
        flash('Book not found!', 'error')
    
    return redirect(url_for('books'))

@app.route('/categories')
def categories():
    """Categories management page"""
    data = load_data()
    return render_template('categories.html', categories=data['categories'], data=data)

@app.route('/categories/add', methods=['POST'])
def add_category():
    """Add new category"""
    data = load_data()
    
    category = {
        'id': request.form['id'],
        'name': request.form['name'],
        'icon': request.form['icon'],
        'color': request.form['color']
    }
    
    data['categories'].append(category)
    save_data(data)
    
    flash('Category added successfully!', 'success')
    return redirect(url_for('categories'))

@app.route('/upload/<filename>')
def uploaded_file(filename):
    """Serve uploaded files"""
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/api/stats')
def api_stats():
    """API endpoint for statistics"""
    data = load_data()
    return jsonify(data['stats'])

@app.route('/api/books')
def api_books():
    """API endpoint for books"""
    data = load_data()
    return jsonify(data['books'])

@app.route('/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy", 
        "message": "ByteShelf Admin Panel is running",
        "service": "admin"
    })

if __name__ == '__main__':
    print("🔧 Starting ByteShelf Admin Panel...")
    print("📊 Admin panel will be available at: http://localhost:5001")
    print("💡 Press Ctrl+C to stop the server")
    app.run(debug=True, host='0.0.0.0', port=5001)