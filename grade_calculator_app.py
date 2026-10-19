import streamlit as st
st.markdown("""
<style>

/* =========================================
   WHOLE PAGE
   ========================================= */

.stApp {
    background-color: #eeeeec;
    color: #1c1c1c;
}

/* White dashboard/card */
.block-container {
    max-width: 900px;
    background-color: #ffffff;

    margin-top: 35px;
    margin-bottom: 35px;

    padding: 50px 60px 60px 60px;

    border: 1px solid #d4d4d0;
    border-radius: 28px;
}


/* =========================================
   TYPEWRITER FONT
   ========================================= */

html,
body,
.stApp,
button,
input,
textarea,
select,
label,
p,
span,
div {
    font-family:
        "Courier New",
        "Menlo",
        "Monaco",
        monospace !important;
}


/* =========================================
   CUTE BLACK OUTLINE ICONS
   ========================================= */

.block-container::before {
    content: "♡   ୨୧   ☁︎   ☆";
    display: block;

    text-align: center;

    font-size: 24px;
    letter-spacing: 12px;

    color: #1c1c1c;

    margin-bottom: 12px;
}

.block-container::after {
    content: "☆   ♡   ☁︎   ୨୧";
    display: block;

    text-align: center;

    font-size: 20px;
    letter-spacing: 12px;

    color: #1c1c1c;

    margin-top: 40px;
}


/* =========================================
   TITLE
   ========================================= */

h1 {
    text-align: center;

    font-size: 40px !important;
    font-weight: 400 !important;

    letter-spacing: 2px;

    color: #1c1c1c;

    margin-bottom: 35px !important;
}


/* =========================================
   LABELS
   ========================================= */

label p {
    font-size: 16px !important;
    font-weight: 400 !important;

    letter-spacing: 0.5px;

    color: #222222 !important;
}


/* =========================================
   TEXT INPUT BOXES
   ========================================= */

div[data-baseweb="input"] > div {

    background-color: #f8f8f7 !important;

    border: 1.5px solid #222222 !important;
    border-radius: 2px !important;

    min-height: 62px;

    box-shadow: none !important;
}

div[data-baseweb="input"] > div:hover {
    border-color: #000000 !important;
}

div[data-baseweb="input"] input {

    background-color: transparent !important;

    color: #191919 !important;

    font-size: 18px !important;

    padding-left: 18px !important;
}


/* =========================================
   DROPDOWN / SUBJECT BOX
   ========================================= */

div[data-baseweb="select"] > div {

    background-color: #f8f8f7 !important;

    border: 1.5px solid #222222 !important;
    border-radius: 2px !important;

    min-height: 58px;

    box-shadow: none !important;
}


/* =========================================
   CALCULATE BUTTON
   ========================================= */

.stButton > button {

    width: 100%;

    background-color: #ffffff !important;

    color: #1c1c1c !important;

    border: 1.5px solid #1c1c1c !important;
    border-radius: 2px !important;

    min-height: 56px;

    font-family:
        "Courier New",
        monospace !important;

    font-size: 17px !important;

    letter-spacing: 2px;

    margin-top: 15px;

    transition: 0.2s ease;
}

.stButton > button:hover {

    background-color: #1c1c1c !important;

    color: white !important;

    border-color: #1c1c1c !important;
}


/* =========================================
   RESULT / SUCCESS BOX
   if you use st.success()
   ========================================= */

div[data-testid="stAlert"] {

    background-color: #f8f8f7 !important;

    border: 1.5px solid #1c1c1c !important;

    border-radius: 2px !important;

    color: #1c1c1c !important;

    padding: 25px !important;

    margin-top: 25px;
}

div[data-testid="stAlert"] p {

    text-align: center;

    font-size: 22px !important;

    letter-spacing: 1px;
}


/* =========================================
   TWO COLUMNS
   ========================================= */

div[data-testid="stHorizontalBlock"] {
    gap: 35px;
}


/* =========================================
   REMOVE SOME STREAMLIT CLUTTER
   ========================================= */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}


/* =========================================
   MOBILE
   ========================================= */

@media (max-width: 700px) {

    .block-container {

        margin-top: 10px;

        padding: 30px 20px 40px 20px;

        border-radius: 18px;
    }

    h1 {
        font-size: 29px !important;
    }

}

</style>
""", unsafe_allow_html=True)
st.title("Year 3 SOTA Grade Calculator")

subject = st.selectbox(
    "Which subject?",
    [
        "Math",
        "Chinese",
        "Chemistry",
        "Physics",
        "Biology",
        "Literature",
        "ELCT",
        "Geography",
        "History"
    ]
)
term1 = st.text_input("Enter your Term 1 score:")
term2 = st.text_input("Enter your Term 2 score:")
term3 = st.text_input("Enter your Term 3 score:")
if subject == "ELCT":
    re_score = st.text_input("Enter your RE score:")
term4 = st.text_input("Enter your EOY score:")
if st.button("Calculate"):
    if subject in ["Math", "Chinese", "Chemistry", "Physics", "Biology", "Geography", "History"]:
        parts = term1.split("/")
        obtained = float(parts[0])
        total = float(parts[1])
        percentage1 = obtained / total * 100
        parts = term2.split("/")
        obtained = float(parts[0])
        total = float(parts[1])
        percentage2 = obtained / total * 100
        parts = term3.split("/")
        obtained = float(parts[0])
        total = float(parts[1])
        percentage3 = obtained / total * 100
        parts = term4.split("/")
        obtained = float(parts[0])
        total = float(parts[1])
        percentage4 = obtained / total * 100
        overall = (percentage1 * 0.15) + (percentage2 * 0.15) + \
            (percentage3 * 0.15) + (percentage4 * 0.55)
        st.success(f"Your overall is {overall:.2f}%")
    elif subject == "Literature":
        parts = term1.split("/")
        obtained = float(parts[0])
        total = float(parts[1])
        percentage1 = obtained / total * 100
        parts = term2.split("/")
        obtained = float(parts[0])
        total = float(parts[1])
        percentage2 = obtained / total * 100
        parts = term3.split("/")
        obtained = float(parts[0])
        total = float(parts[1])
        percentage3 = obtained / total * 100
        parts = term4.split("/")
        obtained = float(parts[0])
        total = float(parts[1])
        percentage4 = obtained / total * 100
        overall = (percentage1 * 0.15) + (percentage2 * 0.10) + \
            (percentage3 * 0.15) + (percentage4 * 0.60)
        st.success(f"Your overall is {overall:.2f}%")
    elif subject == "ELCT":
        parts = term1.split("/")
        obtained = float(parts[0])
        total = float(parts[1])
        percentage1 = obtained / total * 100
        parts = term2.split("/")
        obtained = float(parts[0])
        total = float(parts[1])
        percentage2 = obtained / total * 100
        parts = term3.split("/")
        obtained = float(parts[0])
        total = float(parts[1])
        percentage3 = obtained / total * 100
        parts = re_score.split("/")
        obtained = float(parts[0])
        total = float(parts[1])
        percentage4 = obtained / total * 100
        parts = term4.split("/")
        obtained = float(parts[0])
        total = float(parts[1])
        percentage5 = obtained / total * 100
        overall = (percentage1 * 0.15) + (percentage2 * 0.15) + \
            (percentage3 * 0.15) + (percentage4 * 0.25) + (percentage5 * 0.30)
        st.success(f"Your overall is {overall:.2f}%")
