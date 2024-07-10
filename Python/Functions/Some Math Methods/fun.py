def div(num1,num2):
    return num1//num2
def mod(num1, num2):
    if num1 < num2:
        return num1
    else:
        while num1 >= num2:
            num1 -= num2
        
        return num1            
def Mod(num1, num2):
    if num2==0:
        return 
    else:
         return num1-((num1//num2) * num2)
def sumAll(min, max):
    return ((max-min)+1) * (min + max) // 2

print(sumAll(5,8))
# print(Mod(10, 3))   

