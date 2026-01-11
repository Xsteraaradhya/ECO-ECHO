import streamlit as st
from datetime import date

# ------------------ CONFIG ------------------
st.set_page_config(
    page_title="Eco-Echo",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------ PREMIUM CINEMATIC CSS ------------------
st.markdown("""
<style>
/* IMPORTING FONTS: 'Allura' for aesthetic cursive headers, 'Cormorant Garamond' for body */
@import url('https://fonts.googleapis.com/css2?family=Allura&family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,400&family=Montserrat:wght@300;400&display=swap');

/* GLOBAL RESETS */
html, body, [class="css-1d391kg"] {
    margin: 0;
    padding: 0;
    background: linear-gradient(135deg, #032b1e 0%, #0a402b 100%);
    color: #e6f4ea;
    font-family: 'Cormorant Garamond', serif;
    overflow-x: hidden;
}

/* HIDING DEFAULT STREAMLIT ELEMENTS */
header, footer { visibility: hidden; }
#MainMenu { visibility: hidden; }

/* TYPOGRAPHY */
h1, h2, h3 {
    font-family: 'Allura', cursive;
    font-weight: 400;
    letter-spacing: 1px;
    margin-bottom: 0.5rem;
    color: #f0fdf4;
    text-shadow: 0 4px 12px rgba(0,0,0,0.3);
}

h1 { font-size: 5rem; line-height: 1.1; }
h2 { font-size: 3.5rem; }
h3 { font-size: 2.5rem; }

p, li, span {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.3rem;
    line-height: 1.8;
    color: #d1e7dd;
}

/* SIDEBAR CUSTOMIZATION */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #021e14 0%, #064d32 100%);
    color: #e6f4ea;
    border-right: 1px solid rgba(255,255,255,0.05);
}

section[data-testid="stSidebar"] .css-ng1t4o {
    font-family: 'Montserrat', sans-serif;
    font-weight: 300;
    letter-spacing: 2px;
    text-transform: uppercase;
    font-size: 0.9rem;
}

section[data-testid="stSidebar"] label {
    font-family: 'Montserrat', sans-serif;
    font-size: 1rem;
    color: #a7f3d0;
}

/* GLASSMORPHISM UTILITIES */
.glass-panel {
    background: rgba(255, 255, 255, 0.03);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 24px;
    padding: 40px;
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.2);
    transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275), box-shadow 0.4s ease;
}

.glass-panel:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 40px 0 rgba(0, 0, 0, 0.3);
    border-color: rgba(255, 255, 255, 0.15);
}

/* HEADER */
.sticky-header {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    height: 80px;
    background: rgba(3, 43, 30, 0.7);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 8%;
    z-index: 999;
    border-bottom: 1px solid rgba(255,255,255,0.05);
}

.logo {
    font-family: 'Allura', cursive;
    font-size: 2.5rem;
    color: #86efac;
    text-decoration: none;
}

.nav-btn {
    padding: 10px 30px;
    background: linear-gradient(135deg, #4ade80 0%, #22c55e 100%);
    color: #022c22;
    border: none;
    border-radius: 50px;
    font-family: 'Montserrat', sans-serif;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
    font-size: 0.8rem;
    cursor: pointer;
    box-shadow: 0 0 20px rgba(74, 222, 128, 0.4);
    transition: all 0.3s ease;
    text-decoration: none;
}

.nav-btn:hover {
    transform: scale(1.05);
    box-shadow: 0 0 30px rgba(74, 222, 128, 0.6);
}

/* HERO SECTION */
.hero-container {
    position: relative;
    height: 100vh;
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    overflow: hidden;
    margin-top: -80px; /* Offset header */
}

.hero-bg {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-image: url('https://images.unsplash.com/photo-1440557653026-d8d89441202b?q=80&w=2070&auto=format&fit=crop');
    background-size: cover;
    background-position: center;
    z-index: -2;
    animation: slowZoom 20s infinite alternate;
}

.hero-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(to bottom, rgba(3,43,30,0.3), rgba(3,43,30,0.9));
    z-index: -1;
}

.hero-content {
    max-width: 800px;
    padding: 20px;
    z-index: 1;
    animation: fadeInUp 1.5s ease-out;
}

.hero-content p {
    font-size: 1.8rem;
    font-weight: 300;
    margin: 30px 0;
    color: #f0fdf4;
}

/* 3D TILES */
.tiles-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 40px;
    padding: 80px 8%;
}

.tile-3d {
    position: relative;
    height: 400px;
    perspective: 1000px;
}

.tile-inner {
    position: relative;
    width: 100%;
    height: 100%;
    text-align: center;
    transition: transform 0.8s;
    transform-style: preserve-3d;
    border-radius: 24px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.2);
}

.tile-3d:hover .tile-inner {
    transform: rotateY(10deg) rotateX(5deg);
}

.tile-img {
    position: absolute;
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 24px;
    backface-visibility: hidden;
}

.tile-content {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    padding: 30px;
    background: linear-gradient(to top, rgba(3,43,30,0.95), transparent);
    border-radius: 0 0 24px 24px;
    text-align: left;
    backface-visibility: hidden;
}

/* STATS SECTION */
.stats-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 30px;
    padding: 80px 8%;
}

.stat-number {
    font-family: 'Cormorant Garamond', serif;
    font-size: 4rem;
    font-weight: 600;
    color: #86efac;
    display: block;
    line-height: 1;
}

.stat-label {
    font-family: 'Montserrat', sans-serif;
    text-transform: uppercase;
    letter-spacing: 2px;
    font-size: 0.85rem;
    opacity: 0.8;
}

/* PROCESS SECTION */
.process-row {
    display: flex;
    align-items: center;
    gap: 60px;
    margin: 80px 8%;
    padding: 40px;
    border-radius: 24px;
}

.process-row:nth-child(even) {
    flex-direction: row-reverse;
}

.process-img {
    flex: 1;
    border-radius: 24px;
    box-shadow: 0 20px 40px rgba(0,0,0,0.3);
    border: 1px solid rgba(255,255,255,0.1);
}

.process-text {
    flex: 1;
}

/* PLANT GAME */
.plant-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 60vh;
}

.plant-img {
    width: 350px;
    border-radius: 200px 200px 20px 20px;
    box-shadow: 0 20px 50px rgba(0,0,0,0.4);
    border: 2px solid rgba(134, 239, 172, 0.3);
    margin-bottom: 40px;
    transition: all 0.5s ease;
}

/* CUSTOM BUTTON */
.stButton > button {
    background: transparent;
    color: #86efac;
    border: 1px solid #86efac;
    border-radius: 50px;
    padding: 12px 40px;
    font-family: 'Montserrat', sans-serif;
    font-size: 1rem;
    letter-spacing: 1px;
    text-transform: uppercase;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: none;
}

.stButton > button:hover {
    background: #86efac;
    color: #022c22;
    box-shadow: 0 0 20px rgba(134, 239, 172, 0.4);
}

/* ANIMATIONS */
@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(50px); }
    to { opacity: 1; transform: translateY(0); }
}

@keyframes slowZoom {
    from { transform: scale(1); }
    to { transform: scale(1.1); }
}

/* COMMUNITY BAR */
.floating-bar {
    position: fixed;
    bottom: 30px;
    left: 50%;
    transform: translateX(-50%);
    background: rgba(3, 43, 30, 0.85);
    backdrop-filter: blur(12px);
    padding: 15px 40px;
    border-radius: 50px;
    border: 1px solid rgba(255,255,255,0.1);
    display: flex;
    gap: 30px;
    align-items: center;
    z-index: 998;
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
}

.bar-item {
    display: flex;
    align-items: center;
    gap: 10px;
    font-family: 'Montserrat', sans-serif;
    font-size: 0.85rem;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: #e6f4ea;
}

/* RESPONSIVE */
@media (max-width: 768px) {
    h1 { font-size: 3.5rem; }
    .hero-content p { font-size: 1.3rem; }
    .process-row { flex-direction: column !important; gap: 30px; margin: 40px 5%; }
    .tiles-grid { grid-template-columns: 1fr; }
    .floating-bar { width: 90%; flex-direction: column; gap: 10px; padding: 15px; }
}
</style>
""", unsafe_allow_html=True)

# ------------------ STICKY HEADER ------------------
st.markdown("""
<div class="sticky-header">
    <div class="logo">Eco-Echo</div>
    <a href="#" class="nav-btn">Start Journey</a>
</div>
""", unsafe_allow_html=True)

# ------------------ SIDEBAR ------------------
st.sidebar.markdown("""
<div style="text-align: center; padding: 20px 0;">
    <h1 style="font-size: 3rem; margin: 0;">Eco-Echo</h1>
    <p style="font-size: 0.9rem; letter-spacing: 2px; opacity: 0.7;">SUSTAINABLE LUXURY</p>
</div>
""", unsafe_allow_html=True)

page = st.sidebar.radio(
    "",
    ["Home", "Plant Care", "Daily Plant", "Earth Today", "Global Action"],
    label_visibility="collapsed"
)

# ------------------ HOME ------------------
if page == "Home":
    # Hero Section
    st.markdown("""
    <div class="hero-container">
        <div class="hero-bg"></div>
        <div class="hero-overlay"></div>
        <div class="hero-content">
            <h1>Step Into the Stillness of Nature</h1>
            <p>
                A digital sanctuary where luxury meets sustainability. 
                Curated eco-experiences for the modern guardian.
            </p>
            <a href="#" class="nav-btn" style="display:inline-block; text-decoration:none; font-size:1rem;">Explore the Echo</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Introduction Glass Card
    st.markdown("""
    <div class="glass-panel" style="margin: 60px 8%; text-align: center;">
        <h2>Harmonized Living</h2>
        <p>
            We believe that true luxury lies in the balance between human ingenuity and the organic world. 
            Our platform is designed to guide you through a journey of environmental stewardship wrapped in 
            uncompromising aesthetic beauty.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # 3D Floating Tiles
    st.markdown("""
    <div class="tiles-grid">
        <div class="tile-3d">
            <div class="tile-inner">
                <img src="https://images.unsplash.com/photo-1542601906990-b4d3fb778b09?q=80&w=1613&auto=format&fit=crop" class="tile-img">
                <div class="tile-content">
                    <h3>Biodiversity</h3>
                    <p>Protecting the intricate web of life.</p>
                </div>
            </div>
        </div>
        <div class="tile-3d">
            <div class="tile-inner">
                <img src="https://images.unsplash.com/photo-1473448912268-2022ce9509d8?q=80&w=1647&auto=format&fit=crop" class="tile-img">
                <div class="tile-content">
                    <h3>Rainforests</h3>
                    <p>The lungs of our planet, breathing life.</p>
                </div>
            </div>
        </div>
        <div class="tile-3d">
            <div class="tile-inner">
                <img src="https://images.unsplash.com/photo-1462275646964-a0e3571f4f7f?q=80&w=1628&auto=format&fit=crop" class="tile-img">
                <div class="tile-content">
                    <h3>Ocean Preservation</h3>
                    <p>Healing the blue heart of the Earth.</p>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Stats Section
    st.markdown("""
    <div class="stats-container">
        <div class="glass-panel" style="text-align: center; padding: 30px;">
            <span class="stat-number">30%</span>
            <span class="stat-label">Carbon Offset</span>
        </div>
        <div class="glass-panel" style="text-align: center; padding: 30px;">
            <span class="stat-number">12k</span>
            <span class="stat-label">Trees Planted</span>
        </div>
        <div class="glass-panel" style="text-align: center; padding: 30px;">
            <span class="stat-number">5.0</span>
            <span class="stat-label">Community Rating</span>
        </div>
        <div class="glass-panel" style="text-align: center; padding: 30px;">
            <span class="stat-number">100%</span>
            <span class="stat-label">Committed</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Process Section
    st.markdown("""
    <div class="glass-panel process-row">
        <img src="https://images.unsplash.com/photo-1596395919256-03bba77e48d7?q=80&w=2070&auto=format&fit=crop" class="process-img">
        <div class="process-text">
            <h2>Discovery</h2>
            <p>Understanding the unique ecological footprint of your lifestyle to tailor a bespoke sustainability path.</p>
        </div>
    </div>
    
    <div class="glass-panel process-row">
        <img src="https://images.unsplash.com/photo-1530836369250-ef72a3f5cda8?q=80&w=2070&auto=format&fit=crop" class="process-img">
        <div class="process-text">
            <h2>Integration</h2>
            <p>Seamlessly weaving eco-conscious choices into your daily routine through mindful practices and premium alternatives.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ------------------ PLANT CARE ------------------
elif page == "Plant Care":
    st.markdown("<br><br>", unsafe_allow_html=True) # Spacer
    st.markdown("""
    <div class="glass-panel" style="margin: 40px 8%;">
        <h2>Botanical Wisdom</h2>
        <p>
            Plants are not mere decorations; they are living companions. Care for them with the same gentleness you offer yourself.
            Water with intention, prune with love, and watch life unfold in silence and splendor.
        </p>
        <div style="margin-top: 30px; display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px;">
            <div class="glass-panel" style="padding: 20px; text-align: center;">
                <h3 style="font-size: 2rem;">💧</h3>
                <h4>Water</h4>
                <p style="font-size: 1rem;">Touch the soil. If dry, water deeply.</p>
            </div>
            <div class="glass-panel" style="padding: 20px; text-align: center;">
                <h3 style="font-size: 2rem;">☀️</h3>
                <h4>Light</h4>
                <p style="font-size: 1rem;">Bright, indirect light is best.</p>
            </div>
            <div class="glass-panel" style="padding: 20px; text-align: center;">
                <h3 style="font-size: 2rem;">🌬️</h3>
                <h4>Air</h4>
                <p style="font-size: 1rem;">Ensure good circulation.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ------------------ DAILY PLANT ------------------
elif page == "Daily Plant":
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("""
    <div class="glass-panel plant-container">
        <h2>Grow Your Digital Sanctuary</h2>
        <p>Nurture your virtual plant daily to cultivate mindfulness.</p>
    """, unsafe_allow_html=True)

    if "stage" not in st.session_state:
        st.session_state.stage = 0
        st.session_state.last = None
        st.session_state.watered = False

    today = date.today()
    if st.session_state.last != today:
        st.session_state.watered = False
        st.session_state.last = today

    images = [
        "https://images.unsplash.com/photo-1616690248973-098a5e08c8c7?q=80&w=1974&auto=format&fit=crop", # Seed
        "https://images.unsplash.com/photo-1509423350716-97f9360b4e09?q=80&w=1974&auto=format&fit=crop", # Sprout
        "https://images.unsplash.com/photo-1520412099551-62b6bafeb5bb?q=80&w=2070&auto=format&fit=crop", # Small Plant
        "https://images.unsplash.com/photo-1518531933037-91b2f5f229cc?q=80&w=1929&auto=format&fit=crop"  # Tree
    ]

    st.markdown(f'<img src="{images[st.session_state.stage]}" class="plant-img">', unsafe_allow_html=True)

    if not st.session_state.watered:
        if st.button("✨ Nurture Today"):
            st.session_state.watered = True
            st.session_state.stage = min(3, st.session_state.stage + 1)
            st.success("Your intention has been planted. Return tomorrow for growth.")
    else:
        st.info("The plant has absorbed today's love. Rest and return tomorrow.")

    st.markdown("</div>", unsafe_allow_html=True)

# ------------------ EARTH TODAY ------------------
elif page == "Earth Today":
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("""
    <div class="glass-panel" style="margin: 40px 8%;">
        <h2>Planet Pulse</h2>
        <div style="display: flex; gap: 40px; align-items: center; flex-wrap: wrap;">
            <img src="https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=2072&auto=format&fit=crop" style="width: 100%; max-width: 500px; border-radius: 20px;">
            <div>
                <p>
                    As of today, the collective consciousness is shifting. Forests are reclaiming abandoned lands in parts of Europe, 
                    renewable energy sources have outpaced coal in several nations, and the oceans are slowly healing as marine protected areas expand.
                </p>
                <p>
                    The Earth is speaking in whispers of recovery. We must listen.
                </p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ------------------ GLOBAL ACTION ------------------
elif page == "Global Action":
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("""
    <div class="glass-panel" style="margin: 40px 8%;">
        <h2>Unified Movements</h2>
        <p>
            From the rewilding projects in the Scottish Highlands to the massive solar arrays in the Sahara, 
            humanity is learning to cooperate with nature rather than dominate it.
        </p>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin-top: 30px;">
            <div class="glass-panel" style="padding: 20px;">
                <h3>Costa Rica</h3>
                <p>98% Renewable Energy</p>
            </div>
            <div class="glass-panel" style="padding: 20px;">
                <h3>Bhutan</h3>
                <p>Carbon Negative Nation</p>
            </div>
            <div class="glass-panel" style="padding: 20px;">
                <h3>Sweden</h3>
                <p>Recycling Revolution</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ------------------ COMMUNITY BAR ------------------
st.markdown("""
<div class="floating-bar">
    <div class="bar-item">
        <span style="font-size: 1.2rem;">🌍</span>
        <span>12,405 Guardians</span>
    </div>
    <div style="width: 1px; height: 15px; background: rgba(255,255,255,0.3);"></div>
    <div class="bar-item">
        <span style="font-size: 1.2rem;">✨</span>
        <span>89 Active Retreats</span>
    </div>
    <div style="width: 1px; height: 15px; background: rgba(255,255,255,0.3);"></div>
    <div class="bar-item">
        <span style="font-size: 1.2rem;">★</span>
        <span>4.9/5 Ecosystem Rating</span>
    </div>
</div>
""", unsafe_allow_html=True)
