def bmi(weight, height):
    result = weight / (height*height)
    return round(result,2)


print (bmi(50.95,1.71))