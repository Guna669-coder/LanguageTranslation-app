# 🌐 LinguaFlow — Language Translation Tool

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://linguaflow-codealpha.streamlit.app)
![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32+-red?logo=streamlit&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
[![Test & Lint](https://github.com/Guna669-coder/LanguageTranslation-app/actions/workflows/deploy.yml/badge.svg)](https://github.com/Guna669-coder/LanguageTranslation-app/actions/workflows/deploy.yml)

> **CodeAlpha AI Internship — Task 1: Language Translation Tool**

A beautifully designed, browser-based language translation app built with **Streamlit**, **deep-translator**, and **gTTS**. Supports 26+ languages with text-to-speech, translation history, and a sleek dark UI.

---

## 🔗 Live Demo

👉 **[https://linguaflow-codealpha.streamlit.app](https://linguaflow-codealpha.streamlit.app)**

> *After deploying on Streamlit Cloud, update this URL with your actual app URL.*

---

## 🔄 How It Works

```
User enters text
      ↓
Selects source & target language
      ↓
Clicks "Translate Now"
      ↓
deep_translator calls Google Translate API (free, no key needed)
      ↓
Translated text shown in styled result box
      ↓
Optional: gTTS generates audio → st.audio plays it in browser
```

---

## ✨ Features

| Feature | Details |
|---------|---------|
| 🌍 26+ Languages | Incl. Telugu, Hindi, Tamil, French, German, Arabic, Japanese… |
| ⇄ Swap Languages | One-click source ↔ target swap |
| 🔊 Text-to-Speech | Listen to translations via gTTS (23 languages) |
| 📋 Copy Result | Code block for easy copying |
| 🕘 History | Session-based translation history with clear option |
| 📱 Responsive | Works on desktop & mobile |
| 🎨 Dark UI | Gradient dark theme with glassmorphism cards |
| ⚙️ .env Config | App name, default language, char limit — all configurable |

---

## 🗂️ File Structure

```
LanguageTranslation-app/
├── app.py                        # Main Streamlit application
├── requirements.txt              # Python dependencies
├── .env.example                  # Environment variable template ✅ commit this
├── .gitignore                    # Ignores .env, venv, __pycache__, etc.
├── .streamlit/
│   └── config.toml               # Streamlit theme & server config
├── .github/
│   └── workflows/
│       └── deploy.yml            # GitHub Actions CI (syntax + import check)
└── README.md
```

---

## 🚀 Local Development

```bash
# 1. Clone the repo
git clone https://github.com/Guna669-coder/LanguageTranslation-app.git
cd LanguageTranslation-app

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
cp .env.example .env
# Edit .env if you want to change defaults (optional)

# 5. Run the app
streamlit run app.py
# Opens at http://localhost:8501
```

---

## 🌍 Deploy to Streamlit Cloud (Free)

This is the recommended way to deploy Streamlit apps publicly.

### Step 1 — Push to GitHub
Make sure all files are committed and pushed to `main`.

### Step 2 — Sign up at Streamlit Cloud
Go to **[share.streamlit.io](https://share.streamlit.io)** and sign in with your GitHub account.

### Step 3 — Deploy your app
1. Click **"New app"**
2. Select your repo: `Guna669-coder/LanguageTranslation-app`
3. Branch: `main`
4. Main file: `app.py`
5. Click **"Deploy!"**

### Step 4 — Add Secrets (optional)
In your app dashboard → **Settings → Secrets**, add:
```toml
APP_NAME = "LinguaFlow"
APP_TAGLINE = "Translate anything, instantly"
DEFAULT_TARGET_LANG = "Telugu"
MAX_CHARS = "5000"
```

Your app will be live at:
`https://your-app-name.streamlit.app`

---

## ⚙️ Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `APP_NAME` | `LinguaFlow` | App title shown in header |
| `APP_TAGLINE` | `Translate anything…` | Subtitle shown below header |
| `MAX_CHARS` | `5000` | Max input character limit |
| `DEFAULT_TARGET_LANG` | `Telugu` | Default target language on load |

Copy `.env.example` → `.env` for local use. For Streamlit Cloud, use the Secrets panel.

---

## 📦 Dependencies

| Package | Purpose |
|---------|---------|
| `streamlit` | Web UI framework |
| `deep-translator` | Google Translate API wrapper (free, no key) |
| `gTTS` | Google Text-to-Speech audio generation |
| `python-dotenv` | Load `.env` variables |

---

## 🧠 Tech Stack

- **Python 3.11**
- **Streamlit** — UI framework
- **deep-translator** — Translation (Google Translate, no API key required)
- **gTTS** — Text-to-speech in 23 languages
- **GitHub Actions** — CI pipeline (syntax check on every push)
- **Streamlit Cloud** — Free hosting

---

## 📌 CodeAlpha Internship

Built as part of the **CodeAlpha AI Internship Program**
- ✅ **Task 1: Language Translation Tool** ← *this repo*
- 🔗 Task 2: [CodeAlpha_ChatbotFAQ](https://github.com/Guna669-coder/CodeAlpha_ChatbotFAQ)
- 🔗 Task 4: [CodeAlpha_ObjectDetectionTracking](https://github.com/Guna669-coder/CodeAlpha_ObjectDetectionTracking)
