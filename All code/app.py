"""
ByteShelf Main Application
Combined Frontend and Backend Flask Application
"""
import os
import sys
from pathlib import Path
from flask import Flask, send_from_directory
from flask_cors import CORS
from dotenv import load_dotenv

# Load environment variables from .env file
env_path = Path(__file__).parent / '.env'
load_dotenv(env_path)

# Add backend to path
backend_path = Path(__file__).parent / "backend"
sys.path.insert(0, str(backend_path))

# Import backend routes
from routes.main import main_bp
from routes.notes import notes_bp
from config import config

def create_app(config_name=None):
    """Application factory pattern"""
    if config_name is None:
        config_name = os.environ.get('FLASK_ENV', 'default')
    
    app = Flask(__name__, static_folder='frontend', static_url_path='')
    app.config.from_object(config[config_name])
    
    # Enable CORS
    CORS(app)
    
    # Register blueprints - notes first so /api/ routes take precedence
    app.register_blueprint(notes_bp)
    app.register_blueprint(main_bp)
    
    # Serve frontend static files
    frontend_path = Path(__file__).parent / 'frontend'
    
    @app.route('/')
    def index():
        """Serve main index page"""
        return send_from_directory(frontend_path, 'index.html')
    
    @app.route('/<path:filename>')
    def serve_static(filename):
        """Serve static files from frontend"""
        # Don't serve /api/ routes as static files
        if filename.startswith('api/'):
            return "Not found", 404
        
        try:
            return send_from_directory(frontend_path, filename)
        except FileNotFoundError:
            return "File not found", 404
    
    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        """Handle 404 errors"""
        return "Page not found", 404

    @app.errorhandler(500)
    def internal_error(error):
        """Handle 500 errors"""
        return "Internal server error", 500
    
    return app

# Create app instance for WSGI servers
app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    app.run(
        host='0.0.0.0',
        port=port,
        debug=debug
    )
