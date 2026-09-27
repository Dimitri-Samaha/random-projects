# Random Projects

A grab bag of beginner Python exercises and small scripts.

- `Basic1-Ex1.py` through `Basic1-Ex10.py`: a numbered series of tiny beginner exercises from an intro course, covering printing, `sys.version`, string swapping, the current date and time, splitting a string into a list or tuple, parsing a file extension, list indexing, formatted output, string and number concatenation, and circle area.
- `choose_your_adventure.py`: a short branching text adventure story.
- `numerical_derivative.py`: numerically approximates the derivative of a user supplied function at a point (needs `matplotlib` and `numpy`).
- `Hangman.py`: a minimal Hangman prototype with a random word and letter guessing, needing `english-words`.
- `recursive_power.py`: a recursive function for integer powers.
- `password_vault.py`: a tiny password store and viewer gated by a master password (a simpler, earlier take on `tools/password_manager`).
- `Plot_tuto.py`: a `matplotlib` plotting tutorial, showing a line chart of salaries by age.

## Requirements
```
pip install matplotlib numpy english-words
```
These are only needed for `numerical_derivative.py`, `Plot_tuto.py`, and `Hangman.py` respectively; everything else uses only the standard library.

## Running it
Each file is standalone, for example:
```
python Hangman.py
```
