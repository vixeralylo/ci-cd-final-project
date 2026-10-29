# ci-cd-final-project

## Project Name

**ci-cd-final-project** — a minimal Python project created for learning Continuous Integration / Continuous Deployment (CI/CD) concepts as part of a Coursera course.

## Description

This project intentionally keeps the application logic as simple as possible (a single `print("Hello, World!")`) so that the focus stays entirely on building and understanding a CI/CD pipeline rather than on application complexity.

## Project Structure

```
.
├── main.py                     # Entry point - prints "Hello, World!"
├── test_main.py                 # Basic test for the application
├── .github/
│   └── workflows/
│       └── workflow.yml         # GitHub Actions CI pipeline
├── .tekton/
│   ├── tasks.yml                 # Tekton Tasks (cleanup, flake8, nose-test)
│   └── pipeline.yml              # Tekton Pipeline definition
└── README.md
```

## Requirements

- Python 3.8+

## How to Run

```bash
python main.py
```

Expected output:

```
Hello, World!
```

## How to Test

```bash
pip install pytest
pytest -v
```

## CI/CD

This repository uses **GitHub Actions** (see [`.github/workflows/workflow.yml`](.github/workflows/workflow.yml)) to automatically:

1. Check out the code
2. Set up Python
3. Install dependencies
4. Lint with flake8
5. Run unit tests with nose
6. Run the application

The pipeline is triggered on every `push` and `pull_request` to the `main`/`master` branch.

## Author

Sandy Taufik
