# Import Library yang digunakan
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Dashboard with Streamlit")

with st.sidebar:

    st.text('Sidebar')

    values = st.slider(
        label='Select range of values',
        min_value=0, max_value=100, value=(0, 100)
    )
    st.write('Values:', values)



col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.header("Kucing")
    st.image("https://static.streamlit.io/examples/cat.jpg") 

with col2:
    st.header("Anjing")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("Burhan")
    st.image("https://static.streamlit.io/examples/owl.jpg")     





tab1, tab2, tab3 = st.tabs(["Tab1", "Tab2", "Tab3"])

with tab1:
    st.header("Kucing")
    st.image("https://static.streamlit.io/examples/cat.jpg") 

with tab2:
    st.header("Anjing")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with tab3:
    st.header("Burhan")
    st.image("https://static.streamlit.io/examples/owl.jpg")



with st.container():
    st.write("Inside the container")
    x = np.random.normal(15, 5, 250)

    fig, ax = plt.subplots()
    ax.hist(x=x, bins=15)
    st.pyplot(fig)

with st.expander("See explanation"):
    st.write( """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
        nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor 
        in reprehenderit in voluptate velit esse cillum dolore eu fugiat 
        nulla pariatur. Excepteur sint occaecat cupidatat non proident, 
        sunt in culpa qui officia deserunt mollit anim id est laborum.
        """
         )    




