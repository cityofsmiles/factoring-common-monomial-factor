# Factoring Polynomials with Common Monomial Factor

This web application provides an interactive flashcard-based learning tool to practice factoring polynomials with a common monomial factor.

Hosted at: [https://cityofsmiles.github.io/factoring-common-monomial-factor](https://cityofsmiles.github.io/factoring-common-monomial-factor)

## Features

- Interactive flashcards on factoring polynomials
- Automatically shuffles and loads 10 random questions per session
- Instant feedback on answers (correct or incorrect)
- Final results page with score and answer key
- Option to retry with a new set of flashcards

## How It Works

1. A set of flashcards is loaded from a JSON file.
2. Users are presented with polynomial factoring problems.
3. The user types in the factored form (e.g., `2x(x^3 - 9)`).
4. The app checks answers automatically, ignoring spaces and capitalization.
5. After finishing, the user can view their score and the complete answer key.

## Tech Stack

- **React** (UI framework)
- **Framer Motion** (animations)
- **CSS** (styling)
- **GitHub Pages** (deployment)

## Local Development

Clone the repository and install dependencies:

```bash
git clone https://github.com/cityofsmiles/factoring-common-monomial-factor.git
cd factoring-common-monomial-factor
npm install
```

Run the development server:

```bash
npm run dev
```

Build for production:

```bash
npm run build
```

## Deployment

The app is automatically deployed to GitHub Pages at:

[https://cityofsmiles.github.io/factoring-common-monomial-factor](https://cityofsmiles.github.io/factoring-common-monomial-factor)

## Author

Developed by **Jonathan R. Bacolod, LPT**

---

This project is intended for educational purposes to help students practice factoring polynomials with common monomial factors.