# ByteShelf Backend

Flask server for the ByteShelf CS knowledge platform.

## Structure

```
backend/
├── routes/
│   ├── __init__.py
│   └── main.py        # Main routes (index, static files, health)
├── app.py             # Flask application factory
├── config.py          # Configuration classes
├── requirements.txt   # Python dependencies
└── README.md          # This file
```

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the development server:
```bash
python app.py
```

## Configuration

The app uses different configurations for development and production:

- **Development**: Debug mode enabled, detailed error messages
- **Production**: Debug disabled, secure settings

Set the environment:
```bash
export FLASK_ENV=production  # or development
```

## API Endpoints

- `GET /` - Serves the main website from frontend/
- `GET /health` - Health check endpoint
- `GET /favicon.ico` - Handles favicon requests
- `GET /<path:filename>` - Serves static files from frontend/

## Adding New Routes

1. Create a new blueprint in `routes/`
2. Register it in `app.py`
3. Follow the existing pattern for consistency

Example:
```python
# routes/api.py
from flask import Blueprint, jsonify

api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('/books')
def get_books():
    return jsonify({"books": []})
```

Then register in `app.py`:
```python
from routes.api import api_bp
app.register_blueprint(api_bp)
```