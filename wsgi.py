"""
WSGI entry point for Vercel deployment
"""
import os
import sys
from pathlib import Path

# Add the backend directory to the path
backend_path = Path(__file__).parent / "All code" / "backend"
sys.path.insert(0, str(backend_path))

# Now import the create_app function
from app import create_app

# Create the Flask app
app = create_app()

if __name__ == "__main__":
    app.run()
