
"""
When to use assertions:

* at beginning of functions
* after function call
* check any impossible situations
* assert preconditions are true
"""


def fahrenheitToCelsius(temp):
    assert type(temp) in (int, float)
    assert temp >= -459.67, "Under absolute zero"
    return (temp - 32) / 1.8

