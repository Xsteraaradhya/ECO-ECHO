import streamlit as st
from datetime import date

# ------------------ PAGE CONFIG ------------------
# ---------- SIDEBAR NAVIGATION (SAFE) ----------
if "page" not in st.session_state:
    st.session_state.page = "Home"

st.sidebar.title("🌿 Menu")

st.session_state.page = st.sidebar.radio(
    "Navigate",
    ["Home", "Plant Care Tips", "Daily Plant Game", "Environment News", "Global Solutions"],
    key="sidebar_radio_unique"
)

page = st.session_state.page


# ------------------ CUSTOM CSS ------------------
st.markdown("""
    <style>
        body {
            background-color: #eaf7ef;
        }
        .main {
            background-color: #eaf7ef;
        }
        h1, h2, h3 {
            color: #2f7d32;
        }
        .card {
            background-color: #dff5e3;
            padding: 20px;
            border-radius: 15px;
            margin-bottom: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# ------------------ TITLE ------------------
st.title("🌱 Eco-Echo")
st.subheader("Care for plants. Care for Earth.")

# ------------------ SIDEBAR ------------------

   page = st.sidebar.radio(
    "Navigate",
    ["Home", "Plant Care Tips", "Daily Plant Game", "Environment News", "Global Solutions"],
    key="navigation"
)

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

    if "watered" not in st.session_state:
        st.session_state.watered = False
        st.session_state.last_day = None

    today = date.today()

    if st.session_state.last_day != today:
        st.session_state.watered = False
        st.session_state.last_day = today

    st.image(
        "https://images.unsplash.com/photo-1524594154908-eddc6f1a1b13",
        caption="Your virtual plant",
        width=300
    )

    if not st.session_state.watered:
        if st.button("💧 Water Plant"):
            st.session_state.watered = True
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
st.markdown("🌱 *Eco-Echo – Small steps, big impact.*")
import streamlit as st
from datetime import date

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Eco-Echo 🌱",
    page_icon="🌿",
    layout="wide"
)

# ------------------ CUSTOM CSS ------------------
st.markdown("""
    <style>
        body {
            background-color: #eaf7ef;
        }
        .main {
            background-color: #eaf7ef;
        }
        h1, h2, h3 {
            color: #2f7d32;
        }
        .card {
            background-color: #dff5e3;
            padding: 20px;
            border-radius: 15px;
            margin-bottom: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# ------------------ TITLE ------------------
st.title("🌱 Eco-Echo")
st.subheader("Care for plants. Care for Earth.")

# ------------------ SIDEBAR ------------------
st.sidebar.title("🌿 Menu")
page = st.sidebar.radio(
    "Navigate",
    ["Home", "Plant Care Tips", "Daily Plant Game", "Environment News", "Global Solutions"]
)

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

    if "watered" not in st.session_state:
        st.session_state.watered = False
        st.session_state.last_day = None

    today = date.today()

    if st.session_state.last_day != today:
        st.session_state.watered = False
        st.session_state.last_day = today

    st.image(
        "https://images.unsplash.com/photo-1524594154908-eddc6f1a1b13",
        caption="Your virtual plant",
        width=300
    )

    if not st.session_state.watered:
        if st.button("💧 Water Plant"):
            st.session_state.watered = True
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
st.markdown("🌱 *Eco-Echo – Small steps, big impact.*")
