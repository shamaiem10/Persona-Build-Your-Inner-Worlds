<<<<<<< HEAD
from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3
from datetime import datetime
import random
import requests
import time
from huggingface_api import ask_persona
import os
=======
from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime
>>>>>>> a64c11c490c4843b70df0587722e0e2719e4f0fc

app = Flask(__name__)
app.secret_key = 'your_secret_key'

<<<<<<< HEAD
HUGGINGFACE_API_KEY = os.getenv("HF_TOKEN")

# 🧐 DB Connection Helper
=======
# 🧠 DB Connection Helper
>>>>>>> a64c11c490c4843b70df0587722e0e2719e4f0fc
def get_db_connection():
    conn = sqlite3.connect('data.db')
    conn.row_factory = sqlite3.Row
    return conn

# 🔮 Splash Screen Route
@app.route('/')
def logo():
    return render_template('logo.html')

# 🏠 Main Dashboard – Shows All Personas
@app.route('/home')
def home():
    conn = get_db_connection()
    personas = conn.execute('SELECT * FROM personas').fetchall()
    conn.close()
    return render_template('home.html', personas=personas)

# ✨ Create Persona Form
@app.route('/create', methods=['GET'])
def create_persona_form():
    return render_template('create_persona.html')

<<<<<<< HEAD
# 📂 Handle Persona Creation
=======
# 💾 Handle Persona Creation
>>>>>>> a64c11c490c4843b70df0587722e0e2719e4f0fc
@app.route('/create', methods=['POST'])
def create_persona():
    name = request.form['name']
    mood = request.form['mood']
    quote = request.form['quote']
    theme = request.form['theme']
    last_active = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    conn = get_db_connection()
    conn.execute(
        'INSERT INTO personas (name, mood, quote, theme, last_active) VALUES (?, ?, ?, ?, ?)',
        (name, mood, quote, theme, last_active)
    )
    conn.commit()
    conn.close()

<<<<<<< HEAD
    return redirect(url_for('home'))





=======
    return redirect(url_for('dashboard'))

# 💬 Group Chat Between Personas
@app.route('/chat', methods=['GET', 'POST'])
def chat():
    conn = get_db_connection()

    if request.method == 'POST':
        persona_id = request.form['persona_id']
        message = request.form['message']
        conn.execute('INSERT INTO messages (persona_id, message) VALUES (?, ?)', (persona_id, message))
        conn.commit()

    messages = conn.execute('''
        SELECT messages.message, messages.timestamp, personas.name, personas.theme
        FROM messages
        JOIN personas ON messages.persona_id = personas.id
        ORDER BY messages.timestamp ASC
    ''').fetchall()

    personas = conn.execute('SELECT * FROM personas').fetchall()
    conn.close()

    return render_template('chat.html', messages=messages, personas=personas)
>>>>>>> a64c11c490c4843b70df0587722e0e2719e4f0fc

# 🎯 View & Add Goals
@app.route('/goals/<int:persona_id>', methods=['GET', 'POST'])
def goals(persona_id):
    conn = get_db_connection()

    if request.method == 'POST':
        task = request.form['task']
        conn.execute('INSERT INTO goals (persona_id, task) VALUES (?, ?)', (persona_id, task))
        conn.commit()

    persona = conn.execute('SELECT * FROM personas WHERE id = ?', (persona_id,)).fetchone()
    goals = conn.execute('SELECT * FROM goals WHERE persona_id = ?', (persona_id,)).fetchall()

    conn.close()
    return render_template('goals.html', persona=persona, goals=goals)

# ✅ Mark Goal as Done
@app.route('/goals/<int:persona_id>/done/<int:goal_id>')
def mark_goal_done(persona_id, goal_id):
    conn = get_db_connection()
    conn.execute('UPDATE goals SET is_done = 1 WHERE id = ?', (goal_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('goals', persona_id=persona_id))

# 📓 Journal Page
@app.route('/journal/<int:persona_id>', methods=['GET', 'POST'])
def journal(persona_id):
    conn = get_db_connection()

    persona = conn.execute('SELECT * FROM personas WHERE id = ?', (persona_id,)).fetchone()
    if not persona:
        conn.close()
        return "Persona not found", 404

    if request.method == 'POST':
        entry = request.form['entry']
        conn.execute('INSERT INTO journals (persona_id, entry) VALUES (?, ?)', (persona_id, entry))
        conn.commit()

    journals = conn.execute(
        'SELECT * FROM journals WHERE persona_id = ? ORDER BY timestamp DESC',
        (persona_id,)
    ).fetchall()

    conn.close()
    return render_template('journal.html', persona=persona, journals=journals)

<<<<<<< HEAD



def generate_persona_prompt(persona, user_message):
    return f"""You are {persona['name']} with the mood '{persona['mood']}'. 
You always reply with the vibe of your theme: {persona['theme']}. 
You love saying things like: \"{persona['quote']}\".

Now, respond in your own unique style to this message from a friend:

Q: {user_message}
A:"""


@app.route("/chat", methods=["GET", "POST"])
def chat():
    conn = get_db_connection()

    if request.method == "POST":
        persona_id = request.form.get('persona_id')
        user_message = request.form.get('message')

        # Get all personas
        all_personas = conn.execute("SELECT * FROM personas").fetchall()

        # Identify the one who is asking
        asker = conn.execute("SELECT * FROM personas WHERE id = ?", (persona_id,)).fetchone()

        if asker is None:
            conn.close()
            return jsonify({"responses": [{"name": "System", "message": "[Error]: Persona not found."}]}), 404

        responses = []

        # Generate reply from each persona *except* the asker
        for persona in all_personas:
            if str(persona['id']) == str(persona_id):
                continue  # Skip the asker

            prompt = generate_persona_prompt(persona, user_message)
            ai_reply = ask_persona(prompt)

            responses.append({
                "name": persona["name"],
                "message": ai_reply
            })

        conn.close()

        return jsonify({"responses": responses})

    else:
        personas = conn.execute("SELECT * FROM personas").fetchall()
        conn.close()
        return render_template("chat.html", personas=personas, messages=[])


=======
# 🚀 Run Server
>>>>>>> a64c11c490c4843b70df0587722e0e2719e4f0fc
if __name__ == '__main__':
    app.run(debug=True)
