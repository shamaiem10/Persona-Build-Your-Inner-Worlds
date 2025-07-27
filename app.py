from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3
from datetime import datetime
import random
import requests
import time
from huggingface_api import ask_persona
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

HUGGINGFACE_API_KEY = os.getenv("HF_TOKEN")

# 🧐 DB Connection Helper
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

# 📂 Handle Persona Creation
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

    return redirect(url_for('home'))






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






from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3
from datetime import datetime
import random
import requests
import time
from huggingface_api import ask_persona
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

HUGGINGFACE_API_KEY = os.getenv("HF_TOKEN")

# 🧐 DB Connection Helper
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

# 📂 Handle Persona Creation
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

    return redirect(url_for('home'))






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

    # Mark the goal as done
    conn.execute('UPDATE goals SET is_done = 1 WHERE id = ?', (goal_id,))

    # Increment the persona's completed goal count
    conn.execute('UPDATE personas SET goals_completed = goals_completed + 1 WHERE id = ?', (persona_id,))

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

        # Insert the journal entry
        conn.execute('INSERT INTO journals (persona_id, entry) VALUES (?, ?)', (persona_id, entry))

        # Update the journal count
        conn.execute('UPDATE personas SET journal_count = journal_count + 1 WHERE id = ?', (persona_id,))

        conn.commit()

    journals = conn.execute(
        'SELECT * FROM journals WHERE persona_id = ? ORDER BY timestamp DESC',
        (persona_id,)
    ).fetchall()

    conn.close()
    return render_template('journal.html', persona=persona, journals=journals)


def generate_persona_prompt(persona, user_message):
    return f"""
You are {persona['name']} — a personality with the mood '{persona['mood']}' and the unique vibe of "{persona['theme']}". 
You're known for phrases like: "{persona['quote']}".

Now, someone just messaged you: "{user_message}"

👉 Reply in your signature tone and theme. Keep it *very* short and realistic — 1 to 2 lines only. Avoid being dramatic or robotic. 
Make it sound like a quick, clever text message you’d actually send in a group chat.

Your reply:
"""




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
    "message": ai_reply,
    "theme": persona["theme"]  # 👈 Add this line
})


        conn.close()

        return jsonify({"responses": responses})

    else:
        personas = conn.execute("SELECT * FROM personas").fetchall()
        conn.close()
        return render_template("chat.html", personas=personas, messages=[])



@app.route('/reflections')
def reflections():
    conn = get_db_connection()
    personas = conn.execute("SELECT * FROM personas").fetchall()

    reflections = []

    for persona in personas:
        pid = persona["id"]

        # Count journals and completed goals
        journal_count = conn.execute("SELECT COUNT(*) FROM journals WHERE persona_id = ?", (pid,)).fetchone()[0]
        goal_count = conn.execute("SELECT COUNT(*) FROM goals WHERE persona_id = ? AND is_done = 1", (pid,)).fetchone()[0]

        # Simple vibe score logic
        vibe = 50
        if journal_count > 0:
            vibe += 20
        if goal_count > 0:
            vibe += 30
        if journal_count == 0 and goal_count == 0:
            vibe -= 20
        vibe_percent = min(100, max(0, vibe))

        # Use AI to generate reflection
        prompt = f"""
You are {persona['name']} and your mood is '{persona['mood']}'. You speak in the vibe of "{persona['theme']}" and love saying things like: "{persona['quote']}".

This week, your human wrote {journal_count} journal entries and completed {goal_count} goals.

Write a very short and fun 1-line weekly reflection message. Make it poetic, funny, encouraging, or sarcastic.
"""

        try:
            message = ask_persona(prompt).strip()
        except:
            message = "Hmm... couldn't think of anything deep right now 😅"

        reflections.append({
            "name": persona["name"],
            "message": message,
            "theme": persona["theme"],
            "vibe_percent": vibe_percent,
            "journal_count": journal_count,
            "journal_percent": min(100, journal_count * 20),
            "goals_completed": goal_count,
            "goals_percent": min(100, goal_count * 25),
            "emoji": "🌸" if "soft" in (persona["theme"] or "").lower() else "🌟"
        })

    conn.close()
    return render_template("reflections.html", reflections=reflections)

if __name__ == '__main__':
    app.run(debug=True)


