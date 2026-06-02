from classes.game_utils.base_game import BaseActions

# Object type -> (width, height) mapping.
# Values sourced from OCAtari RAM extraction (ocatari/ram/skiing.py).
# Tree/Mogul/Flag heights are variable in the RAM extractor (depend on y-position),
# so we use representative typical values observed during gameplay.
skiing_wh_dict = {
    'player': (10, 18),
    'tree': (16, 30),
    'mogul': (16, 7),
    'flag': (5, 14),
    'score': (6, 7),
    'clock': (6, 7),
}

# The skier's horizontal velocity changes with steering; vertical scroll is
# implicit (the world moves up).  15 px/frame is a conservative upper bound.
SKIING_MAX_ABS_VELOCITY = 15

SKIING_HISTORY_LENGTH = 100

SKIING_MAX_ABS_SIZE_CHANGE = 5

# ALE action names for Skiing.
# The skier can only steer left or right; FIRE has no effect.
SKIING_ACTIONS = ['NOOP', 'RIGHT', 'LEFT']


class SkiingActions(BaseActions):
    NOOP = 'NOOP'
    RIGHT = 'RIGHT'
    LEFT = 'LEFT'

    @staticmethod
    def get_all_possible_actions():
        return ['NOOP', 'RIGHT', 'LEFT']
