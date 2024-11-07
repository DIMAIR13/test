# done
import math

a = float(input("Введіть значення для a: "))
b = float(input("Введіть значення для b: "))
 
y = ( ((a-b)/(a+b)) * math.e**(math.log(math.cos(a-b)*math.pi/8) / 0.137 ) )**(1/3)
 
print(y)
