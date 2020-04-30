This repository contains a PIP package which is an OpenAI environment for
Guessing number game


## Installation

Install the [OpenAI gym](https://gym.openai.com/docs/).

Then install this package via

```
pip install -e .
```

## Usage

```
import gym
import guessing_number

env = gym.make('GuessingNumber-v0')
```

