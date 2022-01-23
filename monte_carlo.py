import numpy as np
from GridWorld import standard_grid , negative_grid , ACTION_SPACE
from Policy_evaluation_deterministic import print_policy , print_values


gamma = 0.9

def play_game(grid , policy , max_steps=20):
    start_states = list(grid.actions.keys())
    start_index = np.random.choice(len(start_states))
    grid.set_state(start_states[start_index])
    
    s = grid.current_state()
    
    states = [s]
    rewards = [0]
    
    steps = 0
    
    while not grid.game_over():
        a = policy[s]
        r = grid.move(a)
        next_s = grid.current_state()
        states.append(next_s)
        rewards.append(r)
        steps+=1
        if steps>=max_steps:
            break
        
        s = next_s
        
    return states , rewards

if __name__ == '__main__':
    g = standard_grid()
    rewards = g.rewards
    print("rewards:")
    print_values(rewards , g)
    
    policy ={}
    
    
    
    
    policy = {
    
        (2, 0): 'U',
        (1, 0): 'U',
        (0, 0): 'R',
        (0, 1): 'R',
        (0, 2): 'R',
        (1, 2): 'R',
        (2, 1): 'R',
        (2, 2): 'R',
        (2, 3): 'U'




        
        
        
    }
    
    
   # print_policy(policy , standard_grid())
    V = {}
    returns = {}
    states = g.all_states()
    for s in states:
        if s in g.actions:
            returns[s] = []
        else:
            V[s]=0
            
    for _ in range(100):
        
        states , rewards =  play_game(g , policy)
        T = len(states)
        G = 0
        
        for t in range(T-2 , -1 , -1):
            
            s = states[t]
            r = rewards[t+1]
            G = r + gamma *G
            
        if s not in states[:t]:
                returns[s].append(G)
                V[s] = np.mean(returns[s])

    print("values:")
    print_values(V , g)
    print("Policy")
    print_policy(policy , g)