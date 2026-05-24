# Quick Note Application 📝

A beginner-friendly single-page application for writing and saving notes. This application demonstrates the complete request-response flow between a frontend and backend, with data persistence using SQLite database.

## Features

- ✍️ Write and save notes
- 📋 View all saved notes
- 🗑️ Delete notes
- 💾 Automatic database storage
- 🎨 Beautiful, responsive UI
- ⌨️ Keyboard shortcut (Ctrl+Enter to save)

## Tech Stack

- **Backend**: Python Flask
- **Database**: SQLite
- **Frontend**: HTML, CSS, JavaScript
- **API**: RESTful endpoints

## Project Structure

```
Quick Note Application/
├── app.py                 # Flask backend with database operations
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Frontend HTML with embedded CSS and JavaScript
└── notes.db              # SQLite database (created automatically)
```

## Setup Instructions

### Prerequisites

- Python 3.7 or higher installed on your system
- Basic understanding of command line

### Step 1: Install Dependencies

Open your terminal/command prompt and navigate to the project directory:

```bash
cd "d:/VirtualWorksIntern/Quick Note Application"
```

Install the required packages:

```bash
pip install -r requirements.txt
```

### Step 2: Run the Application

Start the Flask server:

```bash
python app.py
```

You should see output indicating the server is running:
```
 * Running on http://127.0.0.1:5000
```

### Step 3: Use the Application

Open your web browser and go to:
```
http://127.0.0.1:5000
```

## How It Works

### Backend (app.py)

1. **Database Setup**: Creates a SQLite database (`notes.db`) with a `notes` table
2. **API Endpoints**:
   - `GET /` - Serves the HTML page
   - `GET /api/notes` - Retrieves all notes
   - `POST /api/notes` - Saves a new note
   - `DELETE /api/notes/<id>` - Deletes a specific note

### Frontend (templates/index.html)

1. **User Interface**: Clean, modern design with input area and notes display
2. **JavaScript Functions**:
   - `saveNote()` - Sends note data to backend via POST request
   - `loadNotes()` - Fetches and displays all notes via GET request
   - `deleteNote()` - Removes a note via DELETE request
3. **Features**:
   - Real-time note display
   - Formatted timestamps
   - XSS protection for user input
   - Keyboard shortcut support

## API Endpoints

### Get All Notes
```http
GET /api/notes
```
Response: Array of note objects with `id`, `content`, and `created_at`

### Save Note
```http
POST /api/notes
Content-Type: application/json

{
  "content": "Your note text here"
}
```
Response: Created note object

### Delete Note
```http
DELETE /api/notes/<note_id>
```
Response: Success message

## Database Schema

```sql
CREATE TABLE notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
```

## Beginner Tips

- The database file (`notes.db`) is created automatically when you first run the app
- All notes are persisted even after you close the browser
- The server runs in debug mode, so you'll see error messages in the terminal
- You can stop the server by pressing `Ctrl+C` in the terminal

## Troubleshooting

**Port already in use?**
- Change the port in `app.py`: `app.run(debug=True, port=5001)`

**Database errors?**
- Delete `notes.db` and restart the app (it will recreate the database)

**Notes not saving?**
- Check that the server is running
- Look at the terminal for error messages
- Open browser developer tools (F12) to see JavaScript errors

## Learning Objectives

This project teaches:
- Building a Flask web application
- Creating RESTful API endpoints
- Working with SQLite database
- Making HTTP requests from JavaScript
- Handling JSON data
- Building responsive user interfaces
- Understanding client-server architecture

## License

This is a learning project. Feel free to use and modify as needed.
