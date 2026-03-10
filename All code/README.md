# ByteShelf - CS Knowledge Platform

A modern web platform for computer science students to access premium PDF books and resources, with a comprehensive admin panel for content management.

## Project Structure

```
├── frontend/           # Static HTML, CSS, JS files
│   ├── assets/        # Static assets (CSS, JS, images)
│   ├── index.html     # Main website file
│   └── package.json   # Frontend configuration
├── backend/           # Flask server for main website
│   ├── routes/        # Route handlers
│   ├── app.py         # Main Flask application
│   ├── config.py      # Configuration settings
│   └── requirements.txt # Python dependencies
├── admin/             # Admin panel for content management
│   ├── templates/     # Admin HTML templates
│   ├── static/        # Admin CSS/JS assets
│   ├── uploads/       # File upload storage
│   ├── app.py         # Admin Flask application
│   └── data.json      # Data storage (JSON)
├── .gitignore         # Git ignore rules
├── README.md          # This file
├── run.py             # Main website runner
└── run_admin.py       # Admin panel runner
```

## Quick Start

### Main Website (Frontend + Backend)

1. **Install dependencies**:
```bash
cd backend
pip install -r requirements.txt
```

2. **Run the main website**:
```bash
# From project root
python run.py

# Or from backend directory
cd backend
python app.py
```

3. **Access the website**:
```
http://localhost:5000
```

### Admin Panel

1. **Install admin dependencies**:
```bash
cd admin
pip install -r requirements.txt
```

2. **Run the admin panel**:
```bash
# From project root
python run_admin.py

# Or from admin directory
cd admin
python app.py
```

3. **Access the admin panel**:
```
http://localhost:5001
```

## Features

### Main Website
- **Modern Design**: Dark theme with CS-focused branding
- **Responsive Layout**: Mobile-first, works on all devices
- **Interactive Elements**: Custom cursor, smooth animations
- **Book Showcase**: Featured books with categories
- **Pricing Plans**: Multiple subscription tiers
- **Student Testimonials**: Social proof section

### Admin Panel
- **📊 Dashboard**: Statistics and overview
- **📚 Book Management**: Add, edit, delete books with file uploads
- **🏷️ Category Management**: Organize books by topics
- **📁 File Uploads**: PDF, DOC, DOCX, TXT support (16MB max)
- **✨ Featured Books**: Highlight important content
- **🎨 Modern UI**: Consistent with main website design

## Development

Both servers run in debug mode by default with auto-reload on code changes.

### Ports
- **Main Website**: `http://localhost:5000`
- **Admin Panel**: `http://localhost:5001`

### Environment Variables
- `FLASK_ENV`: Set to 'development' or 'production'
- `SECRET_KEY`: Set in production for security

### Data Storage
The admin panel currently uses JSON file storage (`admin/data.json`). For production, consider migrating to PostgreSQL or SQLite.

## API Endpoints

### Main Website
- `GET /` - Serves the main website
- `GET /health` - Health check endpoint
- `GET /<filename>` - Serves static files from frontend

### Admin Panel
- `GET /` - Admin dashboard
- `GET /books` - Books management
- `POST /books/add` - Add new book
- `GET /categories` - Category management
- `GET /api/stats` - Statistics API
- `GET /upload/<filename>` - Serve uploaded files

## File Upload Management

The admin panel handles file uploads for books:

- **Supported formats**: PDF, DOC, DOCX, TXT
- **Maximum size**: 16MB per file
- **Storage**: `admin/uploads/` directory
- **Security**: Filename sanitization and type validation

## Deployment

### Development
Both servers can run simultaneously for full functionality.

### Production
1. **Set environment variables**:
```bash
export FLASK_ENV=production
export SECRET_KEY=your-secret-key
```

2. **Use production WSGI server**:
```bash
pip install gunicorn

# Main website
gunicorn -w 4 -b 0.0.0.0:5000 --chdir backend app:app

# Admin panel (with authentication in production)
gunicorn -w 2 -b 0.0.0.0:5001 --chdir admin app:app
```

3. **Security considerations for admin panel**:
   - Add authentication/authorization
   - Use HTTPS
   - Implement CSRF protection
   - Add input validation
   - Use proper database instead of JSON

## Integration

The admin panel and main website are designed to work together:

- **Shared data**: Admin manages content that appears on the main site
- **File serving**: Uploaded files can be served by either application
- **Consistent design**: Both use the same color scheme and typography
- **API compatibility**: Admin provides APIs that the main site can consume

## Customization

### Adding New Features
1. **Backend**: Add routes in respective `app.py` files
2. **Frontend**: Update templates and static files
3. **Data**: Modify the JSON structure or migrate to database

### Styling
- **Main site**: Inline CSS in `frontend/index.html`
- **Admin panel**: `admin/static/css/admin.css`
- **Consistent theming**: Both use CSS custom properties

### Content Management
Use the admin panel to:
- Add new books with file uploads
- Organize content by categories
- Feature important books on homepage
- Track statistics and engagement