# Faded Journals - Simple HTML Game

A simple little HTML game that was developed to learn [Vue 3](https://v3.vuejs.org/), [Vue Router](https://router.vuejs.org/), [FastAPI](https://fastapi.tiangolo.com/), and [Axios](https://axios-http.com/).

# TOC

* [Game Goal](#game-goal)
* [Code Stack](#code-stack)
  - [Back-end](#back-end)
  - [Front-end](#front-end)
* [Port Usage](#port-usage-debug-recommended-setup)
  - [FastAPI](#fastapi-8000---api-for-front-end-to-access-database)
  - [Vite](#vite-3000---front-end-display)
* [Installation](#installation)

## Game Goal

* Simple to pick up and play
* Extremely responsive to user input
* Global player leaderboards
* Universal access across all platforms

## Code Stack

### Back-end

* `Python` - Backend base language
* `SQLAlchemy` - Database ORM
* `Vite 4` - Development auto-refresh
* `NPM` - Used to manage packages for JavaScript
* `FastAPI` - Python middleware for communicating between `Vue` and `Python`

### Front-end

* `Vue 3` - Front-end display
  * `Vue Router` - Single File Application routing for `Vue 3`
* `Axios` - API Middleware built in JavaScript to communicate with `FastAPI`
* [`NaiveUI`](https://www.naiveui.com/) - Vue3 UX plugin system
* [`Bulma`](https://bulma.io/) - CSS UI Framework

## Port Usage, Debug, Recommended Setup

### FastAPI (8000) - API for Front End to access Database

`python -m uvicorn main:app --reload`

### Vite (3000) - Front End display

`run dev --scripts-prepend-node-path=auto`

# Installation

1. Setup `venv`  
(*Run the remaining code in venv*)
2. Install Python Helpers - `pip install -r requirements.txt`
3. Run NPM Setup - `npm install`

---

# Database Schema

## Tables

| **Table Name** | **Definition**                                  |
|:---------------|:------------------------------------------------|
| author         | "Author" information (commonly known as users). |
| authorhistory  | Author login, logout, failure tracking.         |
| authorstatus   | Author status related information, counts, etc. |