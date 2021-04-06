Write a function that verifies provided argument is either an integer or a floating-point number, returning true if it
is or false otherwise.

Pointers

Numeric quantities are signed (optionally when positive, e.g. "+5" is valid notation)
Floats less than 1 (not considering possible exponent!) can be written without a leading "0" (e.g. ".00001")
Order-of-magnitude (i.e. 10, 100, 1000, etc.) can be written in E notation (the exponent is also signed, optionally so
if positive, e.g. all the following are valid 1e2, 1E2, 1e-2, 1E-2, 1e+2)
Probably obvious, but no spaces are allowed anywhere (we aim to represent a real-life number)
You can mix-n'-match any or all above pointers in any single numeric quantity