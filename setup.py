#!/usr/bin/env python3
"""
ByteShelf Development Setup Script

This script helps set up the development environment for ByteShelf.
"""

import os
import sys
import subprocess
import json
from pathlib import Path

class SetupManager:
    def __init__(self):
        self.root_dir = Path(__file__).parent
        self.backend_dir = self.root_dir / "All code" / "backend"
        self.admin_dir = self.root_dir / "admin"
    
    def check_python_version(self):
        """Check if Python version is compatible"""
        version = sys.version_info
        if version.major < 3 or (version.major == 3 and version.minor < 8):
            print("❌ Python 3.8+ is required")
            return False
        print(f"✅ Python {version.major}.{version.minor}.{version.micro}")
        return True
    
    def check_node_version(self):
        """Check if Node.js is available"""
        try:
            result = subprocess.run(['node', '--version'], capture_output=True, text=True)
            if result.returncode == 0:
                print(f"✅ Node.js {result.stdout.strip()}")
                return True
        except FileNotFoundError:
            pass
        
        print("⚠️ Node.js not found (optional for development)")
        return False
    
    def install_python_dependencies(self):
        """Install Python dependencies for both backend and admin"""
        print("\n📦 Installing Python dependencies...")
        
        # Backend dependencies
        if self.backend_dir.exists():
            requirements_file = self.backend_dir / "requirements.txt"
            if requirements_file.exists():
                print("  Installing backend dependencies...")
                result = subprocess.run([
                    sys.executable, '-m', 'pip', 'install', '-r', str(requirements_file)
                ], cwd=self.backend_dir)
                if result.returncode == 0:
                    print("  ✅ Backend dependencies installed")
                else:
                    print("  ❌ Failed to install backend dependencies")
        
        # Admin dependencies
        if self.admin_dir.exists():
            requirements_file = self.admin_dir / "requirements.txt"
            if requirements_file.exists():
                print("  Installing admin dependencies...")
                result = subprocess.run([
                    sys.executable, '-m', 'pip', 'install', '-r', str(requirements_file)
                ], cwd=self.admin_dir)
                if result.returncode == 0:
                    print("  ✅ Admin dependencies installed")
                else:
                    print("  ❌ Failed to install admin dependencies")
    
    def install_node_dependencies(self):
        """Install Node.js dependencies if available"""
        if not self.check_node_version():
            return
        
        print("\n📦 Installing Node.js dependencies...")
        
        # Root dependencies
        if (self.root_dir / "package.json").exists():
            result = subprocess.run(['npm', 'install'], cwd=self.root_dir)
            if result.returncode == 0:
                print("  ✅ Root dependencies installed")
    
    def create_directories(self):
        """Create necessary directories"""
        print("\n📁 Creating directories...")
        
        directories = [
            self.admin_dir / "uploads",
            self.root_dir / "logs",
            self.root_dir / "backups"
        ]
        
        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)
            print(f"  ✅ {directory.relative_to(self.root_dir)}")
    
    def create_env_files(self):
        """Create environment files"""
        print("\n🔧 Creating environment files...")
        
        # Backend .env
        backend_env = self.backend_dir / ".env"
        if not backend_env.exists():
            with open(backend_env, 'w') as f:
                f.write("""# ByteShelf Backend Environment
FLASK_ENV=development
SECRET_KEY=dev-secret-key-change-in-production
DEBUG=True
HOST=0.0.0.0
PORT=5000
""")
            print(f"  ✅ Created {backend_env.relative_to(self.root_dir)}")
        
        # Admin .env
        admin_env = self.admin_dir / ".env"
        if not admin_env.exists():
            with open(admin_env, 'w') as f:
                f.write("""# ByteShelf Admin Environment
FLASK_ENV=development
SECRET_KEY=admin-secret-key-change-in-production
DEBUG=True
HOST=0.0.0.0
PORT=5001
UPLOAD_FOLDER=uploads
MAX_CONTENT_LENGTH=16777216
""")
            print(f"  ✅ Created {admin_env.relative_to(self.root_dir)}")
    
    def initialize_data(self):
        """Initialize data files"""
        print("\n💾 Initializing data files...")
        
        data_file = self.admin_dir / "data.json"
        if not data_file.exists():
            initial_data = {
                "books": [],
                "categories": [
                    {"id": "algorithms", "name": "Algorithms & DSA", "icon": "⚡", "color": "default"},
                    {"id": "ml", "name": "AI & Machine Learning", "icon": "🧠", "color": "purple"},
                    {"id": "security", "name": "Cybersecurity", "icon": "🔒", "color": "red"},
                    {"id": "system", "name": "System Design", "icon": "🌐", "color": "yellow"}
                ],
                "stats": {
                    "total_books": 0,
                    "total_students": 12000,
                    "total_categories": 4
                }
            }
            
            with open(data_file, 'w', encoding='utf-8') as f:
                json.dump(initial_data, f, indent=2, ensure_ascii=False)
            
            print(f"  ✅ Created {data_file.relative_to(self.root_dir)}")
    
    def run_health_check(self):
        """Run health check on the setup"""
        print("\n🏥 Running health check...")
        
        checks = [
            ("Python version", self.check_python_version),
            ("Backend directory", lambda: self.backend_dir.exists()),
            ("Admin directory", lambda: self.admin_dir.exists()),
            ("Backend requirements", lambda: (self.backend_dir / "requirements.txt").exists()),
            ("Admin requirements", lambda: (self.admin_dir / "requirements.txt").exists()),
            ("Admin data file", lambda: (self.admin_dir / "data.json").exists()),
        ]
        
        all_passed = True
        for name, check in checks:
            try:
                result = check()
                status = "✅" if result else "❌"
                print(f"  {status} {name}")
                if not result:
                    all_passed = False
            except Exception as e:
                print(f"  ❌ {name}: {e}")
                all_passed = False
        
        return all_passed
    
    def print_next_steps(self):
        """Print next steps for the user"""
        print("\n🚀 Setup complete! Next steps:")
        print("\n1. Start the backend server:")
        print("   cd \"All code/backend\"")
        print("   python app.py")
        print("\n2. Start the admin panel (in another terminal):")
        print("   cd admin")
        print("   python app.py")
        print("\n3. Access the applications:")
        print("   - Main website: http://localhost:5000")
        print("   - Admin panel: http://localhost:5001")
        print("\n4. Optional: Use npm scripts for easier management:")
        print("   npm run start:all    # Start both servers")
        print("   npm run health       # Check server health")
        print("   python version.py show  # Check versions")

def main():
    print("🔧 ByteShelf Development Setup")
    print("=" * 40)
    
    setup = SetupManager()
    
    # Run setup steps
    setup.check_python_version()
    setup.check_node_version()
    setup.create_directories()
    setup.create_env_files()
    setup.initialize_data()
    setup.install_python_dependencies()
    setup.install_node_dependencies()
    
    # Health check
    if setup.run_health_check():
        print("\n✅ Setup completed successfully!")
        setup.print_next_steps()
    else:
        print("\n❌ Setup completed with some issues. Please check the errors above.")

if __name__ == '__main__':
    main()