# PoE-World Extended: Alien, Assault, and Skiing

> **Fork of [topwasu/poe-world](https://github.com/topwasu/poe-world)** — adds three OCAtari games
> (Alien, Assault, Skiing) on top of the original PoE-World baseline for comparative world-model
> evaluation. For the original paper, base-game instructions (Pong, MontezumaRevenge, Pitfall,
> Breakout), and citation, see **[UPSTREAM_README.md](UPSTREAM_README.md)**.

This document explains **what was added**, **why**, and **how to run** the three new games.

---

## Background

[PoE-World](https://arxiv.org/abs/2505.10819) originally supports four Atari games:
MontezumaRevenge, Pong, Pitfall, and Breakout. This extension adds three games from the OCAtari
suite to serve as additional baselines and evaluation environments for a comparative study.

The three games were chosen because they cover a spectrum of **environment stochasticity**:

| Game | Key stochasticity | WM focus |
|---|---|---|
| **Alien** | Enemy tracking + random respawn | Player dynamics + alien patrol |
| **Assault** | Random bullet timing + enemy spawn | Player cannon movement |
| **Skiing** | Procedural obstacle generation | Skier physics (turning inertia) |

---

## Files Changed / Added

### New files

| File | Purpose |
|---|---|
| `classes/game_utils/alien.py` | Object size dict (`alien_wh_dict`), velocity constants, `AlienActions` enum |
| `classes/game_utils/assault.py` | Object size dict (`assault_wh_dict`), velocity constants, `AssaultActions` enum |
| `classes/game_utils/skiing.py` | Object size dict (`skiing_wh_dict`), velocity constants, `SkiingActions` enum |
| `actions_lists/actions_list_alien.py` | Short scripted action sequence (`alien_actions_basic1`) |
| `actions_lists/actions_list_assault.py` | Short scripted action sequence (`assault_actions_basic1`) |
| `actions_lists/actions_list_skiing.py` | Short scripted action sequence (`skiing_actions_basic1`) |
| `conf/alien.yaml` | Hydra config override for Alien |
| `conf/assault.yaml` | Hydra config override for Assault |
| `conf/skiing.yaml` | Hydra config override for Skiing |

### Modified files

| File | Change |
|---|---|
| `classes/game_utils/__init__.py` | Export three new game_utils modules |
| `actions_lists/__init__.py` | Export three new action sequence modules |
| `classes/helper.py` | Add `elif` branches in `set_global_constants` for Alien / Assault / Skiing |
| `classes/envs/env.py` | Add `elif` branches in `create_atari_env` for the three new games; add game names to the `AtariEnv.__init__` allowlist |
| `make_observations.py` | Add `elif` branches in `main` for the three new games |

---

## Installation

Follow the steps in [UPSTREAM_README.md](UPSTREAM_README.md) (conda env, submodules, API keys).
No extra dependencies are required beyond the upstream setup.

---

## Why Each Design Decision Was Made

### 1. `GenericGameStateTracker` for all three games

PoE-World has custom `GameStateTracker` subclasses for Montezuma (life-loss detection via
RAM byte 112) and Pong (win/loss detection). The three new games do not require this
level of custom tracking for **world-model training** — the WM synthesizer only needs
`NORMAL` / `RESTART` signals. `GenericGameStateTracker` always returns `NORMAL`, which
is sufficient.

If you later want to enable agent-mode planning that tracks lives (e.g. for Alien), you
can implement a dedicated `AlienStateTracker` mirroring the Montezuma pattern.

### 2. `obj_type: player` as default in Hydra configs

The PoE-World baseline already defaults to `obj_type: player` for MontezumaRevenge
(see `conf/config.yaml`). Player dynamics are fully **deterministic** given the action
sequence, making them the most reliably learnable part of the world model.

Enemy / obstacle objects introduce stochasticity (random respawn in Alien, bullet timing
in Assault, procedural tree generation in Skiing) that degrades WM accuracy. Starting
with `player` only is therefore the scientifically fair baseline comparison point.

To attempt full-scene modelling, override with `world_model_learner.obj_type: all`.

### 3. `frameskip=3` for Alien, `frameskip=1` for Assault and Skiing

- **Alien** is a platform action game similar to MontezumaRevenge: frameskip 3 is the
  same value used by the original baseline and matches standard ALE evaluation practice.
- **Assault** and **Skiing** have faster-moving objects (missiles, scroll) where
  frameskip 3 would skip important intermediate states. Using frameskip 1 preserves
  finer-grained transition data for the synthesizer.

### 4. Short scripted sequences in `actions_list_*.py`

The original PoE-World provides scripted sequences of ~500–1500 actions for
MontezumaRevenge (to reach the first key) and Pong (full rally). For the three new
games, short generic sequences are provided as a **quick-start scaffold**. Their purpose
is to verify the pipeline end-to-end, not to produce a production-quality WM.

**For paper-quality results, always use `manual_control: true`** to record a human
demonstration that covers the diverse object states the WM needs to learn from.

---

## How to Run

### Step 1 — Collect observations (scripted)

```bash
# Alien (scripted)
python make_observations.py --config-name=alien

# Assault (scripted)
python make_observations.py --config-name=assault

# Skiing (scripted)
python make_observations.py --config-name=skiing
```

Output: `saved_data/obs_Alien_basic1.pickle`, `obs_Assault_basic1.pickle`,
`obs_Skiing_basic1.pickle`.

### Step 1 (alternative) — Collect observations (manual)

For a richer training set, record a human playthrough interactively:

```bash
python make_observations.py --config-name=alien manual_control=true
# Play the game in the window that opens. Close the window to save.
# Output: saved_data/obs_manual_Alien<obs_suffix>.pickle
```

Repeat for Assault and Skiing by changing the config name.

### Step 2 — Synthesize the World Model

```bash
# Alien
python run.py --config-name=alien

# Assault
python run.py --config-name=assault

# Skiing
python run.py --config-name=skiing
```

The synthesizer calls the LLM configured in `conf/config.yaml` (`provider`, `llm_model`)
and saves checkpoints to `saved_checkpoints_<task><obs_suffix>/`.

### Step 3 — Change the obs_suffix if using manual data

If you recorded a manual trajectory in Step 1, update the config to match:

```bash
python run.py --config-name=alien obs_suffix=_manual
```

### Optional — Model all object types

```bash
python run.py --config-name=alien world_model_learner.obj_type=all
```

This instructs PoE-World to synthesize expert programs for every object class
(alien, pulsar, egg, …) in addition to the player. Expect lower accuracy for
stochastically-created objects but richer rule coverage.

---

## Object Type Reference

### Alien (`ALE/Alien-v5`)

| Category | Width | Height | Notes |
|---|---|---|---|
| `player` | 6 | 13 | The astronaut |
| `alien` | 8 | 13 | Up to 3 enemies; can track player |
| `pulsar` | 7 | 5 | Alien projectile |
| `egg` | 1 | 2 | Collectible; up to 156 on screen |
| `score` | 6 | 7 | HUD element (excluded by default) |
| `life` | 5 | 5 | HUD element (excluded by default) |

### Assault (`ALE/Assault-v5`)

| Category | Width | Height | Notes |
|---|---|---|---|
| `player` | 8 | 8 | The ground cannon |
| `playermissilevertical` | 1 | 8 | Player's vertical shot |
| `playermissilehorizontal` | 4 | 2 | Player's horizontal shot |
| `mothership` | 32 | 16 | Top of screen; deploys enemies |
| `enemy` | 16 | 8 | Up to 9 enemy drones |
| `enemymissile` | 1 | 6 | Enemy projectile |

### Skiing (`ALE/Skiing-v5`)

| Category | Width | Height | Notes |
|---|---|---|---|
| `player` | 10 | 18 | The skier |
| `tree` | 16 | 30 | Procedurally generated obstacle |
| `mogul` | 16 | 7 | Snow bump; variable height |
| `flag` | 5 | 14 | Gate pole; variable height |

---

## Known Limitations

1. **Stochastic object creation**: Assault bullet timing and Skiing tree positions are
   procedurally random. The PoE-World synthesizer can generate creation rules but their
   predictive accuracy will be lower than for deterministic games.
2. **`GenericGameStateTracker`**: Life-loss events in Alien are not explicitly signalled
   to the WM. If a life-loss causes an abrupt object-list reset, the WM may see it as
   a spurious transition. A dedicated `AlienStateTracker` would fix this.
3. **Short scripted sequences**: The bundled `*_actions_basic1` sequences are short by
   design. Replace them with human-recorded trajectories for production experiments.

---

## Citation

If you use the original PoE-World method, please cite the upstream paper (see
[UPSTREAM_README.md](UPSTREAM_README.md)).
