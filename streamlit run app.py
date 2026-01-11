import streamlit as st
from datetime import date

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Eco-Echo 🌱",
    page_icon="🌿",
    layout="wide"
)

# ------------------ CUSTOM CSS (Hello Kitty Green + Black Chancery) ------------------
st.markdown("""
    <style>
        /* Page background */
        body {
            background-color: #c8f2c8;  /* Hello Kitty green pastel */
            font-family: 'Black Chancery', cursive;
            color: #1b3a1b;  /* Dark green text */
        }

        /* Main container */
        .main {
            background-color: #c8f2c8;
        }

        /* Headers */
        h1, h2, h3 {
            color: #1b3a1b;
            font-family: 'Black Chancery', cursive;
        }

        /* Sidebar */
        .css-1d391kg {
            background-color: #b8e6b8;  /* pastel green */
            color: #1b3a1b;
        }
        .css-1d391kg .stRadio label {
            color: #1b3a1b;
        }

        /* Cards */
        .card {
            background-color: #d4f1d4;
            padding: 20px;
            border-radius: 15px;
            margin-bottom: 20px;
        }

        /* Buttons */
        .stButton>button {
            background-color: #a0e0a0;
            color: #1b3a1b;
            font-family: 'Black Chancery', cursive;
        }

        /* Footer text */
        .footer {
            color: #1b3a1b;
            font-family: 'Black Chancery', cursive;
            font-size: 16px;
        }
    </style>

    <!-- Load Black Chancery font from Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Black+Chancery&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

# ------------------ SIDEBAR NAVIGATION ------------------
if "page" not in st.session_state:
    st.session_state.page = "Home"

st.sidebar.title("🌿 Eco Menu")
st.session_state.page = st.sidebar.radio(
    "Navigate",
    ["Home", "Plant Care Tips", "Daily Plant Game", "Environment News", "Global Solutions"],
    key="sidebar_radio_unique"
)
page = st.session_state.page

# ------------------ TITLE ------------------
st.title("🌱 Eco-Echo")
st.subheader("Care for plants. Care for Earth.")

# ------------------ HOME ------------------
if page == "Home":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.write(
        "Eco-Echo is an educational app designed to help people learn about plant care, "
        "environmental protection, and sustainable habits. Through simple tips, global "
        "environmental updates, and a daily plant-care game, Eco-Echo encourages users "
        "to make eco-friendly choices every day."
    )
    st.image(
        "https://images.unsplash.com/photo-1469474968028-56623f02e42e",
        caption="Protect nature for future generations",
        use_container_width=True
    )
    st.markdown("</div>", unsafe_allow_html=True)

# ------------------ PLANT CARE TIPS ------------------
elif page == "Plant Care Tips":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("🌿 Plant Care & Watering Tips")
    st.image(
        "https://images.unsplash.com/photo-1501004318641-b39e6451bec6",
        use_container_width=True
    )
    st.markdown("""
    - Water plants early in the morning or evening  
    - Avoid overwatering; check soil moisture first  
    - Use compost or natural fertilizers  
    - Place plants where they receive proper sunlight  
    - Remove dry or damaged leaves regularly  
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# ------------------ DAILY PLANT GAME ------------------
elif page == "Daily Plant Game":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("🎮 Daily Plant Care Game")

    # Initialize plant growth state
    if "watered" not in st.session_state:
        st.session_state.watered = False
        st.session_state.last_day = None
        st.session_state.growth_stage = 0  # 0 = seed, 1 = sprout, 2 = small tree, 3 = grown tree

    today = date.today()

    # Reset daily watering
    if st.session_state.last_day != today:
        st.session_state.watered = False
        st.session_state.last_day = today

    # Tree growth images based on stage
    growth_images = [
        "https://i.imgur.com/Jf6F0G7.png",  # seed
        "https://i.imgur.com/4a2p9Q6.png",  # sprout
        "https://i.imgur.com/EJ2Vq7y.png",  # small tree
        "https://i.imgur.com/q3RklbY.png"   # full grown tree
    ]

    st.image(
        growth_images[st.session_state.growth_stage],
        caption=f"🌳 Plant growth stage: {st.session_state.growth_stage}/3",
        width=300
    )

    if not st.session_state.watered:
        if st.button("💧 Water Plant", key="water_button"):
            st.session_state.watered = True
            # Increase growth stage (max 3)
            if st.session_state.growth_stage < 3:
                st.session_state.growth_stage += 1
            st.success("Great job! Your plant is happy today 🌱")
    else:
        st.info("You already watered your plant today. Come back tomorrow!")

    st.markdown("</div>", unsafe_allow_html=True)

# ------------------ ENVIRONMENT NEWS ------------------
elif page == "Environment News":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("🌍 Environmental News")
    st.image(
        "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee",
        use_container_width=True
    )
    st.markdown("""
    - 🌡️ Climate change awareness is increasing worldwide  
    - 🌳 Tree plantation drives are growing globally  
    - ♻️ Recycling and plastic reduction initiatives are expanding  
    - 🔋 Renewable energy usage is rising  
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# ------------------ GLOBAL SOLUTIONS ------------------
elif page == "Global Solutions":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("🏛️ Global Environmental Solutions")
    st.markdown("""
    **🌱 Germany:** Investment in renewable energy and recycling systems  
    **🌿 India:** Large-scale tree plantation and solar power missions  
    **🌍 Sweden:** Waste-to-energy programs and low emissions policies  
    **🌳 Costa Rica:** Forest conservation and eco-tourism initiatives  
    """)
    st.image(
        "https://images.unsplash.com/photo-1483729558449-99ef09a8c325",
        use_container_width=True
    )
    st.markdown("</div>", unsafe_allow_html=True)

# ------------------ FOOTER ------------------
st.markdown("---")
st.markdown('<p class="footer">🌱 Eco-Echo – Small steps, big impact.</p>', unsafe_allow_html=True)

