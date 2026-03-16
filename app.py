"""
ByteShelf Main Application Entry Point
This is the root app.py that Vercel will detect and use
"""
import os
import sys
from pathlib import Path

# Add the backend directory to the path BEFORE any imports
backend_path = Path(__file__).parent / "All code" / "backend"
if str(backend_path) not in sys.path:
    sys.path.insert(0, str(backend_path))

# Now import the create_app function
from app import create_app

# Create the Flask app
app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    app.run(host='0.0.0.0', port=port, debug=debug)

