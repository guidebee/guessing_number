from gym.envs.registration import register

register(id="GuessingNumber-v0", entry_point="guessing_number.envs:GuessingNumberEnv")
