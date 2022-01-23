import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

banditProb = [0.23 , 0.47 , 0.875]
num_trails = 2000

class Bandit():
    def __init__(self , p):
        
        self.p = p
        self.a = 1
        self.b = 1
        self.N = 0
        
    def pull(self):
        return np.random.random() < self.p
    
    def sample(self):
        return np.random.beta(self.a , self.b)
    
    def update(self , x):
        
        self.a += x
        self.b += 1-x
        self.N +=1




def plot(bandits , trails):
    x = np.linspace(0 , 1 , 200)
    for b in bandits:
       
        y = beta.pdf(x , b.a , b.b)
        plt.plot(x,y , label =f"real P : {b.p : .4f}  , win_rate = {(b.a-1)}/{b.N}")
    plt.title(f"Bandit Distributions after '{trails}' trails")
    plt.legend()
    plt.show()
def experiment():
    bandits = [Bandit(p) for p in banditProb]
    rewards = np.zeros(num_trails)
    sample_points = [5, 10, 20, 50, 100, 200, 500, 1000, 1500, 2000]
    
    for i in range(num_trails):
        
        j = np.argmax([f.sample() for f in bandits])
        
        if i in sample_points:
            plot(bandits , i)
        x =bandits[j].pull()
        
        rewards[i]= x
        bandits[j].update(x)
        
        


if __name__=="__main__":
    experiment()