# Core Library
import logging

# Third party
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(id="GuessingNumber-v0", entry_point="guessing_number.envs:GuessingNumberEnv")
