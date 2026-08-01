# Custom AI Systems Website

This repository contains a first-draft website for a custom AI systems and consulting company. The site presents the company's workflow-first approach, connected system capabilities, civil engineering use case, and human review model.

The site remains intentionally lightweight: static HTML pages with one shared stylesheet and interaction script. There is no install step, build step, package manager, or framework.

## How Conductor Uses This Project

Conductor creates each workspace as its own git worktree and branch. The checked-in `.conductor/settings.toml` tells Conductor how to prepare and run this starter app:

```toml
"$schema" = "https://conductor.build/schemas/settings.repo.schema.json"

[scripts]
setup = "true"
run = "python3 dev_server.py"
run_mode = "concurrent"
```

When you create a workspace, setup succeeds immediately. When you click Run, Conductor serves the website on the port assigned to that workspace.

## Local Development

Start a local server:

```sh
CONDUCTOR_PORT=8000 python3 dev_server.py
```

Open `http://127.0.0.1:8000/` in a browser. Edit `index.html`, then refresh the page.

## Project Structure

- `index.html` contains the home page, live workflow example, capability system, controlled-data sequence, and offer overview.
- `services.html`, `industries.html`, `enterprise.html`, and `about.html` cover the core offer and company model.
- `included.html` and `faq.html` contain detailed scope and buying questions.
- `readiness.html` and `roi.html` contain the interactive AI readiness diagnostic and directional ROI calculator.
- `contact.html` contains the three-step project inquiry.
- `site.css` contains the shared responsive visual system, product mockups, and motion states.
- `site.js` contains navigation, generated ASCII fields, product-demo motion, tab systems, quiz scoring, ROI calculations, contact steps, and scroll behavior.
- `dev_server.py` serves the local preview with caching disabled so design iterations cannot mix old CSS or JavaScript with new HTML.
- `public/fonts/` contains the locally served Geist typeface and its license note.
- `.conductor/settings.toml` contains the shared Conductor workspace scripts.
- `.context/` is available in Conductor workspaces for gitignored notes and handoff files between agents.

## Learn More

- [Conductor docs](https://conductor.build/docs)
