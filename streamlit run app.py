import streamlit as st
from datetime import date
# ------------------ CONFIG ------------------
st.set_page_config(
    page_title="Eco-Echo",
    page_icon="🌿",
    layout="wide"
)
# ------------------ ADVANCED CINEMATIC CSS ------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;700&family=Inter:wght@300;400;600&display=swap');
html, body {
    margin: 0;
    padding: 0;
    background-color: #0c1f16;
    color: #eef5f0;
    font-family: 'Inter', sans-serif;
}
header, footer {visibility: hidden;}
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0c1f16, #143527);
    color: #eaf5ee;
}
h1, h2, h3 {
    font-family: 'Playfair Display', serif;
}
/* HERO */
.hero {
    height: 92vh;
    background:
        linear-gradient(rgba(12,31,22,0.55), rgba(12,31,22,0.85)),
        url("https://images.unsplash.com/photo-1500530855697-b586d89ba3ee");
    background-size: cover;
    background-position: center;
    display: flex;
    align-items: center;
    padding-left: 8%;
}
.hero-content h1 {
    font-size: 72px;
    line-height: 1.05;
}
.hero-content p {
    max-width: 520px;
    font-size: 18px;
    opacity: 0.85;
}
/* BUTTON */
.cta {
    margin-top: 30px;
    display: inline-block;
    padding: 14px 34px;
    border-radius: 40px;
    background: #8cc9a3;
    color: #0c1f16;
    font-weight: 600;
}
/* GLASS SECTIONS */
.glass {
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(14px);
    border-radius: 24px;
    padding: 40px;
    margin-bottom: 40px;
}
/* GRID */
.grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 30px;
}
/* CARDS */
.card img {
    width: 100%;
    border-radius: 18px;
}
.card p {
    opacity: 0.85;
}
/* GAME IMAGE */
.plant {
    width: 260px;
    margin-bottom: 20px;
    border-radius: 20px;
}
.stButton>button {
    background: linear-gradient(135deg, #9fd9b8, #6ca98a);
    border-radius: 30px;
    border: none;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)
# ------------------ SIDEBAR ------------------
st.sidebar.title("🌿 Eco-Echo")
page = st.sidebar.radio(
    "Explore",
    ["Home", "Plant Care", "Daily Plant", "Earth Today", "Global Action"]
)
# ------------------ HOME ------------------
if page == "Home":
    st.markdown("""
    <div class="hero">
        <div class="hero-content">
            <h1>Step Into the<br>Stillness of Nature</h1>
            <p>
                Step into a world where forests breathe softly and the planet
                reveals its quiet strength through light, growth, and balance.
            </p>
            <span class="cta">Explore the Earth</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="glass">
        <h2>Think Outside. No Box Required.</h2>
        <p>
            Eco-Echo is a calm digital sanctuary designed to reconnect people with
            nature through mindful interaction, environmental awareness, and
            small daily actions that grow into lasting change.
        </p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="grid">
        <div class="card">
            <img src="https://images.unsplash.com/photo-1469474968028-56623f02e42e">
            <p>Forests & Biodiversity</p>
        </div>
        <div class="card">
            <img src="https://images.unsplash.com/photo-1500530855697-b586d89ba3ee">
            <p>Planet Earth Ecosystems</p>
        </div>
        <div class="card">
            <img src="https://images.unsplash.com/photo-1483729558449-99ef09a8c325">
            <p>Sustainable Futures</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
# ------------------ PLANT CARE ------------------
elif page == "Plant Care":
    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    st.header("🌱 Plant Care Essentials")
    st.markdown("""
    Plants thrive when we slow down enough to notice them.
    Water during cooler hours, allow the soil to breathe,
    offer gentle sunlight, and observe changes patiently.
    Caring for plants is less about control and more about attention.
    """)
    st.markdown("</div>", unsafe_allow_html=True)
# ------------------ DAILY PLANT ------------------
elif page == "Daily Plant":
    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    st.header("🌿 Grow Your Plant")
    if "stage" not in st.session_state:
        st.session_state.stage = 0
        st.session_state.last = None
        st.session_state.watered = False
    today = date.today()
    if st.session_state.last != today:
        st.session_state.watered = False
        st.session_state.last = today
    images = [
        "https://images.unsplash.com/photo-1501004318641-b39e6451bec6", # seed
        "https://images.unsplash.com/photo-1524593166156-312f362cada0", # sprout
        "https://images.unsplash.com/photo-1500534314209-a25ddb2bd429", # young tree
        "https://images.unsplash.com/photo-1501785888041-af3ef285b470" # forest
    ]
    st.markdown(f'<img src="{images[st.session_state.stage]}" class="plant">', unsafe_allow_html=True)
    if not st.session_state.watered:
        if st.button("💧 Water Plant"):
            st.session_state.watered = True
            st.session_state.stage = min(3, st.session_state.stage + 1)
            st.success("Growth takes patience. The plant responds 🌱")
    else:
        st.info("Return tomorrow to continue the journey")
    st.markdown("</div>", unsafe_allow_html=True)
# ------------------ EARTH TODAY ------------------
elif page == "Earth Today":
    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    st.header("🌍 Planet Earth Today")
    st.markdown("""
    Across the globe, forests are being restored, renewable energy is reshaping
    cities, and communities are rethinking how they coexist with nature.
    Progress unfolds quietly, rooted in awareness and shared responsibility.
    """)
    st.markdown("</div>", unsafe_allow_html=True)
# ------------------ GLOBAL ACTION ------------------
elif page == "Global Action":
    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    st.header("🌎 Global Environmental Action")
    st.markdown("""
    From Costa Rica’s rainforest protection to Germany’s renewable leadership,
    nations around the world are proving that sustainability and progress can
    grow together when guided by long-term vision.
    """)
    st.markdown("</div>", unsafe_allow_html=True)
# ------------------ FOOTER ------------------
st.markdown("""
<p style="text-align:center; opacity:0.6; margin:50px 0;">
Eco-Echo 🌿 — Inspired by forests, built for the future
</p>
""", unsafe_allow_html=True)
