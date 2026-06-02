from classes.game_utils.base_game import BaseActions

# Object type -> (width, height) mapping.
# Values sourced from OCAtari RAM extraction (ocatari/ram/assault.py).
# Category names are lowercase class names as returned by OCAtari objects.
assault_wh_dict = {
    'player': (8, 8),
    'playermissilevertical': (1, 8),
    'playermissilehorizontal': (4, 2),
    'mothership': (32, 16),
    'enemy': (16, 8),
    'enemymissile': (1, 6),
    'playerscore': (6, 8),
    'lives': (8, 8),
    'health': (8, 8),
}

# Assault enemies and missiles can move quickly on screen.
ASSAULT_MAX_ABS_VELOCITY = 20

ASSAULT_HISTORY_LENGTH = 100

ASSAULT_MAX_ABS_SIZE_CHANGE = 1

# ALE action names used by poe-world for Assault.
# Assault is a fixed-screen shooter: the player cannon moves left/right and
# fires vertically; horizontal missiles require left/right fire combos.
ASSAULT_ACTIONS = [
    'NOOP', 'FIRE', 'UP', 'RIGHT', 'LEFT', 'RIGHTFIRE', 'LEFTFIRE',
]


class AssaultActions(BaseActions):
    NOOP = 'NOOP'
    FIRE = 'FIRE'
    RIGHT = 'RIGHT'
    LEFT = 'LEFT'
    RIGHTFIRE = 'RIGHTFIRE'
    LEFTFIRE = 'LEFTFIRE'
    UP = 'UP'

    @staticmethod
    def get_all_possible_actions():
        return ['NOOP', 'FIRE', 'UP', 'RIGHT', 'LEFT', 'RIGHTFIRE', 'LEFTFIRE']
