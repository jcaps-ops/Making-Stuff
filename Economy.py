import time
import random

Lowclass_per = 0.48
middleclass_per = 0.51
upclass_per = 0.01
population = 10000

low_pop = population * Lowclass_per
middle_pop = population * middleclass_per
Up_pop = population * upclass_per
low_pop = int(low_pop)
middle_pop = int(middle_pop)
Up_pop = int(Up_pop)

gdp = 0
low_inc = 1
mid_inc = 10
Up_inc = 100

trickleval = 0.005
up_trickle = 0.0001

imagration_scale = 1
imagration_low = 1000
imagration_mid = 100
imagration_up = 10 

def Trickle(low=low_pop,mid=middle_pop,up=Up_pop,trickleval=trickleval):
    lowval = low * trickleval
    low -= lowval
    mid += lowval
    midval =  mid * trickleval
    mid -= midval
    up += midval
    low = int(low)
    mid = int(mid)
    up = int(up)
    return low,mid,up
def GDP_update(low=low_pop,mid=middle_pop,up=Up_pop,gdp=gdp,low_inc=low_inc,mid_inc=mid_inc,up_inc = Up_inc):
    gdp += low * low_inc
    gdp += mid * mid_inc
    gdp += up * up_inc
    gdp = int(gdp)
    return gdp
def pop_update(low=low_pop,mid=middle_pop,up=Up_pop,low_im = imagration_low,mid_im = imagration_mid,up_im=imagration_up,scale=imagration_scale):
    low = random.randrange(1,imagration_low) * imagration_scale
    mid = random.randrange(1,imagration_mid) * imagration_scale
    up = random.randrange(1,imagration_up) * imagration_scale
    print(f"")
    low = int(low)
    mid = int(mid)
    up = int(up)
    return low,mid,up
while True:
    ply_int = input("")
    if ply_int != "E" or ply_int != "e":
        low_pop,middle_pop,Up_pop = Trickle(low_pop,middle_pop,Up_pop,trickleval)
        gdp = GDP_update(low_pop,middle_pop,Up_pop,gdp,low_inc,mid_inc,Up_inc)
        print(f"lowerclass population {low_pop}\nmiddle class population {middle_pop}\nupper class population {Up_pop}")
        print(f"GDP of {gdp}")
        time.sleep(1)
    else:
        break

