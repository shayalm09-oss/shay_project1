import streamlit as st

# הגדרות דף קבועות
st.set_page_config(
    page_title="מחשבון חיזוי נדל"ל",
    page_icon="🏠",
    layout="centered"
)

# כותרת ראשית וסגנון
st.title("🏠 מחשבון לחיזוי מחירי בתים")
st.subheader("מערכת חכמה להערכת שווי נכסים מבוססת Machine Learning")
st.markdown("---")

# תפריט צדדי (Sidebar) להסבר
st.sidebar.header("ℹ️ אודות המודל")
st.sidebar.write("מערכת זו משתמשת במודל **Linear Regression** שהאומן על מאגר נתוני נדל\"ל.")
st.sidebar.info("המודל מחשב את המחיר המוערך לפי מספר הקומות שבחרת.")

# מקדמי המודל (מתוך Google Colab)
W = 19092.82005981288
B = 499615.318210763

st.markdown("### 📊 הזני את מאפייני הבית")

# סרגל גרירה ברוחב מלא ללא חלוקה לעמודות
floors = st.slider(
    "בחר את מספר הקומות בבית:",
    min_value=1,
    max_value=10,
    value=2,
    step=1
)

st.markdown("---")

# כפתור חישוב בולט
if st.button("🚀 חשב מחיר משוער", use_container_width=True):
    # חישוב החיזוי
    predicted_price = (W * floors) + B
    
    # הצגת התוצאה
    st.balloons()
    st.success("החישוב הושלם בהצלחה!")
    
    st.metric(
        label=f"מחיר מוערך לבית בעל {floors} קומות:",
        value=f"${predicted_price:,.2f}"
    )
    
    st.caption(f"* הערכה זו מבוססת על מקדם של כ-${W:,.0f} לכל קומה נוספת + מחיר בסיס של כ-${B:,.0f}.")
