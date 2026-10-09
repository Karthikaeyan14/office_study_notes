# Pytest — Quick Revision Notes

## 1. Basics & Naming Rules
```python
# file must start/end with test_ or _test
# test_login.py

def test_addition():          # function must start with "test_"
    assert 2 + 2 == 4
```
Run tests:
```bash
pytest                     # run all tests
pytest test_login.py       # run one file
pytest -v                  # verbose
pytest -k "login"          # run tests matching name
pytest -m smoke            # run tests with marker "smoke"
pytest -x                  # stop after first failure
pytest --maxfail=2         # stop after 2 failures
pytest -s                  # show print() output
```

---

## 2. Assertions
```python
def test_values():
    assert 5 > 2
    assert "abc" in "abcdef"
    assert [1,2,3] == [1,2,3]

def test_exception():
    with pytest.raises(ZeroDivisionError):
        10 / 0

def test_exception_msg():
    with pytest.raises(ValueError, match="invalid"):
        raise ValueError("invalid input")
```

---

## 3. Fixtures (Setup/Teardown)
```python
import pytest

@pytest.fixture
def driver():
    print("Setup: open browser")
    d = "browser_instance"
    yield d                      # value passed to test
    print("Teardown: close browser")

def test_home_page(driver):
    assert driver == "browser_instance"
```
`yield` splits fixture into setup (before) and teardown (after test).

### Fixture Scope
```python
@pytest.fixture(scope="function")  # default - runs per test
@pytest.fixture(scope="class")     # runs once per class
@pytest.fixture(scope="module")    # runs once per file
@pytest.fixture(scope="session")   # runs once per test run
```

### Autouse Fixture
```python
@pytest.fixture(autouse=True)
def log_start_end():
    print("Test starting")
    yield
    print("Test ending")
```

---

## 4. conftest.py (Shared Fixtures)
```python
# conftest.py — no import needed, auto-discovered by pytest
import pytest

@pytest.fixture
def driver():
    from selenium import webdriver
    d = webdriver.Chrome()
    yield d
    d.quit()
```
Any `test_*.py` file in the same folder (or subfolder) can use `driver` directly without importing it.

---

## 5. Parametrize (Data-Driven Testing)
```python
import pytest

@pytest.mark.parametrize("a,b,result", [
    (2,3,5),
    (10,5,15),
    (0,0,0),
])
def test_add(a, b, result):
    assert a + b == result
```
Runs the same test 3 times with different inputs — very useful for testing multiple login credentials, form data, etc.

---

## 6. Markers
```python
@pytest.mark.smoke
def test_login():
    pass

@pytest.mark.skip(reason="not ready yet")
def test_feature_x():
    pass

@pytest.mark.skipif(condition=True, reason="only on Linux")
def test_linux_only():
    pass

@pytest.mark.xfail(reason="known bug")
def test_known_issue():
    assert 1 == 2
```
Register custom markers in `pytest.ini`:
```ini
[pytest]
markers =
    smoke: quick smoke tests
    regression: full regression tests
```
Run only smoke tests: `pytest -m smoke`

---

## 7. Grouping Tests in a Class
```python
class TestLogin:
    def test_valid_login(self):
        assert True

    def test_invalid_login(self):
        assert True
```
Run: `pytest -k "TestLogin"`

---

## 8. Fixture with Params (Multiple Setup Data)
```python
@pytest.fixture(params=["chrome", "firefox"])
def browser(request):
    return request.param

def test_browser(browser):
    print(f"Running on {browser}")
```
Runs the test once for each browser value.

---

## 9. Reports & Plugins
```bash
pip install pytest-html
pytest --html=report.html --self-contained-html    # HTML report

pip install pytest-xdist
pytest -n 4                 # run tests in parallel (4 workers)

pip install pytest-rerunfailures
pytest --reruns 2            # rerun failed tests 2 times
```

---

## 10. Combine with Selenium (Real Example)
```python
# conftest.py
import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    d = webdriver.Chrome()
    d.get("https://example.com")
    yield d
    d.quit()

# test_home.py
def test_title(driver):
    assert "Example" in driver.title

@pytest.mark.parametrize("query", ["python", "selenium", "pytest"])
def test_search(driver, query):
    driver.find_element("name","q").send_keys(query)
```

---

## 11. Useful pytest.ini / Config
```ini
[pytest]
markers =
    smoke: smoke tests
    regression: regression tests
addopts = -v -s
testpaths = tests
```

---

## What Else You Should Learn Next
- **assert with soft assertions** (`pytest-check` plugin) — continue test even if one assertion fails
- **Page Object Model (POM)** — design pattern to structure Selenium+pytest framework cleanly
- **Logging** (`logging` module) — better than print for debugging test runs
- **pytest-bdd** — if your team writes Gherkin/BDD style tests
- **CI/CD integration** — running pytest in Jenkins/GitHub Actions pipelines
- **Allure Reports** (`allure-pytest`) — advanced, more visual reporting than pytest-html
- **Environment config handling** (`pytest-dotenv` or `.ini`/`.yaml` config files) — running tests on different environments (QA/Staging/Prod)
