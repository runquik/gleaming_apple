# 001 — Conway's Game of Life

A terminal-based implementation of [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life),
the classic cellular automaton.

## Rules

1. Any live cell with 2 or 3 live neighbors survives.
2. Any dead cell with exactly 3 live neighbors becomes alive.
3. All other live cells die. All other dead cells stay dead.

## Running

```bash
python3 life.py
```

### Options

```
python3 life.py --width 60 --height 30    # Custom grid size
python3 life.py --density 0.4             # Initial fill density (0.0-1.0)
python3 life.py --speed 0.1               # Seconds between frames
python3 life.py --pattern glider          # Start with a known pattern
python3 life.py --pattern pulsar
python3 life.py --pattern gosper-gun
```

Press `Ctrl+C` to stop.

## No Dependencies

Pure Python 3. Uses only the standard library.
