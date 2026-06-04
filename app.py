import streamlit as st
from utils.ai_engine import generate_research_paper

st.set_page_config(
    page_title="ResearchGenAI",
    page_icon="🔬",
    layout="centered",
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Space Grotesk', sans-serif;
    }

    .stApp {
        background-color: #0d0d0f;
        color: #e8e8f0;
    }

    .main-title {
        text-align: center;
        font-size: 2.8rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 0.2rem;
        letter-spacing: -0.5px;
    }

    .subtitle {
        text-align: center;
        color: #8888aa;
        font-size: 1rem;
        margin-bottom: 2.5rem;
    }

    .section-card {
        background: #13131a;
        border: 1px solid #2a2a3a;
        border-radius: 12px;
        padding: 1.5rem 1.8rem;
        margin-bottom: 1.2rem;
    }

    .section-card h3 {
        color: #a78bfa;
        font-size: 1rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 0.6rem;
    }

    .section-card p, .section-card li {
        color: #c8c8d8;
        font-size: 0.95rem;
        line-height: 1.75;
    }

    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        background-color: #ffffff !important;
        color: #000000 !important;
        border: 1.5px solid #3a3a5c !important;
        border-radius: 8px !important;
        font-family: 'Space Grotesk', sans-serif !important;
        font-size: 0.95rem !important;
    }

    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: #7c3aed !important;
        box-shadow: 0 0 0 2px rgba(124, 58, 237, 0.2) !important;
    }

    label {
        color: #c8c8d8 !important;
        font-size: 0.9rem !important;
        font-weight: 500 !important;
    }

    div.stButton > button {
        background: linear-gradient(135deg, #7c3aed, #5b21b6);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.65rem 2.2rem;
        font-size: 1rem;
        font-weight: 600;
        font-family: 'Space Grotesk', sans-serif;
        width: 100%;
        cursor: pointer;
        transition: all 0.2s ease;
    }

    div.stButton > button:hover {
        background: linear-gradient(135deg, #6d28d9, #4c1d95);
        transform: translateY(-1px);
        box-shadow: 0 4px 20px rgba(124, 58, 237, 0.4);
    }

    div.stButton > button:active {
        transform: translateY(0px);
    }

    .output-header {
        color: #a78bfa;
        font-size: 1.4rem;
        font-weight: 700;
        border-bottom: 2px solid #2a2a3a;
        padding-bottom: 0.6rem;
        margin-bottom: 1.2rem;
    }

    .stAlert {
        background-color: #1a0a2e !important;
        border: 1px solid #7c3aed !important;
        border-radius: 8px !important;
    }

    .stMarkdown h2 {
        color: #a78bfa;
        font-size: 1.2rem;
        font-weight: 700;
        margin-top: 1.5rem;
        margin-bottom: 0.5rem;
        border-left: 3px solid #7c3aed;
        padding-left: 0.8rem;
    }

    .stMarkdown p, .stMarkdown li {
        color: #c8c8d8;
        font-size: 0.95rem;
        line-height: 1.8;
    }

    .divider {
        border: none;
        border-top: 1px solid #2a2a3a;
        margin: 1.5rem 0;
    }

    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)


# ── Header ──────────────────────────────────────────────────────────────────
st.markdown('<div class="main-title">🔬 ResearchGenAI</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Generate academic research papers instantly with Gemini AI</div>', unsafe_allow_html=True)
st.markdown('<hr class="divider">', unsafe_allow_html=True)


# ── Input Form ───────────────────────────────────────────────────────────────
topic = st.text_input(
    "Research Topic",
    placeholder="e.g. Machine Learning in Healthcare Diagnostics",
)

keywords = st.text_input(
    "Keywords",
    placeholder="e.g. deep learning, neural networks, medical imaging, diagnosis",
)

generate_clicked = st.button("⚡ Generate Research Paper")


# ── Generation Logic ─────────────────────────────────────────────────────────
if generate_clicked:
    if not topic.strip():
        st.warning("⚠️ Please enter a research topic.")
    elif not keywords.strip():
        st.warning("⚠️ Please enter at least one keyword.")
    else:
        with st.spinner("Generating your research paper with Gemini AI..."):
            try:
                result = generate_research_paper(topic.strip(), keywords.strip())
                st.markdown('<hr class="divider">', unsafe_allow_html=True)
                st.markdown('<div class="output-header">📄 Generated Research Paper</div>', unsafe_allow_html=True)
                st.markdown(result)
            except ValueError as e:
                st.error(f"🔑 API Key Error: {str(e)}")
            except RuntimeError as e:
                st.error(f"❌ Generation Error: {str(e)}")
            except Exception as e:
                st.error(f"❌ Unexpected error: {str(e)}")
