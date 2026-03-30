# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A Flask single-page application that randomly draws fruits ("明天吃什么水果") and displays nutritional information. Chinese-language interface with 20 fruits.

## Running

```bash
pip install flask
python app.py
# App runs on http://0.0.0.0:5001
```

No tests, no build step. Test the API directly:
```bash
curl http://localhost:5001/draw
```

## Architecture

**Single-file Flask backend** (`app.py`):
- `/` renders `templates/index.html` passing the full `FRUITS` dict
- `/draw` returns a random fruit as JSON `{"name": "...", "data": {...}}`
- All fruit data is hardcoded in the `FRUITS` dict (20 entries) with calories, vitamin_c, fiber, sugar, best_time, amount, color, nutrition fields

**Single-file frontend** (`templates/index.html`):
- Server-rendered via Jinja2 loop for fruit cards, then JavaScript handles:
  - `fruitEmojis` map: fruit name → emoji character
  - `fruitImages` map: fruit name → SVG path (for fruits without suitable emojis: 石榴, 山竹, 火龙果, 荔枝)
  - `setFruitDisplay(element, fruitName, size)`: renders either an `<img>` or emoji text depending on whether the fruit has an SVG
  - Draw animation cycles through random fruits, then calls `/draw` for the result
  - Audio plays during draw animation

**Static assets** (`static/`):
- `style.css` — all styling with CSS variables, gradients, responsive breakpoints
- `images/` — SVG icons for fruits lacking Unicode emojis

## Conventions

- Fruit names are Chinese strings used as dictionary keys throughout backend and frontend
- Each fruit has a `color` hex value used for card border theming
- Frontend has no build tools or frameworks — vanilla JS only
- No database; all data lives in `app.py`
