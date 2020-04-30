import gym
from gym import wrappers, logger
import guessing_number


class RandomAgent(object):
    """The world's simplest agent!"""

    def __init__(self, action_space):
        self.action_space = action_space

    def act(self, observation, reward, done):
        return self.action_space.sample()


class BetterRandomAgent(object):
    """The world's simplest agent!"""

    def __init__(self, action_space):
        self.action_space = action_space

    def act(self, observation, last_action):
        new_action = last_action
        if observation == 1:
            new_action = last_action + abs(last_action / 2)

        elif observation == 3:
            new_action = last_action - abs(last_action / 2)
        if abs(last_action - new_action) < 1e-1:
            new_action = self.action_space.sample()
        return new_action


if __name__ == '__main__':

    # You can set the level to logger.DEBUG or logger.WARN if you
    # want to change the amount of output.
    logger.set_level(logger.INFO)

    env = gym.make('GuessingNumber-v0')
    env.seed(0)
    agent = BetterRandomAgent(env.action_space)

    episode_count = 100
    reward = 0
    done = False

    total_reward = 0
    total_guesses = 0
    for i in range(episode_count):
        last_action = env.action_space.sample()
        ob = env.reset()
        while True:
            action = agent.act(ob, last_action)
            ob, reward, done, info = env.step(action)
            last_action = action

            # print(f'count={info["guesses"]},number={info["number"]},guess={action},ob={ob},reward={reward}')
            if done:
                total_reward += reward
                total_guesses += int(info["guesses"])
                break
            # Note there's no env.render() here. But the environment still can open window and
            # render if asked by env.monitor: it calls env.render('rgb_array') to record video.
            # Video is not recorded every episode, see capped_cubic_video_schedule for details.

    # Close the env and write monitor result info to disk

    print(f'Total better random reward {total_reward}, average guess {round(total_guesses/100,1)}')

    env.seed(0)
    agent = RandomAgent(env.action_space)
    reward = 0
    done = False

    total_reward = 0
    total_guesses = 0

    for i in range(episode_count):
        ob = env.reset()
        while True:
            action = agent.act(ob, reward, done)
            ob, reward, done, info = env.step(action)

            if done:
                total_reward += reward
                total_guesses += int(info["guesses"])
                break
            # Note there's no env.render() here. But the environment still can open window and
            # render if asked by env.monitor: it calls env.render('rgb_array') to record video.
            # Video is not recorded every episode, see capped_cubic_video_schedule for details.

    # Close the env and write monitor result info to disk
    env.close()
    print(f'Total better random reward {total_reward}, average guess {round(total_guesses/100,1)}')

