import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Real Estate Price Predictor",
    page_icon="🏠",
    layout="centered"
)

st.markdown("""
    <style>
    /* שינוי צבע הרקע של כל העמוד */
    .stApp {
        background-color: #f5f7fa;
    }
    
    /* שינוי צבע הכתב של הכותרת הראשית */
    h1 {
        color: #1E3A8A !important;
    }
    
    /* שינוי צבע הרקע של סרגל הצד (Sidebar) */
    [data-testid="stSidebar"] {
        background-color: #e2e8f0;
    }
    
    /* שינוי צבע הכפתור */
    .stButton>button {
        background-color: #2563EB;
        color: white;
        border-radius: 8px;
    }
    
    /* שינוי צבע הכפתור כשעוברים עליו עם העכבר */
    .stButton>button:hover {
        background-color: #1D4ED8;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Main Title and Subtitle
st.title("🏠 House Price Prediction Calculator")
st.subheader("Smart Real Estate Valuation Powered by Machine Learning")
st.markdown("---")

# Sidebar
st.sidebar.header("ℹ️ About the Model")
st.sidebar.write("This app uses a **Linear Regression** model trained on a real estate dataset.")
st.sidebar.info("The model calculates the estimated price based on the selected number of floors.")
st.sidebar.info("the model was trained with sklearn in google colab by making x the number of floors to a matrix and than training it.")
st.sidebar.info("the loss for the baseline is:239050.39114499997 ."+"the loss for this model is: 238744.2118532495 .")

# Model Coefficients (from Google Colab)
W = 19092.82005981288
B = 499615.318210763

st.markdown("### 📊 Enter Property Features")

# Number input field (safe from browser translation bugs)
floors = st.number_input(
    "Select the number of floors:",
    min_value=1,
    max_value=10,
    value=1,
    step=1
)

st.markdown("---")

# Prediction Button
if st.button("🚀 Calculate Estimated Price", use_container_width=True):
    # Calculate Prediction
    predicted_price = (W * floors) + B
    
    # Display Results
    st.balloons()
    st.success("Calculation completed successfully!")
    
    st.metric(
        label=f"Estimated Price for a {floors}-Floor House:",
        value=f"${predicted_price:,.2f}"
    )
    
    st.caption(f"* This estimation is based on a coefficient of ~${W:,.0f} per additional floor + a base price of ~${B:,.0f}.")
