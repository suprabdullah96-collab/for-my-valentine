import streamlit as st

# Set page config for a mobile-friendly look
st.set_page_config(page_title="Valentine?", page_icon="❤️")

# Custom CSS to style the buttons and center everything
st.markdown("""
    <style>
    .stButton button {
        width: 100%;
        border-radius: 20px;
    }
    .yes-button button {
        background-color: #4caf50 !important;
        color: white !important;
    }
    .no-button button {
        background-color: #f44336 !important;
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

if 'stage' not in st.session_state:
    st.session_state.stage = 0
if 'yes_size' not in st.session_state:
    st.session_state.yes_size = 20

messages = [
    "No", "Are you sure?", "Really sure??", "Pookie please...", 
    "Just think about it!", "I will be very sad...", "Don't do this to me!"
]

# If she hasn't clicked "Yes" yet
if st.session_state.stage < 100:
    st.title("Will you be my Valentine? 🌹")
    
    # Placeholder for a cute image/GIF link
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHp1bmNid2Z4dzRieXp0eXpueXpueXpueXpueXpueXpueXpueXpueCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/cLS1cfxvGOPVpf9g3y/giphy.gif")

    col1, col2 = st.columns([1, 1])

    with col1:
        # The Yes button grows
        if st.button("Yes", key="yes_btn"):
            st.session_state.stage = 100
            st.rerun()

    with col2:
        # The No button cycles through messages
        no_text = messages[st.session_state.stage % len(messages)]
        if st.button(no_text, key="no_btn"):
            st.session_state.stage += 1
            st.session_state.yes_size += 20  # Logic for button growth (visual effect varies by platform)
            st.rerun()

else:
    st.balloons()
    st.title("Knew you would say yes! ❤️")

    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHp1bmNid2Z4dzRieXp0eXpueXpueXpueXpueXpueXpueXpueXpueCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/K976VvCc8z4xG/giphy.gif")
