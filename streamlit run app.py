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
    background-color: #062C1B;
    color: #eef5f0;
    font-family: 'Inter', sans-serif;
}

header, footer {visibility: hidden;}

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #062C1B, #0A3A26);
    color: #eaf5ee;
}

h1, h2, h3 {
    font-family: 'Playfair Display', serif;
}

/* HEADER */
.sticky-header {
    position: sticky;
    top: 0;
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(20px);
    padding: 15px 8%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    z-index: 1000;
    border-bottom: 1px solid rgba(255,255,255,0.1);
}

.sticky-header .logo {
    font-size: 24px;
    font-weight: 700;
}

.sticky-header .nav-button {
    padding: 10px 24px;
    background: #32CD32;
    color: #062C1B;
    border-radius: 40px;
    font-weight: 600;
    box-shadow: 0 0 15px rgba(50,205,50,0.5);
}

/* HERO */
.hero {
    height: 92vh;
    background:
        linear-gradient(rgba(6,44,27,0.55), rgba(6,44,27,0.85)),
        url("https://images.unsplash.com/photo-1500530855697-b586d89ba3ee");
    background-size: cover;
    background-position: center;
    background-attachment: fixed; /* Parallax effect */
    display: flex;
    align-items: center;
    padding-left: 8%;
    position: relative;
    overflow: hidden;
}

.hero-content h1 {
    font-size: 72px;
    line-height: 1.05;
    font-weight: 700;
}

.hero-content p {
    max-width: 520px;
    font-size: 18px;
    opacity: 0.85;
    font-family: 'Inter', sans-serif;
}

/* CTA */
.cta {
    margin-top: 30px;
    display: inline-block;
    padding: 14px 34px;
    border-radius: 40px;
    background: #32CD32;
    color: #062C1B;
    font-weight: 600;
    box-shadow: 0 0 20px rgba(50,205,50,0.6);
    transition: transform 0.3s ease;
}

.cta:hover {
    transform: scale(1.05);
}

/* 3D FLOATING TILES */
.tiles {
    perspective: 1000px;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 40px;
    padding: 60px 8%;
}

.tile {
    background: rgba(255,255,255,0.1);
    backdrop-filter: blur(14px);
    border-radius: 32px;
    padding: 30px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.2);
    transform: rotateY(10deg) rotateX(5deg);
    transition: transform 0.5s ease;
}

.tile:hover {
    transform: rotateY(0) rotateX(0) scale(1.05);
}

.tile img {
    width: 100%;
    border-radius: 24px;
    margin-bottom: 20px;
}

/* GLASS SECTIONS */
.glass {
    background: rgba(255,255,255,0.1);
    backdrop-filter: blur(14px);
    border-radius: 32px;
    padding: 50px;
    margin: 40px 8%;
    box-shadow: 0 4px 30px rgba(0,0,0,0.1);
}

/* GRID */
.grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 40px;
    margin: 40px 8%;
}

/* CARDS */
.card {
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(14px);
    border-radius: 32px;
    padding: 30px;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card:hover {
    transform: translateY(-10px);
    box-shadow: 0 12px 40px rgba(0,0,0,0.2);
}

.card img {
    width: 100%;
    border-radius: 24px;
}

.card p {
    opacity: 0.85;
}

/* STATS CARDS */
.stats-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 30px;
    margin: 40px 8%;
}

.stat-card {
    background: rgba(255,255,255,0.1);
    backdrop-filter: blur(14px);
    border-radius: 32px;
    padding: 30px;
    text-align: center;
    opacity: 0;
    transform: translateY(50px);
    transition: opacity 0.5s ease, transform 0.5s ease;
}

.stat-card.visible {
    opacity: 1;
    transform: translateY(0);
}

.stat-value {
    font-size: 48px;
    font-weight: 700;
    color: #8cc9a3;
}

.stat-label {
    font-size: 16px;
    opacity: 0.85;
}

/* PROCESS SECTION */
.process {
    margin: 60px 8%;
}

.process-step {
    display: flex;
    align-items: center;
    margin-bottom: 60px;
    gap: 40px;
}

.process-step:nth-child(even) {
    flex-direction: row-reverse;
}

.process-image {
    width: 50%;
    border-radius: 40px;
    box-shadow: 0 10px 40px rgba(0,0,0,0.3);
}

.process-text {
    width: 50%;
}

/* COMMUNITY BAR */
.community-bar {
    position: fixed;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
    background: rgba(255,255,255,0.1);
    backdrop-filter: blur(14px);
    border-radius: 40px;
    padding: 10px 30px;
    display: flex;
    align-items: center;
    gap: 20px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.2);
}

.community-stat {
    font-size: 14px;
    opacity: 0.9;
}

.stars {
    color: #FFD700;
}

/* GAME IMAGE */
.plant {
    width: 300px;
    margin-bottom: 30px;
    border-radius: 30px;
    box-shadow: 0 5px 25px rgba(0,0,0,0.2);
}

.stButton>button {
    background: linear-gradient(135deg, #9fd9b8, #6ca98a);
    border-radius: 40px;
    border: none;
    font-weight: 600;
    padding: 12px 28px;
    box-shadow: 0 0 15px rgba(108,169,138,0.4);
}

/* ANIMATIONS */
@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(50px); }
    to { opacity: 1; transform: translateY(0); }
}

.glass, .card, .tile {
    animation: fadeInUp 1s ease-out;
}

/* RESPONSIVE */
@media (max-width: 768px) {
    .hero-content h1 {
        font-size: 48px;
    }
    .tiles, .grid, .stats-grid {
        grid-template-columns: 1fr;
    }
    .process-step {
        flex-direction: column;
    }
    .process-image, .process-text {
        width: 100%;
    }
    .community-bar {
        width: 90%;
        padding: 10px 15px;
    }
}
</style>
""", unsafe_allow_html=True)

# ------------------ STICKY HEADER ------------------
st.markdown("""
<div class="sticky-header">
    <div class="logo">🌿 Eco-Echo</div>
    <div class="nav-button">Get Started</div>
</div>
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
                Rediscover the beauty of the outdoors through curated retreats,
                immersive eco-experiences, and sustainable travel.
            </p>
            <span class="cta">Explore the Echo</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="glass">
        <h2>Think Outside. No Box Required.</h2>
        <p>
            Eco-Echo is a premium digital sanctuary crafted to harmonize human ingenuity with nature's wisdom, fostering mindful interactions that inspire sustainable living and profound environmental stewardship.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # 3D Floating Tiles
    st.markdown("""
    <div class="tiles">
        <div class="tile">
            <img src="https://images.unsplash.com/photo-1469474968028-56623f02e42e">
            <h3>Forests & Biodiversity</h3>
            <p>Explore thriving ecosystems and their vital role in our planet's health.</p>
        </div>
        <div class="tile">
            <img src="https://images.unsplash.com/photo-1500530855697-b586d89ba3ee">
            <h3>Planet Earth Ecosystems</h3>
            <p>Dive into the interconnected web of life across global biomes.</p>
        </div>
        <div class="tile">
            <img src="https://images.unsplash.com/photo-1483729558449-99ef09a8c325">
            <h3>Sustainable Futures</h3>
            <p>Envision and build resilient communities in harmony with nature.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Stats Cards
    st.markdown("""
    <div class="stats-grid">
        <div class="stat-card">
            <div class="stat-value">30%</div>
            <div class="stat-label">Carbon Footprint Reduction</div>
        </div>
        <div class="stat-card">
            <div class="stat-value">20%</div>
            <div class="stat-label">Reduced Energy Bills</div>
        </div>
        <div class="stat-card">
            <div class="stat-value">10K+</div>
            <div class="stat-label">Worldwide Users</div>
        </div>
        <div class="stat-card">
            <div class="stat-value">★★★★★</div>
            <div class="stat-label">User Ratings</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Process Section
    st.markdown("""
    <div class="process">
        <div class="process-step">
            <img src="https://images.unsplash.com/photo-1501004318641-b39e6451bec6" class="process-image">
            <div class="process-text">
                <h3>Discovery and Consultation</h3>
                <p>Our architects engage with clients to understand their vision, preferences.</p>
            </div>
        </div>
        <div class="process-step">
            <img src="https://images.unsplash.com/photo-1524593166156-312f362cada0" class="process-image">
            <div class="process-text">
                <h3>Native Plant Integration</h3>
                <p>Garden Tree Landscape prioritizes the use of native plants in our designs.</p>
            </div>
        </div>
        <div class="process-step">
            <img src="https://images.unsplash.com/photo-1500534314209-a25ddb2bd429" class="process-image">
            <div class="process-text">
                <h3>Water-Efficient Irrigation</h3>
                <p>Garden Tree Landscape is committed to responsible water management.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ------------------ PLANT CARE ------------------
elif page == "Plant Care":
    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    st.header("🌱 Plant Care Essentials")
    st.markdown("""
    Plants flourish in harmony with nature's rhythms. Nurture them with mindful watering in dawn's light, 
    allow the earth to respire freely, bathe in filtered sunbeams, and observe their subtle transformations with patience.
    True care emerges from presence, not dominance.
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
        "https://images.unsplash.com/photo-1501004318641-b39e6451bec6",  # seed
        "https://images.unsplash.com/photo-1524593166156-312f362cada0",  # sprout
        "https://images.unsplash.com/photo-1500534314209-a25ddb2bd429",  # young tree
        "https://images.unsplash.com/photo-1501785888041-af3ef285b470"   # forest
    ]
    st.markdown(f'<img src="{images[st.session_state.stage]}" class="plant">', unsafe_allow_html=True)
    if not st.session_state.watered:
        if st.button("💧 Water Plant"):
            st.session_state.watered = True
            st.session_state.stage = min(3, st.session_state.stage + 1)
            st.success("In nature's time, growth unfolds. Your care resonates 🌱")
    else:
        st.info("The cycle renews at dawn. Return tomorrow to nurture further.")
    st.markdown("</div>", unsafe_allow_html=True)

# ------------------ EARTH TODAY ------------------
elif page == "Earth Today":
    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    st.header("🌍 Planet Earth Today")
    st.markdown("""
    In silent symphony, forests regenerate across continents, solar innovations illuminate urban landscapes, 
    and global collectives redefine coexistence with the natural world. Evolution proceeds in whispers, 
    anchored in collective consciousness and stewardship.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# ------------------ GLOBAL ACTION ------------------
elif page == "Global Action":
    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    st.header("🌎 Global Environmental Action")
    st.markdown("""
    From Costa Rica's verdant canopy guardianship to Germany's renewable vanguard, 
    sovereigns worldwide demonstrate that ecological harmony and advancement entwine 
    when illuminated by prescient foresight.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# ------------------ COMMUNITY BAR ------------------
st.markdown("""
<div class="community-bar">
    <div class="community-stat">10K+ Global Users</div>
    <div class="community-stat">|</div>
    <div class="community-stat">Active Retreats: 874</div>
    <div class="community-stat">|</div>
    <div class="community-stat stars">★★★★★ 4.9/5</div>
</div>
""", unsafe_allow_html=True)

# ------------------ FOOTER ------------------
st.markdown("""
<p style="text-align:center; opacity:0.6; margin:50px 0;">
Eco-Echo 🌿 — A digital ecosystem woven from nature's essence, for tomorrow's guardians
</p>
""", unsafe_allow_html=True)
