# Pytest

## Usage
Download pytest
```bash
uv add pytest
```

### Creating test cases
1. Create a `tests/` directory
2. In the `tests/` directory, create files with the following formats: `test_*.py` or `*_test.py`
3. Create test functions inside the `.py` files with the following names: `test_*` or `*_test`

### Running test cases
Run from root (make sure to add `__init__.py` files.
```
python -m pytest
```
