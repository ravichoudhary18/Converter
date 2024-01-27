from .serializers import TEMPERATURE_CHOICES_LIST, TIME_CHOICES_LIST

class TemperatureCalculator:

    conversion_factor_celsius = 9/5
    conversion_factor_fahrenheit = 5/9
    scaling_and_shifting_celsius = 32
    scaling_and_shifting_kelvin = 273.15
    TEMPERATURE_CHOICES = TEMPERATURE_CHOICES_LIST

    def __init__(self) -> None:
        pass
        
    def validate_temperature(self, temperature):
        if temperature not in self.TEMPERATURE_CHOICES:
            raise ValueError(f"Invalid convetion type: {temperature}")

    def celsius_to_fahrenheit(self, celsius):
        fahrenheit = (celsius * self.conversion_factor_celsius) + self.scaling_and_shifting_celsius
        return fahrenheit
    
    def celsius_to_kelvin(self, celsius):
        kelvin = celsius + self.scaling_and_shifting_kelvin
        return kelvin
    
    def fahrenheit_to_celsius(self, fahrenheit):
        celsius = (fahrenheit - self.scaling_and_shifting_celsius) * self.conversion_factor_fahrenheit
        return celsius
    
    def fahrenheit_to_kelvin(self, fahrenheit):
        celsius = self.fahrenheit_to_celsius(fahrenheit)
        kelvin = self.celsius_to_kelvin(celsius)
        return kelvin
    
    def kelvin_to_celsius(self, kelvin):
        celsius = kelvin - self.scaling_and_shifting_kelvin
        return celsius
    
    def kelvin_to_fahrenheit(self, kelvin):
        celsius = self.kelvin_to_celsius(kelvin)
        fahrenheit = self.celsius_to_fahrenheit(celsius)
        return fahrenheit
    
    def convert_temperature(self, degrees:float, from_:str = 'celsius', to_:str = 'fahrenheit'):
        self.validate_temperature(from_)
        self.validate_temperature(to_)
        if from_ == to_:
            raise ValueError("'from_' and 'to_' values cannot be the same.")
        method_call = f'self.{from_}_to_{to_}({degrees})'
        result = eval(method_call)
        return result
    

class TimeCalculator:

    def __init__(self) -> None:
        pass

    def nanosecond_to_microsecond(self, nanosecond):
        microsecond = nanosecond / 1_000
        return microsecond
    
    def nanosecond_to_millisecond(self, nanosecond):
        millisecond = nanosecond / 1_000_000
        return millisecond
    
    def nanosecond_to_second(self, nanosecond):
        second = nanosecond / 1_000_000_000
        return second
    
    def nanosecond_to_minute(self, nanosecond):
        seconds = self.nanosecond_to_second(nanosecond)
        minute = seconds / 60
        return minute
    
    def nanosecond_to_hour(self, nanosecond):
        minute = self.nanosecond_to_minute(nanosecond)
        hour = minute / 60
        return hour
    
    def nanosecond_to_day(self, nanosecond):
        hour = self.nanosecond_to_hour(nanosecond)
        day = hour / 24
        return day
    
    def nanosecond_to_week(self, nanosecond):
        day = self.nanosecond_to_day(nanosecond)
        week = day / 7
        return week
    
    def nanosecond_to_month(self, nanosecond):
        day = self.nanosecond_to_week(nanosecond)
        month = day / 30.44
        return month
    
    def nanosecond_to_year(self, nanosecond):
        month = self.nanosecond_to_month(nanosecond)
        calendar_year = month / 365.25
        return calendar_year
    
    def nanosecond_to_decade(self, nanosecond):
        calendar_year = self.nanosecond_to_year(nanosecond)
        decade = calendar_year / 10
        return decade
    
    def nanosecond_to_century(self, nanosecond):
        decade = self.nanosecond_to_decade(nanosecond)
        century = decade / 365.25
        return century


if __name__ == '__main__':
    t = TemperatureCalculator()
    result = t.convert_temperature(500.5)
    print(result)