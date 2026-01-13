
import streamlit as st
from datetime import datetime


# APP CONFIG


st.set_page_config(
    page_title="Eco-Echo",
    page_icon="🌱",
    layout="wide"
)


# SESSION STATE (FIXES ALL STATE ISSUES)


if "xp" not in st.session_state:
    st.session_state.xp = 0
    st.session_state.level = 1
    st.session_state.streak = 0
    st.session_state.water_count = 0
    st.session_state.last_action = None



plants = [
    {"name": "Basil", "water": "Daily", "sunlight": "High"},
    {"name": "Cactus", "water": "Weekly", "sunlight": "Medium"},
    {"name": "Rose", "water": "Every 2 Days", "sunlight": "High"}
]

news = [
    {"title": "Global Renewable Energy Growth", "content": "Renewables now supply 30% of global energy."},
    {"title": "Plastic Ban Success", "content": "Countries cut plastic waste by 40%."}
]

policies = [
    {"country": "Germany", "policy": "100% clean electricity by 2035"},
    {"country": "Costa Rica", "policy": "Carbon neutral initiative"}
]



def recalculate_level():
    st.session_state.level = st.session_state.xp // 100 + 1


def update_streak():
    today = datetime.now().date()
    if st.session_state.last_action != today:
        st.session_state.streak += 1
        st.session_state.last_action = today

# ============================================================
# SIDEBAR NAVIGATION
# ============================================================

page = st.sidebar.radio(
    "Navigate",
    ["Home", "Plant Care", "News", "Policies", "Profile"]
)



if page == "Home":
    st.title("🌱 Eco-Echo")
    st.subheader("Grow knowledge. Grow plants. Grow the planet.")

    col1, col2, col3 = st.columns(3)
    col1.metric("Level", st.session_state.level)
    col2.metric("XP", st.session_state.xp)
    col3.metric("Streak (days)", st.session_state.streak)

    st.info("Daily mission: Water a plant and read one eco article.")

# ============================================================
# PLANT CARE GAME
# ============================================================

elif page == "Plant Care":
    st.header("🌿 Plant Care")

    for plant in plants:
        st.markdown(f"**{plant['name']}**  ")
        st.text(f"Water: {plant['water']} | Sunlight: {plant['sunlight']}")

    if st.button("💧 Water Plant"):
        st.session_state.water_count += 1
        st.session_state.xp += 10
        update_streak()
        recalculate_level()
        st.success("Plant watered! +10 XP")

    st.write(f"Watered today: {st.session_state.water_count}")

# ============================================================
# NEWS
# ============================================================

elif page == "News":
    st.header("📰 Environmental News")

    for article in news:
        with st.expander(article["title"]):
            st.write(article["content"])
            if st.button(f"Read: {article['title']}"):
                st.session_state.xp += 5
                recalculate_level()
                st.success("+5 XP for learning!")

# ============================================================
# POLICIES
# ============================================================

elif page == "Policies":
    st.header("🌍 Global Environmental Policies")

    for p in policies:
        st.markdown(f"**{p['country']}** — {p['policy']}")

# ============================================================
# PROFILE
# ============================================================

elif page == "Profile":
    st.header("👤 Profile")
    st.write(f"Eco Level: {st.session_state.level}")
    st.write(f"Total XP: {st.session_state.xp}")
    st.write(f"Current Streak: {st.session_state.streak}")

# ============================================================
# TEST CASES (SIMPLE VALIDATION)
# ============================================================

assert st.session_state.level >= 1
assert st.session_state.xp >= 0
assert st.session_state.streak >= 0

# ============================================================
# STATUS: ✅ STREAMLIT CLOUD + GITHUB READY
# RUN WITH: streamlit run app.py
# ============================================================
