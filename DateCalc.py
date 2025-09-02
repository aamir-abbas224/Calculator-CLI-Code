import BasicCalc as bc
from datetime import datetime

class DateCalc(bc.BasicCalculator):
    
    def dayselapsed(self,start_date,end_date)->int:
        try:
            start = datetime.strptime(start_date,'%d-%m-%Y') 
            end = datetime.strptime(end_date,'%d-%m-%Y')
            result = end - start
            return result.days
        except ValueError:
            return "Invalid input!"
        

if __name__ == "__main__":
    
    start_input = input("Enter start date (DD-MM-YY): ")
    end_input = input("Enter end date (DD-MM-YY): ")
    
    calc = DateCalc(start_input,end_input)
    
    print("Days elapsed:", calc.dayselapsed(start_input, end_input))        
        
        