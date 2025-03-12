import streamlit as st

similarity_analysis = st.Page("Similarity_Analysis.py", title="Similarity Analysis", icon=":material/analytics:")
elements_grouping = st.Page("Elements_Grouping.py", title="Elements Grouping", icon=":material/group_work:")
type_assignment = st.Page("Type_Assignment.py", title="Type Assignment", icon=":material/category:")

pg = st.navigation([similarity_analysis, elements_grouping, type_assignment])
st.set_page_config(page_title="Form Elements Processing", page_icon="assets/favicon.jpg")
pg.run()