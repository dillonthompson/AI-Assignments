import gym
from gym import envs
env = gym.make('MountainCar-v0')
env.reset()
print(envs.registry.all())
for _ in range(1000):
    env.render()
    env.step(env.action_space.sample())  # take a random action
env.close()