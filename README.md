# Random Projects

A grab-bag of beginner Python exercises and small scripts.

| File | What it does |
|---|---|
| `Basic1-Ex1.py` … `Basic1-Ex10.py` | A numbered series of tiny beginner exercises from an intro course: printing, `sys.version`, string swapping, current date/time, splitting a string into a list/tuple, file-extension parsing, list indexing, formatted output, string/number concatenation, circle area |
| `choose_your_adventure.py` | A short branching text-adventure story |
| `numerical_derivative.py` | Numerically approximates the derivative of a user-supplied function at a point (needs `matplotlib`, `numpy`) |
| `Hangman.py` | A minimal Hangman prototype (random word + letter guessing), needs `english-words` |
| `recursive_power.py` | A recursive integer-power function |
| `password_vault.py` | A tiny password store/viewer gated by a master password (a simpler, earlier take on `tools/password_manager`) |
| `Plot_tuto.py` | A `matplotlib` plotting tutorial (line chart of salaries by age) |

## Requirements
```
pip install matplotlib numpy english-words
```
(only needed for `numerical_derivative.py`, `Plot_tuto.py`, and `Hangman.py` respectively — everything else is standard library)

## Running it
Each file is standalone, e.g.:
```
python Hangman.py
```
