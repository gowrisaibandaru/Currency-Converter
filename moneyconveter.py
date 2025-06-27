exchange_rates = {
    "USD": {"INR": 83.0, "EUR": 0.91},
    "INR": {"USD": 0.012, "EUR": 0.011},
    "EUR": {"USD": 1.10, "INR": 88.0}
}

def convert_currency(amount, from_currency, to_currency):
    if from_currency in exchange_rates and to_currency in exchange_rates[from_currency]:
        converted_amount = amount * exchange_rates[from_currency][to_currency]
        return f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}"
    else:
        return "Invalid currency selection!"

amount = float(input("Enter amount: "))
from_currency = input("Enter currency to convert from (e.g., USD): ").upper()
to_currency = input("Enter currency to convert to (e.g., INR): ").upper()

print(convert_currency(amount, from_currency, to_currency))
