import numpy as np
import matplotlib.pyplot as plt

bandit_prob= [0.2, 0.5, 0.7]
num_trails = 10000

class Bandit():
    def __init__(self , p):
        self.p = p
        self.p_est = 5.
        self.N = 1.
    
    def pull(self):
        return np.random.random() < self.p
    
    def update(self , x):
        self.N+=1.
        self.p_est = ((self.N-1)*self.p_est + x)/self.N
    
    
def experiment():
    rewards = np.zeros(num_trails)
    bandit = [Bandit(a) for a in bandit_prob]
    
    for i in range(num_trails):
        
        j = np.argmax([b.p_est  for b in bandit])
        
        x= bandit[j].pull()
        
        rewards[i] = x

        bandit[j].update(x)

    cumulative_rewards = np.cumsum(rewards)
    win_rates = cumulative_rewards / (np.arange(num_trails) + 1)
    plt.ylim([0, 1])
    plt.plot(win_rates)
    plt.plot(np.ones(num_trails) * np.max(bandit_prob))
    plt.show()


if __name__ == "__main__":

  experiment()