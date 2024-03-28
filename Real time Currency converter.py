import tkinter as tk
from tkinter import ttk
from forex_python.converter import CurrencyRates

def converter_moeda():
    c = CurrencyRates()
    amount = int(quantidade_entry.get())
    from_currency = moeda_origem_entry.get().upper()
    to_currency = moeda_destino_entry.get().upper()
    resultado_label.config(text=f"{from_currency} to {to_currency}:")
    resultado = c.convert(from_currency, to_currency, amount)
    resultado_convertido_label.config(text=f"{resultado:.2f}")

janela = tk.Tk()
janela.title("Currency converter")

tk.Label(janela, text="Enter the amount:").grid(row=0, column=0, padx=10, pady=5)
quantidade_entry = ttk.Entry(janela)
quantidade_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(janela, text="From Currency:").grid(row=1, column=0, padx=10, pady=5)
moeda_origem_entry = ttk.Entry(janela)
moeda_origem_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(janela, text="To Currency:").grid(row=2, column=0, padx=10, pady=5)
moeda_destino_entry = ttk.Entry(janela)
moeda_destino_entry.grid(row=2, column=1, padx=10, pady=5)

calcular_button = ttk.Button(janela, text="Calculate", command=converter_moeda)
calcular_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

resultado_label = tk.Label(janela, text="")
resultado_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

resultado_convertido_label = tk.Label(janela, text="")
resultado_convertido_label.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

janela.mainloop()
