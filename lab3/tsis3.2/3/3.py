#chicken has 2 legs x = chicken
#rabbit has 4 legs  y = rabbit  
"""
x + y = 35(numheads)
2x + 4y = 94(numlegs)

x + y = 35
x + 2y = 47

y = 35 - x
x = 47 - 2(35 - x) = 47 - 70 + 2x = 2x - 23 so 
    
x = 23
y = 35 - 23 = 12
    
"""
heads = 35
legs = 94
def solve(numheads, numlegs):
  
    rabbit = (numlegs / 2) - numheads
    chicken = numheads - rabbit
    print("chickens : ", int(chicken))
    print("rabbits : ", int(rabbit))
solve(heads, legs)