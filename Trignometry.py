import BasicCalc as bc
import numpy as np


class TrigClac(bc.BasicCalculator):
    def sin(self):
        return np.sin(np.deg2rad(self.num1))
    
    def cos(self):
        return np.cos(np.deg2rad(self.num1))
 
    def tan(self):
        return np.tan(np.deg2rad(self.num1))

    def arcsin(self):
        return np.arcsin(np.deg2rad(self.num1))
    
    def arccos(self):
        return np.arccos(np.deg2rad(self.num1))
    
    def arctan(self):
        return np.arctan(np.deg2rad(self.num1))
    
    
if __name__ == "__main__":
    num1 = float(input("Enter first number: "))
    num2 = 0  # dummy, not used for trig functions
    
    calc = TrigClac(num1, num2)
    
    while True:
        print("\nSelect operation:")
        print("1. Sine")
        print("2. Cosine")
        print("3. Tangent")
        print("4. Arcsin")
        print("5. Arccos")
        print("6. Arctan")
        print("7. Exit")
        
        choice = input("Enter choice: ").strip()
        
        try:
            if choice == "1":
                print("Sin:", calc.sin())
            elif choice == "2":
                print("Cos:", calc.cos())
            elif choice == "3":
                print("Tan:", calc.tan())
            elif choice == "4":
                print("Arcsin (radians):", calc.arcsin())
            elif choice == "5":
                print("Arccos (radians):", calc.arccos())
            elif choice == "6":
                print("Arctan (radians):", calc.arctan())
            elif choice == "7":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Try again.")
        except ValueError as e:
            print("Error:", e)
