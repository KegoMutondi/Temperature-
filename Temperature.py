class Temperature:
    @staticmethod
    def convertFahrenheit(celsius):
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")

    @staticmethod
    def convertCelsius(fahrenheit):
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")

# Example usage
if __name__ == "__main__":
    temp = Temperature()
    
    celsius = float(input("Enter temperature in Celsius: "))
    temp.convertFahrenheit(celsius)
    
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    temp.convertCelsius(fahrenheit)
