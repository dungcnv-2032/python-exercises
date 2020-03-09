#Celsius to Fahrenheit (°C to °F) App
#Write a console programme that
#(1) Allows users to enter a number as temperature in Celsius
#(2) Makes sure what users entered is valid
#(3) Prints the temperature in Fahrenheit
def celsius_to_fahreheit():
    try:
        number_temperature = float(input('Please input a number temperature as temperature in Celsius as temperature in Celsius:'))
        print('Temperature in Fahrenheit is :', number_temperature * 1.8 + 32)
    except:
        print('Sorry, Please input temperature is number !')
        celsius_to_fahreheit()

celsius_to_fahreheit()