import numpy as np

import matplotlib.pyplot as plt

class Bandit():
    def __init__(self , m):
        self.p = m
        self.p_est = 0.
        self.N = 0.
        
    def pull(self):
        return np.random.randn()+self.p
    
    def update(self , x):
        self.N += 1
        self.p_est = (((self.N-1)*self.p)+x)/self.N
        
def experiment(m1 , m2 , m3 ,eps ,  N_trails):
    Bandits = [Bandit(m1) , Bandit(m2) , Bandit(m3)]
    rewards = np.zeros(N_trails)
    
    
    for i in range(N_trails):
        
        if np.random.random()<eps:
            j = np.random.randint(len(Bandits))
        
        else:
            j = np.argmax([b.p_est  for b in Bandits])
            
        
        x = Bandits[j].pull()
        rewards[i] = x
        Bandits[j].update(x)
        
    cumrew = np.cumsum([rewards])
    win_rates = cumrew/(np.arange(N_trails)+1)
    plt.plot(win_rates)
    plt.plot(np.ones(N_trails)*m1)
    plt.plot(np.ones(N_trails) * m2)
    plt.plot(np.ones(N_trails) * m3)
    plt.xscale('log')
    plt.show()
    
    return win_rates
    

if __name__ == '__main__' :
    w1 = experiment(1.5 , 2.5 , 3.5 , 0.01 , 10000)
    w2 = experiment(1.5, 2.5, 3.5, 0.05, 10000)
    w3 = experiment(1.5, 2.5, 3.5, 0.1, 10000)
    
    plt.plot(w1 , label = 'eps = 0.01')
    plt.plot(w2, label='eps = 0.05')
    plt.plot(w3, label='eps = 0.1')
    plt.legend()
    plt.xscale('log')
    plt.show()
    
   