"""Main module for the streamlit app"""
import streamlit as st

import src.pages.demo_3d
import src.pages.demo_2d

PAGES = {
    "2D Demo": src.pages.demo_2d,
    "3D Demo": src.pages.demo_3d,
}


st.set_page_config(layout='wide', initial_sidebar_state='expanded')

with open('styles/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    

def main():
    """Main function of the App"""
    st.sidebar.title("Dimensionality Reduction Examples")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    page = PAGES[selection]

    with st.spinner(f"Loading {selection} ..."):
        #ast.shared.components.write_page(page)
        page.write()


if __name__ == "__main__":
    main()