import streamlit as st
import math

# 1. إعدادات التصميم والخلفية الجميلة (CSS)
st.set_page_config(page_title="تطبيق زاوية القبلة", page_icon="🕋", layout="centered")

st.markdown("""
    <style>
    /* تصميم الخلفية المتدرجة */
    .stApp {
        background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
        color: #ffffff;
    }
    
    /* تصميم الحاويات (Cards) */
    .stNumberInput, .stButton {
        background-color: rgba(400, 255, 255, 0.05);
        border-radius: 10px;
        padding: 10px;
    }

    /* تغيير لون العناوين للذهبي */
    h1, h2, h3 {
        color: #D4AF37 !important;
        text-align: center;
    }

    /* تخصيص الزر */
    .stButton>button {
        width: 100%;
        background-color: #D4AF37 !important;
        color: #000000 !important;
        font-weight: bold;
        border: None;
        height: 3em;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. واجهة المستخدم
st.title("🕋 حاسبة زاوية القبلة")
st.write("أداة دقيقة لحساب زاوية القبلة مقارنة بالشمال الحقيقي أو الشمال الشبكي")

with st.container():
    st.subheader("إحداثيات الموقع")
    col1, col2 = st.columns(2)
    with col1:
        lat_a = st.number_input("خط العرض (Latitude)", value=35.24, format="%.5f")
    with col2:
        lon_a = st.number_input("خط الطول (Longitude)", value=-0.52, format="%.5f")

st.markdown("---")

if st.button("حساب الزاوية الهندسية"):
    # الثوابت (مكة ومرجع الزون 30)
    lat_b, lon_b = 21.4225, 39.8262
    central_meridian = -3.0

    # العمليات الحسابية
    lat1_r, lat2_r = math.radians(lat_a), math.radians(lat_b)
    d_lon_r = math.radians(lon_b - lon_a)

    y = math.sin(d_lon_r) * math.cos(lat2_r)
    x = math.cos(lat1_r) * math.sin(lat2_r) - math.sin(lat1_r) * math.cos(lat2_r) * math.cos(d_lon_r)
    
    true_az = (math.degrees(math.atan2(y, x)) + 360) % 360
    conv = (lon_a - central_meridian) * math.sin(lat1_r)
    grid_az = true_az + conv

    # 3. عرض النتائج بشكل جمالي
    st.markdown(f"""
        <div style="background-color: rgba(400, 175, 55, 0.1); border: 1px solid #D4AF37; padding: 20px; border-radius: 15px; text-align: center;">
            <p style="margin: 0; font-size: 1.2em;">زاوية الرسم في الأوتوكاد (Grid Azimuth)</p>
            <h1 style="margin: 10px 0; font-size: 3em;">{grid_az:.2f}°</h1>
        </div>
    """, unsafe_allow_html=True)

    st.write("") # مسافة
    
    c1, c2 = st.columns(2)
    c1.metric("السمت الحقيقي (GPS)", f"{true_az:.2f}°")
    c2.metric("تقارب الشبكة", f"{conv:.2f}°")

    st.markdown("---")
    st.caption("إِنَّنِي أَنَا اللَّهُ لَا إِلَٰهَ إِلَّا أَنَا فَاعْبُدْنِي وَأَقِمِ الصَّلَاةَ لِذِكْرِي ... UTM Zone 30N يستخدم هذا التطبيق لإعطاء زاوية القبلة بدقة عالية خاصة لمشاريع المساجد, المنطقة.")
