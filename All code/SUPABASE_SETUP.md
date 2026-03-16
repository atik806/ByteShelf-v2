# Supabase Notes Setup Guide

## Overview
The notes system has been updated to use Supabase as the database backend instead of local JSON files.

## Prerequisites
- Supabase account and project
- Python supabase-py library installed

## Installation

### 1. Install Supabase Python Client
```bash
pip install supabase
```

### 2. Create the Notes Table in Supabase

Go to your Supabase dashboard and run the SQL from `backend/migrations/create_notes_table.sql`:

1. Navigate to your Supabase project
2. Go to SQL Editor
3. Create a new query
4. Copy and paste the contents of `backend/migrations/create_notes_table.sql`
5. Run the query

Alternatively, you can run it via the Supabase CLI:
```bash
supabase db push
```

### 3. Environment Variables

Make sure your `.env` file contains:
```
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-anon-key
```

These are already configured in the `.env` file.

## Database Schema

The `notes` table has the following structure:

| Column | Type | Description |
|--------|------|-------------|
| id | UUID | Primary key, auto-generated |
| user_id | TEXT | User identifier from auth header |
| title | TEXT | Note title |
| content | TEXT | Note content |
| category | TEXT | Note category (general, study, ideas, todo) |
| color | TEXT | Hex color code for the note |
| pinned | BOOLEAN | Whether the note is pinned |
| tags | JSONB | Array of tags |
| created_at | TIMESTAMP | Creation timestamp |
| updated_at | TIMESTAMP | Last update timestamp |

## API Endpoints

All endpoints require the `X-User-ID` header with the user's ID.

### Get All Notes
```
GET /api/notes/
```

### Get Single Note
```
GET /api/notes/<note_id>
```

### Create Note
```
POST /api/notes/
Body: {
  "title": "Note Title",
  "content": "Note content",
  "category": "general",
  "color": "#FFE5B4",
  "tags": []
}
```

### Update Note
```
PUT /api/notes/<note_id>
Body: {
  "title": "Updated Title",
  "content": "Updated content",
  "category": "study",
  "color": "#FFB3BA",
  "pinned": true
}
```

### Delete Note
```
DELETE /api/notes/<note_id>
```

### Search Notes
```
GET /api/notes/search?q=search_query
```

### Get Notes by Category
```
GET /api/notes/category/<category>
```

### Get Pinned Notes
```
GET /api/notes/pinned
```

### Get Statistics
```
GET /api/notes/stats
```

## Row Level Security (RLS)

The table has RLS enabled with policies that ensure:
- Users can only view their own notes
- Users can only insert notes for themselves
- Users can only update their own notes
- Users can only delete their own notes

## Troubleshooting

### "SUPABASE_URL and SUPABASE_KEY environment variables are required"
Make sure your `.env` file is properly configured with Supabase credentials.

### "Failed to create note" errors
Check that:
1. The `notes` table exists in Supabase
2. The table schema matches the migration SQL
3. RLS policies are correctly configured

### Connection issues
Ensure:
1. Your Supabase project is active
2. The anon key has appropriate permissions
3. Network connectivity to Supabase is available

## Migration from JSON

If you had notes stored in `notes_data.json`, you can migrate them to Supabase:

1. Export notes from the JSON file
2. Use the POST `/api/notes/` endpoint to create each note in Supabase
3. Delete the local `notes_data.json` file

The backend will no longer use the JSON file once Supabase is configured.
