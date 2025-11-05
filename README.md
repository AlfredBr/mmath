# Mental Math Practice CLI

An interactive command-line program for practicing mental arithmetic operations.

# Installation
1. Clone the repository
    ```
    git clone https://github.com/kianbroderick/mmath.git
    cd mmath
    ```
2. Run the project directly with `uv`
    ```
    uv run main.py
    ```
    `uv` will automatically create an isolated environemnt, install dependences
    listed in `pyproject.toml`, and execute the script.

## Alternative
The program relies on `colorama` and `numexpr`. These can be installed to a
virtual environment with `pip`.
```
pip install colorama numexpr
```

# Usage
When you start the program, you can follow the prompts to choose an operation. The
options are `+`, `-`, `(+/-)`, `*`, `/`, `^`, `sqrt`, `times tables`, `tt`, 
`custom`, or `default`.
You can enter `q` at any prompt to exit the program. After you complete the
number of questions you specified, you will see how long it took you to
complete, the average time it took to answer each question, and the number of
mistakes.

## Addition, Subtraction, Multiplication
`+`, `-`, `(+/-)`, and `*` let you select a maximum number to compute and asks
you a series of questions.

## Division
`/` asks you to compute the dividend and remainder exactly.

## Square
`^` asks you to compute the square of a number exactly. You can use the
following formula, choosing $d$ to be a convenient number:
```math
n^2 = (n-d)(n+d) + d^2
```
For example, to compute $67^2$:
```math
\begin{align}
67^2 &= (67-3)(67+3) + 3^2 \\
&= (64)(70) + 3^2 \\
&= 4200 + 280 + 9 \\
&= 4489
\end{align}
```
This allows you to convert a squaring problem into an easier 1 digit by 2 digit
multiplication, with an easy addition at the end.

## Times Tables (tt)
'times tables` (`tt` for short) asks you for what times table to practice, and a
maximum number to go to. For example, the "2" times table with a max of 10 will ask
for multiplication of 2 by any number 1-10.

## Square Root
This asks you to compute the square root of a given number. It assumes you are
using one iteration of Newton's method, using the closest perfect square as a
first guess. 
```math
\sqrt{n} \approx x_0 - \frac{x_0^2-n}{2x_0}
```
You can input expressions like "8 + 5/12", and it accepts a range
of solutions +- 0.1 as correct.

## Custom
This walks you through a prompt to select multiple operations. You can select
an operation by giving a maximum number that you want to compute, or not
include an operation by pressing Enter.

## Default
This is setup for my default setting:
    + Addition up to 999
    + Subtraction up to 999
    + Multiplication up to 99
    + Division up to 999
    + Squaring up to 99
    + Square root up to 99

# Future improvements
    + add more operations (complex numbers, more exponents, modulus, fractions)
    + add score tracking and statistics

