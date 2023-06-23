import streamlit as st
import test
from PIL import Image

# Set Grab's brand colors
PRIMARY_COLOR = "#00923F"  # Green color
SECONDARY_COLOR = "#FFD700"  # Gold color

# Set Grab's brand font
FONT = "Arial"  # Replace with the desired font

# Set page config
st.set_page_config(
    page_title='Tasty Foods',
    page_icon="imgs/logo.png",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Apply Grab's brand colors to the Streamlit theme
st.markdown(f"""
    <style>
    .reportview-container .main .block-container {{
        max-width: 1000px;
        padding-top: 2rem;
        padding-right: 1rem;
        padding-left: 1rem;
        padding-bottom: 2rem;
    }}
    .css-1aumxhk {{
        background-color: {PRIMARY_COLOR} !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# Apply Grab's brand font to the Streamlit elements
st.markdown(f"""
    <style>
    .reportview-container .main .block-container .markdown-text-container {{
        font-family: {FONT};
    }}
    </style>
    """, unsafe_allow_html=True)

t = test.result()
foods = t.food()

grab_logo = Image.open("imgs/grab_logo.png")
tasty_food_image = Image.open("imgs/tasty_food_image.png")

st.image(grab_logo, use_column_width=True)

st.markdown("<h1 style='text-align: center;'>Tasty Foods 🍜</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>Food Recommendation System 😋</h2>", unsafe_allow_html=True)

st.image(tasty_food_image, use_column_width=True)

st.write("-----------------")
st.write("-----------------")
food_choice = st.selectbox("Pick a Food", foods)
st.write("------------------")

c1, c2, c3 = st.columns(3)

m1, m2, m3 = t.query(food_choice)

with c1:
    st.subheader("Simple Content Based Filtering")
    st.write("Recommends food based on similar foods")
    st.write("------------------")
    for index, ele in enumerate(m1):
        st.write(index, ele.title())
    st.write("------------------")

with c2:
    st.subheader("Collaborative Based Filtering")
    st.write("Recommends food based on similar users")
    st.write("------------------")
    if m3 is None:
        st.write("**Less user ratings for this food item!!!**")
        st.write("So, the recommender cannot pull any recommendations")
    else:
        for index, ele in enumerate(m3):
            st.write(index, ele.title())
    st.write("------------------")

with c3:
    st.subheader("Advanced Content Based Filtering")
    st.write("Recommends food based on similar foods and its features")
    st.write("------------------")
    for index, ele in enumerate(m2):
        st.write(index, ele.title())
    st.write("------------------")

st.write("------------------")
st.subheader("✨ STAT 280 ML Hackathon ✨")
st.write("------------------")

# TODO: Implement UI enhancements and other recommended features
# Add responsive layout, error handling, caching, personalization, social sharing, external API integration, performance optimization, user feedback and ratings, etc.
# Continue coding and updating the web app based on the recommended enhancements.
