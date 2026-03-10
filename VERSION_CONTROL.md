# ByteShelf Version Control Guide

This document explains the version control system implemented for the ByteShelf platform.

## 📦 Package Structure

The ByteShelf platform uses a monorepo structure with multiple package.json files for comprehensive version management:

```
ByteShelf/
├── package.json                    # Root monorepo configuration
├── All code/
│   ├── package.json               # Main website package
│   └── frontend/
│       └── package.json           # Frontend-specific package
└── admin/
    └── package.json               # Admin panel package
```

## 🔢 Version Management

### Current Versions
- **Root Monorepo**: 1.0.1
- **Main Website**: 1.0.0  
- **Frontend**: 1.0.0
- **Admin Panel**: 1.0.0

### Version Management Script

Use the `version.py` script for comprehensive version management:

```bash
# Show current versions
python version.py show

# Increment patch version (1.0.0 → 1.0.1)
python version.py patch

# Increment minor version (1.0.0 → 1.1.0)
python version.py minor

# Increment major version (1.0.0 → 2.0.0)
python version.py major

# Set specific version
python version.py set 1.2.3

# Update specific component only
python version.py patch admin
python version.py minor frontend

# Create changelog entry
python version.py changelog 1.2.3
```

## 📋 NPM Scripts

### Root Level Commands
```bash
# Start both servers
npm run start:all

# Start individual services
npm run start:website
npm run start:admin

# Install all dependencies
npm run install:all

# Health checks
npm run health

# Version management
npm run version:patch
npm run version:minor
npm run version:major

# Backup and cleanup
npm run backup
npm run clean
```

### Website Commands (All code/)
```bash
cd "All code"

# Start website
npm start
npm run dev

# Install backend dependencies
npm run install-backend

# Health check
npm run health-check
```

### Admin Commands (admin/)
```bash
cd admin

# Start admin panel
npm start
npm run dev

# Install dependencies
npm install  # (runs pip install)

# Data management
npm run backup-data
npm run restore-data
npm run reset-data
npm run validate-data

# Utilities
npm run stats
npm run clean
npm run health
```

## 🛠️ Development Setup

### Automated Setup
```bash
# Run the setup script
python setup.py
```

This will:
- Check Python and Node.js versions
- Install all dependencies
- Create necessary directories
- Initialize environment files
- Set up data files
- Run health checks

### Manual Setup
```bash
# 1. Install backend dependencies
cd "All code/backend"
pip install -r requirements.txt

# 2. Install admin dependencies  
cd ../../admin
pip install -r requirements.txt

# 3. Install Node.js dependencies (optional)
npm install
```

## 🏥 Health Monitoring

### Health Check Commands
```bash
# Check all services
npm run health

# Individual health checks
curl http://localhost:5000/health  # Website
curl http://localhost:5001/health  # Admin

# Using npm scripts
npm run health:website
npm run health:admin
```

### Health Check Endpoints
- **Website**: `GET /health`
- **Admin**: `GET /health`

Both return JSON with status information.

## 📝 Changelog Management

The project uses [Keep a Changelog](https://keepachangelog.com/) format:

```bash
# Create changelog entry
python version.py changelog 1.2.3

# Manual editing
# Edit CHANGELOG.md directly
```

### Changelog Sections
- **Added**: New features
- **Changed**: Changes in existing functionality
- **Deprecated**: Soon-to-be removed features
- **Removed**: Removed features
- **Fixed**: Bug fixes
- **Security**: Security improvements

## 🔄 Release Process

### 1. Development
```bash
# Make changes
# Test locally
npm run start:all
```

### 2. Version Bump
```bash
# Choose appropriate version bump
python version.py patch   # Bug fixes
python version.py minor   # New features
python version.py major   # Breaking changes
```

### 3. Update Changelog
```bash
python version.py changelog <new-version>
```

### 4. Commit and Tag
```bash
git add .
git commit -m "Release v<version>"
git push
```

The version script automatically creates git tags.

## 🌿 Environment Management

### Environment Files
- `All code/backend/.env` - Backend configuration
- `admin/.env` - Admin panel configuration

### Version Files
- `.nvmrc` - Node.js version (18.17.0)
- `.python-version` - Python version (3.11.0)

## 📊 Monitoring and Analytics

### Package Analytics
```bash
# View package stats
npm run stats  # (in admin/)

# Check data integrity
npm run validate-data  # (in admin/)
```

### Version Tracking
All package.json files track:
- Version numbers
- Dependencies
- Scripts
- Metadata
- Configuration

## 🔧 Troubleshooting

### Common Issues

**Version Mismatch**
```bash
python version.py show
# Manually sync versions if needed
```

**Dependency Issues**
```bash
npm run clean
npm run install:all
```

**Health Check Failures**
```bash
# Check if servers are running
npm run health

# Restart services
npm run start:all
```

### Support Commands
```bash
# Clean all caches
npm run clean

# Reinstall everything
npm run install:all

# Reset admin data
cd admin && npm run reset-data

# Backup before major changes
npm run backup
```

## 📚 Best Practices

1. **Always run health checks** before and after changes
2. **Use semantic versioning** (patch/minor/major)
3. **Update changelog** for all releases
4. **Test locally** before version bumps
5. **Backup data** before major changes
6. **Use npm scripts** for consistency
7. **Keep dependencies updated** regularly

## 🚀 Future Enhancements

- Automated testing integration
- CI/CD pipeline setup
- Docker containerization
- Database migration scripts
- Performance monitoring
- Security scanning
- Dependency vulnerability checks