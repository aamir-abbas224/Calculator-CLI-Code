import numpy as np

class BasicCalculator:
    def __init__(self,num1:int,num2:int):
        self._num1 = num1
        self._num2 = num2
        
    @property
    def num1(self):
        return self._num1
    
    @num1.setter
    def num1(self,value):
        self._num1 = value    
        
    @property
    def num2(self):
        return self._num2
    
    @num2.setter
    def num2(self,value):
        self._num2 = value    
        
    def addition(self):
        return self._num1 + self._num2
    
    def subtraction(self):
        return self._num1 - self._num2
    
    def multiplication(self):
        return self._num1 * self._num2
    
    def division(self):
        if self._num2 == 0:
            raise ZeroDivisionError('Error! Cannot be divided by zero')
        else:
            return self._num1 / self._num2
        
    def power(self):
        return self._num1 ** self._num2
    
    def reciprocal(self,number):
        if number == 0:
            raise ZeroDivisionError("Error! No 0 reciprocal allowed")
        else:
            return 1/ number  
    
    def squareroot(self,number):
        if number < 0:
            raise ValueError('Only positive numbers are allowed')
        else:
            return np.sqrt(number)


if __name__ == "__main__":
    num1 = float(input("Enter first number :"))
    num2 = float(input("Enter second number :"))
    
    calc = BasicCalculator(num1,num2)
    
    while True:
        print("\nSelect operation:")
        print('Please Note that only first number is subjected to Reciprocal and Square Root!')
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Power")
        print("6. Reciprocal")
        print("7. Square root ")
        print("8. Exit")
        
        choice = input("Enter choice: ").strip()

        if choice == "1":
            print("Result:", calc.addition())
        elif choice == "2":
            print("Result:", calc.subtraction())
        elif choice == "3":
            print("Result:", calc.multiplication())
        elif choice == "4":
            try:
                print("Result:", calc.division())
            except ZeroDivisionError as e:
                print(e)
        elif choice == "5":
            print("Result:", calc.power())
        elif choice == "6":
            try:
                print("Reciprocal:", calc.reciprocal(calc.num1))
            except ZeroDivisionError as e:
                print(e)
        elif choice == "7":
            try:
                print("Square root:", calc.squareroot(calc.num1))
            except ValueError as e:
                print(e)
        elif choice == "8":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.") 
        