import BasicCalc as bc
import requests

class Currency(bc.BasicCalculator):
    
    def convert(self, amount, from_currency, to_currency):
        """
        Convert `amount` from `from_currency` to `to_currency` using live exchange rates.
        """
        try:
            url = f"https://YOUR URL OR API LINK/{from_currency}&symbols={to_currency}"
            response = requests.get(url).json()
            
            if response.get("success"):
                return round(response["result"], 2)
            else:
                return "Error fetching exchange rate."
        except Exception as e:
            return f"Error: {e}"

if __name__ == "__main__":
    
    amount = float(input("Enter amount: "))
    from_cur = input("From currency: ").upper()
    to_cur = input("To currency: ").upper()
    converter = Currency(from_cur,to_cur)
    
    print(f"{amount} {from_cur} = {converter.convert(amount, from_cur, to_cur)} {to_cur}")
