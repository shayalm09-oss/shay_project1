import streamlit as st
import random

# הגדרות דף
st.set_page_config(
    page_title="Real Estate Price Predictor & Game",
    page_icon="🏠",
    layout="wide"
)

# עיצוב מותאם אישית
st.markdown("""
    <style>
    .stApp {
        background-color: #F0F4F8;
    }
    h1, h2, h3 {
        color: #1E3A8A !important;
    }
    [data-testid="stSidebar"] {
        background-color: #e2e8f0;
    }
    .stButton>button {
        background-color: #2563EB;
        color: white;
        border-radius: 8px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #1D4ED8;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# מקדמי המודל עם שני מאפיינים (מתוך Google Colab)
W1_FLOORS = 19089.4835
W2_AREA = 0.117448
B_INTERCEPT = 499294.7355

# ערכי Loss בשלוש רמות
LOSS_BASELINE = 239050.39
LOSS_ONE_FEATURE = 238744.21
LOSS_TWO_FEATURES = 238743.73

# דוגמאות אמת מתוך ה-Dataset למשחק (Floors, Area, Real Price)
DATASET_SAMPLES = [
    {"floors": 3, "area": 1360, "price": 149919},
    {"floors": 3, "area": 4272, "price": 424998},
    {"floors": 3, "area": 3592, "price": 266746},
    {"floors": 2, "area": 966, "price": 244020},
    {"floors": 2, "area": 4926, "price": 636056},
    {"floors": 1, "area": 2100, "price": 310000},
    {"floors": 4, "area": 3800, "price": 520000},
]

# --- סרגל צד (Sidebar): הסברים והשוואת LOSS ---
st.sidebar.title("ℹ️ About & Model Architecture")
st.sidebar.markdown("""
### Model Features:
1. **$x_1$ (Floors):** Number of floors.
2. **$x_2$ (Area):** Property area in sqft.

### Model Weights:
* $w_1$ (Floors): `19,089.48`
* $w_2$ (Area): `0.1174`
* $b$ (Intercept): `499,294.74`
""")

st.sidebar.markdown("---")
st.sidebar.subheader("📊 Loss Comparison (3 Levels)")
st.sidebar.metric("1. Baseline Loss", f"${LOSS_BASELINE:,.2f}")
st.sidebar.metric("2. One Feature Loss (Floors)", f"${LOSS_ONE_FEATURE:,.2f}", delta=f"-${LOSS_BASELINE - LOSS_ONE_FEATURE:,.2f}", delta_color="normal")
st.sidebar.metric("3. Two Features Loss (Floors + Area)", f"${LOSS_TWO_FEATURES:,.2f}", delta=f"-${LOSS_ONE_FEATURE - LOSS_TWO_FEATURES:,.2f}", delta_color="normal")

st.sidebar.info("""
**Conclusion:** Adding **Area** as a second feature slightly decreases the Mean Absolute Error (Loss), improving model precision compared to predicting with floors alone.
""")

# --- תפריט בלשוניות (Tabs) ---
tab1, tab2 = st.tabs(["🔮 Predictor Calculator", "🎮 Game: Beat the Model!"])

# ==========================================
# TAB 1: מחשבון חיזוי מעודכן
# ==========================================
with tab1:
    st.title("🏠 House Price Prediction Calculator")
    st.subheader("Smart Real Estate Valuation Powered by 2-Feature Linear Regression")
    st.markdown("---")

    st.markdown("### 📊 Enter Property Features")
    col1, col2 = st.columns(2)

    with col1:
        floors = st.number_input("Number of Floors ($x_1$):", min_value=1, max_value=10, value=2, step=1)

    with col2:
        area = st.number_input("Property Area in sqft ($x_2$):", min_value=100, max_value=10000, value=1500, step=50)

    if st.button("🚀 Calculate Estimated Price", use_container_width=True):
        predicted_price = (W1_FLOORS * floors) + (W2_AREA * area) + B_INTERCEPT

        st.balloons()
        st.success("Calculation completed successfully!")
        st.metric(
            label=f"Estimated Price for {floors} Floors & {area:,} sqft Area:",
            value=f"${predicted_price:,.2f}"
        )
        st.caption(f"* Equation: $y = ({W1_FLOORS:,.2f} \\times \\text{{Floors}}) + ({W2_AREA:.4f} \\times \\text{{Area}}) + {B_INTERCEPT:,.2f}$")

# ==========================================
# TAB 2: משחק "נצח את המודל" (5 סיבובים)
# ==========================================
with tab2:
    st.title("🎮 Game: Beat the ML Model!")
    st.write("Can your human intuition predict house prices closer to the actual value than our Machine Learning model?")

    # אתחול Session State למשחק
    if "game_round" not in st.session_state:
        st.session_state.game_round = 1
        st.session_state.user_score = 0
        st.session_state.model_score = 0
        st.session_state.game_over = False
        st.session_state.samples = random.sample(DATASET_SAMPLES, 5)

    if not st.session_state.game_over:
        current_sample = st.session_state.samples[st.session_state.game_round - 1]

        st.markdown(f"### 📍 Round {st.session_state.game_round} of 5")
        st.info(f"**House Specifications:** Floors = **{current_sample['floors']}**, Area = **{current_sample['area']:,} sqft**")

        user_guess = st.number_input(
            "Enter your price estimate ($):",
            min_value=10000,
            max_value=2000000,
            value=300000,
            step=10000,
            key=f"guess_{st.session_state.game_round}"
        )

        if st.button("Submit Guess 🎯", use_container_width=True):
            actual_price = current_sample['price']
            model_prediction = (W1_FLOORS * current_sample['floors']) + (W2_AREA * current_sample['area']) + B_INTERCEPT

            user_error = abs(actual_price - user_guess)
            model_error = abs(actual_price - model_prediction)

            st.markdown("---")
            st.write(f"**Actual House Price:** `${actual_price:,.2f}`")
            st.write(f"**Model Prediction:** `${model_prediction:,.2f}` (Error: `${model_error:,.2f}`)")
            st.write(f"**Your Guess:** `${user_guess:,.2f}` (Error: `${user_error:,.2f}`)")

            if user_error < model_error:
                st.success("🎉 You won this round! Your guess was closer!")
                st.session_state.user_score += 1
            else:
                st.error("🤖 The Model won this round! It was closer to the actual price.")
                st.session_state.model_score += 1

            if st.session_state.game_round < 5:
                st.session_state.game_round += 1
                st.button("Next Round ➡️")
            else:
                st.session_state.game_over = True
                st.rerun()

    else:
        # מסך סיום משחק
        st.balloons()
        st.markdown("## 🏆 Final Game Summary")
        st.write(f"**Your Points:** {st.session_state.user_score}")
        st.write(f"**Model Points:** {st.session_state.model_score}")

        if st.session_state.user_score > st.session_state.model_score:
            st.success("🥇 Congratulations! You defeated the Machine Learning Model!")
        elif st.session_state.user_score < st.session_state.model_score:
            st.warning("🤖 The Model won the match! Keep practicing your real-estate intuition.")
        else:
            st.info("🤝 It's a tie!")

        if st.button("Play Again 🔄"):
            st.session_state.game_round = 1
            st.session_state.user_score = 0
            st.session_state.model_score = 0
            st.session_state.game_over = False
            st.session_state.samples = random.sample(DATASET_SAMPLES, 5)
            st.experimental_rerun()
