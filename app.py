import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Users
users = {"admin": "1234"}

# Session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ---------------- GLOBAL STYLE ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #ffe5e5, #ffffff);
}

.login-box {
    background-color: rgba(255,255,255,0.95);
    padding: 30px;
    border-radius: 15px;
    width: 350px;
    margin: auto;
    margin-top: 100px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.3);
}

.title {
    text-align: center;
    font-size: 40px;
    color: #8B0000;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: #B71C1C;
    font-size: 18px;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- LOGIN PAGE ----------------
def login_page():
    st.markdown('<p class="title">🎓 EduPredict AI</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Predict Student Performance with AI</p>', unsafe_allow_html=True)

    st.markdown('<div class="login-box">', unsafe_allow_html=True)

    username = st.text_input("👤 Username")
    password = st.text_input("🔒 Password", type="password")

    if st.button("Login"):
        if username in users and users[username] == password:
            st.session_state.logged_in = True
            st.success("Login successful!")
            st.rerun()
        else:
            st.error("Invalid credentials")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- SIGNUP PAGE ----------------
def signup_page():
    st.title("📝 Create Account")

    new_user = st.text_input("Username")
    new_pass = st.text_input("Password", type="password")

    if st.button("Signup"):
        users[new_user] = new_pass
        st.success("Account created! Go to login.")

# ---------------- ABOUT PAGE ----------------
def about_page():
    st.markdown('<p class="title">ℹ️ About EduPredict AI</p>', unsafe_allow_html=True)

    st.write("""
    EduPredict AI is a machine learning-based web application that predicts student performance.

    🔴 Built using Python, Streamlit  
    🔴 Uses Random Forest model  
    🔴 Provides interactive UI for prediction  

    This project demonstrates how AI can be used in education systems to analyze and improve student outcomes.
    """)

# ---------------- MAIN APP ----------------
def main_app():

    st.markdown('<p class="title">📊 Student Performance Predictor</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Enter student details below</p>', unsafe_allow_html=True)

    st.image("https://images.unsplash.com/photo-1523240795612-9a054b0db644", use_container_width=True)

    st.write("### 📊 Enter Student Details")

    col1, col2 = st.columns(2)

    with col1:
        studytime = st.slider("Study Time", 1, 4, 2)
        failures = st.slider("Failures", 0, 4, 0)
        absences = st.slider("Absences", 0, 50, 5)

    with col2:
        G1 = st.slider("G1 Marks", 0, 20, 10)
        G2 = st.slider("G2 Marks", 0, 20, 10)

    if st.button("Predict"):
        input_data = pd.DataFrame({
            "studytime": [studytime],
            "failures": [failures],
            "absences": [absences],
            "G1": [G1],
            "G2": [G2]
        })

        prediction = model.predict(input_data)

        st.success(f"🎯 Predicted Final Marks: {prediction[0]:.2f}")

        fig, ax = plt.subplots()
        ax.bar(["Predicted"], [prediction[0]])
        st.pyplot(fig)

# ---------------- NAVIGATION ----------------
if st.session_state.logged_in:
    page = st.sidebar.selectbox("Menu", ["Home", "About", "Logout"])

    if page == "Home":
        main_app()
    elif page == "About":
        about_page()
    else:
        st.session_state.logged_in = False
        st.rerun()
else:
    page = st.sidebar.selectbox("Menu", ["Login", "Signup", "About"])

    if page == "Login":
        login_page()
    elif page == "Signup":
        signup_page()
    else:
        about_page()