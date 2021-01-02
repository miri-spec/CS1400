
import random
import turtle
import math
from statistics import mean
import statistics

t = turtle.Turtle()

select = [1,2]#program chooses which axis to move on, 1 indicates x and 2 indicates y
cardinal = [1,0,-1]#decides whether to add, subtract or stay in the same place
s_favor = [1,1,2,3,4]

pa_record = []
mi_ma_record = []
reg_record = []

def distance(k,p):
    legs = abs(k+p)
    return math.sqrt(legs)

def calculate(lyst):
    lyst.sort()
    ave = mean(lyst)
    if len(lyst) > 1:
        stdv = statistics.stdev(lyst)
    else:
        stdv = 1
    cv = stdv/ave
    print("Min:", "%0.2f" % lyst[0], "Max:", "%0.2f" % lyst[-1],
          "Mean:", "%0.2f" % ave, "CV:", "%0.2f" % cv)
    
def mi_ma(steps, rep):
    t.pencolor("black")
    for b in range(rep):
        side = 0
        forward = 0
        for i in range(steps):
            z = random.choice(s_favor)
            if z == 1:
                forward -= 1
            if z == 2:
                forward += 1
            if z == 3:
                side -=1
            else:
                side += 1
        mi_ma_record.append(distance(side, forward))
        t.goto(side, forward)
        t.dot("black")
    print("Mi-Ma's random walk of ", steps, "steps:")
    calculate(mi_ma_record)

def reg(steps, rep):
    t.pencolor("blue")
    for b in range(rep):
        side = 0
        forward = 0
        for i in range(steps):
            u = random.choice(cardinal)
            side += u
        reg_record.append(abs(side))
        t.goto(side, forward)
        t.dot("blue")
    print("Reg's random walk of ", steps, "steps:")
    calculate(reg_record)

def pa_walk(steps, rep):
    t.pencolor("red")
    for b in range(rep):
        side = 0
        forward = 0
        for i in range(steps):
            w = random.choice(select)
            v = random.choice(cardinal)
            if w == 1:
                side += v
            else:
                forward += v
        pa_record.append(distance(side, forward))
        t.goto(side, forward)
        t.dot("red")
    print("Pa random walk of ", steps, "steps:")
    calculate(pa_record)
    

def main():
    dist = input("Enter the walk lengths to simulate: ")
    reps = int(input("Enter the number of times to simulate each walk length: "))
    player = input("Which wanderer would you like to model; Pa, Mi-Ma, Reg, or All? ")
    trials = dist.split(",")
    for i in trials:
        r = int(i)
        if "Pa" in player:
            pa_walk(r,reps)
        elif "Ma" in player:
            mi_ma(r,reps)
        elif "Reg" in player:
            reg(r,reps)
        elif "All" in player:
            pa_walk(r,reps)
            mi_ma(r,reps)
            reg(r,reps)
        else:
            print("Please enter a valid wanderer.")
    
    
if __name__ == "__main__":
    main()
    