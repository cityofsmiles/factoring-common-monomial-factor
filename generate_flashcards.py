


import sympy as sp
import random
import json
import os

# Pool of high school algebra variables
all_vars = ["a", "b", "c", "m", "n", "p", "q", "x", "y", "z"]

# Ranges
const_range = list(range(2, 10))              # a as constant (2–9)
coef_range = list(range(1, 10))               # coefficients a, b, c (1–9)
exp_range = [1, 2, 3, 4]                      # exponents m, p, q


def format_term(coef, var=None, exp=1):
    """Format term with hidden coefficient 1 and exponent 1."""
    if var is None:
        return str(coef)
    # coefficient
    if coef == 1:
        part1 = ""
    elif coef == -1:
        part1 = "-"
    else:
        part1 = str(coef)
    # variable
    if exp == 1:
        part2 = var
    else:
        part2 = f"{var}^{exp}"
    return part1 + part2


def format_expr(expr):
    """Format Sympy expanded expression with ^ for exponents and clean coefficients."""
    s = sp.sstr(expr, order='lex')
    s = s.replace("**", "^").replace("*", "")
    return s


def pick_vars():
    """Pick x and y such that x comes before y alphabetically."""
    v1, v2 = random.sample(all_vars, 2)
    return tuple(sorted([v1, v2]))


def generate_case(case_type):
    x, y = pick_vars()
    x, y = sp.symbols(x), sp.symbols(y)

    if case_type == 1:
        # a(bx^p ± c)
        a = random.choice(const_range)
        b = random.choice(coef_range)
        c = random.choice(const_range)  # constant
        p = random.choice(exp_range)
        sign = random.choice([1, -1])

        expr = (a) * (b * x**p + sign * c)
        question = f"{a}({format_term(b, x.name, p)} {'+' if sign == 1 else '-'} {c})"

    elif case_type == 2:
        # a(bx^p ± cy^q)
        a = random.choice(const_range)
        b = random.choice(coef_range)
        c = random.choice(coef_range)
        p = random.choice(exp_range)
        q = random.choice(exp_range)
        sign = random.choice([1, -1])

        expr = (a) * (b * x**p + sign * c * y**q)
        question = f"{a}({format_term(b, x.name, p)} {'+' if sign == 1 else '-'} {format_term(c, y.name, q)})"

    elif case_type == 3:
        # ax^m(bx^p ± c)
        a = random.choice(coef_range)
        b = random.choice(coef_range)
        c = random.choice(const_range)
        m = random.choice(exp_range)
        p = random.choice(exp_range)
        sign = random.choice([1, -1])

        expr = (a * x**m) * (b * x**p + sign * c)
        question = f"{format_term(a, x.name, m)}({format_term(b, x.name, p)} {'+' if sign == 1 else '-'} {c})"

    else:
        # ax^m(bx^p ± cy^q)
        a = random.choice(coef_range)
        b = random.choice(coef_range)
        c = random.choice(coef_range)
        m = random.choice(exp_range)
        p = random.choice(exp_range)
        q = random.choice(exp_range)
        sign = random.choice([1, -1])

        expr = (a * x**m) * (b * x**p + sign * c * y**q)
        question = f"{format_term(a, x.name, m)}({format_term(b, x.name, p)} {'+' if sign == 1 else '-'} {format_term(c, y.name, q)})"

    return {
        "question": format_expr(sp.expand(expr)),
        "answer": question
    }


# Generate 200 flashcards equally distributed among 4 cases
flashcards = []
for case_type in range(1, 5):
    for _ in range(50):
        flashcards.append(generate_case(case_type))

# Save JSON to ./public/flashcards.json
output_dir = os.path.join(os.getcwd(), "public")
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "flashcards.json")

with open(output_path, "w") as f:
    json.dump(flashcards, f, indent=2)

print(f"✅ flashcards.json generated with {len(flashcards)} flashcards at {output_path}")


 
