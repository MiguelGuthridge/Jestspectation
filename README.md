# Jestspectation

Pattern matching helper classes designed to allow for testing of complex data
structures in a readable and logical format.

The design is inspired by the `expect` system from JavaScript's Jest testing
framework.

```py
import jestspectation as expect

assert {
    "a": 1,
    "b": 2,
    "c": 3.0,
} == {
    "a": 1,
    "b": expect.Any(int),
    "c": expect.FloatApprox(2.5, magnitude=0.5)
}
```

## Installation

```sh
pip install jestspectation
```

## Usage with Pytest

The library can be used as a pytest plugin, which can give access to much more
detailed error messages when assertions fail.

You can enable it by adding the following lines to your `conftest.py`

```py
pytest_plugins = ("jestspectation.pytest",)
```

This should result in output similar to the following

```
    def test_goodbye():
>       assert 1 == expect.Any(float)
E       assert Type mismatch
E         Expected any object of type float
E         Received 1 (int)
```
