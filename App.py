import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="ContentAI", layout="wide")
st.title("✨ ContentAI - مولد الإعلانات الذكي")
st.markdown("### اصنع إعلانات احترافية في ثوانٍ بقوة الذكاء الاصطناعي!")

# API Key من Secrets
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

st.markdown("---")

# مدخلات المستخدم
col1, col2 = st.columns(2)

with col1:
    product_name = st.text_input("🏷️ اسم المنتج أو الخدمة", placeholder="مثال: عطر ورد الجوري")
    product_type = st.selectbox("📦 نوع المنتج", [
        "منتج عطور",
        "ملابس وأزياء",
        "مطعم وكافيه",
        "متجر إلكتروني",
        "خدمة تقنية",
        "عقارات",
        "سيارات",
        "صحة وجمال",
        "تعليم ودورات",
        "أخرى"
    ])

with col2:
    target_audience = st.text_input("🎯 الجمهور المستهدف", placeholder="مثال: نساء 20-35 سنة")
    tone = st.selectbox("🎨 أسلوب الإعلان", [
        "احترافي وجذاب",
        "عاطفي ومؤثر",
        "مرح وخفيف",
        "فخم وراقي",
        "بسيط ومباشر"
    ])

extra_info = st.text_area("💡 معلومات إضافية (اختياري)", placeholder="مثال: سعر خاص، عرض محدود، مميزات...")

platform = st.selectbox("📱 منصة النشر", [
    "إنستغرام",
    "فيسبوك",
    "تيك توك",
    "تويتر/X",
    "واتساب"
])

st.markdown("---")

if st.button("🚀 اصنع الإعلان الآن!", use_container_width=True):
    if not product_name:
        st.error("⚠️ من فضلك أدخلي اسم المنتج!")
    else:
        with st.spinner("⏳ جاري إنشاء إعلانك..."):
            prompt = f"""
أنت خبير تسويق عربي محترف. اكتب إعلاناً تسويقياً احترافياً باللغة العربية.

المعلومات:
- المنتج/الخدمة: {product_name}
- النوع: {product_type}
- الجمهور المستهدف: {target_audience}
- الأسلوب المطلوب: {tone}
- منصة النشر: {platform}
- معلومات إضافية: {extra_info if extra_info else "لا يوجد"}

اكتب 3 نسخ مختلفة من الإعلان، كل نسخة مناسبة لـ {platform}.
استخدم إيموجي مناسبة، وهاشتاقات إذا كانت المنصة تستدعي ذلك.
اجعل الإعلان جذاباً ومقنعاً ويدفع للتفاعل.
"""
            response = model.generate_content(prompt)
            
            st.success("✅ تم إنشاء إعلانك!")
            st.markdown("### 📢 إعلاناتك الجاهزة:")
            st.markdown(response.text)
            
            st.download_button(
                label="📥 تحميل الإعلانات",
                data=response.text,
                file_name="contentai_ads.txt",
                mime="text/plain"
            )

st.markdown("---")
st.markdown("*Powered by ContentAI × Gemini AI*")
