import math

def circle(r):
    area = math.pi * (r**2)
    circumference = 2 * math.pi * r
    return [area, circumference]
[area, circumference] = circle(5)
rounded_area = round(area, 2)
rounded_circumference = round(circumference, 2)
print('Area : ', area, 'Rounded Area : ', rounded_area)
print('Circumference',circumference, 'Rounded Circumference', rounded_circumference)