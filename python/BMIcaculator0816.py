height=float(input('height(m):'))
wieght=float(input('wieght(kg):'))
BMI=float(wieght/(height**2))
print('BMI=',BMI)
if BMI <= 18.5:
    print('light')
elif BMI >= 24:
    print('heavy')
else:
    print('normal')