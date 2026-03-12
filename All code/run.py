#!/usr/bin/env python3
"""
ByteShelf Development Server Runner

This script provides an easy way to run the ByteShelf Flask server
from the project root directory.
"""

import os
import sys
from pathlib import Path

def main():
    # Get the directory where this script is located
    script_dir = Path(__file__).parent.absolute()
    backend_dir = script_dir / 'backend'
    
    # Check if backend directory exists
    if not backend_dir.exists():
        print("❌ Backend directory not found!")
        print(f"Expected: {backend_dir}")
        return
    
    # Add backend directory to Python path
    sys.path.insert(0, str(backend_dir))
    
    # Change to backend directory for relative imports
    original_cwd = os.getcwd()
    os.chdir(backend_dir)
    
    try:
        # Import and run the Flask app
        from app import create_app
        
        app = create_app()
        print("🚀 Starting ByteShelf Flask Server...")
        print("📖 Website will be available at:")
        print("   - http://localhost:5000")
        print("   - http://127.0.0.1:5000")
        print("💡 Press Ctrl+C to stop the server")
        print(f"📁 Serving frontend from: {script_dir}/frontend/")
        print()
        
        app.run(
            debug=app.config['DEBUG'],
            host=app.config['HOST'],
            port=app.config['PORT']
        )
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("Make sure you're in the correct directory and dependencies are installed.")
    except Exception as e:
        print(f"❌ Error starting server: {e}")
    finally:
        # Restore original working directory
        os.chdir(original_cwd)

if __name__ == '__main__':
    main()