import tkinter as tk
from tkinter import ttk

# Define the exchange rates
exchange_rates = {
    "USD": 1,
    "EUR": 0.92,
    "GBP": 0.79,
    "INR": 83.35,
    # Add more currencies as needed
}

def convert_currency():
    """Converts from one currency to another."""
    amount = float(amount_entry.get())
    from_currency = from_combobox.get()
    to_currency = to_combobox.get()
    
    # Calculate the converted amount
    result = amount / exchange_rates[from_currency] * exchange_rates[to_currency]
    # Update the result label
    result_label.config(text=f"Converted Amount: {result:.2f} {to_currency}")

# Create the main window
root = tk.Tk()
root.title("Currency Converter")

# Create and pack the widgets
amount_label = ttk.Label(root, text="Amount:")
amount_label.pack()

amount_entry = ttk.Entry(root)
amount_entry.pack()

from_label = ttk.Label(root, text="From:")
from_label.pack()

from_combobox = ttk.Combobox(root, values=list(exchange_rates.keys()))
from_combobox.pack()

to_label = ttk.Label(root, text="To:")
to_label.pack()

to_combobox = ttk.Combobox(root, values=list(exchange_rates.keys()))
to_combobox.pack()

convert_button = ttk.Button(root, text="Convert", command=convert_currency)
convert_button.pack()

result_label = ttk.Label(root, text="Converted Amount: ")
result_label.pack()

# Run the application
root.mainloop()
