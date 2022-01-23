import numpy as np
from GridWorld import standard_grid , windy_grid , ACTION_SPACE
from policy_evaluation_prob import get_trans_p_and_rewards
from Policy_evaluation_deterministic import  print_values , print_policy
import math

threshold = math.exp(-3)
gamma = 0.9

if __name__ == '__main__':
    grid = windy_grid()
    trans_prob , rewards = get_trans_p_and_rewards(grid)
    
    V={}
    
    for s in grid.all_states():
        V[s] =0
    
    while True:
        biggest_change = 0
        for s in grid.actions.keys():
            old_v = V[s]
            new_v = float('-inf')
            if not grid.is_terminal(s):
                for a in ACTION_SPACE:
                    v = 0
                    for s2 in grid.all_states():
                        
                        r = rewards.get((s,a,s2),0)
                        v+= trans_prob.get((s,a,s2),0)*(r+ gamma * V[s2])
                    
                    if v>new_v:
                        new_v = v
                
                V[s] = new_v
                biggest_change = max(biggest_change,np.abs(old_v-V[s]))
        
        if biggest_change<threshold:
            break
            
    policy = {}

    
    for s in grid.actions.keys():
            old_v = V[s]
            new_v = float('-inf')
            if not grid.is_terminal(s):
                for a in ACTION_SPACE:
                    v = 0
                    for s2 in grid.all_states():
                        r = rewards.get((s, a, s2),0)
                        v += trans_prob.get((s, a, s2), 0) * (r + gamma * V[s2])
                
                    if v > new_v:
                        new_a = a
                        new_v = v
                policy[s] = new_a

                
    print_policy(policy ,grid)
    print_values(V , grid)
    
            
        
        
        




