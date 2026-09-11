import time
import random

# money,produced resources,resources stockplie, prices of resources,wanted resources,
loc1 = [10,["Tools"],[],[],[]]
loc2 = [10,["Food"],[],[],[]]
loc3 = [10,["Timber"],[],[],[]]
#resources pricing timber :2 Food 3 Tools 4
def resource_gain(Location):
    random_resource = random.randrange(0,len(Location[1]))
    resource = Location[1][random_resource]
    #[random.randrange(0,len(Location[1]))
    print(f"Resource:{resource}")
    Location[2] = resource
    if resource == "Tools":
        Location[3] = 4
    elif resource == "Food":
        Location[3] = 3
    elif resource == "Timber":
        Location[3] = 2
    return Location
def resource_buying(loc1,loc2,loc3):
    diffrentplaces = [loc1,loc2,loc3]
    for x in diffrentplaces:
        for y in x[4]:
            if y in x+1[2]:
                if x[1] > x+1[]
    
    pass
loc1 = resource_gain(loc1)