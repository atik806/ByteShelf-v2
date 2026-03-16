from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, send_from_directory, session
from flask_cors import CORS
import os
import json
from datetime import datetime
from werkzeug.utils import secure_filename
import uuid
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'admin-secret-key-change-in-production')

ADMIN_USERNAME = os.environ.get('ADMIN_USERNAME', 'admin')
ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', 'admin123')

SUPABASE_URL = os.environ.get('SUPABASE_URL')
SUPABASE_KEY = os.environ.get('SUPABASE_KEY')

if SUPABASE_URL and SUPABASE_KEY:
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
else:
    supabase = None

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'txt', 'doc', 'docx', 'ppt', 'pptx'}
MAX_CONTENT_LENGTH = 16 * 1024 * 1024

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

CORS(app)

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

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
        'users': [],
        'stats': {
            'total_books': 0,
            'total_students': 0,
            'total_categories': 0
        }
    }

def calculate_stats(data):
    """Calculate real stats from data"""
    try:
        if supabase:
            users_response = supabase.auth.admin.list_users()
            total_students = len(users_response.users) if users_response.users else 0
        else:
            total_students = len(data.get('users', []))
    except Exception as e:
        print(f"Error fetching users: {e}")
        total_students = len(data.get('users', []))
    
    return {
        'total_books': len(data['books']),
        'total_students': total_students,
        'total_categories': len(data['categories']),
        'featured_books': len([b for b in data['books'] if b.get('featured', False)])
    }

def save_data(data):
    """Save data to JSON file"""
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def is_admin_logged_in():
    """Check if admin is logged in"""
    return session.get('admin_logged_in') is True

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Admin login"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['admin_logged_in'] = True
            session['admin_user'] = {'username': username}
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials.', 'error')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    """Admin logout"""
    session.clear()
    flash('Logged out successfully.', 'success')
    return redirect(url_for('login'))

@app.route('/')
def dashboard():
    """Admin dashboard"""
    if not is_admin_logged_in():
        return redirect(url_for('login'))
    data = load_data()
    stats = calculate_stats(data)
    data['stats'] = stats
    return render_template('dashboard.html', data=data)

@app.route('/books')
def books():
    """Books management page"""
    if not is_admin_logged_in():
        return redirect(url_for('login'))
    data = load_data()
    return render_template('books.html', books=data['books'], categories=data['categories'])

@app.route('/books/add', methods=['GET', 'POST'])
def add_book():
    """Add new book"""
    if not is_admin_logged_in():
        return redirect(url_for('login'))
    if request.method == 'POST':
        data = load_data()
        
        file = request.files.get('file')
        filename = None
        if file and file.filename and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filename = f"{uuid.uuid4().hex[:8]}_{filename}"
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
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
    if not is_admin_logged_in():
        return redirect(url_for('login'))
    data = load_data()
    book = next((b for b in data['books'] if b['id'] == book_id), None)
    
    if not book:
        flash('Book not found!', 'error')
        return redirect(url_for('books'))
    
    if request.method == 'POST':
        file = request.files.get('file')
        filename = book.get('filename')
        if file and file.filename and allowed_file(file.filename):
            if book.get('filename'):
                old_path = os.path.join(app.config['UPLOAD_FOLDER'], book['filename'])
                if os.path.exists(old_path):
                    os.remove(old_path)
            
            filename = secure_filename(file.filename)
            filename = f"{uuid.uuid4().hex[:8]}_{filename}"
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        book['title'] = request.form['title']
        book['author'] = request.form['author']
        book['category'] = request.form['category']
        book['price'] = float(request.form['price'])
        book['pages'] = int(request.form['pages'])
        book['description'] = request.form['description']
        book['badge'] = request.form.get('badge', '')
        book['filename'] = filename
        book['featured'] = request.form.get('featured') == 'on'
        book['updated_at'] = datetime.now().isoformat()
        
        save_data(data)
        flash('Book updated successfully!', 'success')
        return redirect(url_for('books'))
    
    return render_template('edit_book.html', book=book, categories=data['categories'])

@app.route('/books/delete/<book_id>')
def delete_book(book_id):
    """Delete book"""
    if not is_admin_logged_in():
        return redirect(url_for('login'))
    data = load_data()
    book = next((b for b in data['books'] if b['id'] == book_id), None)
    
    if book:
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
    if not is_admin_logged_in():
        return redirect(url_for('login'))
    data = load_data()
    return render_template('categories.html', categories=data['categories'], data=data)

@app.route('/categories/add', methods=['POST'])
def add_category():
    """Add new category"""
    if not is_admin_logged_in():
        return redirect(url_for('login'))
    data = load_data()
    
    category = {
        'id': request.form['id'],
        'name': request.form['name'],
        'icon': request.form['icon'],
        'color': request.form['color']
    }
    
    data['categories'].append(category)
    data['stats']['total_categories'] = len(data['categories'])
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
    stats = calculate_stats(data)
    return jsonify(stats)

@app.route('/api/books')
def api_books():
    """API endpoint for all books"""
    data = load_data()
    return jsonify(data['books'])

@app.route('/api/books/<book_id>')
def api_book(book_id):
    """API endpoint for single book"""
    data = load_data()
    book = next((b for b in data['books'] if b['id'] == book_id), None)
    if book:
        return jsonify(book)
    return jsonify({'error': 'Book not found'}), 404

@app.route('/api/books/featured')
def api_featured_books():
    """API endpoint for featured books"""
    data = load_data()
    featured = [b for b in data['books'] if b.get('featured', False)]
    return jsonify(featured)

@app.route('/api/categories')
def api_categories():
    """API endpoint for categories"""
    data = load_data()
    return jsonify(data['categories'])

@app.route('/api/books/category/<category_id>')
def api_books_by_category(category_id):
    """API endpoint for books by category"""
    data = load_data()
    books = [b for b in data['books'] if b.get('category') == category_id]
    return jsonify(books)

@app.route('/api/search')
def api_search():
    """API endpoint for searching books"""
    query = request.args.get('q', '').lower()
    data = load_data()
    if query:
        books = [b for b in data['books'] 
                 if query in b.get('title', '').lower() 
                 or query in b.get('author', '').lower()]
        return jsonify(books)
    return jsonify(data['books'])

@app.route('/api/register-user', methods=['POST'])
def register_user():
    """API endpoint to register a new user"""
    try:
        user_data = request.json
        data = load_data()
        
        if 'users' not in data:
            data['users'] = []
        
        existing_user = next((u for u in data['users'] if u.get('email') == user_data.get('email')), None)
        
        if not existing_user:
            new_user = {
                'id': user_data.get('id', ''),
                'name': user_data.get('name', ''),
                'email': user_data.get('email', ''),
                'plan': user_data.get('plan', 'starter'),
                'created_at': datetime.now().isoformat()
            }
            data['users'].append(new_user)
            save_data(data)
            return jsonify({'success': True, 'total_users': len(data['users'])})
        
        return jsonify({'success': True, 'total_users': len(data['users']), 'message': 'User already exists'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/users/count')
def api_users_count():
    """API endpoint to get total users count"""
    data = load_data()
    return jsonify({'total_users': len(data.get('users', []))})

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
