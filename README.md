# MTG Deck Builder App (Python Desktop App)

## Overview

Desktop application for managing a Magic: The Gathering card collection and generating decks from owned cards using rule-based logic and optional LLM assistance (GPT/Claude).

The system is designed to run locally as a packaged desktop application.

---

## Core Goals

- Manage a personal MTG card collection
- Search cards via external MTG API (e.g. Scryfall / mtg.io)
- Store cards locally in a database
- Build decks from owned cards
- Generate deck suggestions using LLMs (optional)
- Package into a desktop installer (Windows/macOS)

---

## Architecture

---

## Project Structure
mtg-deck-app/

## Project Structure

```text
mtg-deck-app/
├── app/
│   ├── ui/            # PySide6 desktop UI (windows, screens)
│   ├── core/          # Business logic (deck rules, validation)
│   ├── db/            # Database models + session setup
│   ├── services/      # External APIs (MTG + LLM)
│
├── tests/             # Unit + integration tests
├── main.py            # Application entry point
├── requirements.txt
└── README.md
```

---

## Module Responsibilities

### UI Layer (`app/ui`)
- Desktop interface built with PySide6
- Displays:
  - Card search
  - Collection management
  - Deck builder interface
- Sends user actions to core layer
- Must NOT directly access DB or APIs

---

### Core Layer (`app/core`)
- Implements deck-building logic
- Validates rules (format legality, card counts)
- Converts API data into application models
- Builds prompts for LLM deck generation
- Must NOT directly access UI or DB

---

### Database Layer (`app/db`)
- SQLite database via SQLAlchemy
- Stores:
  - Users
  - Card collection
  - Decks
  - Deck contents
- Responsible only for persistence

---

### Services Layer (`app/services`)
- Handles external API communication:
  - MTG card API (search + metadata)
  - LLM API (GPT / Claude deck generation)
- Normalizes external responses into internal formats
- No UI or database logic allowed

---

### Entry Point (`main.py`)
- Starts application
- Initializes database
- Launches UI
- Keeps logic minimal

---

## Data Model (High Level)

### User
- id
- username
- password hash

### Card
- id
- user_id
- name
- mtg_api_id
- quantity
- metadata (JSON)

### Deck
- id
- user_id
- name
- created_at

### DeckCard
- deck_id
- card_name
- quantity

---

## External Integrations

### MTG API
Used for:
- Searching cards
- Fetching card metadata
- Filtering by attributes (color, mana cost, type)

Example use:
- Search: “Lightning Bolt”
- Filter: Red instants under 2 mana

---

### LLM API (GPT / Claude)

Used for:
- Deck generation suggestions
- Strategy recommendations
- Deck structure optimization

Important constraint:
- LLM only receives user's owned cards
- Output must be validated before saving

---

## Deck Generation Flow

1. User selects deck parameters (format, style, constraints)
2. App fetches user’s card collection from DB
3. Core layer builds structured payload
4. Payload sent to LLM API
5. LLM returns deck suggestion (JSON format)
6. App validates:
   - Cards exist in collection
   - Quantity limits respected
7. Deck saved to database

---

## Testing Strategy

### Unit Tests
- Deck building logic
- Card filtering
- Prompt generation
- Validation rules

### Integration Tests
- Database operations
- API response handling

External APIs should be mocked in tests.

---

## Packaging (Desktop App)

Planned approach:
- PyInstaller (initial version)

Output:
- Windows `.exe` installer
- macOS `.app` bundle (future)

---

## Key Rules

- UI does not contain business logic
- Core layer is independent and testable
- Services layer isolates external APIs
- Database layer only stores/retrieves data
- LLM is assistive, never authoritative

---

## Future Improvements

- Cloud sync of collections
- Deck sharing system
- Multi-format support (Commander, Standard, etc.)
- Advanced deck optimization algorithms
- Real-time card pricing integration