import numpy as np
from GridWorld import standard_grid , negative_grid , ACTION_SPACE
from Policy_evaluation_deterministic import print_policy , print_values

gamma = 0.9
eps = 0.05

def play_game(grid , policy , max_steps = 20):
     
     s = grid.reset()
     a = epslion_greedy(policy , s)
     
     states = [s]
     rewards = [0]
     actions = [a]
     it = 0
     
     while it<=max_steps:
         r = grid.move(a)
         next_s = grid.get_next_state(s , a)
         new_a = epslion_greedy(policy , next_s)
         
         if not grid.game_over():
             states.append(next_s)
             actions.append(new_a)
             rewards.append(r)
             a = policy
             
         s = next_s
         it+=1
    
     return states,actions,rewards

def epslion_greedy(policy ,s , EPS = eps ):
    
    if np.random.random()>EPS:
        print("explored")
        return np.random.choice(ACTION_SPACE)
    else:
        return policy[s]
    
    
    
    
    
    
def max_d(d):
    max_value = max(d.values())
    
    max_keys = []
    
    for keys , values in d.items():
        if max_value == values:
            max_keys.append(keys)
            
    return np.random.choice(max_keys) , max_value
    

if __name__ == '__main__':
    grid = standard_grid()
    
    print("rewards:")
    print_values(grid.rewards , grid)
    
    policy = {}
    
    for s in grid.actions.keys():
        policy[s] = np.random.choice(ACTION_SPACE)
    print("policy:")
    print_policy(policy,grid)
    Q ={}
    number = {}
    states = grid.all_states()
    for s in grid.all_states():
        if not grid.is_terminal(s):
            Q[s]={}
            number[s] = {}
            
            for a in ACTION_SPACE:
                Q[s][a] =0
                number[s][a] = 0
        
        else:
            pass
        
    for _ in range(10000):
        
        states, actions, rewards =play_game(grid , policy)
        state_actions = list(zip(states, actions))
        T = len(states)
        G =0
        for t in range( T-2 , -1 ,-1):
            
            
            s=  states[t]
            a = actions[t]
            G = rewards[t+1]+ gamma * G
            
            if (s , a) not in state_actions[:t]:
                old_q = Q[s][a]
                number[s][a]+=1
                rp = 1/number[s][a]
                Q[s][a] = old_q + rp * (G - old_q)
                policy[s] = max_d(Q[s])[0]
                
                
                
                
                

    print("Updated policy:")
    print_policy(policy, grid)
    
    v={}
    for s , qs in Q.items():
        v[s] = max_d(Q[s])[1]
        
    print("Values:")
    print_values(v , grid)
    
    
    
            
            