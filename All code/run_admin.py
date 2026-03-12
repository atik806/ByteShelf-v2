#!/usr/bin/env python3
"""
ByteShelf Admin Panel Runner

This script provides an easy way to run the ByteShelf admin panel
from the project root directory.
"""

import os
import sys
from pathlib import Path

def main():
    # Get the directory where this script is located
    script_dir = Path(__file__).parent.absolute()
    
    # Look for admin directory - check both current level and parent level
    admin_dir = None
    
    # Check if admin is in current directory
    if (script_dir / 'admin').exists():
        admin_dir = script_dir / 'admin'
    # Check if admin is in parent directory
    elif (script_dir.parent / 'admin').exists():
        admin_dir = script_dir.parent / 'admin'
    
    if not admin_dir:
        print("❌ Admin directory not found!")
        print(f"Searched in: {script_dir} and {script_dir.parent}")
        return
    
    # Add admin directory to Python path
    sys.path.insert(0, str(admin_dir))
    
    # Change to admin directory
    original_cwd = os.getcwd()
    os.chdir(admin_dir)
    
    try:
        # Import and run the Flask app
        from app import app
        
        print("🔧 Starting ByteShelf Admin Panel...")
        print("📊 Admin panel will be available at:")
        print("   - http://localhost:5001")
        print("   - http://127.0.0.1:5001")
        print("💡 Press Ctrl+C to stop the server")
        print("🌐 Main website should be running at: http://localhost:5000")
        print(f"📁 Admin directory: {admin_dir}")
        print()
        
        app.run(debug=True, host='0.0.0.0', port=5001)
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("Make sure dependencies are installed in the admin directory.")
        print(f"Try: cd {admin_dir} && pip install -r requirements.txt")
    except Exception as e:
        print(f"❌ Error starting admin server: {e}")
    finally:
        # Restore original working directory
        os.chdir(original_cwd)

if __name__ == '__main__':
    main()