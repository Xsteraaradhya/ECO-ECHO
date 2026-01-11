
import streamlit as st
from datetime import date

# ------------------ CONFIG ------------------
st.set_page_config(
    page_title="Eco-Echo",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------ APPLE-STYLE CINEMATIC CSS ------------------
st.markdown("""
<style>
/* --- FONTS --- */
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;0,700;1,400&family=Great+Vibes&family=Montserrat:wght@200;300;400;600&display=swap');

/* --- GLOBAL RESET & VIBE --- */
html, body, [class="css-1d391kg"] {
    margin: 0;
    padding: 0;
    background-color: #000000;
    color: #f5f5f7;
    font-family: 'Cormorant Garamond', serif;
    overflow-x: hidden;
    scroll-behavior: smooth;
}

/* HIDING STREAMLIT DEFAULTS */
header, footer { visibility: hidden; }
#MainMenu { visibility: hidden; }

/* --- TYPOGRAPHY --- */
h1 {
    font-family: 'Cormorant Garamond', serif;
    font-weight: 700;
    font-size: 5.5rem;
    line-height: 1.05;
    letter-spacing: -0.02em;
    background: linear-gradient(180deg, #ffffff 0%, #a3e6cd 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 20px;
}

h2 {
    font-family: 'Great Vibes', cursive; /* The "Hot" Cursive Font */
    font-size: 3.5rem;
    color: #86efac;
    margin-bottom: 10px;
}

h3 {
    font-family: 'Montserrat', sans-serif;
    font-weight: 600;
    font-size: 1.5rem;
    color: #e0e0e0;
    letter-spacing: 0.05em;
}

p {
    font-family: 'Montserrat', sans-serif;
    font-weight: 300;
    font-size: 1.25rem;
    line-height: 1.6;
    color: #86868b;
}

/* --- SIDEBAR --- */
section[data-testid="stSidebar"] {
    background: rgba(0, 0, 0, 0.95);
    backdrop-filter: blur(20px);
    border-right: 1px solid rgba(255,255,255,0.1);
    width: 300px !important;
}

section[data-testid="stSidebar"] .css-ng1t4o {
    font-family: 'Montserrat', sans-serif;
    text-transform: uppercase;
    font-size: 0.75rem;
    letter-spacing: 0.2em;
    color: #86868b;
    margin-bottom: 2rem;
}

section[data-testid="stSidebar"] label {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.4rem;
    font-weight: 600;
    color: #f5f5f7;
    cursor: pointer;
    transition: all 0.3s ease;
}

section[data-testid="stSidebar"] label:hover {
    color: #86efac;
    transform: translateX(10px);
}

/* --- HEADER --- */
.sticky-header {
    position: fixed;
    top: 0;
    width: 100%;
    height: 48px;
    background: rgba(0, 0, 0, 0.8);
    backdrop-filter: saturate(180%) blur(20px);
    -webkit-backdrop-filter: saturate(180%) blur(20px);
    z-index: 9999;
    border-bottom: 1px solid rgba(255,255,255,0.1);
    transition: background 0.3s ease;
}

.header-content {
    max-width: 980px;
    margin: 0 auto;
    height: 100%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 20px;
}

.apple-logo {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.2rem;
    color: #f5f5f7;
    font-weight: 700;
    letter-spacing: 0.05em;
}

.nav-links a {
    color: #d1d1d1;
    font-family: 'Montserrat', sans-serif;
    font-size: 0.75rem;
    text-decoration: none;
    margin-left: 24px;
    transition: color 0.3s ease;
}

.nav-links a:hover {
    color: #ffffff;
}

/* --- HERO SECTION (iPhone Style) --- */
.hero-section {
    position: relative;
    height: 100vh;
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
    padding-top: 120px;
    text-align: center;
    overflow: hidden;
    background-color: #000;
}

.hero-bg {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-image: url('https://images.unsplash.com/photo-1518173946687-a4c8892bbd9f?q=80&w=2069&auto=format&fit=crop'); /* Dark Forest */
    background-size: cover;
    background-position: center;
    z-index: -2;
    opacity: 0.6;
    animation: mistMove 30s infinite alternate ease-in-out;
}

.mist-overlay {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 50%;
    background: linear-gradient(to top, #000000, transparent);
    z-index: -1;
    pointer-events: none;
}

.hero-text-wrapper {
    z-index: 10;
    max-width: 800px;
    margin-bottom: 40px;
}

.cta-button {
    background: #2997ff; /* Apple Blue style, but we can tweak to green */
    background: linear-gradient(135deg, #34d399 0%, #059669 100%);
    color: white;
    padding: 12px 24px;
    border-radius: 980px;
    font-family: 'Montserrat', sans-serif;
    font-size: 1.1rem;
    text-decoration: none;
    transition: transform 0.3s cubic-bezier(0.25, 0.1, 0.25, 1);
    box-shadow: 0 4px 15px rgba(5, 150, 105, 0.4);
}

.cta-button:hover {
    transform: scale(1.05);
    box-shadow: 0 6px 20px rgba(5, 150, 105, 0.6);
}

/* --- SCROLLING SECTIONS (Bento Grid Style) --- */
.bento-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
    padding: 20px;
    max-width: 1200px;
    margin: 0 auto;
}

.bento-item {
    background: #151516;
    border-radius: 28px;
    padding: 40px;
    overflow: hidden;
    position: relative;
    transition: transform 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    height: 500px;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    border: 1px solid rgba(255,255,255,0.05);
}

.bento-item:hover {
    transform: scale(1.02);
}

.bento-img {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    opacity: 0.7;
    transition: opacity 0.5s ease;
    z-index: 1;
}

.bento-item:hover .bento-img {
    opacity: 0.9;
}

.bento-content {
    position: relative;
    z-index: 2;
    background: linear-gradient(to top, rgba(0,0,0,0.9), transparent);
    padding-top: 60px;
}

/* --- DARK GLASS PANEL --- */
.dark-glass {
    background: rgba(255, 255, 255, 0.03);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 24px;
    padding: 60px;
    margin: 100px 8%;
}

/* --- ANIMATIONS --- */
@keyframes mistMove {
    0% { transform: scale(1); }
    100% { transform: scale(1.1); }
}

/* --- FLOATING BAR --- */
.floating-stats {
    position: fixed;
    bottom: 30px;
    left: 50%;
    transform: translateX(-50%);
    background: rgba(28, 28, 30, 0.85);
    backdrop-filter: blur(25px);
    -webkit-backdrop-filter: blur(25px);
    padding: 10px 20px;
    border-radius: 50px;
    border: 1px solid rgba(255,255,255,0.1);
    z-index: 1000;
    display: flex;
    gap: 30px;
    box-shadow: 0 10px 40px rgba(0,0,0,0.5);
}

.stat-pill {
    font-family: 'Montserrat', sans-serif;
    font-size: 0.8rem;
    color: #f5f5f7;
    display: flex;
    align-items: center;
    gap: 8px;
}

/* --- RESPONSIVE --- */
@media (max-width: 768px) {
    h1 { font-size: 3rem; }
    .bento-grid { grid-template-columns: 1fr; }
    .hero-bg { opacity: 0.4; }
    .floating-stats { width: 90%; justify-content: space-around; bottom: 20px;}
}
</style>
""", unsafe_allow_html=True)

# ------------------ STICKY HEADER ------------------
st.markdown("""
<div class="sticky-header">
    <div class="header-content">
        <div class="apple-logo">Eco-Echo </div>
        <div class="nav-links">
            <a href="#">Store</a>
            <a href="#">Mac</a>
            <a href="#">iPad</a>
            <a href="#">Nature</a>
            <a href="#">Support</a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ------------------ SIDEBAR NAV ------------------
st.sidebar.markdown("""
<div style="margin-top: 80px; margin-bottom: 40px;">
    <h1 style="font-size: 2.5rem; color: #fff; margin:0;">Eco-Echo</h1>
</div>
""", unsafe_allow_html=True)

page = st.sidebar.radio(
    "", 
    ["Home", "Plant Care", "Daily Plant", "Earth Today", "Global Action"],
    label_visibility="collapsed"
)

# ------------------ PAGE LOGIC ------------------
if page == "Home":
    # 1. HERO SECTION
    st.markdown("""
    <section class="hero-section">
        <div class="hero-bg"></div>
        <div class="mist-overlay"></div>
        
        <div class="hero-text-wrapper">
            <h2>Pro. Beyond.</h2>
            <h1>Reclaiming the<br>Wild Within.</h1>
            <p style="margin-bottom: 30px;">The most advanced ecosystem ever designed.<br>Deeply immersive. Simply beautiful.</p>
            <a href="#" class="cta-button">Watch the Film</a>
            <a href="#" class="cta-button" style="background: transparent; border: 1px solid #34d399; margin-left: 10px;">Learn more</a>
        </div>
    </section>
    """, unsafe_allow_html=True)

    # 2. BENTO GRID SHOWCASE
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown("""
    <div class="bento-grid">
        <div class="bento-item">
            <img src="https://images.unsplash.com/photo-1542601906990-b4d3fb778b09?q=80&w=1613&auto=format&fit=crop" class="bento-img">
            <div class="bento-content">
                <h3>Titanium. Strong.</h3>
                <h2>Forest Shield</h2>
                <p>Forged in the deepest woods, our protection is natural yet impenetrable.</p>
            </div>
        </div>
        <div class="bento-item">
            <img src="https://images.unsplash.com/photo-1473448912268-2022ce9509d8?q=80&w=1647&auto=format&fit=crop" class="bento-img">
            <div class="bento-content">
                <h3>A17 Bionic Chip</h3>
                <h2>Photosynthesis</h2>
                <p>Nature’s power source. Unlimited energy from a single leaf.</p>
            </div>
        </div>
        <div class="bento-item" style="grid-column: span 2;">
            <img src="https://images.unsplash.com/photo-1462275646964-a0e3571f4f7f?q=80&w=1628&auto=format&fit=crop" class="bento-img">
            <div class="bento-content" style="text-align: center; background: linear-gradient(to top, #000 0%, transparent 100%);">
                <h2>The Ocean. Clean.</h2>
                <p>Retina-level clarity in every wave.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # 3. TEXT SECTION
    st.markdown("""
    <div class="dark-glass" style="text-align: center; margin-top: 100px;">
        <h2 style="color: #fff;">Designed for Earth.</h2>
        <h3 style="color: #86868b; font-weight: 300; max-width: 600px; margin: 0 auto;">
            Every curve, every shadow, every pixel is crafted to bring you closer to nature. 
            It’s not just a website. It’s a movement.
        </h3>
    </div>
    """, unsafe_allow_html=True)

elif page == "Plant Care":
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("""
    <div class="dark-glass">
        <h2>Botanical Pro</h2>
        <h3>Intelligent Care System.</h3>
        <div style="margin-top: 40px; display: grid; grid-template-columns: repeat(3, 1fr); gap: 30px;">
            <div style="text-align: center;">
                <div style="font-size: 3rem; margin-bottom: 10px;">💧</div>
                <h4>Hydration</h4>
                <p>Precision watering sensors.</p>
            </div>
            <div style="text-align: center;">
                <div style="font-size: 3rem; margin-bottom: 10px;">☀️</div>
                <h4>Light</h4>
                <p>Adaptive spectral analysis.</p>
            </div>
            <div style="text-align: center;">
                <div style="font-size: 3rem; margin-bottom: 10px;">🍃</div>
                <h4>Nutrients</h4>
                <p>Soil health monitoring.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

elif page == "Daily Plant":
    st.markdown("<br><br>", unsafe_allow_html=True)
    # Session State Logic
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
    <div style="text-align: center; margin-top: 50px;">
        <h2>Your Digital Forest</h2>
        <p>Tap to Nurture. Experience the growth.</p>
        <img src="{images[st.session_state.stage]}" style="width: 300px; height: 300px; object-fit: cover; border-radius: 50%; border: 4px solid #333; box-shadow: 0 0 50px rgba(52, 211, 153, 0.2);">
    </div>
    """, unsafe_allow_html=True)

    if not st.session_state.watered:
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("✨ Nurture Now", use_container_width=True):
                st.session_state.watered = True
                st.session_state.stage = min(3, st.session_state.stage + 1)
                st.success("Growth sequence initiated.")
    else:
        st.info("Cycle complete. Return tomorrow for the next stage.")

elif page == "Earth Today":
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("""
    <div style="height: 80vh; position: relative; overflow: hidden; border-radius: 30px; margin: 0 5%;">
        <img src="https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=2072&auto=format&fit=crop" style="width: 100%; height: 100%; object-fit: cover;">
        <div style="position: absolute; bottom: 40px; left: 40px; background: rgba(0,0,0,0.6); padding: 30px; border-radius: 20px; backdrop-filter: blur(10px);">
            <h2>Planet Earth</h2>
            <h3>The Ultimate Edition.</h3>
            <p>Real-time ecosystem data.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

elif page == "Global Action":
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("""
    <div class="bento-grid">
        <div class="bento-item">
            <img src="https://images.unsplash.com/photo-1596395919256-03bba77e48d7?q=80&w=2070&auto=format&fit=crop" class="bento-img">
            <div class="bento-content">
                <h2>Reforestation</h2>
                <p>Project Costa Rica.</p>
            </div>
        </div>
        <div class="bento-item">
            <img src="https://images.unsplash.com/photo-1530836369250-ef72a3f5cda8?q=80&w=2070&auto=format&fit=crop" class="bento-img">
            <div class="bento-content">
                <h2>Ocean Cleanup</h2>
                <p>Project Pacific.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ------------------ FLOATING STATS BAR ------------------
st.markdown("""
<div class="floating-stats">
    <div class="stat-pill"><span style="color: #34d399;">●</span> Live</div>
    <div class="stat-pill">12,405 Guardians</div>
    <div class="stat-pill">Carbon Neutral</div>
</div>
""", unsafe_allow_html=True)
```
