import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Real Estate Price Predictor",
    page_icon="🏠",
    layout="centered"
)

# Main Title and Subtitle
st.title("🏠 House Price Prediction Calculator")
st.subheader("Smart Real Estate Valuation Powered by Machine Learning")
st.markdown("---")

# Sidebar
st.sidebar.header("ℹ️ About the Model")
st.sidebar.write("This app uses a **Linear Regression** model trained on a real estate dataset.")
st.sidebar.info("The model calculates the estimated price based on the selected number of floors.")

# Model Coefficients (from Google Colab)
W = 19092.82005981288
B = 499615.318210763

st.markdown("### 📊 Enter Property Features")

# Full-width slider
floors = st.slider(
    "Select the number of floors:",
    min_value=1,
    max_value=10,
    value=2,
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
