# ITT-LAB

My solutions to the **Internet Technologies and Tools (ITT) lab** exercises — HTML, CSS and
vanilla JavaScript in labs 1–4 and 8, Python and SQLite in labs 5–7. The lab manual these follow
is included as `ITT-labmanual-2022.pdf`.

## What's in each lab

| Folder | Topic | Exercises |
| --- | --- | --- |
| `LAB1/` | HTML basics | Q1 links (image, page, `mailto:`), Q2 campus feedback form, Q3 student registration form, Q4 multi-page bookstore (home, login, registration, profile, catalogue, cart, checkout, confirmation) |
| `LAB2/` | HTML image maps, frames, tables | Q1 clickable campus image map, Q2 frames / iframe navigation pages, Q3 tables with CSS |
| `LAB3/` | JavaScript strings and DOM | Q1 growing/shrinking text animation, Q2 Pig Latin converter, Q3 split a phone number into area code and number, Q4 3-letter combinations of a 5-letter word, Q5 table of squares and cubes 0–9 |
| `LAB4/` | JavaScript events | Q1 Fibonacci series and square table (prompt / alert), Q2 left-most vowel and string reversal, Q3 overlapping boxes brought to front on hover, Q4 USN (university serial number) validation with a regex, Q5 calculator, Q6 change the background colour on hover |
| `LAB5/` | Python basics | Arithmetic, matrix loops, recursion (sum, Fibonacci, list sum), palindrome list, list reversal, bubble sort, primes in a range |
| `LAB6/` | Python strings | Palindromes, removing punctuation, sorting words, building email addresses, regex find-and-replace, printing environment variables, Armstrong and strong numbers |
| `LAB7/` | Python + SQLite | Create a `STUDENT` table, insert records, sort by CGPA, insert from user input with validation, look up by registration number, update CGPA |
| `LAB8/` | Mini project | `question.html` — a small in-browser medical inventory table (add medicine + quantity) |

## Running it

**HTML / JavaScript labs (1–4, 8).** Serve the repo root and open a lab's page in the browser:

```bash
python3 -m http.server 8000
# then open e.g. http://localhost:8000/LAB4/Q5)/index.html
```

Opening the `.html` files directly from disk works for almost all of them too.

**Python labs (5–7).** Each file is a standalone script (Python 3, standard library only):

```bash
python3 LAB5/bubble_sort.py
```

The SQLite scripts in `LAB7/` create their database (`test.db`, `Q1.db`, `students.db`) in the
directory you run them from, and are meant to be run in order:

```bash
cd LAB7
python3 1a.py   # create the STUDENT table
python3 1b.py   # insert sample records
python3 1c.py   # list students by CGPA
python3 2.py    # insert a student from keyboard input
python3 3.py    # look up a student by registration number
python3 4.py    # update a student's CGPA
```

The `.db` files are generated at runtime and are git-ignored.

## Project structure

```
ITT-LAB/
├── ITT-labmanual-2022.pdf   # lab manual the exercises follow
├── LAB1/ … LAB4/            # one folder per question: index.html + QN.js (+ style.css)
├── LAB5/ LAB6/              # standalone Python scripts
├── LAB7/                    # Python + SQLite scripts
└── LAB8/question.html       # medical inventory mini project
```

## Tech stack

HTML5, CSS, vanilla JavaScript, Python 3 (`sqlite3`, `re`, `string`, `os` from the standard library).

The static pages could be hosted with GitHub Pages; it is not enabled for this repo.
