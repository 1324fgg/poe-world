from classes.game_utils.base_game import BaseActions

# Object type -> (width, height) mapping.
# Values sourced from OCAtari RAM extraction (ocatari/ram/alien.py).
# The 'egg' objects are numerous (up to 156) but tiny; they are included here
# for completeness though the WM typically focuses on player and alien objects.
alien_wh_dict = {
    'player': (6, 13),
    'alien': (8, 13),
    'pulsar': (7, 5),
    'egg': (1, 2),
    'score': (6, 7),
    'life': (5, 5),
}

# Conservative upper bound on pixel displacement per frame (frameskip=3).
# Alien enemies can move fairly fast when chasing the player.
ALIEN_MAX_ABS_VELOCITY = 15

ALIEN_HISTORY_LENGTH = 100

ALIEN_MAX_ABS_SIZE_CHANGE = 1

# ALE action names used by poe-world for Alien.
# Alien is a platformer with 8-directional movement and a FIRE action.
ALIEN_ACTIONS = [
    'NOOP', 'FIRE', 'UP', 'RIGHT', 'LEFT', 'DOWN',
    'UPRIGHT', 'UPLEFT', 'DOWNRIGHT', 'DOWNLEFT',
    'UPFIRE', 'RIGHTFIRE', 'LEFTFIRE', 'DOWNFIRE',
    'UPRIGHTFIRE', 'UPLEFTFIRE', 'DOWNRIGHTFIRE', 'DOWNLEFTFIRE',
]


class AlienActions(BaseActions):
    NOOP = 'NOOP'
    FIRE = 'FIRE'
    UP = 'UP'
    RIGHT = 'RIGHT'
    LEFT = 'LEFT'
    DOWN = 'DOWN'
    UPRIGHT = 'UPRIGHT'
    UPLEFT = 'UPLEFT'
    DOWNRIGHT = 'DOWNRIGHT'
    DOWNLEFT = 'DOWNLEFT'
    UPFIRE = 'UPFIRE'
    RIGHTFIRE = 'RIGHTFIRE'
    LEFTFIRE = 'LEFTFIRE'
    DOWNFIRE = 'DOWNFIRE'
    UPRIGHTFIRE = 'UPRIGHTFIRE'
    UPLEFTFIRE = 'UPLEFTFIRE'
    DOWNRIGHTFIRE = 'DOWNRIGHTFIRE'
    DOWNLEFTFIRE = 'DOWNLEFTFIRE'

    @staticmethod
    def get_all_possible_actions():
        return [
            'NOOP', 'FIRE', 'UP', 'RIGHT', 'LEFT', 'DOWN',
            'UPRIGHT', 'UPLEFT', 'DOWNRIGHT', 'DOWNLEFT',
            'UPFIRE', 'RIGHTFIRE', 'LEFTFIRE', 'DOWNFIRE',
            'UPRIGHTFIRE', 'UPLEFTFIRE', 'DOWNRIGHTFIRE', 'DOWNLEFTFIRE',
        ]
