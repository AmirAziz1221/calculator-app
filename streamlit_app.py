import streamlit as st

st.set_page_config(page_title="Calculator", page_icon="🧮", layout="centered")

# ---------- Styling to match original green/black Tkinter look ----------
st.markdown("""
<style>
    .stApp { background-color: #000000; }
    div.stButton > button {
        background-color: #00a65a;
        color: white;
        font-size: 20px;
        font-weight: bold;
        height: 60px;
        width: 100%;
        border-radius: 6px;
        border: none;
    }
    div.stButton > button:hover {
        background-color: #008c4c;
        color: white;
    }
    .display-box {
        background-color: #000000;
        color: white;
        font-size: 36px;
        font-weight: bold;
        text-align: right;
        padding: 15px;
        border: 1px solid #333;
        border-radius: 6px;
        margin-bottom: 15px;
        min-height: 60px;
        overflow-x: auto;
    }
    h1 { color: white; text-align: center; }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>🧮 Calculator</h1>", unsafe_allow_html=True)

# ---------- State (mirrors the Tkinter globals) ----------
if "display" not in st.session_state:
    st.session_state.display = ""
if "first_number" not in st.session_state:
    st.session_state.first_number = None
if "operator" not in st.session_state:
    st.session_state.operator = None


def get_digit(digit):
    st.session_state.display += str(digit)


def clear():
    st.session_state.display = ""
    st.session_state.first_number = None
    st.session_state.operator = None


def get_operator(op):
    if st.session_state.display == "":
        return
    st.session_state.first_number = int(st.session_state.display)
    st.session_state.operator = op
    st.session_state.display = ""


def get_result():
    if st.session_state.operator is None or st.session_state.display == "":
        return
    second_number = int(st.session_state.display)
    first_number = st.session_state.first_number
    op = st.session_state.operator

    if op == "+":
        st.session_state.display = str(first_number + second_number)
    elif op == "-":
        st.session_state.display = str(first_number - second_number)
    elif op == "*":
        st.session_state.display = str(first_number * second_number)
    elif op == "/":
        if second_number == 0:
            st.session_state.display = "Error"
        else:
            st.session_state.display = str(round(first_number / second_number, 2))

    st.session_state.operator = None


# ---------- Display ----------
st.markdown(f"<div class='display-box'>{st.session_state.display}</div>", unsafe_allow_html=True)

# ---------- Button grid (same layout as the Tkinter version) ----------
row1 = st.columns(4)
row1[0].button("7", on_click=get_digit, args=(7,), use_container_width=True)
row1[1].button("8", on_click=get_digit, args=(8,), use_container_width=True)
row1[2].button("9", on_click=get_digit, args=(9,), use_container_width=True)
row1[3].button("+", on_click=get_operator, args=("+",), use_container_width=True)

row2 = st.columns(4)
row2[0].button("4", on_click=get_digit, args=(4,), use_container_width=True)
row2[1].button("5", on_click=get_digit, args=(5,), use_container_width=True)
row2[2].button("6", on_click=get_digit, args=(6,), use_container_width=True)
row2[3].button("-", on_click=get_operator, args=("-",), use_container_width=True)

row3 = st.columns(4)
row3[0].button("1", on_click=get_digit, args=(1,), use_container_width=True)
row3[1].button("2", on_click=get_digit, args=(2,), use_container_width=True)
row3[2].button("3", on_click=get_digit, args=(3,), use_container_width=True)
row3[3].button("*", on_click=get_operator, args=("*",), use_container_width=True)

row4 = st.columns(4)
row4[0].button("C", on_click=clear, use_container_width=True)
row4[1].button("0", on_click=get_digit, args=(0,), use_container_width=True)
row4[2].button("=", on_click=get_result, use_container_width=True)
row4[3].button("/", on_click=get_operator, args=("/",), use_container_width=True)
