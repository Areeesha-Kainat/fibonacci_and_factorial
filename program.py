import streamlit as st

# Initialize session state for dark mode
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False

# Custom CSS for dark/light mode
def set_theme():
    bg_color = "#0E1117" if st.session_state.dark_mode else "#FFFFFF"
    text_color = "#FFFFFF" if st.session_state.dark_mode else "#000000"
    result_bg = "rgba(255, 255, 255, 0.1)" if st.session_state.dark_mode else "rgba(0, 0, 0, 0.1)"
    
    # Conditional button styling for dark mode
    button_style = """
        .stButton>button {
            background-color: #FFFFFF !important;
            color: #000000 !important;
            border: 1px solid #FFFFFF !important;
        }
    """ if st.session_state.dark_mode else ""
    
    custom_css = f"""
        <style>
            .stApp {{
                background-color: {bg_color} !important;
                color: {text_color} !important;
            }}
            header {{
                background-color: {bg_color} !important;
            }}
            .st-b7, .st-cg, .st-ch, .st-ci, label {{
                color: {text_color} !important;
            }}
            .result-box {{
                background-color: {result_bg};
                border-radius: 15px;
                padding: 25px;
                margin: 20px 0;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }}
            .title {{
                font-family: 'Arial Rounded MT Bold', sans-serif;
                color: {'#00FF88' if st.session_state.dark_mode else '#FF4B4B'} !important;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
            }}
            .theme-switch {{
                position: fixed;
                right: 30px;
                top: 20px;
                z-index: 999;
            }}
            {button_style}
        </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

# Theme toggle button
col1, col2 = st.columns([4, 1])
with col1:
    st.markdown('<h1 class="title">Math Magic Studio</h1>', unsafe_allow_html=True)
with col2:
    if st.button("🌙" if not st.session_state.dark_mode else "☀️", key="theme"):
        st.session_state.dark_mode = not st.session_state.dark_mode

set_theme()

# Main content layout
fib_col, fact_col = st.columns(2)

# Fibonacci Section
with fib_col:
    st.header("Fibonacci Generator", divider='rainbow')
    fib_input = st.number_input("Enter maximum number:", min_value=0, key="fib_num")
    
    if st.button("Generate Sequence"):
        x, y = 0, 1
        fib_sequence = []
        fib_sequence.append(x)
        while y <= fib_input:
            fib_sequence.append(y)
            x, y = y, x + y
        
        with st.container():
            st.markdown(f"""
            <div class="result-box">
                <h4 style="color: {'#00FF88' if st.session_state.dark_mode else '#FF4B4B'};">Fibonacci Sequence up to {fib_input}:</h4>
                <div style="max-height: 200px; overflow-y: auto;">
                    {' • '.join(map(str, fib_sequence))}
                </div>
            </div>
            """, unsafe_allow_html=True)

# Factorial Section
with fact_col:
    st.header("Factorial Calculator", divider='rainbow')
    fact_input = st.number_input("Enter a number:", min_value=0, key="fact_num")
    
    if st.button("Calculate Factorial"):
        fact = 1
        current = fact_input
        while current > 0:
            fact *= current
            current -= 1
        
        with st.container():
            st.markdown(f"""
            <div class="result-box">
                <h4 style="color: {'#00FF88' if st.session_state.dark_mode else '#FF4B4B'};">Factorial Result:</h4>
                <p style="font-size: 1.5em; font-weight: bold;">
                    {fact_input}! = {fact:,}
                </p>
            </div>
            """, unsafe_allow_html=True)

# Decorative elements
st.markdown("""
<style>
    [data-testid="stDecoration"] {
        background-image: linear-gradient(90deg, #00FF88, #FF4B4B) !important;
    }
</style>
""", unsafe_allow_html=True)