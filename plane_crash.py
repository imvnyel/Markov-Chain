# 1.) Place this code into a file and save it as "plane_crash.py".
# 2.) Run this code in your shell ("python plane_crash.py"). You'll see that it works.
# 3.) Try to understand how the code works.
# 4.) Think about code style improvements and change the code accordingly (so that is still runs afterwards ;) )
# 5.) We will then discuss together, how to refactor the code.

from random import choices

# States the aircraft is in 
states = ['airport', 'air', 'crashed']

#Probablity of state change
probabilities = {'airport': [0.4, 0.6, 0.0],
                 'air': [0.8, 0.19999, 0.00001],
                 }
        
    
def mcmc(i, probabilities):
    list = [i]
    s = i
    while s!='crashed':
        probs = probabilities[s]
        s = choices(states, probs) [0]
        list.append(s)
        print(s)
        if list[-1] == 'crashed':
            return list
        
        
print(f"crashed after {len(mcmc('airport', probabilities))} days of service")














