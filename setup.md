# Project Setup Guide

This guide explains how to clone and run the project from scratch.
There are several steps including installing requirements which should be followed

---

## 1. Clone the Repository
Open terminal and enter: 
```bash
git clone https://github.com/Clathamr/MTG_Deck_Builder.git
cd <repo>
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

### Activate environment

**Windows (PowerShell):**
```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Enable Pre-Commit Hooks (required for commits)

```bash
pre-commit install
pre-commit install --hook-type commit-msg
```

Run once to ensure everything is working:

```bash
pre-commit run --all-files
```

---

## 5. Code Quality Rules

### Formatting (Black)
Automatically formats all Python code.

### Linting (Ruff)
Checks for:
- Code errors
- Bad practices
- Unused imports
- Style issues

### Commit Rules (Conventional Commits)
Docs: https://www.conventionalcommits.org/en/v1.0.0/

All commit messages must follow the below patter (note the use of present tense):

```text
feat: add new feature
fix: resolve bug
chore: update dependencies
docs: update documentation
```

Commits that do not follow this format will be blocked automatically.