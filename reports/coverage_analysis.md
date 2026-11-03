# Lab 6 Coverage Analysis

All measurements below were collected with `coverage.py` against `Lab 6/food_delivery.py`.

| Run | Tests | Line coverage | Branch coverage |
|---|---:|---:|---:|
| Initial line run | 2 passed | 36% | Not measured in line-only run |
| Initial branch run | 2 passed | 36% | 30% |
| Final code coverage suite | 15 passed | 100% | Not measured in line-only run |
| Final branch coverage suite | 22 passed | 100% | 100% (24/24 branches) |
| Complete pytest suite | 35 passed | — | — |

The initial branch report also includes line coverage. The final code coverage report is produced without branch measurement, while the branch report uses `coverage run --branch`. The application source was not changed.

Run all tests from the repository root with `python3 -m pytest -q`.

Reproduce the final code coverage report from the repository root with:

```sh
python3 -m coverage erase
python3 -m coverage run --include='Lab 6/food_delivery.py' -m pytest -q 'Lab 6/test_food_delivery.py' 'Lab 6/CodeCoverageTest_PES1UG24CS443_application.py'
python3 -m coverage report -m
```

Reproduce the final branch coverage report with:

```sh
python3 -m coverage erase
python3 -m coverage run --branch --include='Lab 6/food_delivery.py' -m pytest -q 'Lab 6/test_food_delivery.py' 'Lab 6/BranchCoverageTest_PES1UG24CS443_application.py'
python3 -m coverage report -m
```
