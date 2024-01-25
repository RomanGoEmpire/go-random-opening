import random
from tkinter import Image
from PIL import Image

OPENINGS = [
    "high_chinese",
    "low_chinese",
    "micro_chinese",
    "kobayashi",
    "san_ren_sei",
    "black_hole",
]
STONES = [
    "3-3",
    "3-4",
    "3-5",
    "3-6",
    "4-4",
    "4-5",
    "4-6",
    "5-5",
]
ALIGNMENTS = ["diagonal", "facing each other", "facing opponent", "alternate"]

import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme(
    "blue"
)  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.title = "Random Opening"
app.geometry("400x450")

selected_opening = None


def generate_opening():
    global selected_opening
    opening_or_stone = random.choice(["opening", "stone"])
    if opening_or_stone == "opening":
        selected_opening = [random.choice(OPENINGS)]

    else:
        selected_opening = [random.choice(STONES) for _ in range(2)]

    if len(selected_opening) == 1:
        image_path = f"openings/{selected_opening[0]}.png"
        image = Image.open(image_path)
        image = customtkinter.CTkImage(image, image, size=(400, 400))
        image_label = customtkinter.CTkLabel(
            master=app, image=image, text=selected_opening[0]
        )
        image_label.grid(row=1, column=0, columnspan=2, sticky="nsew")

    else:
        image_paths = [f"stones/{stone}.png" for stone in selected_opening]
        images = [Image.open(image_path) for image_path in image_paths]
        images[1] = images[1].rotate(90)
        images = [
            customtkinter.CTkImage(image, image, size=(200, 200)) for image in images
        ]
        image_labels = [
            customtkinter.CTkLabel(master=app, image=image, text=stone)
            for image, stone in zip(images, selected_opening)
        ]
        for i, image_label in enumerate(image_labels):
            image_label.grid(
                row=1,
                column=i,
                sticky="nsew",
            )


# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(
    master=app, text="Get Opening", command=generate_opening
)
button.grid(row=0, column=0, columnspan=2, pady=10, sticky="ew")

app.mainloop()
