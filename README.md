# 💫 Persona: Build Your Inner Worlds

![Status](https://img.shields.io/badge/status-in_progress-f48fb1)
![Made with](https://img.shields.io/badge/made%20with-%E2%9D%A4%EF%B8%8F%20Flask-blueviolet)
![Hackathon](https://img.shields.io/badge/hackathon-CS%20Girlies%20AI%20vs%20HI-ff69b4)
![UI Vibe](https://img.shields.io/badge/vibe-cute_pastel-ffc0cb)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

---

> 🌸 *"Make anything but make it YOU."*  
> **Built for the CS Girlies Hackathon: AI vs HI**

---

## 🌈 What's Persona?

**Persona** is a pastel-themed, beautifully chaotic digital sanctuary where all your inner personas — moods, thoughts, and alter-egos — come to life.  
You create them, give them voices, and let them chat like a wholesome little WhatsApp group inside your brain 💬✨

---

## ✨ Features 

✅ **Splash Screen Logo Page**  
✅ **Dashboard** to view all created personas  
✅ **Create Persona** form (with name, mood, theme color, etc.)  
✅ **Group Chat** (WhatsApp-style!) where your personas can talk to each other  
✅ **Goal Tracker** per persona  
✅ **Journal Entries** for persona reflections  
✅ Consistent **aesthetic UI** using pastel vibes and cutesy fonts 🎀

---

## 🛠 Tech Stack

- **Python + Flask** (Back-end)
- **HTML, CSS, Bootstrap Icons**
- **SQLite** (Database)
- Fonts via **Google Fonts**
- Style powered by ✨vibes✨ and a lot of love

---
## 🚀 Installation

1. Clone this repo:  
   `git clone https://github.com/yourusername/Persona.git`

2. Create and activate virtual environment:  
   `python -m venv venv`  
   `source venv/bin/activate` (Linux/macOS) or `venv\Scripts\activate` (Windows)

3. Install dependencies:  
   `pip install -r requirements.txt`

4. Add your Hugging Face API key in `.env`:  
   `HF_API_KEY=your_token_here`

5. Run the app:  
   `python app.py`

6. Open your browser at `http://localhost:5000`
   
---

## 🤖 Hugging Face Integration

We use the **Hugging Face Inference API** to give your personas their own AI-generated replies.  
You can configure each persona with a prompt/personality, and when they chat — responses are generated on the fly.

---

### 💡 Example

If your persona is **"Sassy Sleepy Cat"**, it might respond like:

"ugh... do we really have to talk before 3pm? 😴"

---

### 🔧 Setup Steps

#### 1️⃣ Get your Hugging Face API Token

- Go to 👉 [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)  
- Log in or create an account  
- Generate a new token (with `read` access)

---

#### 2️⃣ Save the Token Securely

Create a `.env` file in your project root and add:

HF_API_KEY=your_token_here

## 📁 Folder Structure

```markdown

Persona/
│
├── static/                # CSS, icons, custom styling (soon)
├── templates/             # All HTML files (dashboard, chat, journal, etc.)
├── venv/                  # Virtual environment (ignored in Git)
├── app.py                 # Main Flask app logic
├── data.db                # SQLite database
└── README.md              # This file 💅


```
---

### 👩‍💻 About

This project was **built solo by Shamaiem Shabbir** for the **CS Girlies Hackathon: AI vs HI** track.
