import numpy as np
from GridWorld import standard_grid , ACTION_SPACE
import math

threshold = math.exp(-3)

def print_values(v,g):
    for i in range(g.rows):
        print("----------------------------")
        for j in range(g.cols):
            V = v.get((i,j),0)
            if V>=0:
                print(" %.2f|"%V , end="")
            else:
                print("%.2f|"%V , end="")
        print("")

def print_policy(P,g):
    for i in range(g.rows):
        print("----------------------------")
        for j in range(g.cols):
            a = P.get((i,j),'')
            print(" %s  |"%a , end="")
        print("")
        
if __name__ == '__main__':
    transition_prob = {}
    rewards = {}
    grid = standard_grid()
    for i in range(grid.rows):
        for j in range(grid.cols):
            s = (i,j)
            if not grid.is_terminal(s):
                for a in ACTION_SPACE:
                    s2 = grid.get_next_state(s , a)
                    transition_prob[(s,a,s2)]=1
                    if s2  in grid.rewards:
                        rewards[(s,a,s2)]=grid.rewards[s2]
    
    print(rewards)
    policy = {
    
    (2,0):'U',
    (1,0):'U',
    (0,0):'R',
    (0,1):'R',
    (0,2):'R',
    (1,2):'U',
    (2,1):'R',
    (2,2):'U',
    (2,3):'L',
    
    
    }
    
    
    print_policy(policy , grid)
    print("")
    v = {}
    for s in grid.all_states():
        v[s]=0
    
    
    gamma = 0.9
    it = 0
    
    while True:
        biggest_change = 0
        for s in grid.all_states():
            old_v =v[s]
            new_v=0
            for a in ACTION_SPACE:
                for s2 in grid.all_states():
                    action_prob = 1 if policy.get(s) == a else 0
                      #  action_prob = 1
                    #else: action_prob =0
                    r = rewards.get((s,a,s2),0)
                    new_v += action_prob*transition_prob.get((s,a,s2),0)*(r+gamma*v[s2])
                    
                    
            v[s]=new_v
            biggest_change = max(biggest_change , np.abs(new_v - old_v))
        
        print(f" itr : {it} ,  Biggest Change : {biggest_change} \n" )
        print_values(v,grid)
        it+=1
        
        if biggest_change<threshold:
            break
    
    print("\nTask Completed")