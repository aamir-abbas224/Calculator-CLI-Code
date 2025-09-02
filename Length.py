import BasicCalc as bc
import numpy as np


class LengthCalc(bc.BasicCalculator):
    
       conversion_rates = {
        "angstroms": 1e-10,
        "nanometres": 1e-9,
        "microns": 1e-6,
        "millimetres": 1e-3,
        "centimetres": 1e-2,
        "meters": 1,
        "kilometres": 1e3,
        "inches": 0.0254,
        "feet": 0.3048,
        "yards": 0.9144,
        "miles": 1609.344,
        "nautical miles": 1852}
       
       def length_conversion(self,value,from_unit,to_unit):
           #'''Default is Metres'''
           
           from_unit = from_unit.lower()
           to_unit = to_unit.lower()
           
           if from_unit not in self.conversion_rates:
               return f'Error : {from_unit} is not supported'
           if to_unit not in self.conversion_rates:
               return f'Error : {from_unit} is not supported'
           
           #'Conversion'
           value_inmetres = value * self.conversion_rates[from_unit]
           converted_value = value_inmetres / self.conversion_rates[to_unit]
           return converted_value
           
           

if __name__ == '__main__':
    value = float(input("Enter value to convert: "))
    from_unit = input("From unit (e.g., meters, inches, miles): ")
    to_unit = input("To unit (e.g., meters, inches, miles): ")  
    
    calc = LengthCalc(0,0)  # dummy values
    
    result = calc.length_conversion(value, from_unit, to_unit)
    print(f"{value} {from_unit} = {result} {to_unit}")
            
                            
    