# Pytest

## Table of contents
- [Introduction](#introduction)
- [Applications](#applications)
- [Installation process](#installation-process)
- [How to Create and Run a Test](#how-to-create-and-run-a-test)
  - [Convention to Test Directory](#convention-to-test-directory)
  - [Example](#example)
- [Pytest + HTML Report](#pytest--html-report)
- [Future Features](#future-features)
- [Recommendations & References](#recommendations--references)


## Introduction
Pytest is a [open source](https://github.com/pytest-dev/pytest) framework for testing in Python that makes it easy to write small, readable tests, and can scale to support complex functional testing for applications and libraries.

[It has integration with `unittest` framework.](https://docs.pytest.org/en/7.1.x/how-to/unittest.html#:~:text=pytest%20supports%20running%20Python%20unittest%20%2Dbased%20tests%20out%20of%20the%20box.)


## Applications
Pytest is used for all types of tests in Python when:
- Unit tests (Individual components)
- Integration tests (Interaction between two or more components)
- Acceptance tests (Check whether the system meets the requirements specified by the user or customer)
- Charge tests (Check the system's performance)
- Regression tests (If the system still works after a change)


## Installation process
The run process will be explained before

1. Create a virtual environment:
```bash
python -m venv ./.venv
```

2. Activate the virtual environment in windows:
```bash
./.venv/Scripts/activate
```
  a. In Linux, the path is `./.venv/bin/activate`.
  b. In Windows, not forget to allow the execution of scripts with the command `Set-ExecutionPolicy Unrestricted -Scope Process`.

3. Install the Pytest:
```bash
pip install pytest
```

4. (OPTIONAL) Install the Pytest-html to generate a report in HTML:
```bash
pip install pytest-html
```


## How to Create and Run a Test

### Convention to Test Directory
When `pytest` is executed, it will search for files that start with `test_` or end with `_test.py` and will execute it.

It's hight recommended to create a archive called `__init__.py` in the modules folder to pytest acknowledge the folder as a module.

### Example
Creating a test file and running it:

```python
# tests/test_sample.py
def test_sample():
  assert 1 == 1
```
```bash
pytest tests/test_sample.py
```
Or just run the command below to run all tests in the project:
```bash
pytest
```


## Pytest + HTML Report
To generate a HTML report, run the command below:
1. Install the `pytest-html` package:
```bash
pip install pytest-html
```
2. Run the command below:
```bash
pytest --html=test_report/report.html
```


## Future Features
- Create cases to compare the Pytest with the Unittest using second link in [Recommendations & References](#recommendations--references).
- Create a topic explaining how to containerize the tests with Docker.
- Remove the `Foo` folder and the second line in `.env` file, because they are not necessary for the project, for academic purposes only.


## Recommendations & References
- Create [configuration files](https://docs.pytest.org/en/stable/reference/reference.html#configuration-options) to your tests, like `pytest.ini` or `setup.cfg`.
- [Documentation](https://docs.pytest.org/en/stable/index.html)
- [Pytest vs Unittest](https://docs.pytest.org/en/7.1.x/how-to/unittest.html#:~:text=pytest%20supports%20running%20Python%20unittest%20%2Dbased%20tests%20out%20of%20the%20box.)
- [Medium](https://medium.com/assertqualityassurance/tutorial-de-pytest-para-iniciantes-cbdd81c6d761)
- [Pytest history](https://docs.pytest.org/en/stable/history.html)
