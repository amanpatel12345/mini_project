import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import random
from PIL import Image, ImageTk
import requests
from io import BytesIO

# Sample data: dictionary of quotes categorized by themes
quotes = {
    "Inspiration": [
        ("The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
         "https://ibb.co/Tc7QsRS"),
        ("You are never too old to set another goal or to dream a new dream. - C.S. Lewis",
         "https://ibb.co/JFWD9X8"),
        ("Believe you can and you're halfway there. - Theodore Roosevelt",
         "https://ibb.co/JxDCWDq"),
    ],
    "Love": [
        ("Love is composed of a single soul inhabiting two bodies. - Aristotle",
         "https://ibb.co/B4WKgXq"),
        ("The best thing to hold onto in life is each other. - Audrey Hepburn",
         "https://ibb.co/f9PcdHk"),
        ("I have decided to stick with love. Hate is too great a burden to bear. - Martin Luther King Jr.",
         "https://ibb.co/nPJwC6P"),
    ],
    "Success": [
        ("Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
         "https://ibb.co/3srkgPy"),
        ("Success is not the key to happiness. Happiness is the key to success. - Albert Schweitzer",
         "https://ibb.co/fXVMJZD"),
        ("The only place where success comes before work is in the dictionary. - Vidal Sassoon",
         "https://ibb.co/PDLX43M"),
        ("Success usually comes to those who are too busy to be looking for it. - Henry David Thoreau",
         "https://ibb.co/sQjSdqb"),
    ],
    "Wisdom": [
        ("The only true wisdom is in knowing you know nothing. - Socrates",
         "https://ibb.co/vqwrytQ"),
        ("The fool doth think he is wise, but the wise man knows himself to be a fool. - William Shakespeare",
         "https://ibb.co/9N4HMMF"),
        ("The only way to do great work is to love what you do. - Steve Jobs",
         "https://ibb.co/8jgybRC"),
        ("Wisdom is not a product of schooling but of the lifelong attempt to acquire it. - Albert Einstein",
         "https://ibb.co/HK0BVhC"),
    ],
    "Happiness": [
        ("Happiness is not something ready-made. It comes from your own actions. - Dalai Lama",
         "https://ibb.co/7JykTpy"),
        ("The greatest happiness you can have is knowing that you do not necessarily require happiness. - William Saroyan",
         "https://ibb.co/hK797dy"),
        ("Happiness is not having what you want. It is wanting what you have. - Rabbi Hyman Schachtel",
         "https://ibb.co/qsGgqxq"),
        ("Happiness is not a goal; it is a by-product. - Eleanor Roosevelt",
         "https://ibb.co/6RTWFzx"),
    ],

    # Add more categories and quotes here
}


def get_quote():
    selected_category = category_var.get()
    if selected_category == "All":
        all_quotes = [quote for quotes_list in quotes.values()
                      for quote in quotes_list]
        selected_category_quotes = all_quotes
    else:
        selected_category_quotes = quotes.get(selected_category, [])

    if not selected_category_quotes:
        messagebox.showinfo(
            "No Quotes", "No quotes available for the selected category.")
        return

    quote, image_url = random.choice(selected_category_quotes)

    try:
        response = requests.get(image_url)
        image = Image.open(BytesIO(response.content))
        # Using LANCZOS for resizing
        image = image.resize((300, 200), Image.LANCZOS)
        image = ImageTk.PhotoImage(image)
    except Exception as e:
        # If the image loading fails, display a default image or handle the error
        print(f"Error loading image: {e}")
        image = ImageTk.PhotoImage(
            Image.new("RGBA", (300, 200), (255, 255, 255, 0)))

    # Create the popup window
    popup = tk.Toplevel(root)
    popup.title("Random Quote with Image")

    quote_label = tk.Label(popup, text=quote, wraplength=250)
    quote_label.pack(pady=10)

    image_label = tk.Label(popup, image=image)
    image_label.image = image  # Retain a reference to the image
    image_label.pack(pady=10)

    popup.mainloop()


root = tk.Tk()
root.title("Quote Generator")

# Create a Combobox to select a category
categories = ["All"] + list(quotes.keys())
category_var = tk.StringVar()
category_var.set("All")
category_combobox = ttk.Combobox(
    root, values=categories, textvariable=category_var)
category_combobox.pack(pady=10)

get_quote_button = tk.Button(root, text="Get Random Quote", command=get_quote)
get_quote_button.pack(pady=10)

root.mainloop()