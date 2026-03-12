from flask import Flask
from routes.main import main_bp
from config import config
import os

def create_app(config_name=None):
    """Application factory pattern"""
    if config_name is None:
        config_name = os.environ.get('FLASK_ENV', 'default')
    
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Register blueprints
    app.register_blueprint(main_bp)
    
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

if __name__ == '__main__':
    app = create_app()
    print("🚀 Starting ByteShelf Flask Server...")
    print("📖 Website will be available at: http://localhost:5000")
    print("💡 Press Ctrl+C to stop the server")
    app.run(
        debug=app.config['DEBUG'],
        host=app.config['HOST'],
        port=app.config['PORT']
    )