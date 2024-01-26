import streamlit as st
import random
from PIL import Image, ImageOps
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
ALIGNMENTS = ["diagonal", "facing each other", "facing opponent", "alternate"]

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
        "Opening", openings, default=openings, help="Openings that have specfic names."
    )
    stones = st.multiselect(
        "Stones",
        stones,
        default=stones,
        help="Openings that consist of two stones.",
    )
    alignment = st.checkbox("Align stones", disabled=not stones)
    # Only show the aligment options if the checkbox is checked
    aligments = None
    if alignment:
        aligments = st.multiselect(
            "Alignment",
            ALIGNMENTS,
            default=ALIGNMENTS,
            help="Select the alignment of the stones",
        )


st.title("Random Opening")
st.write("This app generates a random opening or stone position for Go.")


generate_opening = st.button("Generate Opening")


def only_opening():
    selected_opening = random.choice(opening)
    st.subheader(selected_opening)
    st.image(f"images/{selected_opening}.png")


def create_2x2_grid_image(img1, img2, img3, img4):
    # Assume all images have the same size
    width, height = img1.size

    # Create a new image that can fit the 2x2 grid
    new_img = Image.new("RGB", (2 * width, 2 * height))

    # Paste the images into the new image
    new_img.paste(img1, (0, 0))
    new_img.paste(img2, (width, 0))
    new_img.paste(img3, (0, height))
    new_img.paste(img4, (width, height))

    return new_img


def only_stones():
    selected_stones = [random.choice(stones), random.choice(stones)]
    sub_header_string = f"{selected_stones[0]} and {selected_stones[1]}"
    selected_alignment = None
    if alignment and aligments:
        selected_alignment = random.choice(aligments) if aligments else None
        sub_header_string += f" {selected_alignment}"
    st.subheader(sub_header_string)

    empty = [Image.open("empty.png"), Image.open("empty.png")]
    if alignment:
        if "diagonal" == selected_alignment:
            new_image = create_2x2_grid_image(
                empty[0].rotate(-90),
                Image.open(f"images/{selected_stones[0]}.png").rotate(180),
                Image.open(f"images/{selected_stones[1]}.png"),
                empty[1].rotate(90),
            )
            st.image(new_image)

        elif "facing each other" == selected_alignment:
            new_image = create_2x2_grid_image(
                empty[0].rotate(-90),
                Image.open(f"images/{selected_stones[0]}.png").rotate(180),
                empty[1],
                ImageOps.mirror((Image.open(f"images/{selected_stones[1]}.png"))),
            )
            st.image(new_image)

        elif "facing opponent" == selected_alignment:
            new_image = create_2x2_grid_image(
                empty[0].rotate(-90),
                ImageOps.mirror(Image.open(f"images/{selected_stones[0]}.png")).rotate(
                    90
                ),
                empty[1],
                Image.open(f"images/{selected_stones[1]}.png").rotate(90),
            )
            st.image(new_image)

        elif "alternate" == selected_alignment:
            new_image = create_2x2_grid_image(
                empty[0].rotate(-90),
                Image.open(f"images/{selected_stones[0]}.png").rotate(180),
                empty[1],
                Image.open(f"images/{selected_stones[1]}.png").rotate(90),
            )
            st.image(new_image)

    else:
        new_image = create_2x2_grid_image(
            empty[0].rotate(-90),
            Image.open(f"images/{selected_stones[0]}.png").rotate(180),
            empty[1],
            Image.open(f"images/{selected_stones[1]}.png").rotate(90),
        )
        st.image(new_image)


if generate_opening:
    if len(opening) == 0 and len(stones) == 0:
        st.error("Please select at least one option.")
    elif sum([len(opening), len(stones)]) == 1:
        st.warning("You only selected one option. This will always be the result.")
        if len(opening) == 1:
            st.subheader(opening[0])
        else:
            st.subheader(stones[0])
        selected_opening = opening + stones
        st.image(f"images/{selected_opening[0]}.png")
    elif len(stones) == 0:
        only_opening()
    elif len(opening) == 0:
        only_stones()
    else:
        selected_choice = random.choice(["opening", "stones"])
        if selected_choice == "opening":
            only_opening()
        else:
            only_stones()
