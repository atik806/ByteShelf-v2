"""
WSGI entry point for Vercel deployment
Located in All code folder
"""
import os
import sys
from pathlib import Path

# Add backend to path
backend_path = Path(__file__).parent / "backend"
sys.path.insert(0, str(backend_path))

# Import and create app
from app import create_app

# Create the Flask app
app = create_app()

if __name__ == "__main__":
    app.run()
