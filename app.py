import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import io
import os
from dotenv import load_dotenv

# ── Load environment variables from .env ──
load_dotenv()

APP_NAME    = os.getenv("APP_NAME", "LinguaFlow")
APP_TAGLINE = os.getenv("APP_TAGLINE", "Translate anything, instantly — powered by Google Translate")
MAX_CHARS   = int(os.getenv("MAX_CHARS", "5000"))
DEFAULT_TARGET_LANG = os.getenv("DEFAULT_TARGET_LANG", "Telugu")

# ── Page config ──
st.set_page_config(
    page_title=f"{APP_NAME} — Language Translation",
    page_icon="🌐",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ── CSS ──
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;700;800&family=DM+Sans:ital,wght@0,300;0,400;1,300&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    min-height: 100vh;
}

h1 {
    font-family: 'Syne', sans-serif !important;
    font-weight: 800 !important;
    font-size: 3rem !important;
    background: linear-gradient(90deg, #a78bfa, #60a5fa, #34d399);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-align: center;
    letter-spacing: -1px;
    margin-bottom: 0 !important;
}

.subtitle {
    text-align: center;
    color: #94a3b8;
    font-size: 1rem;
    margin-top: -6px;
    margin-bottom: 8px;
    font-style: italic;
}

.intern-badge-wrap {
    text-align: center;
    margin-bottom: 28px;
}

.intern-badge {
    display: inline-block;
    background: rgba(96, 165, 250, 0.12);
    border: 1px solid rgba(96, 165, 250, 0.35);
    color: #93c5fd;
    border-radius: 99px;
    padding: 4px 16px;
    font-size: 0.72rem;
    font-family: 'Syne', sans-serif;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
}

.card {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 20px;
    padding: 28px;
    backdrop-filter: blur(10px);
    margin-bottom: 20px;
}

.result-box {
    background: rgba(167, 139, 250, 0.1);
    border: 1px solid rgba(167, 139, 250, 0.4);
    border-radius: 16px;
    padding: 24px;
    color: #e2e8f0;
    font-size: 1.15rem;
    line-height: 1.8;
    margin-top: 10px;
    min-height: 100px;
    word-break: break-word;
}

label, .stSelectbox label, .stTextArea label {
    color: #a78bfa !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important;
    font-size: 0.82rem !important;
    letter-spacing: 1px !important;
    text-transform: uppercase !important;
}

.stButton > button {
    background: linear-gradient(90deg, #7c3aed, #2563eb);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 12px 32px;
    font-family: 'Syne', sans-serif;
    font-weight: 700;
    font-size: 1rem;
    width: 100%;
    transition: all 0.3s ease;
    letter-spacing: 0.5px;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(124, 58, 237, 0.5);
}

.stTextArea textarea {
    background: rgba(255,255,255,0.07) !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    border-radius: 12px !important;
    color: #e2e8f0 !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 1rem !important;
}

.stSelectbox > div > div {
    background: rgba(255,255,255,0.07) !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    border-radius: 12px !important;
    color: #e2e8f0 !important;
}

.badge-success {
    display: inline-block;
    background: rgba(52, 211, 153, 0.15);
    border: 1px solid rgba(52, 211, 153, 0.4);
    color: #34d399;
    border-radius: 99px;
    padding: 3px 14px;
    font-size: 0.75rem;
    font-family: 'Syne', sans-serif;
    font-weight: 700;
    letter-spacing: 1px;
}

.char-count {
    text-align: right;
    font-size: 0.78rem;
    margin-top: 4px;
}

.char-ok   { color: #64748b; }
.char-warn { color: #f59e0b; }
.char-over { color: #ef4444; }

.swap-hint {
    text-align: center;
    color: #64748b;
    font-size: 0.78rem;
    margin: 6px 0 0;
    font-style: italic;
}

.section-divider {
    border: none;
    border-top: 1px solid rgba(255,255,255,0.08);
    margin: 20px 0;
}

.footer {
    text-align: center;
    color: #475569;
    font-size: 0.75rem;
    margin-top: 40px;
    padding-bottom: 20px;
    font-family: 'DM Sans', sans-serif;
}
</style>
""", unsafe_allow_html=True)

# ── Languages ──
LANGUAGES = {
    "Auto Detect": "auto",
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta",
    "Kannada": "kn",
    "Malayalam": "ml",
    "Bengali": "bn",
    "Gujarati": "gu",
    "Marathi": "mr",
    "Punjabi": "pa",
    "Urdu": "ur",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Italian": "it",
    "Portuguese": "pt",
    "Dutch": "nl",
    "Russian": "ru",
    "Japanese": "ja",
    "Chinese (Simplified)": "zh-CN",
    "Korean": "ko",
    "Arabic": "ar",
    "Turkish": "tr",
    "Polish": "pl",
    "Swedish": "sv",
    "Greek": "el",
}

# Languages supported by gTTS for text-to-speech
TTS_SUPPORTED = {
    "en", "hi", "te", "ta", "kn", "ml", "bn", "gu", "mr",
    "fr", "de", "es", "it", "pt", "ru", "ja", "ko", "ar",
    "zh-CN", "tr", "pl", "nl", "sv",
}

# ── Session state ──
if "history" not in st.session_state:
    st.session_state.history = []

# ── Header ──
st.markdown(f"<h1>🌐 {APP_NAME}</h1>", unsafe_allow_html=True)
st.markdown(f'<p class="subtitle">{APP_TAGLINE}</p>', unsafe_allow_html=True)
st.markdown(
    '<div class="intern-badge-wrap">'
    '<span class="intern-badge">CodeAlpha AI Internship · Task 1</span>'
    '</div>',
    unsafe_allow_html=True,
)

# ── Main card ──
st.markdown('<div class="card">', unsafe_allow_html=True)

# Language selectors
col1, swap_col, col2 = st.columns([5, 1, 5])

with col1:
    source_lang = st.selectbox(
        "Source Language",
        list(LANGUAGES.keys()),
        index=0,
        key="source_lang",
    )

with swap_col:
    st.markdown("<br><br>", unsafe_allow_html=True)
    swap = st.button("⇄", help="Swap languages", key="swap_btn")

with col2:
    target_options = [k for k in LANGUAGES.keys() if k != "Auto Detect"]
    default_idx = target_options.index(DEFAULT_TARGET_LANG) if DEFAULT_TARGET_LANG in target_options else 0
    target_lang = st.selectbox(
        "Target Language",
        target_options,
        index=default_idx,
        key="target_lang",
    )

# Swap logic — rerun with swapped values
if swap:
    if source_lang != "Auto Detect":
        src_name = source_lang
        tgt_name = target_lang
        # Swap via session state
        st.session_state["source_lang"] = tgt_name
        st.session_state["target_lang"] = src_name if src_name in target_options else target_options[0]
        st.rerun()

# Text input
input_text = st.text_area(
    "Enter Text to Translate",
    height=160,
    placeholder="Type or paste your text here… (Tip: supports multi-line text)",
    max_chars=MAX_CHARS,
    key="input_text",
)

# Character count with colour coding
char_count = len(input_text)
pct = char_count / MAX_CHARS
char_class = "char-over" if pct >= 1.0 else "char-warn" if pct >= 0.85 else "char-ok"
st.markdown(
    f'<p class="char-count {char_class}">{char_count:,} / {MAX_CHARS:,} characters</p>',
    unsafe_allow_html=True,
)

translate_btn = st.button("🔄  Translate Now", key="translate_btn")
st.markdown('</div>', unsafe_allow_html=True)

# ── Translation ──
if translate_btn:
    if not input_text.strip():
        st.warning("⚠️ Please enter some text to translate.")
    elif source_lang != "Auto Detect" and source_lang == target_lang:
        st.info("ℹ️ Source and target languages are the same.")
    else:
        with st.spinner("Translating…"):
            try:
                src_code = LANGUAGES[source_lang]
                tgt_code = LANGUAGES[target_lang]

                translator = GoogleTranslator(source=src_code, target=tgt_code)
                result = translator.translate(input_text)

                if not result:
                    st.error("Translation returned empty. Please try again.")
                else:
                    # Save to history
                    st.session_state.history.insert(0, {
                        "src_lang": source_lang,
                        "tgt_lang": target_lang,
                        "source": input_text[:120],
                        "result": result[:120],
                    })
                    st.session_state.history = st.session_state.history[:10]

                    # Result display
                    st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)
                    st.markdown(
                        f'<span class="badge-success">✓ TRANSLATED TO {target_lang.upper()}</span>',
                        unsafe_allow_html=True,
                    )
                    st.markdown(f'<div class="result-box">{result}</div>', unsafe_allow_html=True)

                    st.markdown("<br>", unsafe_allow_html=True)
                    col_copy, col_tts = st.columns(2)

                    with col_copy:
                        st.code(result, language=None)

                    with col_tts:
                        if tgt_code in TTS_SUPPORTED:
                            if st.button("🔊 Listen to Translation", key="tts_btn"):
                                with st.spinner("Generating audio…"):
                                    try:
                                        tts_lang = tgt_code if tgt_code != "zh-CN" else "zh"
                                        tts = gTTS(text=result, lang=tts_lang)
                                        buf = io.BytesIO()
                                        tts.write_to_fp(buf)
                                        buf.seek(0)
                                        st.audio(buf, format="audio/mp3")
                                    except Exception as tts_err:
                                        st.warning(f"Audio generation failed: {tts_err}")
                        else:
                            st.info("🔇 Text-to-speech not available for this language.")

            except Exception as e:
                st.error(f"Translation failed: {str(e)}\n\nPlease check your internet connection and try again.")

# ── Translation History ──
if st.session_state.history:
    st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)
    with st.expander("🕘 Recent Translations", expanded=False):
        for i, entry in enumerate(st.session_state.history):
            col_a, col_b = st.columns([1, 3])
            with col_a:
                st.markdown(
                    f"<small style='color:#a78bfa;font-family:Syne,sans-serif;font-weight:700'>"
                    f"{entry['src_lang']} → {entry['tgt_lang']}</small>",
                    unsafe_allow_html=True,
                )
            with col_b:
                st.markdown(
                    f"<small style='color:#94a3b8'>{entry['source'][:80]}{'…' if len(entry['source']) >= 80 else ''}</small>"
                    f"<br><small style='color:#c4b5fd'>{entry['result'][:80]}{'…' if len(entry['result']) >= 80 else ''}</small>",
                    unsafe_allow_html=True,
                )
            if i < len(st.session_state.history) - 1:
                st.markdown("<hr style='border-color:rgba(255,255,255,0.05);margin:8px 0'>", unsafe_allow_html=True)

        if st.button("🗑️ Clear History"):
            st.session_state.history = []
            st.rerun()

# ── Footer ──
st.markdown(
    '<div class="footer">'
    'Built with Streamlit · deep-translator · gTTS &nbsp;|&nbsp; '
    '<a href="https://github.com/Guna669-coder/LanguageTranslation-app" '
    'style="color:#6366f1;text-decoration:none">GitHub</a>'
    '</div>',
    unsafe_allow_html=True,
)
