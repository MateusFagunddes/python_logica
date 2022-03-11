import keyboard as k 

while True:
    if k.is_pressed('a'):
        x = 2 
        y = 3
        x += y 
        print(x) 

    if k.is_pressed('b'):
        x = 3 
        y = 2 
        x -= 2
        print(x)
