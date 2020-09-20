def bmi(A,B):
    BMI=A/(B)**2
    return BMI

height=float(input('height(m):'))
weight=float(input('weight(kg):'))
BMI=bmi(weight,height)
print('BMI:',BMI)
if BMI <= 18.5:
    print('light')
elif BMI >= 24:
    print('heavy')
else:
    print('normal')