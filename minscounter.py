import time
import sys


input("enter minutes ")
for remaining in range(10, 0, -1):
    sys.stdout.write("\r")
    sys.stdout.write("{:2d} minutes remaining.".format(remaining)) 
    sys.stdout.flush()
    time.sleep(60)

sys.stdout.write("\rComplete!            \n")

