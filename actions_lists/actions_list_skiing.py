# Scripted action sequence for Skiing used by make_observations.py.
#
# Purpose: provide a minimal scripted trajectory that exercises the steering
# mechanics: left/right turns and straight skiing (NOOP).  The world model
# will focus on player physics (turning inertia, speed decay) which are fully
# deterministic given the action; obstacle (tree/mogul/flag) appearance is
# procedurally generated and is harder to model precisely.
#
# Skiing action vocabulary: NOOP, RIGHT, LEFT
#
# For richer training data, use `manual_control: true` to record a human run.

skiing_actions_basic1 = (
    ['NOOP'] * 10
    + ['RIGHT'] * 5
    + ['NOOP'] * 5
    + ['LEFT'] * 5
    + ['NOOP'] * 5
    + ['RIGHT'] * 8
    + ['NOOP'] * 3
    + ['LEFT'] * 8
    + ['NOOP'] * 5
    + ['RIGHT'] * 4
    + ['LEFT'] * 4
    + ['NOOP'] * 4
    + ['RIGHT'] * 6
    + ['NOOP'] * 6
    + ['LEFT'] * 6
    + ['NOOP'] * 6
    + ['RIGHT'] * 3
    + ['NOOP'] * 4
    + ['LEFT'] * 3
    + ['NOOP'] * 4
    + ['RIGHT'] * 5
    + ['LEFT'] * 5
    + ['NOOP'] * 8
    + ['RIGHT'] * 4
    + ['NOOP'] * 4
    + ['LEFT'] * 4
    + ['NOOP'] * 4
    + ['RIGHT'] * 3
    + ['LEFT'] * 3
    + ['NOOP'] * 10
)

# Human demonstration derived from Skiing_manual.csv, first 500 steps.
skiing_actions_basic2 = (
    ['NOOP'] * 35
    + ['RIGHT'] * 3
    + ['NOOP'] * 20
    + ['LEFT'] * 5
    + ['NOOP'] * 25
    + ['LEFT'] * 3
    + ['NOOP'] * 46
    + ['RIGHT'] * 3
    + ['NOOP'] * 49
    + ['RIGHT'] * 3
    + ['NOOP'] * 51
    + ['LEFT'] * 4
    + ['NOOP'] * 83
    + ['LEFT'] * 10
    + ['NOOP'] * 48
    + ['LEFT'] * 4
    + ['NOOP'] * 21
    + ['RIGHT'] * 4
    + ['NOOP'] * 59
    + ['RIGHT'] * 4
    + ['NOOP'] * 20
)
