import numpy as np
ACTION_SPACE = ['U', 'D' , 'L' , 'R']

class Grid:
    def __init__(self , rows , cols , start):
        self.rows = rows
        self.cols = cols
        self.i = start[0]
        self.j = start[1]

    def set(self , rewards , actions):
        self.rewards=rewards
        self.actions = actions
        
    def set_state(self,s):
        self.i = s[0]
        self.j = s[1]
        
    def current_state(self):
        return  (self.i , self.j)
    
    def is_terminal(self , s):
        return s  not in self.actions
    
    def reset(self):
        self.i = 2
        self.j = 0
        
        return (self.i , self.j)
    
    def get_next_state(self , s , a):
        
        self.i = s[0]
        self.j = s[1]
        
        if a in self.actions[(self.i,self.j)]:
            if a=='U':
                self.i-=1
            elif a=='D':
                self.i+=1
            elif a=='R':
                self.j+=1
            elif a=='L':
                self.j-=1
        
        return (self.i,self.j)
    
    def move(self , action):
        if action in self.actions[(self.i, self.j)]:
            if action == 'U':
                self.i -= 1
            elif action == 'D':
                self.i += 1
            elif action == 'R':
                self.j += 1
            elif action == 'L':
                self.j -= 1
            
        return self.rewards.get((self.i , self.j ) , 0)
    
    
    
    def all_states(self):
        return set(self.actions.keys()|self.rewards.keys())
    
    def game_over(self):
        return (self.i,self.j) not in self.actions

def standard_grid():
        step_cost = -0.1
        g = Grid(3, 4, (2, 0))
        rewards = {(0, 3): 1, (1, 3): -1 ,
                   (0, 0): step_cost,
            (0, 1): step_cost,
            (0, 2): step_cost,
            (1, 0): step_cost,
            (1, 2): step_cost,
            (2, 0): step_cost,
            (2, 1): step_cost,
            (2, 2): step_cost,
            (2, 3): step_cost}
        
        
        actions = {
            (0, 0): ('D', 'R'),
            (0, 1): ('L', 'R'),
            (0, 2): ('L', 'D', 'R'),
            (1, 0): ('U', 'D'),
            (1, 2): ('U', 'D', 'R'),
            (2, 0): ('U', 'R'),
            (2, 1): ('L', 'R'),
            (2, 2): ('L', 'R', 'U'),
            (2, 3): ('L', 'U'),
            
        
        }
        
        g.set(rewards, actions)
        return g
        
class W_Grid():
    
    def __init__(self , rows , cols , start):
        
        
        self.i = start[0]
        self.j = start[1]
        self.rows = rows
        self.cols = cols
    
    def set(self , rewards , actions , probs ):
        
        self.actions = actions
        self.rewards = rewards
        self.probs = probs
        
    
    def current_state(self ):
        return (self.i , self.j)
    
    def is_terminal(self,s):
        return s not in self.actions
    
    def game_over(self):
        return (self.i , self . j) not in self.actions
    
    def all_states(self):
        return set(self.actions.keys()|self.rewards.keys())
    
    def move(self , action):
    
        s = (self.i , self.j)
        a = action
        
        probs = self.probs[(s,a)]
        next_prob = list(probs.keys())
        next_states = list(probs.values())
        s2 = np.random.choice(next_states , next_prob)
        (self.i , self.j) = s2
        
        return self.rewards.get(s,0)
    
def windy_grid():
    g = W_Grid(3,4,(2,0))
    step_cost = -0.1
    rewards = {(0, 3): 1, (1, 3): -1 , (0, 0): step_cost,
    (0, 1): step_cost,
    (0, 2): step_cost,
    (1, 0): step_cost,
    (1, 2): step_cost,
    (2, 0): step_cost,
    (2, 1): step_cost,
    (2, 2): step_cost,
    (2, 3): step_cost}
    actions = {
        (0, 0): ('D', 'R'),
        (0, 1): ('L', 'R'),
        (0, 2): ('L', 'D', 'R'),
        (1, 0): ('U', 'D'),
        (1, 2): ('U', 'D', 'R'),
        (2, 0): ('U', 'R'),
        (2, 1): ('L', 'R'),
        (2, 2): ('L', 'R', 'U'),
        (2, 3): ('L', 'U'),
    
    }

    probs = {
        ((2, 0), 'U'): {(1, 0): 1.0},
        ((2, 0), 'D'): {(2, 0): 1.0},
        ((2, 0), 'L'): {(2, 0): 1.0},
        ((2, 0), 'R'): {(2, 1): 1.0},
        ((1, 0), 'U'): {(0, 0): 1.0},
        ((1, 0), 'D'): {(2, 0): 1.0},
        ((1, 0), 'L'): {(1, 0): 1.0},
        ((1, 0), 'R'): {(1, 0): 1.0},
        ((0, 0), 'U'): {(0, 0): 1.0},
        ((0, 0), 'D'): {(1, 0): 1.0},
        ((0, 0), 'L'): {(0, 0): 1.0},
        ((0, 0), 'R'): {(0, 1): 1.0},
        ((0, 1), 'U'): {(0, 1): 1.0},
        ((0, 1), 'D'): {(0, 1): 1.0},
        ((0, 1), 'L'): {(0, 0): 1.0},
        ((0, 1), 'R'): {(0, 2): 1.0},
        ((0, 2), 'U'): {(0, 2): 1.0},
        ((0, 2), 'D'): {(1, 2): 1.0},
        ((0, 2), 'L'): {(0, 1): 1.0},
        ((0, 2), 'R'): {(0, 3): 1.0},
        ((2, 1), 'U'): {(2, 1): 1.0},
        ((2, 1), 'D'): {(2, 1): 1.0},
        ((2, 1), 'L'): {(2, 0): 1.0},
        ((2, 1), 'R'): {(2, 2): 1.0},
        ((2, 2), 'U'): {(1, 2): 1.0},
        ((2, 2), 'D'): {(2, 2): 1.0},
        ((2, 2), 'L'): {(2, 1): 1.0},
        ((2, 2), 'R'): {(2, 3): 1.0},
        ((2, 3), 'U'): {(1, 3): 1.0},
        ((2, 3), 'D'): {(2, 3): 1.0},
        ((2, 3), 'L'): {(2, 2): 1.0},
        ((2, 3), 'R'): {(2, 3): 1.0},
        ((1, 2), 'U'): {(0, 2): 0.5, (1, 3): 0.5},
        ((1, 2), 'D'): {(2, 2): 1.0},
        ((1, 2), 'L'): {(1, 2): 1.0},
        ((1, 2), 'R'): {(1, 3): 1.0},
    }

    g.set(rewards, actions , probs)
    return g

def negative_grid():
    step_cost = -0.1
    g = standard_grid()
    g.rewards.update({
        (0, 0): step_cost,
        (0, 1): step_cost,
        (0, 2): step_cost,
        (1, 0): step_cost,
        (1, 2): step_cost,
        (2, 0): step_cost,
        (2, 1): step_cost,
        (2, 2): step_cost,
        (2, 3): step_cost
    })
    
    return g
    