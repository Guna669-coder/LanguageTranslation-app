import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import base64
import io

st.set_page_config(page_title="Language Translation", page_icon="🌐", layout="centered")

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
}

.subtitle {
    text-align: center;
    color: #94a3b8;
    font-size: 1rem;
    margin-top: -10px;
    margin-bottom: 30px;
    font-style: italic;
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
    line-height: 1.7;
    margin-top: 10px;
    min-height: 100px;
}

label, .stSelectbox label, .stTextArea label {
    color: #a78bfa !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important;
    font-size: 0.85rem !important;
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
}

.stSelectbox > div > div {
    background: rgba(255,255,255,0.07) !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    border-radius: 12px !important;
    color: #e2e8f0 !important;
}

.badge {
    display: inline-block;
    background: rgba(52, 211, 153, 0.15);
    border: 1px solid rgba(52, 211, 153, 0.4);
    color: #34d399;
    border-radius: 99px;
    padding: 3px 12px;
    font-size: 0.75rem;
    font-family: 'Syne', sans-serif;
    font-weight: 700;
    letter-spacing: 1px;
}

.char-count {
    text-align: right;
    color: #64748b;
    font-size: 0.78rem;
    margin-top: 4px;
}
</style>
""", unsafe_allow_html=True)

LANGUAGES = {
    "Auto Detect": "auto",
    "English": "en", "Hindi": "hi", "Telugu": "te", "Tamil": "ta",
    "Kannada": "kn", "Malayalam": "ml", "Bengali": "bn", "Gujarati": "gu",
    "Marathi": "mr", "Punjabi": "pa", "Urdu": "ur",
    "French": "fr", "German": "de", "Spanish": "es", "Italian": "it",
    "Portuguese": "pt", "Dutch": "nl", "Russian": "ru", "Japanese": "ja",
    "Chinese (Simplified)": "zh-CN", "Korean": "ko", "Arabic": "ar",
    "Turkish": "tr", "Polish": "pl", "Swedish": "sv", "Greek": "el",
}

TTS_SUPPORTED = ["en", "hi", "fr", "de", "es", "it", "pt", "ru", "ja", "ko", "ar", "zh-CN"]

st.markdown("<h1>🌐 Language Translation</h1>", unsafe_allow_html=True)
st.markdown('<p class="subtitle">Translate anything, instantly — powered by Google Translate</p>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        source_lang = st.selectbox("Source Language", list(LANGUAGES.keys()), index=0)
    with col2:
        target_options = [k for k in LANGUAGES.keys() if k != "Auto Detect"]
        target_lang = st.selectbox("Target Language", target_options, index=target_options.index("Telugu") if "Telugu" in target_options else 0)

    input_text = st.text_area("Enter Text to Translate", height=150, placeholder="Type or paste your text here...")
    char_count = len(input_text)
    st.markdown(f'<p class="char-count">{char_count} / 5000 characters</p>', unsafe_allow_html=True)

    translate_btn = st.button("🔄 Translate Now")
    st.markdown('</div>', unsafe_allow_html=True)

if translate_btn:
    if not input_text.strip():
        st.warning("⚠️ Please enter some text to translate.")
    else:
        with st.spinner("Translating..."):
            try:
                src_code = LANGUAGES[source_lang]
                tgt_code = LANGUAGES[target_lang]
                translator = GoogleTranslator(source=src_code, target=tgt_code)
                result = translator.translate(input_text)

                st.markdown("---")
                st.markdown(f'<span class="badge">✓ TRANSLATED TO {target_lang.upper()}</span>', unsafe_allow_html=True)
                st.markdown(f'<div class="result-box">{result}</div>', unsafe_allow_html=True)

                col_copy, col_tts = st.columns(2)

                with col_copy:
                    st.code(result, language=None)

                with col_tts:
                    if tgt_code in TTS_SUPPORTED:
                        if st.button("🔊 Listen to Translation"):
                            tts = gTTS(text=result, lang=tgt_code)
                            buf = io.BytesIO()
                            tts.write_to_fp(buf)
                            buf.seek(0)
                            st.audio(buf, format="audio/mp3")
                    else:
                        st.info("TTS not available for this language.")

            except Exception as e:
                st.error(f"Translation failed: {str(e)}")
