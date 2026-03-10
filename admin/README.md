# ByteShelf Admin Panel

A comprehensive admin panel for managing the ByteShelf CS knowledge platform.

## Features

### 📊 Dashboard
- Overview statistics (books, students, categories)
- Recent activity monitoring
- Quick action buttons
- System health status

### 📚 Book Management
- Add new books with file uploads
- Edit existing book information
- Delete books (with file cleanup)
- Featured book management
- Category assignment
- Price and metadata management

### 🏷️ Category Management
- Create new categories
- Manage category icons and colors
- View books per category
- Category organization

### 📁 File Management
- PDF, DOC, DOCX, TXT file uploads
- File size validation (16MB max)
- Secure file storage
- File serving and downloads

## Setup

1. **Install Dependencies**:
```bash
cd admin
pip install -r requirements.txt
```

2. **Run the Admin Server**:
```bash
# From admin directory
python app.py

# Or using the runner script
python run_admin.py

# Or from project root (if run_admin.py is available there)
python run_admin.py
```

3. **Access Admin Panel**:
```
http://localhost:5001
```

## File Structure

```
admin/
├── templates/          # HTML templates
│   ├── base.html      # Base template with navigation
│   ├── dashboard.html # Main dashboard
│   ├── books.html     # Books listing
│   ├── add_book.html  # Add new book form
│   ├── edit_book.html # Edit book form
│   └── categories.html # Category management
├── static/            # Static assets
│   ├── css/
│   │   └── admin.css  # Admin panel styles
│   └── js/
│       └── admin.js   # Admin panel JavaScript
├── uploads/           # Uploaded files storage
├── app.py            # Main Flask application
├── data.json         # Data storage (JSON file)
└── requirements.txt  # Python dependencies
```

## Data Storage

The admin panel uses a JSON file (`data.json`) for data storage. In production, consider migrating to a proper database like PostgreSQL or SQLite.

### Data Structure
```json
{
  "books": [
    {
      "id": "unique-id",
      "title": "Book Title",
      "author": "Author Name",
      "category": "category-id",
      "price": 9.99,
      "pages": 500,
      "description": "Book description",
      "badge": "Bestseller",
      "filename": "uploaded-file.pdf",
      "featured": true,
      "created_at": "2026-03-08T01:00:00",
      "updated_at": "2026-03-08T02:00:00"
    }
  ],
  "categories": [
    {
      "id": "algorithms",
      "name": "Algorithms & DSA",
      "icon": "⚡",
      "color": "default"
    }
  ],
  "stats": {
    "total_books": 0,
    "total_students": 12000,
    "total_categories": 40
  }
}
```

## Security Considerations

⚠️ **Important**: This admin panel is for development/demo purposes. For production use:

1. **Add Authentication**: Implement user login/logout
2. **Add Authorization**: Role-based access control
3. **Secure File Uploads**: Additional validation and scanning
4. **Use HTTPS**: Encrypt all communications
5. **Database**: Replace JSON storage with proper database
6. **Input Validation**: Server-side validation for all inputs
7. **CSRF Protection**: Add CSRF tokens to forms

## API Endpoints

- `GET /` - Dashboard
- `GET /books` - Books listing
- `GET /books/add` - Add book form
- `POST /books/add` - Create new book
- `GET /books/edit/<id>` - Edit book form
- `POST /books/edit/<id>` - Update book
- `GET /books/delete/<id>` - Delete book
- `GET /categories` - Categories management
- `POST /categories/add` - Add new category
- `GET /upload/<filename>` - Serve uploaded files
- `GET /api/stats` - Statistics API
- `GET /api/books` - Books API

## Customization

### Adding New Fields
1. Update the form templates
2. Modify the Flask routes to handle new fields
3. Update the data structure in `data.json`

### Styling
- Modify `static/css/admin.css` for visual changes
- The design follows the main website's dark theme
- Uses CSS custom properties for easy theming

### Functionality
- Add new routes in `app.py`
- Create corresponding templates
- Update navigation in `base.html`

## Integration with Main Website

The admin panel is designed to work alongside the main ByteShelf website:

- **Main Website**: `http://localhost:5000`
- **Admin Panel**: `http://localhost:5001`
- **Shared Data**: Both can read from the same `data.json` file
- **File Serving**: Admin uploads can be served by the main website

## Troubleshooting

### File Upload Issues
- Check file size (max 16MB)
- Verify file permissions in `uploads/` directory
- Ensure supported file types: PDF, DOC, DOCX, TXT

### Data Not Saving
- Check write permissions for `data.json`
- Verify JSON format validity
- Check Flask debug output for errors

### Port Conflicts
- Admin runs on port 5001 by default
- Main website runs on port 5000
- Change ports in respective `app.py` files if needed