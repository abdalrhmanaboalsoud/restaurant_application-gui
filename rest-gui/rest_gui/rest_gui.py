import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk()
root.title("Order Form")
root.geometry("600x400")

# Pizza Quantity selection
pizza_quantity_label = ttk.Label(root, text="Pizza Quantity:")
pizza_quantity_label.grid(row=0, column=0, padx=50, pady=5)
pizza_quantity_var = tk.StringVar()
pizza_quantity_entry = ttk.Entry(root, textvariable=pizza_quantity_var)
pizza_quantity_entry.grid(row=0, column=1, padx=10, pady=5)
pizza_quantity_var.set(1)

# Pizza Size selection
pizza_size_label = ttk.Label(root, text="Pizza Size:")
pizza_size_label.grid(row=0, column=2, padx=50, pady=5)

pizza_size_options = ["Small", "Medium", "Large"]
pizza_size_var = tk.StringVar()
pizza_size_dropdown = ttk.OptionMenu(root, pizza_size_var, *pizza_size_options)
pizza_size_dropdown.grid(row=0, column=3, padx=0, pady=5)
pizza_size_var.set(pizza_size_options[0])

# Burger Quantity Selection
burger_quantity_label = ttk.Label(root, text="Burger Quantity:")
burger_quantity_label.grid(row=1, column=0, padx=5, pady=5)
burger_quantity_var = tk.StringVar()
burger_quantity_entry = ttk.Entry(root, textvariable=burger_quantity_var)
burger_quantity_entry.grid(row=1, column=1, padx=10, pady=5)
burger_quantity_var.set(1)

# Burger Size selection
burger_size_label = ttk.Label(root, text="Burger Size:")
burger_size_label.grid(row=1, column=2, padx=10, pady=5)

burger_size_options = ["Classic", "Big", "Triple"]
burger_size_var = tk.StringVar()
burger_size_dropdown = ttk.OptionMenu(root, burger_size_var, *burger_size_options)
burger_size_dropdown.grid(row=1, column=3, padx=10, pady=5)
burger_size_var.set(burger_size_options[0])

# sof drink quantity

soft_drinks_quantity_label = ttk.Label(root,text = "Soft Drinks Quantity:")
soft_drinks_quantity_label.grid(row=2, column=0)
soft_drinks_quantity_var = tk.StringVar()
soft_drinks_quantity_entry = ttk.Entry(root, textvariable=soft_drinks_quantity_var)
soft_drinks_quantity_entry.grid(row=2, column=1, padx=10, pady=5)
soft_drinks_quantity_var.set(0)


# Order type
takeaway_dine = tk.StringVar()
takeaway_option = ttk.Radiobutton(root, text="Takeaway", variable=takeaway_dine, value="takeaway")
takeaway_option.grid(row=3, column=0)

# dine = tk.StringVar()
dine_option = ttk.Radiobutton(root, text="Dine", variable=takeaway_dine , value="dine")
dine_option.grid(row=3, column= 1)


# checkboxes extras
cheese_var = tk.BooleanVar()
ketchup_var = tk.BooleanVar()

cheese_checkbox = ttk.Checkbutton(root, text="Extra Cheese", variable=cheese_var)
cheese_checkbox.grid(row=4, column=0)

pepperoni_checkbox = ttk.Checkbutton(root, text="Extra Ketchup", variable=ketchup_var)
pepperoni_checkbox.grid(row=5, column=0)


# streched goal 
def calculate_price ():
    pizza_prices = {
    "Small": 5,
    "Medium": 7,
    "Large": 10
    }

    burger_prices = {
        "Classic": 5, "Big": 7, "Triple": 9
    }
    unit_extra_cheese = 0
    unit_extra_ketchup = 0
    
    pizza_size = pizza_size_var.get()
    pizza_quantity = int(pizza_quantity_var.get())
    burger_quantity = int(burger_quantity_var.get())
    burger_size = burger_size_var.get()
    soft_drinks_quantity = int(soft_drinks_quantity_var.get())
    extra_cheese = cheese_var.get()
    extra_ketchup = ketchup_var.get()

    unit_price_pizza = pizza_prices[pizza_size]
    total_price_pizza = unit_price_pizza * pizza_quantity
    
    unit_bueger_price = burger_prices[burger_size]
    total_price_burger = burger_quantity * unit_bueger_price
    
    soft_drinks_price = soft_drinks_quantity*2
        
    if extra_cheese:
        unit_extra_cheese = 1
    
    if extra_ketchup:
        unit_extra_ketchup = 1

    final_price = total_price_pizza + total_price_burger + soft_drinks_price + unit_extra_cheese + unit_extra_ketchup
    
    return final_price

# Order Summary
def order_pizza():
    pizza_size = pizza_size_var.get()
    pizza_quantity = int(pizza_quantity_var.get())
    burger_quantity = int(burger_quantity_var.get())
    burger_size = burger_size_var.get()
    soft_drinks_quantity = int(soft_drinks_quantity_var.get())
    extra_cheese = cheese_var.get()
    extra_ketchup = ketchup_var.get()
    total_order_price = calculate_price()
    takeOrDine = takeaway_dine.get()

    messagebox.showinfo("Your Order Contains",
                    f"\n{pizza_quantity} Pizza {pizza_size}"
                    f"\n{burger_quantity} Burgers {burger_size}"
                    f"\n{soft_drinks_quantity} Soft Drinks"
                    f"\nExtra Cheese? {extra_cheese}"
                    f"\nExtra Ketchup? {extra_ketchup}"
                    f"\nDine-in or Takeout? {takeOrDine}"
                    f"\nTotal Price: ${total_order_price}")
# Order button
order_button = ttk.Button(root, text="Order", command=order_pizza)
order_button.grid(row=6, columnspan=1, padx=10, pady=10)  

root.mainloop()
