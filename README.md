# rps-starter

A Starter Repository for the [Rock Paper Scissors Exercise](https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md).

## Setup

Create a virtual environment:

```sh
conda create -n rps-env python=3.8
```

Activate the virtual environment:

```sh
conda activate rps-env
```

Install package dependencies (mainly for testing):

```sh
pip install -r requirements.txt
```

## Usage

Run the rock paper scissors game:

```sh
python game.py
```

## Testing

Run tests:

```sh
pytest
```

# Naming
If you'd like to add enter your name for the game to be more interactive, enter the following line of code prior to running the file replacing 'Jon Snow' with your own name 

PLAYER_NAME="Jon Snow" python game.py

