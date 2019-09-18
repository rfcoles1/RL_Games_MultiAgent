import numpy as np
import gym
import gym.spaces 
from Bees_Engine import BeeEngine

class BeeEnv(gym.Env):
    def __init__(self):
        self.engine = BeeEngine()
        self.done = False

        self.actions = {0: self.engine.move_left,
                        1: self.engine.move_right,
                        2: self.engine.move_down,
                        3: self.engine.move_up,
                        4: self.engine.no_move}

        self.action_space = gym.spaces.Discrete(5)

    def reset(self):
        self.engine.reset()
        return self.get_state()

    def get_state(self):
        state = self.engine.get_state()
        state[:,0] = state[:,0]/float(self.engine.xmax)
        state[:,1] = state[:,1]/float(self.engine.ymax)
        return state

    def step(self,a):
        beeID = 0 
        self.actions[a](beeID)
        self.engine.check_bee_pos(beeID)
        next_state = self.get_state()
        reward = np.sum(self.engine.bee_food) + self.engine.hive_food*3 
        return next_state, reward, self.done, {}

    def render(self):
        return 0 
