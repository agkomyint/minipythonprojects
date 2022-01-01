import time
import sys


gg=int(input("Number of minutes to set the timer"))
for remaining in range(gg, 0, -1):
    sys.stdout.write("\r")
    sys.stdout.write("{:2d} minutes remaining.".format(remaining)) 
    sys.stdout.flush()
    time.sleep(60)

sys.stdout.write("\rFinished           \n")

