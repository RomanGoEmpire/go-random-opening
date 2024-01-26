import streamlit as st
import random
from PIL import Image
import os

openings = list(
    map(
        lambda x: x.split(".")[0],
        filter(lambda x: not x[0].isdigit(), os.listdir("images")),
    )
)
stones = list(
    map(
        lambda x: x.split(".")[0],
        filter(lambda x: x[0].isdigit(), os.listdir("images")),
    )
)

# * Page config
st.set_page_config(
    page_title="Random Go Opening",
    page_icon=":black_circle:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# * Sidebar
with st.sidebar:
    st.title("Options")
    st.info("Select which options you want to use for the random opening.")
    opening = st.multiselect(
        "Opening",
        openings,
        default=openings,
        help="Openings that have specfic names.",
    )
    stones = st.multiselect(
        "Stones",
        stones,
        default=stones,
        help="Openings that consist of two stones.",
    )


st.title("Random Opening")
st.write("This app generates a random opening or stone position for Go.")


enough_games = len(opening) + len(stones) > 1
generate_opening = st.button("Generate Opening", disabled=not enough_games)
if not enough_games:
    st.warning("You need to select at least two options to generate an opening.")


def only_opening():
    selected_opening = random.choice(opening)
    st.subheader(selected_opening)
    st.image(f"images/{selected_opening}.png")


def only_stones():
    selected_stones = [random.choice(stones), random.choice(stones)]
    sub_header_string = f"{selected_stones[0]} and {selected_stones[1]}"
    st.subheader(sub_header_string)

    col1, col2 = st.columns(2)
    col1.image(f"images/{selected_stones[0]}.png")
    col2.image(Image.open(f"images/{selected_stones[1]}.png").rotate(90))


if generate_opening:
    if len(stones) == 0:
        only_opening()
    elif len(opening) == 0:
        only_stones()
    else:
        selected_choice = random.choice(["opening", "stones"])
        if selected_choice == "opening":
            only_opening()
        else:
            only_stones()
