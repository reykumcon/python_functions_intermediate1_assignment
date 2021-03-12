import random

def radInt(min=0, max=100):
    
    if max < 0:
        print("Please input a positive number")
    elif max < min:
        num = round(random.random() * (min - max) + max)
        return num
    else:
        num = round(random.random() * (max - min) + min)
        return num

#print(radInt())
print(radInt(max=50))
#print(radInt(min=50))
#print(radInt(min=50, max=500))