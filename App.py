import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="ContentAI", layout="wide")

st.title("ContentAI")
st.markdown("### Generate Professional Ads in Seconds with AI Power!")
st.markdown("---")

# API Key
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash-8b")

# Inputs
col1, col2 = st.columns(2)

with col1:
    product_name = st.text_input("Product / Service Name")
    product_type = st.selectbox("Product Type", [
        "Perfume & Beauty",
        "Fashion & Clothing",
        "Restaurant & Cafe",
        "E-commerce Store",
        "Tech Service",
        "Real Estate",
        "Cars",
        "Health & Wellness",
        "Education & Courses",
        "Other"
    ])
    language = st.selectbox("Ad Language", [
        "Arabic",
        "English",
        "French",
        "Arabic + English"
    ])

with col2:
    target_audience = st.text_input("Target Audience")
    tone = st.selectbox("Ad Style", [
        "Professional & Attractive",
        "Emotional & Impactful",
        "Fun & Light",
        "Luxury & Premium",
        "Simple & Direct"
    ])
    platform = st.selectbox("Platform", [
        "Instagram",
        "Facebook",
        "TikTok",
        "Twitter/X",
        "LinkedIn",
        "WhatsApp"
    ])

extra_info = st.text_area("Additional Info (Optional)")

st.markdown("---")

if st.button("Generate Ad Now!", use_container_width=True):
    if not product_name:
        st.error("Please enter a product name!")
    else:
        with st.spinner("Creating your ad..."):
            prompt = f"""
You are a professional marketing expert. Create a professional advertisement.

Details:
- Product/Service: {product_name}
- Type: {product_type}
- Target Audience: {target_audience}
- Style: {tone}
- Platform: {platform}
- Language: {language}
- Additional Info: {extra_info if extra_info else "None"}

Write 3 different versions of the ad in {language}.
Use appropriate emojis and hashtags if needed for {platform}.
Make each ad engaging, persuasive and action-driven.
"""
            response = model.generate_content(prompt)

            st.success("Your ads are ready!")
            st.markdown("### Your Generated Ads:")
            st.markdown(response.text)

            st.download_button(
                label="Download Ads",
                data=response.text,
                file_name="contentai_ads.txt",
                mime="text/plain"
            )

st.markdown("---")
st.markdown("*Powered by ContentAI x Gemini AI*")

