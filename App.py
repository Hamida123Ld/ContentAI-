import streamlit as st
from groq import Groq

st.set_page_config(page_title="ContentAI", layout="wide")

st.title("ContentAI")
st.markdown("### Generate Professional Ads in Seconds with AI Power!")
st.markdown("---")

# API Key من المستخدم
st.sidebar.title("Settings")
st.sidebar.markdown("### Get your free API Key:")
st.sidebar.markdown("1. Go to [console.groq.com](https://console.groq.com)")
st.sidebar.markdown("2. Click 'Create API Key'")
st.sidebar.markdown("3. Paste it below")
st.sidebar.markdown("---")
user_api_key = st.sidebar.text_input("Your Groq API Key", type="password")

if not user_api_key:
    st.warning("Please enter your Groq API Key in the sidebar to start!")
    st.stop()

client = Groq(api_key=user_api_key)

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
            try:
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
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=1500
                )
                result = response.choices[0].message.content
                st.success("Your ads are ready!")
                st.markdown("### Your Generated Ads:")
                st.markdown(result)
                st.download_button(
                    label="Download Ads",
                    data=result,
                    file_name="contentai_ads.txt",
                    mime="text/plain"
                )
            except Exception as e:
                st.error("Invalid API Key. Please check your Groq API key and try again.")

st.markdown("---")
st.markdown("*Powered by ContentAI x Groq AI*")



