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
    </style>
    """, unsafe_allow_html=True)

if 'stage' not in st.session_state:
    st.session_state.stage = 0

# List of messages - the "No" button will disappear after the last one
messages = [
    "No", 
    "Are you sure?", 
    "Really sure??", 
    "Pookie please...", 
    "Just think about it!", 
    "I will be very sad...", 
    "I will be very very very sad...",
    "Okay, fine... last chance to say yes?"
]

# If she hasn't clicked "Yes" yet
if st.session_state.stage < 100:
    st.title("Will you be my Valentine? 🌹")
    
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHp1bmNid2Z4dzRieXp0eXpueXpueXpueXpueXpueXpueXpueXpueCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/cLS1cfxvGOPVpf9g3y/giphy.gif")

    # If we haven't reached the end of the messages, show two columns
    if st.session_state.stage < len(messages):
        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("Yes", key="yes_btn"):
                st.session_state.stage = 100
                st.rerun()
        with col2:
            no_text = messages[st.session_state.stage]
            if st.button(no_text, key="no_btn"):
                st.session_state.stage += 1
                st.rerun()
    
    # If she clicked "No" until the end, only show the Yes button
    else:
        if st.button("YES! (No button is gone now )", key="final_yes_btn"):
            st.session_state.stage = 100
            st.rerun()

# This is what she sees when she says YES
else:
    st.balloons()
    st.title("Knew you would say yes! ❤️")
    st.subheader("We'll ride horses together! ")
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHp1bmNid2Z4dzRieXp0eXpueXpueXpueXpueXpueXpueXpueXpueCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/K976VvCc8z4xG/giphy.gif")
