import json
import tkinter as tk
from PIL import Image, ImageTk
import os
from canvas import app
from helpers import clean_screen


base_folder = os.path.dirname(__file__)


def update_current_user(username, product_id):
    with open("database/users.txt", "r+", newline='\n') as file:
        users = [json.loads(user.strip()) for user in file]
        for user in users:
            if user["username"] == username:
                user["products"].append(product_id)
                file.seek(0)
                file.truncate()
                file.writelines([json.dumps(u) + '\n' for u in users])
                return


def purchase_product(product_id):
    with open("database/products.txt", "r+") as file:
        products = [json.loads(product.strip()) for product in file]
        for product in products:
            if product["id"] == product_id:
                product["count"] -= 1
                file.seek(0)
                file.truncate()
                file.writelines([json.dumps(p) + '\n' for p in products])


def buy_product(product_id):
    clean_screen()

    with open("database/current_user.txt") as file:
        username = file.read()

    if username:
        update_current_user(username, product_id)
        purchase_product(product_id)

    render_products_screen()

# TODO: admin

def render_products_screen():
    clean_screen()

    with open("database/products.txt") as file:
        products = [json.loads(p.strip()) for p in file]
        products = [product for product in products if product['count'] > 0]

        products_per_line = 6
        lines_per_product = len(products[0])
        for index, product in enumerate(products):
            row = index // products_per_line * lines_per_product
            column = index % products_per_line

            tk.Label(app, text=product["name"]).grid(row=row, column=column)

            img = Image.open(os.path.join(base_folder, "database/images", product["img_path"])).resize((100, 100))
            photo_image = ImageTk.PhotoImage(img)
            image_label = tk.Label(image=photo_image)
            image_label.image = photo_image
            image_label.grid(row=row+1, column=column)

            tk.Label(app, text=product["count"]).grid(row=row+2, column=column)

            tk.Button(app,
                      text=f"Buy {product['id']}",
                      command=lambda i=product["id"]: buy_product(i)
                      ).grid(row=row+3, column=column)
