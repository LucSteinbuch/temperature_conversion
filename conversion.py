def celsius_to_fahrenheit(celsius):
  """Convert degrees Celsius to Fahrenheit 
  
  Args: 
    celsius (float): temperature in degrees Celsius
    
  Returns:  
    float: temperature in degrees Fahrenheit
  
  See also https://en.wikipedia.org/wiki/Anders_Celsius and https://en.wikipedia.org/wiki/Daniel_Gabriel_Fahrenheit
  
  """
  return celsius/5*9+32

def celsius_to_kelvin(celsius):
  return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * (5*9)

