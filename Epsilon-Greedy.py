import numpy as np
import matplotlib.pyplot as plt

Num_trails = 10000
eps = 0.05
bandit_prob = [0.54 , 0.77 , 0.66]

class Bandit :
    def __init__(self , p):
        self.p = p
        self.p_est = 0.
        self.N = 0.
        
    def pull(self):
        return np.random.random()<self.p
    
    def update(self , x ):
        self.N+= 1.
        self.p_est = ((self.N-1)*self.p_est + x)/self.N

def experiment():
    bandits = [Bandit(l) for l in bandit_prob]
    rewards = np.zeros(Num_trails)
    no_explored = 0
    no_exploited = 0
    no_optimal = 0
    optimal_j = np.argmax([b.p for b in bandits])
    
    
    for i in range(Num_trails):
        
        if np.random.random()<eps:
            no_explored +=1
            j = np.random.randint(len(bandits))
        else:
            no_exploited +=1
            j = np.argmax([b.p_est for b in bandits])
    
    
        if j==optimal_j:
            no_optimal +=1
        
        x = bandits[j].pull()
        rewards[i] = x
        bandits[j].update(x)
    
    cumul_reward = np.cumsum([rewards])
    win_rates = cumul_reward/(np.arange(Num_trails)+1)
    print(no_exploited)
    print(no_explored)
    plt.plot(win_rates)
    plt.show()
    
if __name__ == '__main__':
    experiment()
    
        
        