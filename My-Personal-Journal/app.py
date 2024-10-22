from flask import Flask, render_template, request, redirect, url_for
from journal_app import add_entry, search_entries
from datetime import datetime
import sqlite3

app = Flask(__name__)

# Route to show the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to add a new journal entry
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        mood = request.form['mood']
        content = request.form['content']
        tags = request.form['tags']
        add_entry("user_1", mood, content, tags)
        return redirect(url_for('index'))
    return render_template('add.html')

# Route to search journal entries


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_input = request.form['search_term']

        # Try to parse the input as a date
        try:
            search_date = datetime.strptime(search_input, '%Y-%m-%d').date()
            results = search_entries("user_1", date=search_date)
        except ValueError:
            # If parsing fails, treat it as a search term
            results = search_entries("user_1", search_term=search_input)

        return render_template('search_results.html', results=results)

    return render_template('search.html')


# Route to list all unique tags
@app.route('/tags')
def list_tags():
    conn = sqlite3.connect('journal.db')
    cursor = conn.cursor()

    # Fetch unique tags from all entries
    cursor.execute("SELECT DISTINCT tags FROM journal_entries")
    tags_data = cursor.fetchall()
    conn.close()

    # Flatten the tags and remove duplicates
    tags = set()
    for row in tags_data:
        if row[0]:
            tags.update(tag.strip() for tag in row[0].split(','))

    return render_template('tags.html', tags=sorted(tags))

# Route to show journal entries by tag
@app.route('/tags/<tag>')
def entries_by_tag(tag):
    conn = sqlite3.connect('journal.db')
    cursor = conn.cursor()

    # Search for entries that contain the selected tag
    cursor.execute("SELECT * FROM journal_entries WHERE tags LIKE ?", ('%' + tag + '%',))
    results = cursor.fetchall()
    conn.close()

    return render_template('search_results.html', results=results)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
