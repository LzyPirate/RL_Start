import numpy as np
from GridWorld import negative_grid , standard_grid , ACTION_SPACE
from Policy_evaluation_deterministic import print_policy , print_values
gamma = 0.9




def max_dict(d):
    max_value = max(d.values())
    max_keys = []
    for key , values in d.items():
        
        if max_value == values :
            max_keys.append(key)
    
    return np.random.choice(max_keys) , max_value


def play_episode(policy , grid , max_steps = 20):
    all_states = list(grid.actions.keys())
    start_state_index = np.random.choice(len(all_states))
    
    grid.set_state(all_states[start_state_index])
    a = np.random.choice(ACTION_SPACE)

    s = all_states[start_state_index]
    states = [s]
    actions = [a]
    rewards = [0]
    steps = 0
    
    while not grid.game_over():
         
         
         r = grid.move(a)
         next_state = grid.current_state()
         
         rewards.append(r)
         states.append(next_state)
         s = next_state
         
         if grid.game_over():
             break
         else:
             a= policy[s]
             actions.append(a)
            
         
         steps+=1
         
         
         if steps>= max_steps:
             break
    
    
    return rewards , states , actions

if __name__ == '__main__':
    g = negative_grid()
    print("rewards:")
    print_values(g.rewards, g)
    policy = {}

    

    for s in g.actions.keys():
        policy[s] = np.random.choice(ACTION_SPACE)
    
    
    states = g.all_states()
    
    Q ={}
    sample_counts = {}
    
    for s in states:
        if s in g.actions.keys():
            Q[s] = {}
            sample_counts[s] ={}
            for a in ACTION_SPACE:
                Q[s][a] =0
                sample_counts[s][a] = 0
        else:
            pass
        
       
        
    
    
    
    for _ in range(10000):
        
        rewards, states, actions= play_episode(policy , g )
        state_actions = list(zip(states , actions))
        
        T = len(states)
        G =0
        
        for t in range(T-2 , -1 , -1):
            
            s = states[t]
            a = actions[t]
            G = rewards[t+1]+gamma*G
            
            if (s,a) not in state_actions[:t]:
                old_q = Q[s][a]
        
                sample_counts[s][a]+=1
                lr = 1/sample_counts[s][a]
                Q[s][a] = old_q + lr * (G-old_q)
                
                
                policy[s] = max_dict(Q[s])[0]
                
                
    print("final policy:")
    print_policy(policy , g)
    
    v={}
    for s , qs in Q.items():
        v[s] = max_dict(Q[s])[1]
        
    print("vALUES:")
    print_values(v , g)