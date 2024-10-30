import random
import time
letters = ["H","E","l","O","W","R","L","D"]

for i in range(20000):
    print(random.choice(letters), end= "")
    time.sleep(.01)
