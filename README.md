# ci-cd-final-project

## Project Name

**ci-cd-final-project** — a minimal Node.js project created for learning Continuous Integration / Continuous Deployment (CI/CD) concepts as part of a Coursera course.

## Description

This project intentionally keeps the application logic as simple as possible (a single `console.log("Hello, World!")`) so that the focus stays entirely on building and understanding a CI/CD pipeline rather than on application complexity.

## Project Structure

```
.
├── index.js                      # Entry point - prints "Hello, World!"
├── index.test.js                  # Basic test for the application (Jest)
├── package.json                   # Project metadata and dependencies
├── .eslintrc.json                 # ESLint configuration
├── .github/
│   └── workflows/
│       └── workflow.yml           # GitHub Actions CI pipeline
├── .tekton/
│   ├── tasks.yml                   # Tekton Tasks (cleanup, flake8, run-unit-tests-with-nose)
│   └── pipeline.yml                # Tekton Pipeline definition
└── README.md
```

## Requirements

- Node.js 18+

## How to Run

```bash
npm install
node index.js
```

Expected output:

```
Hello, World!
```

## How to Test

```bash
npm install
npm test
```

## How to Lint

```bash
npm install
npm run lint
```

## CI/CD

This repository uses **GitHub Actions** (see [`.github/workflows/workflow.yml`](.github/workflows/workflow.yml)) to automatically, inside a `node:18` container:

1. Checkout the code
2. Setup Node.js
3. Install dependencies
4. Linting (ESLint)
5. Run unit tests (Jest)
6. Run the application

The pipeline is triggered on every `push` and `pull_request` to the `main`/`master` branch.

## Author

Sandy Taufik
