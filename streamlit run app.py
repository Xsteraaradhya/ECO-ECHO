import streamlit as st
from datetime import date

# ------------------ CONFIG ------------------
st.set_page_config(
    page_title="Eco-Echo",
    page_icon="🌿🌍🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------ CSS ------------------
st.markdown("""
<style>
/* FONTS */
@import url('https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,300;0,400;0,500;0,700;1,400&display=swap');

/* GLOBAL RESETS */
html, body, [class="css-1d391kg"] {
    margin: 0;
    padding: 0;
    background-color: #f9fbf9;
    color: #2c3e50;
    font-family: 'Roboto', sans-serif;
}

/* HIDING DEFAULT STREAMLIT ELEMENTS */
header, footer {visibility: hidden;}

/* MAIN APP BACKGROUND */
.stApp {
    background: linear-gradient(to bottom, rgba(255,255,255,0.9), rgba(255,255,255,0.95)), 
        url("https://www.pexels.com/photo/white-windmill-414837/");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* SIDEBAR CUSTOMIZATION (To match the clean theme) */
section[data-testid="stSidebar"] {
    background: #ffffff;
    border-right: 1px solid #e0e0e0;
    padding-top: 20px;
}

section[data-testid="stSidebar"] .css-ng1t4o {
    color: #196f3d;
    font-weight: 700;
    font-size: 1.2rem;
    margin-bottom: 20px;
}

section[data-testid="stSidebar"] label {
    color: #555;
    font-size: 1rem;
    padding: 10px 0;
}

section[data-testid="stSidebar"] label:hover {
    color: #196f3d;
    background: #f0fdf4;
    border-radius: 5px;
}

/* NAV BAR (Visual) */
.nav-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 15px 5%;
    background: rgba(255, 255, 255, 0.95);
    border-bottom: 1px solid #e0e0e0;
    position: sticky;
    top: 0;
    z-index: 999;
    backdrop-filter: blur(10px);
}

.logo {
    display: flex;
    align-items: center;
    font-size: 24px;
    font-weight: 700;
    color: #196f3d;
    text-decoration: none;
}

.logo-icon {
    margin-right: 10px;
    font-size: 28px;
}

.nav-links a {
    color: #196f3d;
    text-decoration: none;
    font-size: 16px;
    font-weight: 500;
    margin-left: 25px;
    transition: color 0.3s;
}

.nav-links a:hover {
    color: #0e3d20;
}

.book-btn {
    background: #196f3d;
    color: white;
    padding: 10px 25px;
    border-radius: 30px;
    text-decoration: none;
    font-weight: 600;
    transition: background 0.3s;
    box-shadow: 0 4px 6px rgba(25, 111, 61, 0.2);
}

.book-btn:hover {
    background: #0e3d20;
}

/* HERO */
.hero {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 80px 5%;
}

.hero h1 {
    font-size: 4rem;
    color: #196f3d;
    line-height: 1.1;
    margin: 0;
    max-width: 800px;
    font-weight: 700;
}

.hero p {
    font-size: 1.2rem;
    color: #57606f;
    max-width: 600px;
    margin: 20px 0 40px;
    font-weight: 300;
}

.hero-buttons {
    display: flex;
    gap: 15px;
}

.hero-btn {
    background: #196f3d;
    color: white;
    padding: 15px 35px;
    border-radius: 30px;
    text-decoration: none;
    font-weight: 600;
    transition: transform 0.2s;
}

.hero-btn-secondary {
    background: transparent;
    border: 2px solid #196f3d;
    color: #196f3d;
    padding: 13px 33px;
}

.hero-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(25, 111, 61, 0.3);
}

/* CONTENT CONTAINER */
.page-content {
    padding: 40px 5%;
    max-width: 1200px;
    margin: 0 auto;
}

/* CARDS (White & Clean) */
.feature-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 30px;
    margin-top: 30px;
}

.card {
    background: white;
    border-radius: 12px;
    padding: 30px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.05);
    transition: transform 0.3s, box-shadow 0.3s;
    border: 1px solid #f0f0f0;
}

.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 25px rgba(0,0,0,0.08);
    border-color: #196f3d;
}

.card h3 {
    color: #196f3d;
    margin-top: 0;
    font-size: 1.5rem;
}

.card p {
    color: #666;
    font-size: 1rem;
}

/* PLANT PAGE */
.plant-container {
    text-align: center;
    background: white;
    padding: 50px;
    border-radius: 20px;
    box-shadow: 0 5px 30px rgba(0,0,0,0.05);
}

.plant-img {
    width: 300px;
    height: 300px;
    object-fit: cover;
    border-radius: 50%;
    margin: 30px 0;
    border: 5px solid #f0fdf4;
}

/* RESPONSIVE */
@media (max-width: 768px) {
    .hero h1 { font-size: 2.5rem; }
    .nav-links { display: none; } /* Hide top links on mobile, use sidebar */
    .hero-buttons { flex-direction: column; width: 100%; }
    .hero-btn { width: 100%; text-align: center; }
}
</style>
""", unsafe_allow_html=True)

# ------------------ TOP NAV BAR ------------------
st.markdown("""
<div class="nav-bar">
    <div class="logo">
        <span class="logo-icon">🌿</span>
        EcoVista
    </div>
    <div class="nav-links">
        <a href="#" class="nav-link">Home</a>
        <a href="#" class="nav-link">About Us</a>
        <a href="#" class="nav-link">Experiences</a>
        <a href="#" class="nav-link">Sustainability</a>
    </div>
    <a href="#" class="book-btn">Book Now</a>
</div>
""", unsafe_allow_html=True)

# ------------------ SIDEBAR (LOGIC) ------------------
st.sidebar.title("Navigation")

# Use a radio button to switch pages
page = st.sidebar.radio(
    "Go to",
    ["Home", "Plant Care", "Daily Plant", "Earth Today", "Global Action"]
)

# ------------------ PAGE LOGIC ------------------

if page == "Home":
    st.markdown("""
    <div class="hero">
        <h1>Step Into the<br>Stillness of Nature.</h1>
        <p>Rediscover the beauty of the outdoors through curated retreats, immersive eco-experiences, and sustainable travel tailored to your soul.</p>
        <div class="hero-buttons">
            <a href="#" class="hero-btn">Explore Our Journeys</a>
            <a href="#" class="hero-btn hero-btn-secondary">Learn About Our Mission</a>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<div class='page-content'>", unsafe_allow_html=True)
    st.markdown("### Why Choose EcoVista?")
    st.markdown("""
        <div class="feature-grid">
            <div class="card">
                <h3>🌱 Sustainable</h3>
                <p>Our retreats are 100% carbon neutral and support local conservation efforts.</p>
            </div>
            <div class="card">
                <h3>🧘 Mindful</h3>
                <p>Curated experiences that connect you deeply with the environment.</p>
            </div>
            <div class="card">
                <h3>🌍 Exclusive</h3>
                <p>Access to hidden natural gems unavailable to the general public.</p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

elif page == "Plant Care":
    st.markdown("<div class='page-content'>", unsafe_allow_html=True)
    st.markdown("<h1>Plant Care Essentials</h1>", unsafe_allow_html=True)
    st.markdown("<p>Expert advice to keep your botanical friends thriving.</p>", unsafe_allow_html=True)
    
    st.markdown("""
        <div class="feature-grid">
            <div class="card">
                <h3>💧 Watering</h3>
                <p>Most plants prefer to dry out slightly between waterings. Stick your finger into the soil—if it's dry an inch down, it's time to water.</p>
            </div>
            <div class="card">
                <h3>☀️ Light</h3>
                <p>Understand your plant's needs. Low light doesn't mean no light. Rotate your plants weekly for even growth.</p>
            </div>
            <div class="card">
                <h3>✂️ Pruning</h3>
                <p>Don't be afraid to trim. Removing dead leaves encourages new growth and keeps pests away.</p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

elif page == "Daily Plant":
    st.markdown("<div class='page-content'>", unsafe_allow_html=True)
    st.markdown("<h1>Your Digital Companion</h1>", unsafe_allow_html=True)
    st.markdown("<p>Nurture a virtual plant daily to build a habit of care.</p>", unsafe_allow_html=True)
    
    # Logic for Daily Plant
    if "stage" not in st.session_state:
        st.session_state.stage = 0
        st.session_state.last = None
        st.session_state.watered = False
    
    today = date.today()
    if st.session_state.last != today:
        st.session_state.watered = False
        st.session_state.last = today

    images = [
        "https://images.unsplash.com/photo-1616690248973-098a5e08c8c7?q=80&w=1974&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1509423350716-97f9360b4e09?q=80&w=1974&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1520412099551-62b6bafeb5bb?q=80&w=2070&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1518531933037-91b2f5f229cc?q=80&w=1929&auto=format&fit=crop"
    ]

    st.markdown(f"""
    <div class="plant-container">
        <img src="{images[st.session_state.stage]}" class="plant-img">
    </div>
    """, unsafe_allow_html=True)

    if not st.session_state.watered:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("💧 Nurture Plant", use_container_width=True):
                st.session_state.watered = True
                st.session_state.stage = min(3, st.session_state.stage + 1)
                st.success("Your care has helped it grow!")
    else:
        st.info("You have already nurtured your plant today. Come back tomorrow!")
    
    st.markdown("</div>", unsafe_allow_html=True)

elif page == "Earth Today":
    st.markdown("<div class='page-content'>", unsafe_allow_html=True)
    st.markdown("<h1>Earth Today</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div style="display: flex; gap: 40px; align-items: flex-start; flex-wrap: wrap; margin-top: 30px;">
        <img src="https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=2072&auto=format&fit=crop" style="width: 100%; max-width: 500px; border-radius: 12px; box-shadow: 0 10px 20px rgba(0,0,0,0.1);">
        <div>
            <h3 style="color: #196f3d; font-size: 2rem; margin-bottom: 10px;">Healing the Planet</h3>
            <p style="font-size: 1.1rem; color: #555;">
                Global efforts are underway to restore our ecosystems. From reforestation projects in the Amazon to ocean cleanup initiatives in the Pacific, positive change is happening. 
                <br><br>
                Today, we celebrate the resilience of nature and the communities dedicated to protecting it.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

elif page == "Global Action":
    st.markdown("<div class='page-content'>", unsafe_allow_html=True)
    st.markdown("<h1>Global Action</h1>", unsafe_allow_html=True)
    st.markdown("<p>Join the movement. See how the world is taking action.</p>", unsafe_allow_html=True)
    
    st.markdown("""
        <div class="feature-grid">
            <div class="card">
                <img src="https://images.unsplash.com/photo-1596395919256-03bba77e48d7?q=80&w=2070&auto=format&fit=crop" style="width:100%; height: 180px; object-fit: cover; border-radius: 8px; margin-bottom: 15px;">
                <h3>Costa Rica</h3>
                <p>Aiming to be the first carbon-neutral country through massive reforestation.</p>
            </div>
            <div class="card">
                <img src="https://images.unsplash.com/photo-1530836369250-ef72a3f5cda8?q=80&w=2070&auto=format&fit=crop" style="width:100%; height: 180px; object-fit: cover; border-radius: 8px; margin-bottom: 15px;">
                <h3>Germany</h3>
                <p>Leading the world in renewable energy adoption and green technology.</p>
            </div>
            <div class="card">
                <img src="https://images.unsplash.com/photo-1466611653911-95081537e5b7?q=80&w=2071&auto=format&fit=crop" style="width:100%; height: 180px; object-fit: cover; border-radius: 8px; margin-bottom: 15px;">
                <h3>Norway</h3>
                <p>Protecting vast marine areas and investing heavily in electric transportation.</p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
