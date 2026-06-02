# Scripted action sequence for Alien used by make_observations.py.
#
# Purpose: provide a minimal scripted trajectory that exercises the core
# object types (player movement, alien movement, egg collection, pulsar).
# This sequence is intentionally short.  For richer world-model training,
# prefer `manual_control: true` in the Hydra config to record a human
# demonstration (saved to saved_data/obs_manual_Alien<suffix>.pickle).
#
# Action vocabulary (18 ALE actions for Alien):
#   NOOP, FIRE, UP, RIGHT, LEFT, DOWN,
#   UPRIGHT, UPLEFT, DOWNRIGHT, DOWNLEFT,
#   UPFIRE, RIGHTFIRE, LEFTFIRE, DOWNFIRE,
#   UPRIGHTFIRE, UPLEFTFIRE, DOWNRIGHTFIRE, DOWNLEFTFIRE

alien_actions_basic1 = (
    ['NOOP'] * 10
    + ['RIGHT'] * 8
    + ['RIGHTFIRE'] * 4
    + ['NOOP'] * 5
    + ['LEFT'] * 8
    + ['LEFTFIRE'] * 4
    + ['NOOP'] * 5
    + ['UP'] * 6
    + ['UPFIRE'] * 3
    + ['NOOP'] * 5
    + ['DOWN'] * 6
    + ['NOOP'] * 5
    + ['UPRIGHT'] * 4
    + ['NOOP'] * 4
    + ['DOWNLEFT'] * 4
    + ['NOOP'] * 4
    + ['FIRE'] * 4
    + ['NOOP'] * 10
    + ['RIGHT'] * 6
    + ['NOOP'] * 4
    + ['RIGHTFIRE'] * 3
    + ['NOOP'] * 5
    + ['LEFT'] * 6
    + ['NOOP'] * 4
    + ['FIRE'] * 2
    + ['NOOP'] * 10
    + ['UP'] * 5
    + ['NOOP'] * 5
    + ['DOWN'] * 5
    + ['NOOP'] * 5
    + ['UPLEFT'] * 3
    + ['NOOP'] * 4
    + ['DOWNRIGHT'] * 3
    + ['NOOP'] * 4
    + ['FIRE'] * 3
    + ['NOOP'] * 10
)

# Human demonstration derived from Alien_manual.csv (1520 steps; use first 500
# steps only — avoids game-over ~520 under default seed).
_alien_actions_basic2_full = (
    ['NOOP'] * 29
    + ['LEFT'] * 10
    + ['NOOP'] * 2
    + ['RIGHT'] * 4
    + ['NOOP'] * 4
    + ['UP'] * 9
    + ['LEFT'] * 6
    + ['UP'] * 14
    + ['RIGHT'] * 8
    + ['NOOP'] * 3
    + ['LEFT'] * 31
    + ['DOWN'] * 12
    + ['RIGHT'] * 2
    + ['DOWN'] * 16
    + ['RIGHT'] * 15
    + ['UPRIGHT'] * 5
    + ['UP'] * 14
    + ['LEFT'] * 38
    + ['NOOP'] * 11
    + ['UP'] * 11
    + ['NOOP'] * 2
    + ['RIGHT'] * 31
    + ['NOOP'] * 8
    + ['RIGHT'] * 3
    + ['NOOP'] * 3
    + ['LEFT'] * 10
    + ['NOOP']
    + ['RIGHT'] * 4
    + ['NOOP'] * 6
    + ['UP'] * 10
    + ['LEFT'] * 4
    + ['NOOP'] * 7
    + ['UP'] * 2
    + ['NOOP'] * 5
    + ['RIGHT'] * 7
    + ['UPRIGHT']
    + ['UP'] * 7
    + ['UPRIGHT']
    + ['RIGHT'] * 11
    + ['NOOP'] * 3
    + ['UP'] * 5
    + ['NOOP']
    + ['LEFT'] * 35
    + ['LEFTFIRE'] * 6
    + ['LEFT'] * 3
    + ['LEFTFIRE'] * 3
    + ['LEFT']
    + ['NOOP']
    + ['RIGHT'] * 2
    + ['RIGHTFIRE'] * 3
    + ['RIGHT'] * 2
    + ['RIGHTFIRE'] * 2
    + ['RIGHT'] * 3
    + ['RIGHTFIRE'] * 3
    + ['RIGHT'] * 2
    + ['RIGHTFIRE'] * 2
    + ['RIGHT']
    + ['RIGHTFIRE'] * 4
    + ['RIGHT'] * 6
    + ['NOOP'] * 27
    + ['LEFT'] * 3
    + ['NOOP'] * 9
    + ['RIGHT'] * 3
    + ['NOOP'] * 3
    + ['UP'] * 6
    + ['LEFT'] * 17
    + ['DOWNLEFT']
    + ['DOWN'] * 10
    + ['NOOP'] * 4
    + ['RIGHT'] * 21
    + ['NOOP'] * 14
    + ['LEFT'] * 2
    + ['NOOP'] * 16
    + ['RIGHT'] * 22
    + ['NOOP']
    + ['DOWN'] * 6
    + ['NOOP']
    + ['RIGHT'] * 20
    + ['NOOP'] * 9
    + ['DOWN'] * 11
    + ['LEFT'] * 34
    + ['NOOP'] * 7
    + ['LEFT'] * 31
    + ['DOWN'] * 12
    + ['DOWNLEFT']
    + ['LEFT'] * 12
    + ['DOWN'] * 9
    + ['DOWNRIGHT']
    + ['RIGHT'] * 18
    + ['NOOP'] * 37
    + ['LEFT'] * 19
    + ['NOOP'] * 5
    + ['RIGHT'] * 4
    + ['NOOP'] * 3
    + ['UP'] * 6
    + ['NOOP']
    + ['LEFT'] * 9
    + ['UP'] * 13
    + ['NOOP'] * 3
    + ['RIGHT'] * 3
    + ['NOOP'] * 4
    + ['UP'] * 10
    + ['NOOP'] * 2
    + ['RIGHT'] * 16
    + ['LEFT'] * 32
    + ['DOWNLEFT']
    + ['DOWN'] * 15
    + ['DOWNRIGHT']
    + ['RIGHT'] * 6
    + ['DOWN'] * 9
    + ['NOOP']
    + ['RIGHT'] * 3
    + ['NOOP']
    + ['DOWN'] * 7
    + ['NOOP']
    + ['RIGHT'] * 21
    + ['DOWNRIGHT']
    + ['DOWN'] * 2
    + ['LEFT'] * 38
    + ['DOWN'] * 19
    + ['DOWNRIGHT']
    + ['RIGHT'] * 23
    + ['NOOP']
    + ['UP'] * 10
    + ['RIGHT'] * 24
    + ['UPRIGHT'] * 2
    + ['UP'] * 12
    + ['UPLEFT']
    + ['LEFT'] * 12
    + ['UPLEFT']
    + ['UP'] * 7
    + ['NOOP']
    + ['RIGHT'] * 33
    + ['NOOP'] * 17
    + ['LEFT'] * 15
    + ['NOOP']
    + ['DOWN'] * 7
    + ['NOOP']
    + ['RIGHT'] * 9
    + ['NOOP']
    + ['LEFT'] * 40
    + ['NOOP'] * 6
    + ['UP'] * 5
    + ['LEFT'] * 2
    + ['NOOP']
    + ['UP'] * 8
    + ['NOOP']
    + ['RIGHT'] * 29
    + ['NOOP'] * 43
    + ['LEFT'] * 2
    + ['NOOP'] * 2
    + ['UP'] * 8
    + ['NOOP']
    + ['RIGHT'] * 4
    + ['NOOP'] * 4
    + ['UP'] * 9
    + ['LEFT'] * 17
    + ['DOWNLEFT'] * 2
    + ['DOWN'] * 17
    + ['NOOP'] * 61
)

alien_actions_basic2 = _alien_actions_basic2_full[:500]
