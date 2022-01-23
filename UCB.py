import numpy as np
import matplotlib.pyplot as plt

num_trails = 10000
bandit_prob = [0.2 , 0.5 , 0.8]

class Bandit():
    def __init__(self , p):
        self.p = p
        self.p_est = 0.
        self.N = 1.
        
    def pull(self):
        return np.random.random()<self.p
    
    def update(self , x):
        self.N+=1
        self.p_est = ((self.N - 1)*self.p_est + x) /self.N
        
def experiment():
    rewards = np.zeros(num_trails)
    bandits = [Bandit(g) for g in bandit_prob]
    n = 0
    def ucb(mean , n , nj) :
        return mean + np.sqrt(2*np.log(n)/nj)
    
    
    for b in range(len(bandits)):
        x = bandits[b].pull()
        bandits[b].update(x)
        n+=1
    
    for i in range(num_trails):
        
        j = np.argmax([ucb(b.p_est , n , b.N) for b in bandits])
        x = bandits[j].pull()
        n+=1
        rewards[i] = x

        bandits[j].update(x)

    cumulative_rewards = np.cumsum(rewards)
    win_rates = cumulative_rewards / (np.arange(num_trails) + 1)
    plt.ylim([0, 1])
    plt.plot(win_rates)
    plt.plot(np.ones(num_trails) * np.max(bandit_prob))
    plt.show()

if __name__ == "__main__":
        experiment()
        
        
        
    