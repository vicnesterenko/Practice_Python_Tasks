import requests
import tkinter as tk
from tkinter import PhotoImage


def get_quote():
    global CANVAS, QUOTE_TEXT
    response = requests.get(url="https://api.kanye.rest/")
    if response.status_code == 200:
        data = response.json()
        if data:
            try:
                quote = data["quote"]
                CANVAS.itemconfig(QUOTE_TEXT, text=quote)
            except KeyError:
                print("No 'quote' key found in data.")
    else:
        print("Error getting data. Status code:", response.status_code)


def window_set():
    global CANVAS, QUOTE_TEXT
    window = tk.Tk()
    window.title("Kanye Says...")
    window.config(padx=50, pady=50)

    CANVAS = tk.Canvas(width=300, height=414)
    background_img = PhotoImage(file="background.png")
    CANVAS.create_image(150, 207, image=background_img)
    QUOTE_TEXT = CANVAS.create_text(
        150,
        207,
        text="Kanye Quote Goes HERE",
        width=250,
        font=("Arial", 19, "bold"),
        fill="white",
    )
    CANVAS.grid(row=0, column=0)

    kanye_img = PhotoImage(file="kanye.png")
    kanye_button = tk.Button(image=kanye_img, highlightthickness=0, command=get_quote)
    kanye_button.grid(row=1, column=0)

    window.mainloop()


if __name__ == "__main__":
    CANVAS = None
    QUOTE_TEXT = None
    window_set()
