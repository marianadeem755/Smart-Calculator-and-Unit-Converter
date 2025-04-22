import streamlit as st
from sympy import sympify, pi, E, sqrt
from pint import UnitRegistry
import datetime

# Setup Unit Registry
ureg = UnitRegistry()
Q_ = ureg.Quantity

# Constants
constants = {
    "π": pi.evalf(),
    "e": E.evalf(),
    "g (gravity)": 9.80665,
    "c (speed of light)": 299792458  # in m/s
}

# Session state for history
if "history" not in st.session_state:
    st.session_state.history = []

# Page config
st.set_page_config(
    page_title="🧪 Scientific Calculator & Unit Converter",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
    <style>
        /* Custom styling for the title */
        .title {
            text-align: center;
            font-size: 2.5rem;
            font-weight: bold;
            color: darkred;  /* Changed to dark red */
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.6);
        }

        /* Sidebar styling (links, icons) */
        .sidebar-links img {
            width: 20px;
            margin-right: 10px;
            vertical-align: middle;
        }

        .sidebar-links a {
            text-decoration: none;
            color: #333;
            font-weight: 500;
        }

        .sidebar-links {
            line-height: 2.5;
        }

        /* Styling for the input fields */
        input, .stTextInput, .stNumberInput, .stButton {
            background-color: rgba(255, 255, 255, 0.8);  /* Light background for input fields */
            border: none;
            border-radius: 5px;
            padding: 10px;
            font-size: 1rem;
        }

        /* Style for the buttons */
        button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 15px;
            border-radius: 5px;
            font-weight: bold;
            cursor: pointer;
        }

        button:hover {
            background-color: #45a049;
        }

        /* Background for the whole app */
        body {
            background-color: #111 !important;
            color: #fff !important;
        }

        h1, h2, h3, .stTextInput label {
            color: rgb(62, 2, 6);
        }

        hr {
            margin-top: 2rem;
            border: 1px solid #444;
        }

        .stTextInput input, .stNumberInput input {
            background-color: #222;
            color: #0ff;
        }

        /* Button styling */
        .stButton>button {
            background-color: #00f5d4;
            color: black;
            font-weight: bold;
            border-radius: 10px;
        }

        /* Background image for both the app and the sidebar */
        .stApp {
            background: url("https://img.freepik.com/premium-photo/abstract-purple-background-with-smooth-curves_1332213-51917.jpg?semt=ais_hybrid&w=740");
            background-size: cover;
            background-position: center;
            height: 100%;
        }

        /* Set a background image for the sidebar */
        [data-testid="stSidebar"] {
            background-image: url("https://img.freepik.com/free-vector/abstract-background-vertical-with-colorful-shape_361591-4081.jpg?semt=ais_hybrid&w=740");
            background-size: cover;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar content
st.sidebar.markdown("## 👨‍💻 Connect with Me")

st.sidebar.markdown("""
    <div class="sidebar-links">
        <a href="https://github.com/marianadeem755" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png"> GitHub
        </a><br>
        <a href="https://www.kaggle.com/marianadeem755" target="_blank">
            <img src="https://cdn4.iconfinder.com/data/icons/logos-and-brands/512/189_Kaggle_logo_logos-512.png"> Kaggle
        </a><br>
        <a href="mailto:marianadeem755@gmail.com">
            <img src="https://cdn-icons-png.flaticon.com/512/561/561127.png"> Email
        </a><br>
        <a href="https://huggingface.co/maria355" target="_blank">
            <img src="https://huggingface.co/front/assets/huggingface_logo-noborder.svg"> Hugging Face
        </a>
    </div>
""", unsafe_allow_html=True)

# App Title
st.markdown("<h1 class='title'>🧮 Smart Calculator & Unit Converter</h1>", unsafe_allow_html=True)

# Tabs for navigation
tab1, tab2, tab3, tab4 = st.tabs(["➕ Simple Calculator", "📐 Scientific Calculator", "🔁 Unit Converter", "🧾 History"])

# Simple Calculator tab
with tab1:
    st.markdown("### Perform basic operations")
    num1 = st.number_input("Enter first number", key="n1")
    num2 = st.number_input("Enter second number", key="n2")

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("➕ Add"):
            res = num1 + num2
            st.success(f"{num1} + {num2} = {res}")
            st.session_state.history.append(f"{num1} + {num2} = {res}")
    with col2:
        if st.button("➖ Subtract"):
            res = num1 - num2
            st.success(f"{num1} - {num2} = {res}")
            st.session_state.history.append(f"{num1} - {num2} = {res}")
    with col3:
        if st.button("✖ Multiply"):
            res = num1 * num2
            st.success(f"{num1} × {num2} = {res}")
            st.session_state.history.append(f"{num1} × {num2} = {res}")

    col4, col5, col6 = st.columns(3)
    with col4:
        if st.button("➗ Divide"):
            if num2 == 0:
                st.error("Cannot divide by zero!")
            else:
                res = num1 / num2
                st.success(f"{num1} ÷ {num2} = {res}")
                st.session_state.history.append(f"{num1} ÷ {num2} = {res}")
    with col5:
        if st.button("🔢 Modulus"):
            res = num1 % num2
            st.success(f"{num1} % {num2} = {res}")
            st.session_state.history.append(f"{num1} % {num2} = {res}")
    with col6:
        if st.button("^ Power"):
            res = num1 ** num2
            st.success(f"{num1} ^ {num2} = {res}")
            st.session_state.history.append(f"{num1} ^ {num2} = {res}")

    if st.button("√ Square Root (of 1st number)"):
        if num1 < 0:
            st.error("❌ Cannot take square root of negative number!")
        else:
            res = sqrt(num1).evalf()
            st.success(f"√{num1} = {res}")
            st.session_state.history.append(f"√{num1} = {res}")

# Scientific Calculator tab
with tab2:
    st.markdown("### Enter your formula:")
    expr_input = st.text_input("Example: 2 * π * 5 or (3 + 2)^2", key="calc_input")

    if st.button("Calculate", key="calc_btn"):
        try:
            for name, val in constants.items():
                expr_input = expr_input.replace(name, str(val))

            result = sympify(expr_input).evalf()
            timestamp = datetime.datetime.now().strftime("%H:%M:%S")
            st.success(f"✅ Result: {result}")
            st.session_state.history.append(f"[{timestamp}] [Scientific] {expr_input} = {result}")
        except Exception as e:
            st.error(f"❌ Error: {e}")

# Unit Converter tab
with tab3:
    st.markdown("### Convert between units:")

    value = st.number_input("Enter value:", step=0.1, key="unit_val")
    from_unit = st.text_input("From unit (e.g. meter, kg, second):")
    to_unit = st.text_input("To unit (e.g. feet, lb, minute):")

    if st.button("Convert", key="convert_btn"):
        try:
            quantity = Q_(value, from_unit)
            converted = quantity.to(to_unit)
            st.success(f"✅ {value} {from_unit} = {converted}")
            st.session_state.history.append(f"{value} {from_unit} = {converted}")
        except Exception as e:
            st.error(f"❌ Conversion Error: {e}")

# History tab
with tab4:
    st.markdown("### 🧾 Your Recent Calculations")
    if st.session_state.history:
        for item in reversed(st.session_state.history[-20:]):
            st.markdown(f"- {item}")
    else:
        st.info("No calculations yet.")
