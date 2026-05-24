from flask import Flask, request, jsonify, render_template
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Database setup - creates a simple SQLite database
def init_db():
    """Initialize the database with a notes table"""
    conn = sqlite3.connect('notes.db')
    cursor = conn.cursor()
    
    # Create table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

# Initialize database when app starts
init_db()

def get_db_connection():
    """Create a database connection"""
    conn = sqlite3.connect('notes.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    """Serve the HTML page"""
    return render_template('index.html')

@app.route('/api/notes', methods=['GET'])
def get_notes():
    """Get all notes from the database"""
    conn = get_db_connection()
    notes = conn.execute('SELECT * FROM notes ORDER BY created_at DESC').fetchall()
    conn.close()
    
    # Convert to list of dictionaries
    notes_list = []
    for note in notes:
        notes_list.append({
            'id': note['id'],
            'content': note['content'],
            'created_at': note['created_at']
        })
    
    return jsonify(notes_list)

@app.route('/api/notes', methods=['POST'])
def save_note():
    """Save a new note to the database"""
    data = request.get_json()
    
    if not data or 'content' not in data:
        return jsonify({'error': 'Content is required'}), 400
    
    content = data['content']
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Insert the new note
    cursor.execute('INSERT INTO notes (content) VALUES (?)', (content,))
    conn.commit()
    
    # Get the inserted note
    note_id = cursor.lastrowid
    note = conn.execute('SELECT * FROM notes WHERE id = ?', (note_id,)).fetchone()
    conn.close()
    
    return jsonify({
        'id': note['id'],
        'content': note['content'],
        'created_at': note['created_at']
    }), 201

@app.route('/api/notes/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    """Delete a note from the database"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Check if note exists
    note = conn.execute('SELECT * FROM notes WHERE id = ?', (note_id,)).fetchone()
    
    if not note:
        conn.close()
        return jsonify({'error': 'Note not found'}), 404
    
    # Delete the note
    cursor.execute('DELETE FROM notes WHERE id = ?', (note_id,))
    conn.commit()
    conn.close()
    
    return jsonify({'message': 'Note deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
