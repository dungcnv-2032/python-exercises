#App to calculate the hypotenuse and the area of a right-angled triangle
#Write a console programme that
#(1) Allows users to enter two numbers as length of legs
#(2) Makes sure what users entered are valid
#(3) Calculated and prints the hypotenuse and the area of the triangle
from math import sqrt
def caculate_triangle():
    try:
        length_leg_one = float(input('Please input length of leg one: '))
        length_leg_two = float(input('Please input length of leg two: '))
        print('The hypotenuse of the triangle is:', sqrt(length_leg_one * 2 + length_leg_two * 2))
        print('The are of the triangle is:', length_leg_one * length_leg_two / 2)
    except:
        print('Sorry, Please input length of leg is number !')
        caculate_triangle()

caculate_triangle()
