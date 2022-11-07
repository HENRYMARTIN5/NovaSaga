# Nova Saga

A roguelike sci-fi game written in Python using Pygame. WIP.

## Installation

1. Clone the repository

2. Create a venv and install the requirements

```sh
python -m venv venv
venv\Scripts\activate.bat (if on windows)
source venv/bin/activate (if on linux)
pip install -r requirements.txt
```

3. Run the game

```sh
python main.py
```

## Contribution Guidelines

#### Imports should be condensed onto the same line.

#### Indents should be 4 spaces

#### There should be newlines before every `if`, `for`, `else` and `elif`, as well as between blocks of repetitive code. 

#### When printing any information, use the included library (`assets.util.logging`)

#### Main.py is a basic entry point. Don't put any content/rendering in it.

#### If requiring an external library, be sure to specify the exact version in `requirements.txt`. (`pip freeze` can help you get the versions of installed packages)

#### When creating or updating sprites, ensure that you use the palette defined in `assets/sprites/player/palette.png`

#### All audio files should be in `.wav` format (uncompressed)

## Level format

All levels used by Nova Saga can be found in `assets/levels`. Each level is its own folder. Each level consists of 2 (somtimes 3) parts.

First up is `data.json`. This file contains the definitions of dynamic parts of the level, as well as particle spawners and teleports. Let's take the `start` level as an example:

```json
{
    "level_scale": 4,
    "type": "start",
    "level_transitions": [
        {
            "style": "new",
            "x": 504,
            "y": 144,
            "w": 8,
            "h": 32,
            "transition_id": 1,
            "dest_x": 503,
            "dest_y": 168
        }
    ],
    "particle_spawners": [
        {
            "x":60,
            "y":60,
            "w":1000,
            "h":100,
            "behavior":"FallingDust",
            "freq":0.000005,
            "duration":1000,
            "color":[192,128,255]
        }
    ],
    "music": "Stardustv2"
}
```

At the start, we define the level scale. This is the amount that the `collision.png` file in the directory is zoomed in, usually to match the `display.png` file. The next attribute is the type of the level. There are three possible value: `start`, `room`, and `test`. `Room`s are put together in a random order to create the feeling of traversing an infinite map.

### `level_transitions`

This object contains the transitions in a level that teleport the player to other levels. There are two styles. `Old` transitions teleport a player to a specific level, wheras `new` transitions teleport the player to a new position in the randomly generated map. `X`, `Y`, `W`, and `H`, specify the X-position, Y-position, Width, and Height respectively. On `new` transitions, `transition_id` is a unique identifier for this transition. On `old` transitions, `dest_level` defines the destination level. `Dest_x` and `Dest_y` define the position the player is teleported to in the destination level.

### `particle_spawners`

This object contains the particle spawners that can be found in a level. Example usage can be found in the code above. Keep in mind that color is in a R, G, B format.

### `teleporters`

WIP

### `interactables`

WIP

### `cutscenes`

WIP

### `boxes`

Dynamic boxes that can be found in a level. Pretty self-explanatory, take a look at `test` for a usage example.

### `enemies`

Not working yet. A list of enemies that spawn in either dynamically or when the level starts. There is only currently one enemy, `mite`.
