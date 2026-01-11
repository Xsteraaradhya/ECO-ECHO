import streamlit as st
from datetime import date

# ------------------ CONFIG ------------------
st.set_page_config(
    page_title="Eco-Echo",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------ CSS ------------------
st.markdown("""
<style>

/* GLOBAL FONT & COLOR */
* {
    font-family: "Times New Roman", serif !important;
    color: #0b3d2e !important;
}

/* PAGE BACKGROUND */
.stApp {
    background: linear-gradient(180deg, #f7fff9, #fff5fa);
}

/* HIDE STREAMLIT UI */
header, footer {visibility: hidden;}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background: #ffffff;
    border-right: 2px solid #b7e4c7;
}

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] label {
    font-weight: bold;
}

/* NAV BAR */
.nav-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 15px 5%;
    background: #ffffff;
    border-bottom: 3px solid #95d5b2;
    position: sticky;
    top: 0;
    z-index: 1000;
}

.logo {
    display: flex;
    align-items: center;
    font-size: 26px;
    font-weight: bold;
}

.logo span {
    font-size: 30px;
    margin-right: 10px;
    color: #1b5e20;
}

.nav-links a {
    margin-left: 25px;
    text-decoration: none;
    font-weight: bold;
}

.book-btn {
    background: #1b5e20;
    color: white !important;
    padding: 10px 25px;
    border-radius: 25px;
    text-decoration: none;
}

/* HERO */
.hero {
    text-align: center;
    padding: 90px 5%;
}

.hero h1 {
    font-size: 4rem;
}

.hero p {
    font-size: 1.3rem;
    max-width: 650px;
    margin: 20px auto;
}

/* BUTTONS */
.hero-btn {
    background: #2d6a4f;
    color: white !important;
    padding: 15px 35px;
    border-radius: 30px;
    text-decoration: none;
    font-weight: bold;
}

.hero-btn-secondary {
    background: transparent;
    border: 2px solid #2d6a4f;
}

/* CARDS */
.card {
    background: #ffffff;
    border-radius: 20px;
    padding: 30px;
    border: 2px solid #d8f3dc;
    box-shadow: 0 8px 20px rgba(0,0,0,0.05);
}

.card h3 {
    font-weight: bold;
}

/* PLANT */
.plant-container {
    background: #ffffff;
    padding: 50px;
    border-radius: 30px;
    border: 3px solid #b7e4c7;
}

.plant-img {
    width: 280px;
    height: 280px;
    border-radius: 50%;
    border: 6px solid #d8f3dc;
}

/* RESPONSIVE */
@media (max-width: 768px) {
    .hero h1 { font-size: 2.6rem; }
    .nav-links { display: none; }
}

</style>
""", unsafe_allow_html=True)

# ------------------ NAV BAR ------------------
st.markdown("""
<div class="nav-bar">
    <div class="logo">
        <span>🎀</span> EcoVista
    </div>
    <div class="nav-links">
        <a href="#">Home</a>
        <a href="#">About</a>
        <a href="#">Experiences</a>
        <a href="#">Sustainability</a>
    </div>
    <a href="#" class="book-btn">Book Now</a>
</div>
""", unsafe_allow_html=True)

# ------------------ SIDEBAR ------------------
st.sidebar.title("Navigation 🎀")

page = st.sidebar.radio(
    "Go to",
    ["Home", "Plant Care", "Daily Plant", "Earth Today", "Global Action"]
)

# ------------------ PAGES ------------------

if page == "Home":
    st.markdown("""
    <div class="hero">
        <h1>Step Into the Stillness of Nature</h1>
        <p>Rediscover the outdoors through immersive, mindful, and sustainable experiences.</p>
        <a class="hero-btn">Explore Journeys</a>
        <br><br>
        <a class="hero-btn hero-btn-secondary">Our Mission</a>
    </div>
    """, unsafe_allow_html=True)

elif page == "Plant Care":
    st.markdown("## 🌿 Plant Care Essentials")
    st.markdown("""
    <div class="card">
        <h3>Watering</h3>
        <p>Allow soil to partially dry before watering.</p>
    </div>
    """, unsafe_allow_html=True)

elif page == "Daily Plant":
    if "stage" not in st.session_state:
        st.session_state.stage = 0
        st.session_state.last = None
        st.session_state.watered = False

    today = date.today()
    if st.session_state.last != today:
        st.session_state.watered = False
        st.session_state.last = today

    images = [
        "https://images.unsplash.com/photo-1520412099551-62b6bafeb5bb",
        "https://images.unsplash.com/photo-1509423350716-97f9360b4e09",
        "https://images.unsplash.com/photo-1616690248973-098a5e08c8c7",
        "https://images.unsplash.com/photo-1518531933037-91b2f5f229cc"
    ]

    st.markdown(f"""
    <div class="plant-container">
        <img src="{images[st.session_state.stage]}" class="plant-img">
    </div>
    """, unsafe_allow_html=True)

    if not st.session_state.watered:
        if st.button("💧 Nurture Plant"):
            st.session_state.stage = min(3, st.session_state.stage + 1)
            st.session_state.watered = True
            st.success("Growth complete for today.")

elif page == "Earth Today":
    st.markdown("## 🌍 Earth Today")
    st.write("Global restoration and sustainability initiatives continue worldwide.")

elif page == "Global Action":
    st.markdown("## 🌱 Global Action")
    st.write("Communities across the world are investing in renewable futures.")
