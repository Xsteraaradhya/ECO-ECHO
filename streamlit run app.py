import streamlit as st
from datetime import date

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Eco-Echo",
    page_icon="🌿",
    layout="wide"
)

# ------------------ GLOBAL STYLES ------------------
st.markdown("""
<style>

/* Import modern eco font */
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;700&family=Inter:wght@300;400;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    color: #eaf5ee;
}

/* Hide Streamlit header/footer */
header, footer {visibility: hidden;}

/* Main background */
.main {
    background: linear-gradient(
        rgba(0,0,0,0.55),
        rgba(0,0,0,0.65)
    ),
    url("https://images.unsplash.com/photo-1500530855697-b586d89ba3ee");
    background-size: cover;
    background-position: center;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: rgba(15, 40, 25, 0.85);
    backdrop-filter: blur(12px);
}

/* Hero section */
.hero {
    padding: 120px 60px;
}

.hero h1 {
    font-family: 'Playfair Display', serif;
    font-size: 64px;
    line-height: 1.1;
}

.hero p {
    font-size: 20px;
    max-width: 600px;
    opacity: 0.9;
}

/* Glass cards */
.glass {
    background: rgba(255, 255, 255, 0.12);
    border-radius: 22px;
    padding: 30px;
    margin-bottom: 30px;
    backdrop-filter: blur(14px);
    box-shadow: 0 20px 50px rgba(0,0,0,0.3);
}

/* Buttons */
.stButton>button {
    background: linear-gradient(135deg, #7fbf9c, #4e8f6f);
    color: #0f2a1c;
    border-radius: 30px;
    padding: 10px 28px;
    border: none;
    font-weight: 600;
}

.stButton>button:hover {
    transform: scale(1.05);
}

/* Images */
img {
    border-radius: 18px;
}

</style>
""", unsafe_allow_html=True)

# ------------------ SIDEBAR ------------------
st.sidebar.title("🌿 Eco-Echo")
page = st.sidebar.radio(
    "Navigate",
    ["Home", "Plant Care Tips", "Daily Plant Game", "Environment News", "Global Solutions"]
)

# ------------------ HOME ------------------
if page == "Home":
    st.markdown("""
    <div class="hero">
        <h1>Step Into the<br>Stillness of Nature</h1>
        <p>
            Eco-Echo helps you reconnect with nature through mindful plant care,
            sustainability education, and small daily actions that grow into real impact.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="glass">
        <h2>🌱 Our Mission</h2>
        <p>
            We believe caring for a single plant can change how we care for the planet.
            Eco-Echo blends education, interaction, and calm design to inspire sustainable living.
        </p>
    </div>
    """, unsafe_allow_html=True)

# ------------------ PLANT CARE ------------------
elif page == "Plant Care Tips":
    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    st.header("🌿 Plant Care Essentials")

    st.image(
        "https://images.unsplash.com/photo-1501004318641-b39e6451bec6",
        use_container_width=True
    )

    st.markdown("""
    - Water early morning or sunset  
    - Check soil before watering  
    - Use organic compost  
    - Rotate plants for even sunlight  
    - Trim damaged leaves regularly  
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# ------------------ DAILY PLANT GAME ------------------
elif page == "Daily Plant Game":
    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    st.header("🌱 Grow Your Plant")

    if "watered" not in st.session_state:
        st.session_state.watered = False
        st.session_state.last_day = None
        st.session_state.growth_stage = 0

    today = date.today()

    if st.session_state.last_day != today:
        st.session_state.watered = False
        st.session_state.last_day = today

    growth_images = [
        "https://i.imgur.com/Jf6F0G7.png",
        "https://i.imgur.com/4a2p9Q6.png",
        "https://i.imgur.com/EJ2Vq7y.png",
        "https://i.imgur.com/q3RklbY.png"
    ]

    st.image(
        growth_images[st.session_state.growth_stage],
        width=300,
        caption=f"Growth Stage {st.session_state.growth_stage}/3"
    )

    if not st.session_state.watered:
        if st.button("💧 Water Plant"):
            st.session_state.watered = True
            if st.session_state.growth_stage < 3:
                st.session_state.growth_stage += 1
            st.success("Your plant grows stronger 🌿")
    else:
        st.info("Come back tomorrow to continue growing 🌱")

    st.markdown("</div>", unsafe_allow_html=True)

# ------------------ ENVIRONMENT NEWS ------------------
elif page == "Environment News":
    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    st.header("🌍 Earth Today")

    st.markdown("""
    - Renewable energy adoption is accelerating  
    - Global reforestation projects are expanding  
    - Plastic bans increasing worldwide  
    - Sustainable cities are on the rise  
    """)

    st.image(
        "https://images.unsplash.com/photo-1469474968028-56623f02e42e",
        use_container_width=True
    )
    st.markdown("</div>", unsafe_allow_html=True)

# ------------------ GLOBAL SOLUTIONS ------------------
elif page == "Global Solutions":
    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    st.header("🌎 Global Green Solutions")

    st.markdown("""
    **Germany** – Renewable energy leadership  
    **India** – Solar missions & tree drives  
    **Sweden** – Waste-to-energy innovation  
    **Costa Rica** – Eco-tourism & conservation  
    """)

    st.image(
        "https://images.unsplash.com/photo-1483729558449-99ef09a8c325",
        use_container_width=True
    )
    st.markdown("</div>", unsafe_allow_html=True)

# ------------------ FOOTER ------------------
st.markdown("""
<p style="text-align:center; opacity:0.7; margin-top:40px;">
Eco-Echo 🌿 — Small steps. Living forests.
</p>
""", unsafe_allow_html=True)
