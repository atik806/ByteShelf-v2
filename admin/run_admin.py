#!/usr/bin/env python3
"""
ByteShelf Admin Panel Runner

This script runs the ByteShelf admin panel from within the admin directory.
"""

import os
import sys
from pathlib import Path

def main():
    # Get the directory where this script is located (admin directory)
    script_dir = Path(__file__).parent.absolute()
    
    # Add current directory to Python path
    sys.path.insert(0, str(script_dir))
    
    # Change to admin directory (we're already here)
    original_cwd = os.getcwd()
    os.chdir(script_dir)
    
    try:
        # Import and run the Flask app
        from app import app
        
        print("🔧 Starting ByteShelf Admin Panel...")
        print("📊 Admin panel will be available at:")
        print("   - http://localhost:5001")
        print("   - http://127.0.0.1:5001")
        print("💡 Press Ctrl+C to stop the server")
        print("🌐 Main website should be running at: http://localhost:5000")
        print()
        
        app.run(debug=True, host='0.0.0.0', port=5001)
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("Make sure you're in the admin directory and dependencies are installed.")
        print("Try: pip install -r requirements.txt")
    except Exception as e:
        print(f"❌ Error starting admin server: {e}")
    finally:
        # Restore original working directory
        os.chdir(original_cwd)

if __name__ == '__main__':
    main()