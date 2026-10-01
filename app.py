import streamlit as st
import pickle
import pandas as pd


# =========================================================
# PAGE SETTINGS
# =========================================================

st.set_page_config(
    page_title="Hyderabad House Price Prediction",
    page_icon="🏠",
    layout="wide"
)


# =========================================================
# LOAD TRAINED MODEL
# =========================================================

with open("house_price_model.pkl", "rb") as file:
    model = pickle.load(file)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

/* =======================================================
   MAIN BACKGROUND
   ======================================================= */

.stApp {
    background: linear-gradient(
        135deg,
        #dbeafe,
        #f0f9ff,
        #ecfeff
    );

}


/* =======================================================
   MAIN TITLE
   ======================================================= */

.main-title {
    text-align: center;
    color: #1e3a8a;
    font-size: 45px;
    font-weight: bold;
    margin-top: 30px;
}


/* =======================================================
   SUBTITLE
   ======================================================= */

.subtitle {
    text-align: center;
    color: #475569;
    font-size: 20px;
    margin-bottom: 40px;
}


/* =======================================================
   INFORMATION BOX
   ======================================================= */

.info-box {
    background-color: white;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
    text-align: center;
}

.info-box h3 {
    color: #1e3a8a !important;
}

.info-box p {
    color: #475569 !important;
}


/* =======================================================
   SECTION HEADINGS
   ======================================================= */

h2 {
    color: #1e3a8a !important;
}


/* =======================================================
   SELECTBOX LABELS
   ======================================================= */

div[data-testid="stSelectbox"] label {
    color: #1e293b !important;
    font-weight: 600;
}


/* =======================================================
   NUMBER INPUT LABELS
   ======================================================= */

div[data-testid="stNumberInput"] label {
    color: #1e293b !important;
    font-weight: 600;
}


/* =======================================================
   SELECTBOX
   ======================================================= */

div[data-baseweb="select"] > div {
    background-color: white !important;
    color: #1e293b !important;
    border: 2px solid #93c5fd !important;
    border-radius: 10px !important;
}


/* Selected value inside selectbox */

div[data-baseweb="select"] span {
    color: #1e293b !important;
}


/* =======================================================
   NUMBER INPUT
   ======================================================= */

div[data-testid="stNumberInput"] input {
    color: #1e293b !important;
    background-color: white !important;
    font-weight: 600;
}


div[data-testid="stNumberInput"] > div {
    background-color: white !important;
    border: 2px solid #93c5fd !important;
    border-radius: 10px !important;
}


/* =======================================================
   PREDICT BUTTON
   ======================================================= */

div.stButton > button {
    background-color: #1e3a8a !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    height: 50px !important;
    font-size: 18px !important;
    font-weight: bold !important;
}


/* Button hover */

div.stButton > button:hover {
    background-color: #2563eb !important;
    color: white !important;
    border: none !important;
}


/* =======================================================
   PREDICTION RESULT
   ======================================================= */

.prediction-box {
    background-color: #dcfce7;
    padding: 30px;
    border-radius: 15px;
    text-align: center;
    margin-top: 20px;
    border: 2px solid #22c55e;
}

.prediction-title {
    color: #166534;
    font-size: 28px;
    font-weight: bold;
}

.prediction-price {
    color: #166534;
    font-size: 42px;
    font-weight: bold;
    margin-top: 15px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# TITLE
# =========================================================

st.markdown(
    '<div class="main-title">🏠 Hyderabad House Price Prediction</div>',
    unsafe_allow_html=True
)


# =========================================================
# SUBTITLE
# =========================================================

st.markdown(
    '<div class="subtitle">Predict property prices using Machine Learning</div>',
    unsafe_allow_html=True
)


# =========================================================
# INFORMATION BOX
# =========================================================

st.markdown("""
<div class="info-box">

<h3>📊 Machine Learning Project</h3>

<p>
Enter the details of a Hyderabad property and our trained
Machine Learning model will estimate its price.
</p>

</div>
""", unsafe_allow_html=True)


# =========================================================
# PROPERTY DETAILS
# =========================================================

st.markdown("## 🏠 Property Details")


# =========================================================
# LOCATION
# =========================================================

location = st.selectbox(
    "📍 Select Location",
    [
        "Kokapet",
        "Gachibowli",
        "Kondapur",
        "Miyapur",
        "Manikonda",
        "Bachupally",
        "Tellapur",
        "Nanakramguda",
        "Jubilee Hills",
        "Banjara Hills",
        "Other"
    ]
)


st.markdown(
    f"""
    <div style="
        background-color: #d1fae5;
        padding: 15px;
        border-radius: 10px;
        color: black;
        font-weight: 600;
        margin-top: 10px;
    ">
        Selected Location: {location}
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# AREA
# =========================================================

area = st.number_input(
    "📐 Area (square feet)",
    min_value=100,
    max_value=50000,
    value=1500,
    step=100
)


st.markdown(
    f"""
    <div style="
        background-color: #dbeafe;
        padding: 15px;
        border-radius: 10px;
        color: black;
        font-weight: 600;
        margin-top: 10px;
    ">
        Selected Area: {area} sqft
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# BHK
# =========================================================

bhk = st.number_input(
    "🛏️ Number of BHK",
    min_value=0,
    max_value=10,
    value=2,
    step=1
)


st.markdown(
    f"""
    <div style="
        background-color: #fef3c7;
        padding: 15px;
        border-radius: 10px;
        color: black;
        font-weight: 600;
        margin-top: 10px;
    ">
        Selected BHK: {bhk}
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# PROPERTY TYPE
# =========================================================

property_type = st.selectbox(
    "🏢 Select Property Type",
    [
        "Apartment",
        "Villa",
        "Independent House",
        "Independent Floor",
        "Residential Plot"
    ]
)


st.markdown(
    f"""
    <div style="
        background-color: #ede9fe;
        padding: 15px;
        border-radius: 10px;
        color: black;
        font-weight: 600;
        margin-top: 10px;
    ">
        Selected Property Type: {property_type}
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# BUILDING STATUS
# =========================================================

building_status = st.selectbox(
    "🚧 Select Building Status",
    [
        "New",
        "Under Construction",
        "Ready to move",
        "Resale"
    ]
)


st.markdown(
    f"""
    <div style="
        background-color: #fee2e2;
        padding: 15px;
        border-radius: 10px;
        color: black;
        font-weight: 600;
        margin-top: 10px;
    ">
        Selected Building Status: {building_status}
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# PREDICTION SECTION
# =========================================================

st.markdown("---")

st.markdown(
    """
    <div style="
        text-align: center;
        color: #1e3a8a;
        font-size: 32px;
        font-weight: bold;
        margin-bottom: 20px;
    ">
        🔮 Predict House Price
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# PREDICTION SECTION
# =========================================================

st.markdown("---")

st.markdown(
    """
    <div style="
        text-align: center;
        color: #1e3a8a;
        font-size: 32px;
        font-weight: bold;
        margin-bottom: 20px;
    ">
        🔮 Predict House Price
    </div>
    """,
    unsafe_allow_html=True
)


if st.button("💰 Predict Price", use_container_width=True):

    # Create input DataFrame
    input_data = pd.DataFrame({
        "location": [location],
        "building_status": [building_status],
        "property_type": [property_type],
        "bhk": [bhk],
        "area_insqft": [area]
    })

    # Predict
    prediction = model.predict(input_data)

    # Get predicted price
    predicted_price = prediction[0]

    # Display result
    st.success("🏠 Estimated House Price")

    st.markdown(
    f'<div style="background-color:white;padding:25px;border-radius:12px;text-align:center;border:2px solid #22c55e;margin-top:10px;"><div style="color:#475569;font-size:18px;font-weight:bold;">Predicted Price</div><div style="color:#166534;font-size:40px;font-weight:bold;margin-top:10px;">₹ {predicted_price:.2f} Lakhs</div></div>',
    unsafe_allow_html=True
)
    

