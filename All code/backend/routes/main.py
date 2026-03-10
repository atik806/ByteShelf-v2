from flask import Blueprint, send_from_directory, jsonify
import os

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """Serve the main index page"""
    frontend_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '..', 'frontend')
    return send_from_directory(frontend_path, 'index.html')

@main_bp.route('/blog')
def blog():
    """Serve the blog page (no login required)"""
    frontend_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '..', 'frontend')
    return send_from_directory(frontend_path, 'blog.html')

@main_bp.route('/about')
def about():
    """Serve the about page"""
    frontend_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '..', 'frontend')
    return send_from_directory(frontend_path, 'about.html')

@main_bp.route('/favicon.ico')
def favicon():
    """Handle favicon requests"""
    return '', 204

@main_bp.route('/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy", 
        "message": "ByteShelf server is running",
        "service": "backend"
    })

@main_bp.route('/<path:filename>')
def static_files(filename):
    """Serve static files from the frontend directory"""
    try:
        frontend_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '..', 'frontend')
        return send_from_directory(frontend_path, filename)
    except FileNotFoundError:
        return "File not found", 404