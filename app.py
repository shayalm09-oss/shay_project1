import streamlit as st

# הגדרת הגדרות דף קבועות (כותרת בלשונית בדפדפן, אייקון ועימוד)
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

# עיצוב אזור הקלט בתוך קופסה מעוצבת
st.markdown("### 📊 הזן את מאפייני הבית")

col1, col2 = st.columns([2, 1])

with col1:
    floors = st.slider(
        "בחר את מספר הקומות בבית:",
        min_value=1,
        max_value=10,
        value=2,
        step=1,
        help="הזז את הסרגל כדי לבחור את מספר הקומות"
    )

with col2:
    st.write("") # מרווח לעיצוב
    st.write("")
    st.metric(label="קומות שנבחרו", value=f"{floors}")

st.markdown("---")

# כפתור חישוב בולט
if st.button("🚀 חשב מחיר משוער", use_container_width=True):
    # חישוב החיזוי
    predicted_price = (W * floors) + B
    
    # הצגת התוצאה בכרטיסיה מעוצבת
    st.balloons() # אפקט חגיגי
    st.success("החישוב הושלם בהצלחה!")
    
    st.metric(
        label="מחיר מוערך לבית:",
        value=f"${predicted_price:,.2f}"
    )
    
    # הסבר נוסף מתחת לתוצאה
    st.caption(f"* הערכה זו מבוססת על מקדם של כ-${W:,.0f} לכל קומה נוספת + מחיר בסיס של כ-${B:,.0f}.")
