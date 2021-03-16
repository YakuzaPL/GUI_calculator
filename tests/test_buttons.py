import unittest

from button import My_button


def test_button_returns_correct_value():
    tested_values = ["1", "2", "+", "=", "a"]
    for value in tested_values:
        new_button = My_button(value, None)
        assert new_button.text() == value


if __name__ == '__main__':
    unittest.main()
