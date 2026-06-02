# Scripted action sequence for Assault used by make_observations.py.
#
# Purpose: provide a minimal scripted trajectory that exercises the core
# mechanics: cannon movement, vertical/horizontal missile firing, and
# exposure to enemy drones and the mother ship.
#
# Assault action vocabulary:
#   NOOP, FIRE (vertical missile), RIGHT, LEFT,
#   RIGHTFIRE (move right + fire), LEFTFIRE (move left + fire),
#   UP (rotate cannon for horizontal shot)
#
# NOTE: Assault features stochastic enemy spawning and bullet timing.
# A short scripted sequence can only capture limited dynamics.
# For richer training data, use `manual_control: true`.

assault_actions_basic1 = (
    ['NOOP'] * 5
    + ['FIRE'] * 3
    + ['NOOP'] * 3
    + ['RIGHT'] * 5
    + ['FIRE'] * 2
    + ['NOOP'] * 3
    + ['RIGHT'] * 5
    + ['RIGHTFIRE'] * 3
    + ['NOOP'] * 3
    + ['LEFT'] * 5
    + ['FIRE'] * 2
    + ['NOOP'] * 3
    + ['LEFT'] * 5
    + ['LEFTFIRE'] * 3
    + ['NOOP'] * 3
    + ['UP'] * 2
    + ['NOOP'] * 3
    + ['FIRE'] * 3
    + ['NOOP'] * 5
    + ['RIGHT'] * 4
    + ['FIRE'] * 2
    + ['RIGHT'] * 3
    + ['RIGHTFIRE'] * 2
    + ['NOOP'] * 4
    + ['LEFT'] * 8
    + ['LEFTFIRE'] * 2
    + ['NOOP'] * 4
    + ['FIRE'] * 3
    + ['NOOP'] * 4
    + ['RIGHT'] * 5
    + ['FIRE'] * 2
    + ['NOOP'] * 3
    + ['UP'] * 2
    + ['NOOP'] * 2
    + ['LEFT'] * 5
    + ['FIRE'] * 2
    + ['NOOP'] * 5
    + ['RIGHTFIRE'] * 3
    + ['NOOP'] * 3
    + ['LEFTFIRE'] * 3
    + ['NOOP'] * 5
    + ['FIRE'] * 3
    + ['NOOP'] * 10
)

# Human demonstration derived from Assault_manual.csv, frames 1500-2100 (600 steps).
assault_actions_basic2 = (
    ['NOOP'] * 23
    + ['UP'] * 4
    + ['NOOP'] * 4
    + ['UP'] * 2
    + ['NOOP'] * 4
    + ['UP'] * 3
    + ['NOOP'] * 3
    + ['UP'] * 2
    + ['NOOP'] * 11
    + ['UP'] * 4
    + ['NOOP'] * 6
    + ['UP'] * 3
    + ['NOOP'] * 3
    + ['UP'] * 2
    + ['NOOP'] * 3
    + ['UP'] * 2
    + ['NOOP'] * 4
    + ['UP']
    + ['NOOP'] * 11
    + ['UP'] * 2
    + ['NOOP'] * 3
    + ['UP'] * 3
    + ['NOOP'] * 3
    + ['UP'] * 2
    + ['NOOP'] * 3
    + ['UP'] * 2
    + ['NOOP'] * 3
    + ['UP'] * 2
    + ['NOOP'] * 5
    + ['UP'] * 2
    + ['NOOP'] * 4
    + ['UP'] * 2
    + ['NOOP'] * 4
    + ['UP']
    + ['NOOP'] * 4
    + ['UP'] * 2
    + ['NOOP'] * 3
    + ['UP'] * 3
    + ['NOOP'] * 2
    + ['UP'] * 3
    + ['NOOP'] * 3
    + ['UP'] * 2
    + ['NOOP'] * 4
    + ['UP'] * 3
    + ['NOOP'] * 9
    + ['RIGHT'] * 3
    + ['NOOP'] * 4
    + ['UP'] * 3
    + ['NOOP'] * 3
    + ['UP'] * 2
    + ['NOOP'] * 3
    + ['UP'] * 2
    + ['NOOP'] * 3
    + ['UP'] * 2
    + ['NOOP'] * 3
    + ['UP'] * 2
    + ['NOOP'] * 3
    + ['UP'] * 2
    + ['NOOP'] * 3
    + ['UP'] * 2
    + ['NOOP'] * 3
    + ['UP'] * 2
    + ['NOOP'] * 3
    + ['UP'] * 2
    + ['NOOP'] * 3
    + ['UP'] * 3
    + ['NOOP'] * 3
    + ['UP'] * 2
    + ['NOOP'] * 3
    + ['UP'] * 2
    + ['NOOP'] * 3
    + ['UP'] * 3
    + ['NOOP'] * 2
    + ['UP'] * 3
    + ['NOOP'] * 2
    + ['UP'] * 2
    + ['NOOP'] * 3
    + ['UP'] * 2
    + ['NOOP'] * 2
    + ['UP'] * 2
    + ['NOOP'] * 3
    + ['UP'] * 2
    + ['NOOP'] * 4
    + ['UP']
    + ['NOOP'] * 4
    + ['UP']
    + ['NOOP'] * 4
    + ['UP'] * 2
    + ['NOOP'] * 3
    + ['UP'] * 3
    + ['NOOP'] * 3
    + ['UP']
    + ['NOOP'] * 4
    + ['UP'] * 2
    + ['NOOP'] * 3
    + ['UP'] * 3
    + ['NOOP'] * 4
    + ['UP']
    + ['NOOP'] * 4
    + ['UP'] * 3
    + ['NOOP'] * 3
    + ['UP'] * 2
    + ['NOOP'] * 3
    + ['UP'] * 2
    + ['NOOP'] * 4
    + ['UP'] * 2
    + ['NOOP'] * 3
    + ['UP'] * 3
    + ['NOOP'] * 3
    + ['UP'] * 3
    + ['NOOP'] * 3
    + ['UP'] * 2
    + ['NOOP'] * 3
    + ['UP'] * 2
    + ['NOOP'] * 4
    + ['UP']
    + ['NOOP'] * 4
    + ['UP'] * 2
    + ['NOOP'] * 3
    + ['UP'] * 3
    + ['NOOP'] * 4
    + ['UP'] * 3
    + ['NOOP'] * 3
    + ['UP'] * 3
    + ['NOOP'] * 3
    + ['UP'] * 2
    + ['NOOP'] * 3
    + ['UP'] * 2
    + ['NOOP'] * 3
    + ['UP'] * 2
    + ['NOOP'] * 31
    + ['UP'] * 2
    + ['NOOP'] * 35
    + ['UP'] * 3
    + ['NOOP'] * 26
    + ['UP'] * 3
    + ['NOOP'] * 16
    + ['UP'] * 2
    + ['NOOP'] * 17
    + ['UP'] * 3
    + ['NOOP'] * 25
    + ['UP'] * 2
    + ['NOOP'] * 15
    + ['UP'] * 2
    + ['NOOP'] * 10
    + ['UP'] * 2
    + ['NOOP'] * 4
)
