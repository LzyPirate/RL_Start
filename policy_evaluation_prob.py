import numpy as np
from GridWorld import windy_grid ,ACTION_SPACE , standard_grid
import math
from Policy_evaluation_deterministic import  print_values , print_policy


threshold = math.exp(-3)
gamma = 0.9


def get_trans_p_and_rewards(grid):
    trans_probs= {}
    rewards = {}
    
    for (s,a),v in grid.probs.items():
        
        for s2 ,p in  v.items():
            trans_probs[(s,a,s2)] =p
            rewards[(s,a,s2)] = grid.rewards.get(s2,0)
        
    return trans_probs , rewards




def eval_deterministic_policy(grid , policy, intV = None  ):
    if intV is None:
        V = {}
        for s in grid.all_states():
            V[s]=0
    
    else:
        V = intV
        
    it = 0
    rewards = get_trans_p_and_rewards(grid)[1]
    tra_probs = get_trans_p_and_rewards(grid)[0]
    
    
    
    while True:
    
        for s in grid.all_states():
            old_v = V[s]
            new_v = 0
            
            for a in ACTION_SPACE:
                for s2 in grid.all_states():
                    
                    if policy.get(s) == a:
                        action_prob = 1
                    else :
                        action_prob = 0

                    
                
                    reward = rewards.get((s,a,s2),0)
                    new_v += action_prob * tra_probs.get((s,a,s2) , 0)* (reward + gamma*V[s2])
                
            V[s] = new_v
        it+=1
        
        if np.abs(old_v - new_v) < threshold:
            break
            

    return V


if __name__ == '__main__':
    
    grid  = windy_grid()
    transition_probs , rewards = get_trans_p_and_rewards(grid)
    
    print("rewards = ")
    print_values(grid.rewards , grid)
    policy = {}
    for s in grid.actions.keys():
        policy[s] = np.random.choice(ACTION_SPACE)
    print("initial_policy:")
    print_policy(policy , grid)
    V = None
    
    while True :
        
        V = eval_deterministic_policy(grid , policy , V)
        
        is_policy_conserved = True
        for s in grid.actions.keys():
            old_a = policy[s]
            new_a = None
            best_v =-(np.inf)
            
            for a in ACTION_SPACE:
                v = 0
                for s2 in grid.all_states():
                    r = rewards.get((s,a,s2),0)
                    v+=transition_probs.get((s,a,s2),0)*(r+(gamma *V[s2]))
                    
                if v>best_v:
                    new_a = a
                    best_v = v
                
            policy[s] = new_a
            if new_a != old_a:
                is_policy_conserved = False
        
        if is_policy_conserved:
            break
            
    print("Values:")
    print_values(V , grid)
    print("Policy:")
    print_policy(policy , grid)