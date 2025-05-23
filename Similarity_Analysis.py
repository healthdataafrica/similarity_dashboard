import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import math
import time

def process_file(df_sim):
    elements_list = df_sim.index.tolist()

    st.sidebar.header("Element Similarity Analysis")
    selected_element = st.sidebar.selectbox("Select an element", elements_list)
    similarity_threshold = st.sidebar.slider("Similarity Threshold", 0.000, 1.000, 0.700, 0.001) 

    if selected_element:
        sorted_similar = df_sim[selected_element].drop_duplicates().sort_values(ascending=False)
        top_similar_elements = sorted_similar[sorted_similar >= similarity_threshold].reset_index()
        top_similar_elements.columns = ["Element", "Similarity"]

        elements_per_page = 10
        total_pages = math.ceil(len(top_similar_elements) / elements_per_page)

        page = st.number_input("Page", min_value=1, max_value=total_pages, value=1, step=1)
        start_idx = (page - 1) * elements_per_page
        end_idx = start_idx + elements_per_page

        paginated_data = top_similar_elements.iloc[start_idx:end_idx]

        st.subheader(f"Top Elements Similar to '{selected_element}' (≥ {similarity_threshold})")
        fig, ax = plt.subplots()
        sns.barplot(x="Similarity", y="Element", hue="Element", data=paginated_data, ax=ax, palette="viridis", legend=False)

        ax.set_xlim(0, 1)
        st.pyplot(fig)

        st.write(f"Page {page} of {total_pages}")

        st.subheader("Download Filtered Similarity Data")
        csv = top_similar_elements.to_csv(index=False)
        st.download_button("Download CSV", csv, f"{selected_element}_similar_elements.csv", "text/csv")

st.title("Similarity Analysis")

st.sidebar.header("Upload Similarity Matrix")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=["csv"])

st.sidebar.markdown('[📥 Download Sample File](https://drive.usercontent.google.com/u/0/uc?id=1_tCrqSZ0Vu4HsB7Qd9rF9FE0JzDv2RUI&export=download)', unsafe_allow_html=True)

@st.cache_data(show_spinner="Processing data. Please wait")
def load_sample_file():
    url = "https://drive.usercontent.google.com/u/0/uc?id=1gA9gALj3es8-0Eg9nIrFMxHBoORQL1qH&export=download"
    
    df = pd.read_csv(url, index_col=0)
    return df

if "use_sample" not in st.session_state:
    st.session_state.use_sample = False

if uploaded_file:
    df_sim = pd.read_csv(uploaded_file, index_col=0)
    process_file(df_sim)
elif not st.session_state.use_sample:
    st.warning("Please upload a similarity matrix CSV file to proceed.")
    if st.button("Click here to use the sample file"):
        st.session_state.use_sample = True
        st.rerun()
else:
    try:
        df_sim = load_sample_file()
        process_file(df_sim)
    except:
        st.warning("There was a problem. Please try again.")
    
    

