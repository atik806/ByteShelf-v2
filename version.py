#!/usr/bin/env python3
"""
ByteShelf Version Management Script

This script helps manage versions across all components of the ByteShelf platform.
"""

import json
import os
import sys
import subprocess
from pathlib import Path
from datetime import datetime

class VersionManager:
    def __init__(self):
        self.root_dir = Path(__file__).parent
        self.package_files = [
            self.root_dir / "package.json",
            self.root_dir / "All code" / "package.json", 
            self.root_dir / "All code" / "frontend" / "package.json",
            self.root_dir / "admin" / "package.json"
        ]
    
    def get_current_versions(self):
        """Get current versions from all package.json files"""
        versions = {}
        for package_file in self.package_files:
            if package_file.exists():
                with open(package_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    relative_path = package_file.relative_to(self.root_dir)
                    versions[str(relative_path)] = data.get('version', '0.0.0')
        return versions
    
    def update_version(self, new_version, component=None):
        """Update version in package.json files"""
        updated_files = []
        
        files_to_update = self.package_files
        if component:
            # Filter to specific component
            files_to_update = [f for f in self.package_files if component in str(f)]
        
        for package_file in files_to_update:
            if package_file.exists():
                with open(package_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                old_version = data.get('version', '0.0.0')
                data['version'] = new_version
                
                with open(package_file, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                
                updated_files.append({
                    'file': str(package_file.relative_to(self.root_dir)),
                    'old_version': old_version,
                    'new_version': new_version
                })
        
        return updated_files
    
    def increment_version(self, increment_type='patch', component=None):
        """Increment version (patch, minor, or major)"""
        current_versions = self.get_current_versions()
        
        # Use the root package.json version as reference
        root_version = current_versions.get('package.json', '1.0.0')
        major, minor, patch = map(int, root_version.split('.'))
        
        if increment_type == 'patch':
            patch += 1
        elif increment_type == 'minor':
            minor += 1
            patch = 0
        elif increment_type == 'major':
            major += 1
            minor = 0
            patch = 0
        
        new_version = f"{major}.{minor}.{patch}"
        return self.update_version(new_version, component)
    
    def create_changelog_entry(self, version, changes):
        """Create or update changelog"""
        changelog_file = self.root_dir / "CHANGELOG.md"
        
        entry = f"""
## [{version}] - {datetime.now().strftime('%Y-%m-%d')}

### Added
- {changes.get('added', 'No new features')}

### Changed
- {changes.get('changed', 'No changes')}

### Fixed
- {changes.get('fixed', 'No fixes')}

### Removed
- {changes.get('removed', 'Nothing removed')}

"""
        
        if changelog_file.exists():
            with open(changelog_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Insert new entry after the header
            lines = content.split('\n')
            header_end = 0
            for i, line in enumerate(lines):
                if line.startswith('## ['):
                    header_end = i
                    break
            
            lines.insert(header_end, entry)
            content = '\n'.join(lines)
        else:
            content = f"# Changelog\n\nAll notable changes to ByteShelf will be documented in this file.\n{entry}"
        
        with open(changelog_file, 'w', encoding='utf-8') as f:
            f.write(content)
    
    def git_tag_version(self, version):
        """Create git tag for version"""
        try:
            subprocess.run(['git', 'tag', f'v{version}'], check=True)
            print(f"✅ Created git tag: v{version}")
        except subprocess.CalledProcessError:
            print(f"❌ Failed to create git tag: v{version}")
        except FileNotFoundError:
            print("⚠️ Git not found, skipping tag creation")

def main():
    vm = VersionManager()
    
    if len(sys.argv) < 2:
        print("Usage: python version.py <command> [options]")
        print("Commands:")
        print("  show                    - Show current versions")
        print("  patch [component]       - Increment patch version")
        print("  minor [component]       - Increment minor version") 
        print("  major [component]       - Increment major version")
        print("  set <version> [component] - Set specific version")
        print("  changelog <version>     - Create changelog entry")
        return
    
    command = sys.argv[1]
    
    if command == 'show':
        versions = vm.get_current_versions()
        print("📦 Current Versions:")
        for file, version in versions.items():
            print(f"  {file}: {version}")
    
    elif command in ['patch', 'minor', 'major']:
        component = sys.argv[2] if len(sys.argv) > 2 else None
        updated = vm.increment_version(command, component)
        
        print(f"🔄 Updated {command} version:")
        for update in updated:
            print(f"  {update['file']}: {update['old_version']} → {update['new_version']}")
        
        if updated:
            new_version = updated[0]['new_version']
            vm.git_tag_version(new_version)
    
    elif command == 'set':
        if len(sys.argv) < 3:
            print("❌ Please specify version: python version.py set 1.2.3")
            return
        
        version = sys.argv[2]
        component = sys.argv[3] if len(sys.argv) > 3 else None
        updated = vm.update_version(version, component)
        
        print(f"🔄 Set version to {version}:")
        for update in updated:
            print(f"  {update['file']}: {update['old_version']} → {update['new_version']}")
        
        vm.git_tag_version(version)
    
    elif command == 'changelog':
        if len(sys.argv) < 3:
            print("❌ Please specify version: python version.py changelog 1.2.3")
            return
        
        version = sys.argv[2]
        changes = {
            'added': input("Added features (press Enter for none): ") or "No new features",
            'changed': input("Changed features (press Enter for none): ") or "No changes", 
            'fixed': input("Fixed issues (press Enter for none): ") or "No fixes",
            'removed': input("Removed features (press Enter for none): ") or "Nothing removed"
        }
        
        vm.create_changelog_entry(version, changes)
        print(f"📝 Created changelog entry for version {version}")
    
    else:
        print(f"❌ Unknown command: {command}")

if __name__ == '__main__':
    main()