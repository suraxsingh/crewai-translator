import streamlit as st
import os
from crew import run_pipeline  # 👈 make sure crew.py has a run_pipeline function

st.title("📘 CrewAI Academic Paper Translator")

uploaded_file = st.file_uploader("Upload a .docx file", type=["docx"])
target_lang = st.selectbox(
    "Select target language",
    ["hi", "fr", "es", "de", "ar", "zh-cn", "ja", "ru"],
    index=0
)

if uploaded_file:
    st.success(f"Uploaded: {uploaded_file.name}")

    if st.button("Translate with CrewAI"):
        input_path = os.path.join("input", uploaded_file.name)
        output_path = os.path.join("output", f"translated_{uploaded_file.name}")

        # Save uploaded file
        with open(input_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Run Crew pipeline
        run_pipeline(input_path, output_path, target_lang)

        st.success("✅ Translation completed!")
        with open(output_path, "rb") as f:
            st.download_button("⬇️ Download Translated Document", f, file_name=f"translated_{uploaded_file.name}")
