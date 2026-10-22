# MediaShelf — Project Description & Reference Guide

> A command-line tool to catalog, search, rate, and analyze a personal collection of books, movies, and albums. Built as a hands-on refresher for Python, Git/GitHub, and the Linux shell, and finished as a portfolio-ready GitHub repository.

|||
|---|---|
|**Project name**|MediaShelf|
|**Owner / Developer**|You|
|**Duration**|12 working days (flexible within 1–2 weeks)|
|**Primary goal**|Re-learn and apply Python, Git, GitHub, and shell skills in one coherent project|
|**Secondary goal**|Produce a polished GitHub portfolio piece|
|**Deliverable**|Public GitHub repository tagged `v1.0`|
|**Document status**|Living document. Tick boxes and add notes as you go|

---

## Table of Contents

1. [Project Charter](#1-project-charter)
2. [Scope](#2-scope)
3. [Functional Requirements](#3-functional-requirements)
4. [Non-Functional Requirements](#4-non-functional-requirements)
5. [Architecture & Repository Layout](#5-architecture--repository-layout)
6. [Data Model](#6-data-model)
7. [Module Specifications](#7-module-specifications)
8. [CLI Specification](#8-cli-specification)
9. [Data Formats](#9-data-formats)
10. [Git & GitHub Workflow](#10-git--github-workflow)
11. [Shell Scripts Specification](#11-shell-scripts-specification)
12. [Concept Coverage Matrix](#12-concept-coverage-matrix)
13. [Day-by-Day Execution Plan](#13-day-by-day-execution-plan)
14. [Milestones & Checkpoints](#14-milestones--checkpoints)
15. [Quality Assurance & Testing](#15-quality-assurance--testing)
16. [Risk Register](#16-risk-register)
17. [Definition of Done](#17-definition-of-done)
18. [README Template](#18-readme-template)
19. [Stretch Goals](#19-stretch-goals)
20. [Working Agreements (Rules for Yourself)](#20-working-agreements-rules-for-yourself)
21. [Appendices](#21-appendices)

---

## 1. Project Charter

### 1.1 Problem statement

You have books you've read, movies you've watched, and albums you love, but no single place to track them, rate them, or ask questions like _"What are my top-rated sci-fi items?"_ or _"What should I enjoy next?"_

### 1.2 Vision

A fast, friendly, offline command-line application that manages a personal media library with search, filtering, sorting, statistics, and import/export, plus shell scripts for backup and reporting.

### 1.3 Learning objectives

By the end of the project you will have **applied, not just read about**:

- **Python fundamentals**: variables, numbers, strings, f-strings, booleans, type conversion
- **Control flow**: conditionals and loops
- **Functions**: parameters, return values, default arguments, scope, `*args`, `**kwargs`, lambdas
- **Data structures**: lists, tuples, sets, dictionaries, slicing, sorting, comprehensions
- **Text and files**: string methods, `pathlib`, context managers, JSON, CSV
- **Robustness**: exception handling and custom exception classes
- **OOP**: classes and inheritance
- **Git**: init, add, commit, branch, merge, rebase, conflict resolution, `.gitignore`
- **GitHub**: remotes, pull requests, code review, clear commit messages
- **Shell**: navigation, `chmod`, `grep`, `awk`, `sed`, `find`, pipes, redirection

### 1.4 Success criteria

|#|Criterion|How it's measured|
|---|---|---|
|1|The app runs end to end|`python main.py` launches the menu and every option works|
|2|Every listed concept is used|All rows in the [Concept Coverage Matrix](#12-concept-coverage-matrix) are ticked|
|3|Git workflow is demonstrated|≥3 feature branches, ≥3 merged PRs, ≥1 resolved conflict, ≥1 rebase|
|4|Shell skills are demonstrated|Both scripts run and use every required tool|
|5|Repo is portfolio-ready|README, sample data, clean history, tagged release|

### 1.5 Assumptions

- Python 3.10+ is installed (`python --version`).
- You are working in a Linux/macOS terminal, or WSL on Windows.
- Git is installed and you have a GitHub account.
- No third-party Python libraries are required (standard library only).

### 1.6 Constraints

- **Standard library only.** This keeps the focus on core Python.
- **No databases.** Persistence is JSON (primary) and CSV (import/export).
- **Single user, offline.** No networking.

---

## 2. Scope

### 2.1 In scope

- Three media types: **Book**, **Movie**, **Album**
- Add, view, edit, delete, rate, and change status
- Search, filter, sort, paginate
- Statistics and simple recommendations
- JSON persistence; CSV import/export
- Shell scripts for backup and reporting
- Git/GitHub workflow with PRs and code review
- Documentation (README, docstrings, this reference)

### 2.2 Out of scope (for v1.0)

- Graphical or web interface
- External APIs (e.g., fetching metadata from IMDb)
- Multi-user accounts
- Cloud sync

### 2.3 Stakeholders

|Role|Who|Interest|
|---|---|---|
|Developer / Product owner|You|Learning and a strong portfolio|
|Reviewer|Friend, mentor, or online community|Code review on PRs|
|Future viewer|Recruiters / peers visiting your GitHub|Clear, working, well-documented project|

---

## 3. Functional Requirements

Priorities: **M** = Must have, **S** = Should have, **C** = Could have.

### 3.1 Library management

|ID|Requirement|Priority|
|---|---|---|
|FR-01|Add a Book (title, author, year, genres, pages, rating, status)|M|
|FR-02|Add a Movie (title, director, year, genres, runtime, rating, status)|M|
|FR-03|Add an Album (title, artist, year, genres, tracklist, rating, status)|M|
|FR-04|Reject duplicates (same type + title + year) with a clear error|M|
|FR-05|Edit any field of an existing item|S|
|FR-06|Delete an item by ID, with confirmation|M|
|FR-07|Assign each item a unique, auto-incrementing integer ID|M|
|FR-08|Record the date added (ISO format `YYYY-MM-DD`)|M|

### 3.2 Rating and status

|ID|Requirement|Priority|
|---|---|---|
|FR-09|Ratings are numbers from 0.0 to 5.0 (half-points allowed); reject others|M|
|FR-10|Status is one of `to-do`, `in-progress`, `finished`|M|
|FR-11|Unrated items store `None` and are excluded from averages|M|

### 3.3 Search, filter, sort

|ID|Requirement|Priority|
|---|---|---|
|FR-12|Case-insensitive title search (substring match)|M|
|FR-13|Filter by type, genre, status, minimum rating, year range|M|
|FR-14|Combine multiple filters in a single call|M|
|FR-15|Sort by title, year, rating, or date added; ascending or descending|M|
|FR-16|Paginate listings (e.g., 10 per page)|S|

### 3.4 Statistics and insights

|ID|Requirement|Priority|
|---|---|---|
|FR-17|Total counts per type and per status|M|
|FR-18|Average rating overall and per type|M|
|FR-19|Count of items per genre|M|
|FR-20|Top 5 rated items; 3 most recently added|M|
|FR-21|"Recommend next": to-do items sharing the most genres with a chosen favorite|S|

### 3.5 Persistence and interchange

|ID|Requirement|Priority|
|---|---|---|
|FR-22|Auto-save to `data/library.json` after every change|M|
|FR-23|Load library at startup; create an empty one if the file is missing|M|
|FR-24|Handle a corrupted JSON file without crashing (message + safe fallback)|M|
|FR-25|Export the library to CSV|M|
|FR-26|Import items from CSV, skipping invalid rows and reporting them|S|

### 3.6 Shell tooling

|ID|Requirement|Priority|
|---|---|---|
|FR-27|`backup.sh` creates a timestamped backup and lists backups older than 7 days|M|
|FR-28|`report.sh` produces a text report from the CSV export using `grep`, `awk`, `sed`, and pipes|M|

---

## 4. Non-Functional Requirements

|ID|Category|Requirement|
|---|---|---|
|NFR-01|Usability|Every prompt explains valid input; invalid input re-prompts instead of crashing|
|NFR-02|Reliability|No unhandled exceptions reach the user; all errors produce a friendly message|
|NFR-03|Maintainability|Code split into modules with single responsibilities; functions under ~30 lines where practical|
|NFR-04|Readability|Docstrings on every module, class, and function; consistent naming (PEP 8)|
|NFR-05|Portability|Uses `pathlib` for all paths; no hard-coded OS-specific separators|
|NFR-06|Privacy|Personal data is never committed to Git|
|NFR-07|Documentation|README lets a stranger install and use the app in under 5 minutes|

---

## 5. Architecture & Repository Layout

### 5.1 Layered design

```
┌─────────────────────────────┐
│  cli.py  (user interaction) │  input(), print(), menus, validation prompts
├─────────────────────────────┤
│  library.py (business logic)│  add/search/filter/sort/stats/recommend
├─────────────────────────────┤
│  models.py (domain objects) │  MediaItem → Book, Movie, Album
├─────────────────────────────┤
│  storage.py (persistence)   │  JSON + CSV via pathlib
└─────────────────────────────┘
        exceptions.py  (shared by all layers)
```

**Rule:** each layer only talks to the layer directly below it. `cli.py` never touches files; `storage.py` never prints.

### 5.2 Repository layout

```
mediashelf/
├── README.md
├── .gitignore
├── main.py                      # entry point: calls cli.run()
├── mediashelf/
│   ├── __init__.py
│   ├── exceptions.py            # custom exception hierarchy
│   ├── models.py                # MediaItem, Book, Movie, Album
│   ├── storage.py               # JSON/CSV read & write
│   ├── library.py               # Library class: logic and stats
│   └── cli.py                   # menu loop and formatted I/O
├── data/
│   └── sample_library.json      # committed demo data
│   # library.json               # YOUR data: git-ignored
├── exports/                     # generated CSVs: git-ignored
├── backups/                     # generated backups: git-ignored
├── scripts/
│   ├── backup.sh
│   └── report.sh
└── docs/
    └── PROJECT_DESCRIPTION.md   # this file
```

### 5.3 `.gitignore` (required contents)

```
__pycache__/
*.pyc
.venv/
venv/
.vscode/
.idea/
.DS_Store
data/library.json
exports/
backups/
*.log
```

---

## 6. Data Model

### 6.1 Class hierarchy

```
MediaItem (base)
├── Book
├── Movie
└── Album

Exception
└── MediaShelfError
    ├── ItemNotFoundError
    ├── DuplicateItemError
    ├── InvalidRatingError
    ├── InvalidStatusError
    └── StorageError
```

### 6.2 `MediaItem` (base class) fields

|Field|Type|Notes|
|---|---|---|
|`item_id`|`int`|Unique, assigned by `Library`|
|`title`|`str`|Required; stripped; stored as entered, compared lowercase|
|`year`|`int`|1000–current year|
|`genres`|`set[str]`|Lowercase, stripped|
|`rating`|`float` or `None`|0.0–5.0 in 0.5 steps|
|`status`|`str`|`to-do` / `in-progress` / `finished`|
|`date_added`|`str`|ISO date|

### 6.3 Subclass-specific fields

|Class|Extra fields|
|---|---|
|`Book`|`author: str`, `pages: int`|
|`Movie`|`director: str`, `runtime_minutes: int`|
|`Album`|`artist: str`, `tracks: tuple[str, ...]`|

### 6.4 Required methods (design guide)

|Method|Purpose|
|---|---|
|`__init__(self, title, year, genres=None, rating=None, status="to-do", **kwargs)`|Base constructor; subclasses call `super().__init__(...)`|
|`to_dict(self) -> dict`|Serialize (convert `set` → sorted `list`, `tuple` → `list`)|
|`from_dict(cls, data) -> MediaItem`|Class method to rebuild an item|
|`describe(self) -> str`|Subclass-specific one-line description (**polymorphism**)|
|`__str__` / `__repr__`|Readable and debug-friendly output|
|`__eq__`|Duplicate check by `(type, title.lower(), year)`|

---

## 7. Module Specifications

### 7.1 `exceptions.py`

- Define the hierarchy from §6.1.
- Each exception takes a helpful message; `ItemNotFoundError` includes the missing ID.

### 7.2 `models.py`

- Implement `MediaItem`, `Book`, `Movie`, `Album`.
- Validation (rating, status, year) happens in the constructor or in property setters, and raises the custom exceptions.
- A module-level constant `VALID_STATUSES = ("to-do", "in-progress", "finished")` (tuple).

### 7.3 `storage.py`

|Function|Behavior|
|---|---|
|`load_library(path: Path) -> list[MediaItem]`|Reads JSON with `with path.open()`. Missing file → empty list. Bad JSON → raises `StorageError`|
|`save_library(items, path: Path) -> None`|Writes pretty JSON (`indent=2`) atomically if possible (write temp file, then replace)|
|`export_csv(items, path: Path) -> int`|Writes a flat CSV with `DictWriter`; returns row count|
|`import_csv(path: Path) -> tuple[list[MediaItem], list[str]]`|Returns `(valid_items, error_messages)`|

Uses: `pathlib.Path`, context managers, `json`, `csv`, `try/except/else/finally`.

### 7.4 `library.py` — the `Library` class

|Method|Behavior|
|---|---|
|`add(item)`|Assigns ID, checks duplicates, appends, returns the item|
|`remove(item_id)`|Removes or raises `ItemNotFoundError`|
|`get(item_id)`|Returns item or raises `ItemNotFoundError`|
|`update(item_id, **changes)`|Applies field changes via `**kwargs`|
|`search(text)`|Case-insensitive substring match on title (and creator)|
|`filter_items(**criteria)`|Supports `media_type`, `genre`, `status`, `min_rating`, `year_from`, `year_to`|
|`sorted_items(items, sort_by="title", reverse=False)`|Uses `sorted()` + lambda key|
|`paginate(items, page, per_page=10)`|Returns a slice|
|`stats()`|Returns a dict of counts and averages|
|`genre_counts()`|Dict comprehension / counting loop|
|`all_genres()`|Set comprehension|
|`top_rated(n=5)`|Sorted + slice|
|`recent(n=3)`|Sorted by `date_added` + slice `[-n:]` or `[:n]`|
|`recommend(item_id, limit=5)`|Set intersection on genres among `to-do` items|

### 7.5 `cli.py`

- `run()` is the main loop (`while True`).
- Helper functions: `prompt_str`, `prompt_int`, `prompt_rating`, `prompt_choice`. Each loops until valid input arrives.
- `format_table(items)` renders aligned columns with f-string format specs.
- Catches `MediaShelfError` at the loop level and prints a friendly message.
- Handles `KeyboardInterrupt` / `EOFError` gracefully (save and exit).

### 7.6 `main.py`

```python
from mediashelf.cli import run

if __name__ == "__main__":
    run()
```

---

## 8. CLI Specification

### 8.1 Main menu

```
=== MediaShelf ===
 1) Add item
 2) List items
 3) Search by title
 4) Filter items
 5) Edit item
 6) Delete item
 7) Statistics
 8) Recommend next
 9) Export to CSV
10) Import from CSV
 11) Save & quit
Choose an option:
```

### 8.2 Sample listing output

```
 ID  Type   Title                           Year  Rating  Status
 --  -----  ------------------------------  ----  ------  -----------
  1  Book   Dune                            1965     4.5  finished
  2  Movie  Arrival                         2016     4.0  finished
  3  Album  Kind of Blue                    1959     5.0  finished
  4  Book   Neuromancer                     1984      --  to-do
Page 1 of 1 | 4 items
```

### 8.3 Sample stats output

```
--- Library Statistics ---
Total items : 12  (Books: 5, Movies: 4, Albums: 3)
Average rating : 4.1  (Books 4.2 | Movies 3.9 | Albums 4.3)
By status : to-do 3 | in-progress 1 | finished 8
Top genres : sci-fi (6), jazz (3), drama (3)
Top 5 rated : 1) Kind of Blue (5.0) ...
```

### 8.4 Input validation rules

|Input|Rule|On failure|
|---|---|---|
|Title|Non-empty after `.strip()`|Re-prompt|
|Year|Integer, 1000 ≤ year ≤ current year|Re-prompt with range hint|
|Rating|Float 0–5 in 0.5 steps, or blank for unrated|Re-prompt|
|Genres|Comma-separated; normalized with `split`, `strip`, `lower`|Blank allowed|
|Menu choice|Must match a listed option|Print "Invalid choice"|

---

## 9. Data Formats

### 9.1 JSON (`data/library.json`)

```json
{
  "version": 1,
  "next_id": 4,
  "items": [
    {
      "item_id": 1,
      "type": "book",
      "title": "Dune",
      "author": "Frank Herbert",
      "year": 1965,
      "pages": 412,
      "genres": ["sci-fi", "adventure"],
      "rating": 4.5,
      "status": "finished",
      "date_added": "2026-10-22"
    },
    {
      "item_id": 3,
      "type": "album",
      "title": "Kind of Blue",
      "artist": "Miles Davis",
      "year": 1959,
      "tracks": ["So What", "Freddie Freeloader", "Blue in Green"],
      "genres": ["jazz"],
      "rating": 5.0,
      "status": "finished",
      "date_added": "2026-10-22"
    }
  ]
}
```

### 9.2 CSV (`exports/library_YYYYMMDD.csv`)

Header row (fixed order):

```
id,type,title,creator,year,genres,rating,status,date_added
```

Rules:

- `creator` = author / director / artist.
- `genres` joined with `;` (e.g., `sci-fi;adventure`) so commas stay as column delimiters.
- Unrated items leave `rating` blank.

Example:

```
1,book,Dune,Frank Herbert,1965,sci-fi;adventure,4.5,finished,2026-10-22
2,movie,Arrival,Denis Villeneuve,2016,sci-fi;drama,4.0,finished,2026-10-22
3,album,Kind of Blue,Miles Davis,1959,jazz,5.0,finished,2026-10-22
```

---

## 10. Git & GitHub Workflow

### 10.1 Branching model

```
main  ──●────────●──────────●───────────●──────────●──▶  (always working)
         \      / \        /  \        /  \        /
          feature/storage   feature/search  feature/csv  feature/scripts
```

- `main` is always runnable. Never commit directly to it after Day 1.
- One short-lived branch per feature, named `feature/<topic>` (or `fix/<topic>`, `docs/<topic>`).

### 10.2 Commit message convention

Format:

```
<type>: <short imperative summary, ≤ 50 chars>

<optional body: what and why, wrapped at ~72 chars>
```

Types: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `style`.

|✅ Good|❌ Bad|
|---|---|
|`feat: add genre filter to library search`|`update`|
|`fix: handle missing JSON file on startup`|`fixed stuff`|
|`docs: add usage examples to README`|`readme changes lol`|
|`refactor: extract prompt helpers from cli`|`more work`|

Rules: one logical change per commit; imperative mood ("add", not "added"); commit often.

### 10.3 Required Git activities (checklist)

|☐|Activity|Evidence|
|---|---|---|
|☐|`git init` and first commit with `.gitignore`|Initial commit in log|
|☐|Create repo on GitHub, `git remote add origin ...`, `git push -u origin main`|Repo visible online|
|☐|Use `git status`, `git diff`, `git log --oneline --graph` regularly|—|
|☐|≥ 4 feature branches created and pushed|Branch list|
|☐|Open a **Pull Request** for each feature branch|≥ 4 PRs|
|☐|**Self-review** each PR: leave ≥ 2 line comments per PR|PR conversations|
|☐|Request an **external review** on at least one PR (friend, mentor, community)|Review comments|
|☐|**Deliberate merge conflict** created and resolved by hand (Day 9)|Merge commit|
|☐|**Rebase** a feature branch onto updated `main` before merging (Day 9)|Linear history on that branch|
|☐|Merge ≥ 3 branches into `main`|Merge commits / squash merges|
|☐|Tag release: `git tag -a v1.0 -m "First release"` and push tags|Release on GitHub|
|☐|Delete merged branches (local and remote)|Clean branch list|

### 10.4 Deliberate conflict exercise (Day 9)

1. From `main`, create `feature/table-style-a` and `feature/table-style-b`.
2. On each, change **the same lines** of `format_table()` differently; commit.
3. Merge A into `main` (fast-forward or merge commit).
4. Merge B into `main` → Git reports a conflict.
5. Open the file, find the `<<<<<<<`, `=======`, `>>>>>>>` markers, decide the final version, remove markers.
6. `git add <file>` → `git commit` (or `git merge --continue`).
7. Write in your notes: _what caused it, how you resolved it, how to avoid it._

### 10.5 Rebase exercise (Day 9)

1. Create `feature/stats-polish` from `main`.
2. Add a commit on `main` (e.g., a README tweak).
3. On the feature branch: `git rebase main`.
4. Observe the history with `git log --oneline --graph --all`.
5. Push with `git push --force-with-lease` (only to **your own** feature branch).

> **Golden rule:** never rebase commits that others have already pulled (shared branches such as `main`).

### 10.6 Pull request template

Copy into each PR description:

```markdown
## What
Short description of the change.

## Why
The problem it solves or the requirement ID(s) it satisfies (e.g., FR-12, FR-13).

## How to test
1. Steps to try it
2. Expected result

## Checklist
- [ ] Code runs without errors
- [ ] Docstrings added
- [ ] No personal data committed
- [ ] Commit messages follow convention
```

### 10.7 Self code-review checklist

- Are names clear and consistent?
- Is any function doing more than one job?
- Are all errors handled with a helpful message?
- Is there duplicated code that could be a function?
- Are there leftover `print()` debug lines or commented-out code?
- Would a stranger understand this in 6 months?

### 10.8 Git command quick reference

```bash
git init                         # start a repo
git status                       # what changed?
git add <file>   |   git add -p  # stage (all of a file | interactively)
git commit -m "feat: ..."        # save a snapshot
git log --oneline --graph --all  # visualize history
git switch -c feature/x          # create + switch to branch
git switch main                  # switch back
git merge feature/x              # merge into the current branch
git rebase main                  # replay current branch on top of main
git remote add origin <url>      # link to GitHub
git push -u origin <branch>      # first push of a branch
git pull --rebase                # update local branch cleanly
git branch -d feature/x          # delete merged local branch
git push origin --delete feature/x   # delete remote branch
git restore <file>               # discard unstaged changes
git stash / git stash pop        # temporarily shelve changes
```

---

## 11. Shell Scripts Specification

### 11.1 General rules

- First line: `#!/usr/bin/env bash`
- Add `set -euo pipefail` near the top (exit on errors, unset variables, and pipe failures).
- Make executable: `chmod +x scripts/*.sh`
- Quote variables: `"$VAR"`.
- Add a usage comment block at the top of each script.

### 11.2 `scripts/backup.sh`

**Purpose:** Safe, timestamped backups of your library.

|Step|Requirement|Concepts|
|---|---|---|
|1|Verify `data/library.json` exists; print an error to stderr (`>&2`) and exit 1 if not|redirection|
|2|`mkdir -p backups`|navigation / dirs|
|3|Build a name: `backups/library_$(date +%Y%m%d_%H%M%S).json`|command substitution|
|4|`cp` the file to that name|copying|
|5|`chmod 600` the backup|permissions|
|6|Print confirmation with `ls -l` of the new file|permissions inspection|
|7|List backups older than 7 days: `find backups/ -name "*.json" -mtime +7`|`find`|
|8|Append a log line to `backups/backup.log` using `>>`|append redirection|

### 11.3 `scripts/report.sh`

**Purpose:** Analyze the CSV export without Python.

Input: path to a CSV (default: newest file in `exports/`, located using `find` + `sort`/`tail`).

|#|Report section|Suggested pipeline|
|---|---|---|
|1|Total rows (excluding header)|`tail -n +2 file \| wc -l`|
|2|Count by type|`tail -n +2 file \| awk -F, '{print $2}' \| sort \| uniq -c \| sort -rn`|
|3|Average rating (ignore blanks)|`awk -F, 'NR>1 && $7!="" {s+=$7; n++} END {printf "%.2f\n", s/n}' file`|
|4|Items rated ≥ 4.0|`awk -F, 'NR>1 && $7>=4.0 {print $3}' file`|
|5|All movies|`grep ',movie,' file`|
|6|Genre frequency|`awk -F, 'NR>1 {print $6}' file \| tr ';' '\n' \| sort \| uniq -c \| sort -rn`|
|7|Clean display version (swap `;` for `/`, remove empty ratings)|`sed 's/;/\//g; s/,,/,--,/g' file`|
|8|Items finished vs to-do|`grep -c ',finished,' file` and similar|

Output handling:

- Write the full report to `exports/report_YYYYMMDD.txt` using `>` (and `>>` to append sections).
- Send error messages to `exports/report_errors.log` with `2>`.
- Demonstrate `2>&1` at least once (merge stdout and stderr into one log).
- Print the report to the screen **and** save it, using `tee`.

### 11.4 Additional shell practice (ad hoc, no script needed)

|Task|Command idea|
|---|---|
|Show where you are and what's there|`pwd`, `ls -la`|
|Find all CSVs anywhere in the project|`find . -name "*.csv"`|
|Find Python files modified in the last day|`find . -name "*.py" -mtime -1`|
|Find TODO comments in your code|`grep -rn "TODO" mediashelf/`|
|Count lines of Python code|`find . -name "*.py" \| xargs wc -l`|
|Rename a genre across the CSV safely|`sed -i.bak 's/scifi/sci-fi/g' file.csv`|
|Inspect permissions|`ls -l scripts/` → read `-rwxr-xr-x`|
|Octal vs symbolic chmod|`chmod 755 x.sh` vs `chmod u+x x.sh`|

### 11.5 Permissions cheat sheet

```
-rwxr-xr--   owner: read/write/execute | group: read/execute | others: read only
 421 421 421   r=4  w=2  x=1
 chmod 754 file   →  7 (rwx) 5 (r-x) 4 (r--)
```

---

## 12. Concept Coverage Matrix

Tick each box once you have **used the concept in real project code** (not just a throwaway test).

### 12.1 Python

| ☐   | Concept                   | Where to apply it                                                                     | Suggested location        |
| --- | ------------------------- | ------------------------------------------------------------------------------------- | ------------------------- |
| ☐   | Variables                 | Item fields, counters, accumulators                                                   | everywhere                |
| ☐   | Numbers (int/float)       | Ratings, years, averages, pages                                                       | `models.py`, `library.py` |
| ☐   | Strings                   | Titles, names, normalization                                                          | `models.py`, `cli.py`     |
| ☐   | f-strings                 | Table rows, stats lines, error messages                                               | `cli.py`                  |
| ☐   | Booleans                  | Validity flags, `is_finished`, filter tests                                           | `models.py`               |
| ☐   | Type conversion           | `int(input())`, `float()`, CSV strings → numbers                                      | `cli.py`, `storage.py`    |
| ☐   | Conditionals              | Menu dispatch, validation, status logic                                               | `cli.py`                  |
| ☐   | `for` loops               | Iterate items, build tables, tally genres                                             | `library.py`              |
| ☐   | `while` loops             | Main menu, re-prompt on invalid input                                                 | `cli.py`                  |
| ☐   | `break` / `continue`      | Skip bad CSV rows, exit loops                                                         | `storage.py`, `cli.py`    |
| ☐   | Functions + return values | Prompts, stats, formatters                                                            | all modules               |
| ☐   | Multiple return values    | `import_csv` → `(items, errors)`                                                      | `storage.py`              |
| ☐   | Default arguments         | `sorted_items(sort_by="title")`, `top_rated(n=5)`                                     | `library.py`              |
| ☐   | Variable scope            | Module constants vs locals; one closure                                               | `cli.py`                  |
| ☐   | `*args`                   | A helper like `print_lines(*lines)`                                                   | `cli.py`                  |
| ☐   | `**kwargs`                | `filter_items(**criteria)`, `update(**changes)`, subclass init                        | `library.py`, `models.py` |
| ☐   | Lambda                    | Sort keys, filter predicates                                                          | `library.py`              |
| ☐   | Basic input/output        | `input()`, `print()` with `sep`/`end`                                                 | `cli.py`                  |
| ☐   | Lists                     | The library, search results                                                           | `library.py`              |
| ☐   | Tuples                    | Tracklist, `VALID_STATUSES`, duplicate key                                            | `models.py`               |
| ☐   | Sets                      | Genres, unique genres, intersection recs                                              | `models.py`, `library.py` |
| ☐   | Dictionaries              | Serialization, grouping, counting                                                     | `models.py`, `library.py` |
| ☐   | Slicing                   | `[:5]`, `[-3:]`, `[::-1]`, pages                                                      | `library.py`              |
| ☐   | Sorting                   | `sorted()` with key; `.sort()`                                                        | `library.py`              |
| ☐   | List comprehension        | Filter titles, build rows                                                             | `library.py`              |
| ☐   | Dict comprehension        | `{genre: count}`                                                                      | `library.py`              |
| ☐   | Set comprehension         | All unique genres                                                                     | `library.py`              |
| ☐   | String methods            | `strip`, `lower`, `title`, `split`, `join`, `replace`, `startswith`, `ljust`/`format` | `cli.py`, `storage.py`    |
| ☐   | `pathlib`                 | All file paths, `exists()`, `mkdir`, `parent`                                         | `storage.py`              |
| ☐   | Context managers          | `with path.open() as f` for every file op                                             | `storage.py`              |
| ☐   | JSON module               | `json.load`, `json.dump(indent=2)`                                                    | `storage.py`              |
| ☐   | CSV module                | `DictReader`, `DictWriter`                                                            | `storage.py`              |
| ☐   | Exception handling        | `try/except/else/finally`, specific exceptions                                        | `storage.py`, `cli.py`    |
| ☐   | Custom exceptions         | Hierarchy in `exceptions.py`                                                          | `exceptions.py`           |
| ☐   | Classes                   | `MediaItem`, `Library`                                                                | `models.py`, `library.py` |
| ☐   | Inheritance               | `Book`/`Movie`/`Album` extend `MediaItem`; `super()`                                  | `models.py`               |
| ☐   | Exception inheritance     | `MediaShelfError` family                                                              | `exceptions.py`           |

### 12.2 Git & GitHub

|☐|Concept|
|---|---|
|☐|`git init`|
|☐|`git add` / `git commit`|
|☐|Branching|
|☐|Merging|
|☐|Rebasing|
|☐|Resolving merge conflicts|
|☐|`.gitignore`|
|☐|Remotes (`origin`) and `push` / `pull`|
|☐|Pull requests|
|☐|Code review (self + external)|
|☐|Clear commit messages|

### 12.3 Shell / Linux

|☐|Concept|
|---|---|
|☐|Navigation (`cd`, `pwd`, `ls`, `mkdir`, `cp`, `mv`, `rm`)|
|☐|File permissions (`chmod`, `ls -l`)|
|☐|`grep`|
|☐|`awk`|
|☐|`sed`|
|☐|`find`|
|☐|Pipes (`\|`)|
|☐|Redirection (`>`, `>>`, `2>`, `2>&1`, `<`)|

---

## 13. Day-by-Day Execution Plan

> **Time budget:** ~2–3 hours per day. If you fall behind, drop the **S/C** items, never the **M** items.

### Day 1: Foundations & Repository Setup

**Goals:** Working repo, structure, and shell comfort.

- [ ] Create the project folder using only the terminal (`mkdir`, `cd`, `touch`)
- [ ] `git init`; create `.gitignore` (§5.3) and a stub `README.md`
- [ ] Create the full folder/file skeleton (§5.2) with empty modules containing docstrings
- [ ] First commit: `chore: initialize project structure`
- [ ] Create the GitHub repo; add the remote; push
- [ ] Copy this document to `docs/PROJECT_DESCRIPTION.md`, commit: `docs: add project description`

**Acceptance:** Repo visible on GitHub with the skeleton and a clean first commit.

### Day 2: Exceptions & Models

**Branch:** `feature/models`

- [ ] Write `exceptions.py` (hierarchy, messages)
- [ ] Write `MediaItem` with validation and `to_dict`/`from_dict`
- [ ] Write `Book`, `Movie`, `Album` with `super().__init__`, `**kwargs`, and `describe()`
- [ ] Write `__str__`, `__repr__`, `__eq__`
- [ ] Test manually in a Python REPL (create items, trigger each exception)
- [ ] Commit in small steps (≥ 4 commits)
- [ ] Open PR → self-review → merge

**Acceptance:** You can create all three item types and bad ratings raise `InvalidRatingError`.

### Day 3: Storage (JSON)

**Branch:** `feature/storage`

- [ ] Implement `load_library` / `save_library` with `pathlib` and `with`
- [ ] Handle: missing file, empty file, invalid JSON, permission errors
- [ ] Create `data/sample_library.json` with ≥ 12 varied items
- [ ] Round-trip test: load → save → load; the data should match
- [ ] PR → review → merge

**Acceptance:** Corrupted JSON gives a friendly error, not a traceback.

### Day 4: Library Core

**Branch:** `feature/library-core`

- [ ] `Library` class: `add`, `remove`, `get`, `update(**changes)`
- [ ] ID assignment and duplicate detection
- [ ] `filter_items(**criteria)` using kwargs
- [ ] PR → review → merge

**Acceptance:** Adding a duplicate raises `DuplicateItemError`; filters combine correctly.

### Day 5: Search, Sort, Slice

**Branch:** `feature/search`

- [ ] `search(text)` with string methods
- [ ] `sorted_items` with lambdas and multi-key sorting (rating desc, then title asc)
- [ ] `paginate`, `top_rated`, `recent` using slicing
- [ ] PR → review → merge

**Acceptance:** Sorting by rating handles `None` ratings without crashing.

### Day 6: Statistics & Recommendations

**Branch:** `feature/stats`

- [ ] `stats()`, `genre_counts()`, `all_genres()` using comprehensions
- [ ] `recommend()` using set intersection
- [ ] PR → review → merge

**Acceptance:** Stats match manual counts on the sample data.

### Day 7: Command-Line Interface

**Branch:** `feature/cli`

- [ ] Prompt helpers with validation loops
- [ ] Table formatter using f-string alignment
- [ ] Main menu loop wired to the `Library`
- [ ] Global error handling and graceful exit
- [ ] PR → review → merge

**Acceptance:** You can use every menu option without a traceback, even with bad input.

### Day 8: CSV Import/Export

**Branch:** `feature/csv`

- [ ] `export_csv` with `DictWriter`
- [ ] `import_csv` with `DictReader`, validating each row, collecting errors
- [ ] Menu options 9 and 10
- [ ] PR → review → merge

**Acceptance:** Export → import into an empty library recreates the same items.

### Day 9: Git Mastery Day

- [ ] Deliberate conflict exercise (§10.4)
- [ ] Rebase exercise (§10.5)
- [ ] Practice `git stash`, `git restore`, `git log --graph`
- [ ] Write notes in `docs/git-notes.md` about what you learned

**Acceptance:** A merge commit resolving a conflict exists in history; one branch was rebased.

### Day 10: Shell Scripts

**Branch:** `feature/scripts`

- [ ] Write `backup.sh` (§11.2)
- [ ] Write `report.sh` (§11.3)
- [ ] Practice commands from §11.4
- [ ] `chmod +x` both scripts; set `chmod 600` on personal data
- [ ] PR → review → merge

**Acceptance:** Both scripts run from the project root and produce correct output.

### Day 11: Refactor, Polish, Test

**Branch:** `refactor/cleanup`

- [ ] Add/verify docstrings on everything
- [ ] Remove duplication, rename unclear variables
- [ ] Run through the QA checklist (§15)
- [ ] Optionally add `tests/` (see §19)
- [ ] PR → review → merge

**Acceptance:** QA checklist fully ticked.

### Day 12: Documentation & Release

**Branch:** `docs/readme`

- [ ] Write the README (§18) with usage examples and a terminal screenshot/GIF
- [ ] Final PR review pass; request external feedback
- [ ] Fresh-clone test: clone your repo to a new folder, run it with sample data
- [ ] Tag and push `v1.0`
- [ ] Create a GitHub Release with notes

**Acceptance:** A stranger can clone, run, and understand the project.

---

## 14. Milestones & Checkpoints

|Milestone|Target day|Exit criteria|
|---|---|---|
|**M0: Project kickoff**|Day 1|Repo live, skeleton pushed|
|**M1: Domain complete**|Day 3|Models + storage working; sample data loads|
|**M2: Core logic complete**|Day 6|Search, filter, sort, stats, recommend all work in the REPL|
|**M3: Usable app**|Day 8|Full CLI plus CSV import/export|
|**M4: Skills showcase**|Day 10|Conflict resolved, rebase done, both scripts working|
|**M5: Release**|Day 12|`v1.0` tagged, README complete|

**Weekly check-in questions (ask yourself at the end of Day 6 and Day 12):**

1. What did I learn that I didn't remember before?
2. Which concept still feels shaky?
3. What would I do differently next time?

---

## 15. Quality Assurance & Testing

### 15.1 Manual test checklist

|☐|Scenario|Expected result|
|---|---|---|
|☐|Start with no `library.json`|Empty library created; no crash|
|☐|Start with corrupted JSON|Friendly error; safe fallback|
|☐|Add each of the 3 item types|Saved and listed correctly|
|☐|Add a duplicate|Clear duplicate error|
|☐|Enter rating `6`, `-1`, `abc`|Re-prompt each time|
|☐|Enter year `abc`, `0`, `3000`|Re-prompt each time|
|☐|Blank title|Re-prompt|
|☐|Search with different letter cases|Same results|
|☐|Filter by multiple criteria at once|Correct intersection|
|☐|Sort by each field, asc and desc|Correct order; no crash on `None`|
|☐|Delete a nonexistent ID|`ItemNotFoundError` message|
|☐|Edit then restart the app|Change persisted|
|☐|Export CSV → open in spreadsheet|Columns correct|
|☐|Import CSV containing 2 bad rows|Valid rows imported; errors reported|
|☐|Press Ctrl+C at the menu|Clean exit; data saved|
|☐|Run `backup.sh` twice|Two distinct timestamped files|
|☐|Run `report.sh` on the latest export|Correct numbers (cross-check by hand)|
|☐|Fresh clone of the repo|Runs with the sample data|

### 15.2 Code quality checklist

- [ ] Follows PEP 8 (consider `python -m pycodestyle .` if available)
- [ ] No unused imports or variables
- [ ] No hard-coded absolute paths
- [ ] No debug prints
- [ ] Every function has a docstring with args and return description
- [ ] No function longer than ~30 lines without a good reason
- [ ] Magic numbers replaced with named constants

### 15.3 Security & privacy checks

- [ ] `git ls-files` does not list `data/library.json`, `exports/`, or `backups/`
- [ ] No usernames, emails, or absolute home paths in committed files
- [ ] Scripts quote all variables

---

## 16. Risk Register

|#|Risk|Likelihood|Impact|Mitigation|
|---|---|---|---|---|
|R1|Scope creep (adding "just one more feature")|High|Medium|Stick to M items first; park ideas in §19|
|R2|Falling behind schedule|Medium|Medium|Drop S/C items; the 12 days include buffer|
|R3|Getting stuck on a bug|High|Low|Time-box to 45 minutes; then read the traceback aloud, use a minimal example, or ask for help|
|R4|Merge conflict panic|Medium|Low|Practice on Day 9; use `git merge --abort` to retreat safely|
|R5|Losing work|Low|High|Commit often; push at the end of every session|
|R6|Committing personal data|Medium|Medium|`.gitignore` on Day 1; check `git status` before every commit|
|R7|Shell script bugs destroying files|Low|High|Test on copies; avoid `rm -rf`; use `set -euo pipefail`|
|R8|Burnout / loss of motivation|Medium|High|Short daily sessions; celebrate each merged PR|

---

## 17. Definition of Done

The project is **done** when **all** of the following are true:

### Functionality

- [ ] All **Must** functional requirements (FR-xx marked M) pass the manual test checklist
- [ ] No unhandled exceptions in normal or erroneous use

### Code

- [ ] All modules implemented per §7
- [ ] Every item in the Python concept matrix (§12.1) is ticked
- [ ] Docstrings and clean structure throughout

### Git & GitHub

- [ ] Every item in the Git checklist (§10.3) is ticked
- [ ] Commit history is readable and follows the convention
- [ ] `main` contains no stray branches or WIP commits

### Shell

- [ ] Both scripts run correctly and use all required tools (§11)
- [ ] Every item in the shell concept matrix (§12.3) is ticked

### Documentation & Release

- [ ] README complete (§18)
- [ ] `sample_library.json` included
- [ ] `v1.0` tag and GitHub Release published
- [ ] Fresh-clone test passed

---

## 18. README Template

Copy this into `README.md` and fill it in:

````markdown
# 📚 MediaShelf

A command-line tool for cataloging and exploring your personal books, movies, and albums.

![demo](docs/demo.gif)  <!-- terminal recording or screenshot -->

## Features
- Track books, movies, and albums with ratings and status
- Search, filter, sort, and paginate
- Statistics and "what to enjoy next" recommendations
- JSON storage; CSV import/export
- Shell scripts for backups and reports

## Requirements
- Python 3.10+
- Bash (Linux, macOS, or WSL) for the scripts

## Installation
```bash
git clone https://github.com/<your-username>/mediashelf.git
cd mediashelf
python main.py
```

## Quick start
1. Copy the sample data: `cp data/sample_library.json data/library.json`
2. Run `python main.py`
3. Choose **2) List items** to see the demo collection

## Usage examples
(Include 3–4 short terminal transcripts: adding an item, filtering, viewing stats.)

## Shell scripts
```bash
./scripts/backup.sh          # timestamped backup of your library
./scripts/report.sh          # text report from the latest CSV export
```

## Project structure
(Short tree + one-line description per module.)

## What I learned
(3–5 honest bullets: Python, Git workflow, shell. Recruiters like this.)

## Roadmap
- [ ] Unit tests
- [ ] `argparse` command-line flags
- [ ] Type hints

## License
MIT
````

---

## 19. Stretch Goals

Only after the Definition of Done is met:

|Idea|Skills practiced|
|---|---|
|Unit tests with `unittest` or `pytest` (`tests/` folder)|Testing, assertions, fixtures|
|Type hints + `mypy`|Static typing|
|`argparse` for non-interactive commands (`mediashelf add --title ...`)|CLI design|
|Dataclasses for models|Modern Python|
|Colored output (ANSI codes)|String formatting|
|Notes/review text per item|Data model extension|
|Reading-time/watch-time totals|Aggregation|
|GitHub Actions workflow to run tests|CI/CD|
|Makefile or shell alias for common tasks|Automation|
|Logging with the `logging` module|Observability|

---

## 20. Working Agreements (Rules for Yourself)

1. **Commit early, commit often.** Small commits are easy to understand and undo.
2. **Never commit to `main` directly** after Day 1. Branch → PR → merge.
3. **Write the docstring first.** If you can't describe the function, you're not ready to write it.
4. **Make it work, make it right, make it fast.** In that order.
5. **Read the traceback bottom-up.** The last line says what, the lines above say where.
6. **Time-box stuck moments** (45 minutes), then simplify, search, or ask.
7. **Type the code yourself.** Copy-pasting teaches far less than typing.
8. **Use the terminal for everything possible.** Navigation, Git, and file work build shell fluency.
9. **End each day with a push** and a one-line note on what's next.
10. **Don't skip the PR reviews.** Reading your own diff is where you catch the most bugs.

---

## 21. Appendices

### Appendix A: Daily log template

Keep a `docs/devlog.md`:

```markdown
## Day N: <date>
**Planned:** ...
**Done:** ...
**Stuck on:** ...
**Learned:** ...
**Next:** ...
```

### Appendix B: Sample data (starter ideas for `sample_library.json`)

|Type|Title|Creator|Year|Genres|
|---|---|---|---|---|
|Book|Dune|Frank Herbert|1965|sci-fi, adventure|
|Book|Neuromancer|William Gibson|1984|sci-fi, cyberpunk|
|Book|Things Fall Apart|Chinua Achebe|1958|fiction, historical|
|Book|The Pragmatic Programmer|Hunt & Thomas|1999|tech, non-fiction|
|Movie|Arrival|Denis Villeneuve|2016|sci-fi, drama|
|Movie|Spirited Away|Hayao Miyazaki|2001|animation, fantasy|
|Movie|Parasite|Bong Joon-ho|2019|thriller, drama|
|Movie|Blade Runner|Ridley Scott|1982|sci-fi, cyberpunk|
|Album|Kind of Blue|Miles Davis|1959|jazz|
|Album|Rumours|Fleetwood Mac|1977|rock, pop|
|Album|To Pimp a Butterfly|Kendrick Lamar|2015|hip-hop, jazz|
|Album|OK Computer|Radiohead|1997|rock, alternative|

Include a mix of ratings (including a few unrated) and all three statuses so every feature has something to show.

### Appendix C: Python patterns to remember

```python
# Safe sorting with None ratings (None → treated as -1)
sorted(items, key=lambda i: (i.rating if i.rating is not None else -1, i.title.lower()), reverse=True)

# Dict comprehension: genre counts
{g: sum(1 for i in items if g in i.genres) for g in all_genres}

# Set comprehension: unique genres
{g for item in items for g in item.genres}

# Set intersection for similarity
shared = favorite.genres & candidate.genres

# Context manager for files
with path.open("w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

# Custom exception
class InvalidRatingError(MediaShelfError):
    def __init__(self, value):
        super().__init__(f"Rating must be 0-5 in 0.5 steps, got {value!r}")

# Re-prompt loop
while True:
    try:
        year = int(input("Year: "))
        break
    except ValueError:
        print("Please enter a whole number.")
```

### Appendix D: Shell patterns to remember

```bash
# Redirection
cmd > out.txt          # overwrite stdout
cmd >> out.txt         # append stdout
cmd 2> err.log         # stderr only
cmd > all.log 2>&1     # both to one file
cmd < input.txt        # feed a file as stdin

# Pipelines
grep -i "sci-fi" file.csv | awk -F, '{print $3}' | sort | head
find . -name "*.py" | xargs grep -n "def "

# awk essentials
awk -F, 'NR>1 {sum+=$7; n++} END {print sum/n}' file.csv
#   -F,  = delimiter     NR = row number     $7 = 7th column

# sed essentials
sed 's/old/new/g' file          # substitute (print result)
sed -i.bak 's/old/new/g' file   # edit in place, keep backup
sed -n '2,5p' file              # print lines 2-5
```

### Appendix E: Glossary

|Term|Meaning|
|---|---|
|**Branch**|An independent line of development in Git|
|**Merge**|Combine the work of one branch into another|
|**Rebase**|Replay your commits on top of another branch's latest commit|
|**Conflict**|Git can't auto-combine two edits to the same lines|
|**PR (Pull Request)**|A GitHub request to merge a branch, with discussion and review|
|**Remote**|A copy of the repo hosted elsewhere (e.g., GitHub)|
|**Context manager**|An object used with `with` that handles setup and cleanup (e.g., closing files)|
|**Serialization**|Converting objects to a storable format such as JSON|
|**Polymorphism**|Different classes responding to the same method name in their own way|
|**Idempotent**|Running it twice gives the same result as running it once|
|**Stdout / Stderr**|Standard output and standard error streams|
|**Octal permissions**|Numeric chmod notation (e.g., 755)|

### Appendix F: Where to get unstuck

- Python docs: `docs.python.org/3` (look at `pathlib`, `json`, `csv`)
- Git book (free): `git-scm.com/book`
- GitHub docs on pull requests: `docs.github.com`
- Shell: `man grep`, `man awk`, `man sed`, `man find`, or `command --help`
- Communities: r/learnpython, Python Discord, Stack Overflow (search before asking)

---

**Final reminder:** the goal isn't a perfect app. It's repeated, deliberate practice with every skill on your list. Ship the simple version first, then improve it.