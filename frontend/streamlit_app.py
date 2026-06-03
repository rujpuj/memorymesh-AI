from __future__ import annotations

from html import escape

import requests
import streamlit as st


st.set_page_config(page_title="MemoryMesh AI", page_icon="M", layout="wide")

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');

:root {
    --ink: #f7f2e8;
    --muted: #aeb8bd;
    --panel: rgba(16, 20, 24, 0.74);
    --panel-strong: rgba(20, 24, 29, 0.92);
    --line: rgba(247, 242, 232, 0.14);
    --red: #ff4d5b;
    --teal: #29d6c6;
    --gold: #e7b75f;
    --blue: #6ca8ff;
}

html, body, [class*="css"] {
    font-family: "Inter", system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

.stApp {
    color: var(--ink);
    background:
        linear-gradient(115deg, rgba(255, 77, 91, 0.08), transparent 24%),
        linear-gradient(245deg, rgba(41, 214, 198, 0.09), transparent 28%),
        radial-gradient(circle at 50% 0%, rgba(231, 183, 95, 0.08), transparent 34%),
        #07090d;
}

.stApp::before {
    content: "";
    position: fixed;
    inset: 0;
    pointer-events: none;
    background:
        linear-gradient(rgba(255, 255, 255, 0.035) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255, 255, 255, 0.025) 1px, transparent 1px);
    background-size: 54px 54px;
    mask-image: linear-gradient(to bottom, rgba(0, 0, 0, 0.84), transparent 86%);
}

.stApp::after {
    animation: filmSweep 9s linear infinite;
    background: repeating-linear-gradient(
        90deg,
        rgba(255, 255, 255, 0.028) 0,
        rgba(255, 255, 255, 0.028) 1px,
        transparent 1px,
        transparent 9px
    );
    content: "";
    inset: 0;
    opacity: 0.26;
    pointer-events: none;
    position: fixed;
}

@keyframes filmSweep {
    from { transform: translateX(-64px); }
    to { transform: translateX(64px); }
}

section[data-testid="stSidebar"] {
    background: rgba(17, 20, 27, 0.92);
    border-right: 1px solid var(--line);
}

section[data-testid="stSidebar"] input {
    background: #080b10;
    border: 1px solid rgba(247, 242, 232, 0.12);
}

.main .block-container {
    max-width: 1280px;
    padding-top: 3.2rem;
}

h1, h2, h3, p {
    letter-spacing: 0;
}

.cinema-hero {
    border: 1px solid var(--line);
    border-radius: 8px;
    background:
        linear-gradient(135deg, rgba(255, 77, 91, 0.15), transparent 30%),
        linear-gradient(90deg, rgba(41, 214, 198, 0.12), transparent 58%),
        rgba(11, 14, 20, 0.78);
    box-shadow: 0 28px 80px rgba(0, 0, 0, 0.38);
    margin-bottom: 1.4rem;
    overflow: hidden;
    padding: 2rem;
    position: relative;
}

.hero-grid {
    align-items: center;
    display: grid;
    gap: 1.5rem;
    grid-template-columns: minmax(0, 1.45fr) minmax(280px, 0.7fr);
    position: relative;
    z-index: 1;
}

.ai-visual {
    aspect-ratio: 1 / 1;
    background:
        radial-gradient(circle at 50% 50%, rgba(41, 214, 198, 0.18), transparent 34%),
        linear-gradient(135deg, rgba(255, 255, 255, 0.09), rgba(255, 255, 255, 0.02));
    border: 1px solid rgba(247, 242, 232, 0.16);
    border-radius: 8px;
    box-shadow: inset 0 0 38px rgba(41, 214, 198, 0.1), 0 20px 60px rgba(0, 0, 0, 0.26);
    overflow: hidden;
    position: relative;
}

.ai-visual img {
    height: 100%;
    object-fit: cover;
    opacity: 0.9;
    width: 100%;
}

.ai-visual::after {
    background:
        linear-gradient(180deg, transparent, rgba(7, 9, 13, 0.35)),
        repeating-linear-gradient(0deg, rgba(255, 255, 255, 0.055) 0 1px, transparent 1px 7px);
    content: "";
    inset: 0;
    pointer-events: none;
    position: absolute;
}

.ai-core {
    animation: coreFloat 5s ease-in-out infinite;
    background:
        radial-gradient(circle, rgba(247, 242, 232, 0.95) 0 6%, transparent 7%),
        conic-gradient(from 120deg, var(--red), var(--gold), var(--teal), var(--blue), var(--red));
    border-radius: 50%;
    filter: saturate(1.25);
    height: 62%;
    left: 19%;
    position: absolute;
    top: 18%;
    width: 62%;
}

.ai-core::before,
.ai-core::after {
    border: 1px solid rgba(247, 242, 232, 0.32);
    border-radius: 50%;
    content: "";
    inset: 13%;
    position: absolute;
}

.ai-core::before {
    animation: orbit 6s linear infinite;
}

.ai-core::after {
    animation: orbit 9s linear infinite reverse;
    inset: -9%;
}

@keyframes coreFloat {
    0%, 100% { transform: translateY(0) scale(1); }
    50% { transform: translateY(-8px) scale(1.04); }
}

@keyframes orbit {
    from { transform: rotate(0deg) scaleX(1.24); }
    to { transform: rotate(360deg) scaleX(1.24); }
}

.cinema-hero::before {
    animation: scanline 5.5s ease-in-out infinite;
    background: linear-gradient(90deg, transparent, rgba(247, 242, 232, 0.24), transparent);
    content: "";
    height: 1px;
    left: -20%;
    position: absolute;
    top: 24%;
    width: 140%;
}

.cinema-hero::after {
    animation: pulseTrack 6s ease-in-out infinite;
    background:
        linear-gradient(90deg, var(--red), var(--gold), var(--teal), var(--blue));
    bottom: 0;
    content: "";
    height: 3px;
    left: 0;
    position: absolute;
    transform-origin: left;
    width: 100%;
}

@keyframes scanline {
    0%, 100% { opacity: 0; transform: translateY(-34px); }
    35%, 65% { opacity: 1; }
    50% { transform: translateY(150px); }
}

@keyframes pulseTrack {
    0%, 100% { transform: scaleX(0.36); opacity: 0.72; }
    50% { transform: scaleX(1); opacity: 1; }
}

.eyebrow {
    color: var(--gold);
    font-size: 0.78rem;
    font-weight: 800;
    letter-spacing: 0.14em;
    text-transform: uppercase;
}

.hero-title {
    color: var(--ink);
    font-size: clamp(2.2rem, 5vw, 5.1rem);
    font-weight: 800;
    line-height: 0.95;
    margin: 0.5rem 0 1rem;
}

.hero-copy {
    color: var(--muted);
    font-size: 1rem;
    max-width: 760px;
}

.stat-row {
    display: grid;
    gap: 0.8rem;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    margin-top: 1.3rem;
}

.stat-card {
    background: rgba(255, 255, 255, 0.045);
    border: 1px solid var(--line);
    border-radius: 8px;
    padding: 0.9rem 1rem;
}

.stat-label {
    color: var(--muted);
    font-size: 0.78rem;
}

.stat-value {
    color: var(--ink);
    font-size: 1.35rem;
    font-weight: 800;
    margin-top: 0.2rem;
}

.memory-frame {
    background: var(--panel);
    border: 1px solid var(--line);
    border-radius: 8px;
    padding: 1.2rem;
}

.section-kicker {
    color: var(--teal);
    font-size: 0.76rem;
    font-weight: 800;
    letter-spacing: 0.11em;
    margin-bottom: 0.5rem;
    text-transform: uppercase;
}

.section-title {
    color: var(--ink);
    font-size: 1.25rem;
    font-weight: 800;
    margin-bottom: 0.4rem;
}

.section-copy {
    color: var(--muted);
    margin-bottom: 1rem;
}

div[data-testid="stTabs"] button {
    color: var(--muted);
    font-weight: 700;
}

div[data-testid="stTabs"] button[aria-selected="true"] {
    color: var(--ink);
}

div[data-testid="stTabs"] [data-baseweb="tab-highlight"] {
    background: linear-gradient(90deg, var(--red), var(--gold), var(--teal));
}

.stTextArea textarea, .stTextInput input, .stNumberInput input {
    background: rgba(7, 10, 15, 0.82);
    border: 1px solid rgba(247, 242, 232, 0.14);
    border-radius: 8px;
    color: var(--ink);
}

.stTextArea textarea:focus, .stTextInput input:focus, .stNumberInput input:focus {
    border-color: rgba(41, 214, 198, 0.72);
    box-shadow: 0 0 0 1px rgba(41, 214, 198, 0.42);
}

.stSlider [data-testid="stTickBar"] {
    display: none;
}

.stButton > button {
    border-radius: 8px;
    font-weight: 800;
    min-height: 2.9rem;
}

.stButton > button[kind="primary"] {
    background: linear-gradient(90deg, #ff4d5b, #e7b75f);
    border: 0;
    color: #080b10;
}

.stButton > button:not([kind="primary"]) {
    background: rgba(255, 255, 255, 0.035);
    border: 1px solid rgba(247, 242, 232, 0.18);
    color: var(--ink);
}

[data-testid="stDataFrame"] {
    border: 1px solid var(--line);
    border-radius: 8px;
    overflow: hidden;
}

@media (max-width: 760px) {
    .main .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }

    .cinema-hero {
        padding: 1.2rem;
    }

    .stat-row {
        grid-template-columns: 1fr;
    }

    .hero-grid {
        grid-template-columns: 1fr;
    }
}
</style>
"""


def api_get(path: str) -> requests.Response:
    response = requests.get(f"{API_URL}{path}", timeout=10)
    response.raise_for_status()
    return response


def api_post(path: str, payload: dict) -> requests.Response:
    response = requests.post(f"{API_URL}{path}", json=payload, timeout=10)
    response.raise_for_status()
    return response


def render_hero(memory_count: int, correction_count: int, ai_gif_url: str) -> None:
    safe_gif_url = escape(ai_gif_url.strip(), quote=True)
    visual = (
        f'<img src="{safe_gif_url}" alt="MemoryMesh AI animated identity">'
        if safe_gif_url
        else '<div class="ai-core"></div>'
    )
    st.markdown(
        f"""
        <div class="cinema-hero">
            <div class="hero-grid">
                <div>
                    <div class="eyebrow">Adaptive recall engine</div>
                    <div class="hero-title">MemoryMesh AI</div>
                    <div class="hero-copy">
                        Capture what matters, compress it into sharp context, and retrieve it like a living
                        cinematic timeline for your next answer.
                    </div>
                    <div class="stat-row">
                        <div class="stat-card">
                            <div class="stat-label">Stored memories</div>
                            <div class="stat-value">{memory_count}</div>
                        </div>
                        <div class="stat-card">
                            <div class="stat-label">Corrections learned</div>
                            <div class="stat-value">{correction_count}</div>
                        </div>
                        <div class="stat-card">
                            <div class="stat-label">Retrieval mode</div>
                            <div class="stat-value">Live</div>
                        </div>
                    </div>
                </div>
                <div class="ai-visual">{visual}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
def section_intro(kicker: str, title: str, copy: str) -> None:
    st.markdown(
        f"""
        <div class="memory-frame">
            <div class="section-kicker">{kicker}</div>
            <div class="section-title">{title}</div>
            <div class="section-copy">{copy}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


with st.sidebar:
    st.markdown("### Control Room")
    API_URL = st.text_input("API URL", "http://localhost:8000")
    ai_gif_url = st.text_input(
        "AI GIF URL",
        "",
        placeholder="Paste a Giphy, Tenor, or .gif URL",
        help="Use a direct animated GIF URL to brand the hero panel. Leave blank for the built-in AI animation.",
    )
    try:
        api_get("/health")
        st.success("Backend online")
    except requests.RequestException:
        st.warning("Backend not reachable")

try:
    memories = api_get("/memories").json()
except requests.RequestException:
    memories = []

try:
    corrections = api_get("/corrections").json()
except requests.RequestException:
    corrections = []

st.markdown(CSS, unsafe_allow_html=True)
render_hero(memory_count=len(memories), correction_count=len(corrections), ai_gif_url=ai_gif_url)

memory_tab, retrieve_tab, corrections_tab = st.tabs(["Memories", "Retrieve", "Corrections"])

with memory_tab:
    section_intro(
        "Scene capture",
        "Store a new memory",
        "Write the raw moment once. MemoryMesh will compress it into a cleaner recall fragment.",
    )
    content = st.text_area("New memory", height=180, placeholder="Example: The user likes polished cinematic UI with motion and depth.")
    col_a, col_b = st.columns([2, 1])
    with col_a:
        importance = st.slider("Importance", 0.0, 1.0, 0.5, 0.05)
    with col_b:
        st.write("")
        st.write("")
        save_clicked = st.button("Save memory", type="primary", use_container_width=True)

    if save_clicked:
        try:
            api_post("/memories", {"content": content, "importance": importance})
            st.success("Memory saved.")
        except requests.RequestException as exc:
            st.error(f"Could not save memory: {exc}")

    if st.button("Refresh memories", use_container_width=True):
        try:
            memories = api_get("/memories").json()
        except requests.RequestException as exc:
            st.error(f"Could not load memories: {exc}")

    if memories:
        st.dataframe(memories, use_container_width=True, hide_index=True)
    else:
        st.info("No memories stored yet.")

with retrieve_tab:
    section_intro(
        "Recall sequence",
        "Retrieve context",
        "Search the mesh and assemble the strongest memory fragments into a prompt-ready context block.",
    )
    col_a, col_b = st.columns([3, 1])
    with col_a:
        query = st.text_input("Search query", placeholder="What should the assistant remember?")
    with col_b:
        limit = st.number_input("Limit", min_value=1, max_value=25, value=5)

    if st.button("Retrieve context", type="primary", use_container_width=True):
        try:
            result = api_post("/retrieve", {"query": query, "limit": limit}).json()
            st.code(result["context"] or "No matching memories yet.", language="text")
            st.dataframe(result["memories"], use_container_width=True, hide_index=True)
        except requests.RequestException as exc:
            st.error(f"Could not retrieve context: {exc}")

with corrections_tab:
    section_intro(
        "Learning room",
        "Teach the system from corrections",
        "Save feedback so future responses can bend toward your preferred answer style and facts.",
    )
    prompt = st.text_area("Prompt", height=110)
    answer = st.text_area("Answer", height=110)
    correction = st.text_area("Correction", height=110)
    if st.button("Save correction", type="primary", use_container_width=True):
        try:
            api_post(
                "/corrections",
                {"prompt": prompt, "answer": answer, "correction": correction},
            )
            st.success("Correction saved.")
        except requests.RequestException as exc:
            st.error(f"Could not save correction: {exc}")
