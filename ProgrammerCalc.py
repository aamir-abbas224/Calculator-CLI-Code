import BasicCalc as bc


class ProgrammerCalc(bc.BasicCalculator):
    
    def binary(self):
        return bin(self.num1) 
    
    def octal(self):
        return oct(self.num1)
    
    def hexadecimal(self):
        return hex(self.num1)
    
    def bitwise_and(self):
        return self.num1 & self.num2
    
    def bitwise_or(self):
        return self.num1 | self.num2
    
    def bitwise_xor(self):
        return self.num1 ^ self.num2
    
    def bitwise_not(self):
        return ~self.num1
    
    def left_shift(self):
        return self.num1 << 1
    
    def right_shift(self):
        return self.num1 >> 1
    
if __name__ == "__main__":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    calc = ProgrammerCalc(num1, num2)
    
    while True:
        print("\nChoose an operation:")
        print("1. Binary")
        print("2. Octal")
        print("3. Hexadecimal")
        print("4. Bitwise AND")
        print("5. Bitwise OR")
        print("6. Bitwise XOR")
        print("7. Bitwise NOT")
        print("8. Left Shift")
        print("9. Right Shift")
        print("0. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            print("Binary:", calc.binary())
        elif choice == '2':
            print("Octal:", calc.octal())
        elif choice == '3':
            print("Hexadecimal:", calc.hexadecimal())
        elif choice == '4':
            print("Bitwise AND:", calc.bitwise_and())
        elif choice == '5':
            print("Bitwise OR:", calc.bitwise_or())
        elif choice == '6':
            print("Bitwise XOR:", calc.bitwise_xor())
        elif choice == '7':
            print("Bitwise NOT:", calc.bitwise_not())
        elif choice == '8':
            print("Left Shift:", calc.left_shift())
        elif choice == '9':
            print("Right Shift:", calc.right_shift())
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")