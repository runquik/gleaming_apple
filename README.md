# The Experiment Lab

A gallery of small, interactive experiments you can play with in your browser.

**[Visit the site](https://runquik.github.io/gleaming_apple/)**

## Experiments

| # | Name | Description |
|---|------|-------------|
| 001 | [Game of Life](experiments/001-game-of-life/) | Conway's cellular automaton — click to draw, watch it evolve |

## How This Repo Works

- **Each experiment gets a numbered directory** under `experiments/`.
- **Each experiment is self-contained** — its own HTML page, its own world.
- **The gallery** at `index.html` links to every experiment with a live preview.
- **No build step.** Pure HTML, CSS, and JS. Open any `index.html` in a browser and it works.
- **Deployable to GitHub Pages** with zero configuration.

## Running Locally

Clone the repo and open `index.html` in your browser, or use any static file server:

```bash
# Python
python3 -m http.server 8000

# Node
npx serve .
```

## Ideas Backlog

Things we might build next:

- [ ] Mandelbrot set renderer
- [ ] Markov chain text generator
- [ ] Maze solver visualizer
- [ ] Tiny ray tracer
- [ ] Langton's Ant simulation
- [ ] Sorting algorithm visualizer
- [ ] Generative art with Canvas

---

*Built by a human and an AI, one experiment at a time.*
