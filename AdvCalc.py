import BasicCalc as bc
import numpy as np

class AdvanceCalc(bc.BasicCalculator):
    
    def pi(self):
        return np.pi * self.num1    #uses property
    
    def eulerCon(self):
        return np.e * self.num1     #uses property
    
    def abs(self):
        return abs(self.num1)   #uses property
    
    def factorial(self):
        if self.num1 < 0:
            raise ValueError('Factorial for negative number is not defined!')
        
        fact = 1 # default factorial value
        for i in range(2, int(self.num1)+1): 
            fact *= i
        return fact
    
    def cubicroot(self):
        return np.cbrt(self.num1)
    
    def cubicpower(self):
        return self.num1 ** 3
    
    def squarepower(self):
        return self.num1 ** 2
    
    def natlog(self): # natural log
        return np.log(self.num1)
    
    def logten(self):
        return np.log10(self.num1)
    
    def log2(self):
        return np.log2(self.num1)
    
    def modulus(self):
        if self.num2 == 0:
         raise ZeroDivisionError("Cannot take modulus with 0")
        return self.num1 % self.num2   


if __name__ == "__main__":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number (if required, else 0): "))
    
    calc = AdvanceCalc(num1, num2)
    
    while True:
        print("\nSelect operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Power")
        print("6. Reciprocal")
        print("7. Square root")
        print("8. Pi * num1")
        print("9. Euler's constant * num1")
        print("10. Absolute value")
        print("11. Factorial of num1")
        print("12. Cubic root of num1")
        print("13. Cubic power of num1")
        print("14. Square power of num1")
        print("15. Natural log of num1")
        print("16. Log base 10 of num1")
        print("17. Log base 2 of num1")
        print("18. Modulus (num1 % num2)")
        print("19. Exit")
        
        choice = input("Enter choice: ").strip()
        
        try:
            if choice == "1":
                print("Result:", calc.addition())
            elif choice == "2":
                print("Result:", calc.subtraction())
            elif choice == "3":
                print("Result:", calc.multiplication())
            elif choice == "4":
                print("Result:", calc.division())
            elif choice == "5":
                print("Result:", calc.power())
            elif choice == "6":
                print("Reciprocal:", calc.reciprocal(calc.num1))
            elif choice == "7":
                print("Square root:", calc.squareroot(calc.num1))
            elif choice == "8":
                print("Pi * num1:", calc.pi())
            elif choice == "9":
                print("Euler's constant * num1:", calc.eulerCon())
            elif choice == "10":
                print("Absolute value:", calc.abs())
            elif choice == "11":
                print("Factorial:", calc.factorial())
            elif choice == "12":
                print("Cubic root:", calc.cubicroot())
            elif choice == "13":
                print("Cubic power:", calc.cubicpower())
            elif choice == "14":
                print("Square power:", calc.squarepower())
            elif choice == "15":
                print("Natural log:", calc.natlog())
            elif choice == "16":
                print("Log base 10:", calc.logten())
            elif choice == "17":
                print("Log base 2:", calc.log2())
            elif choice == "18":
                print("Modulus:", calc.modulus())
            elif choice == "19":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Try again.")
        except (ZeroDivisionError, ValueError) as e:
            print("Error:", e)
   