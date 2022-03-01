# pyqt-dark-calculator

PyQt dark theme calculator

## Note
I'm working on "new" feature(It doesn't work properly).

## Feature
* Basic operation supported by most of the calculators(e.g. Arithmetic operation, square root, round)
* Supporting parentheses calculation
* Being able to open new calculator window
* Show tooltip(helpful message to how the button works) when mouse cursor hovered to button

## Requirements
* PyQt5 >= 5.15

## Included Packages
* <a href="https://github.com/yjg30737/pyqt-dark-gray-theme.git">pyqt-dark-gray-theme</a>
* <a href="https://github.com/yjg30737/pyqt-custom-titlebar-window.git">pyqt-custom-titlebar-window</a>
* <a href="https://github.com/yjg30737/pyqt-resource-helper.git">pyqt-resource-helper</a>

## Setup
```
pip3 install git+https://github.com/yjg30737/pyqt-dark-calculator.git --upgrade
```

## Usage
```python
from pyqt_dark_calculator.calculatorApp import CalculatorApp

if __name__ == "__main__":
    import sys

    app = CalculatorApp(sys.argv)
    app.exec_()
```

Result

![image](https://user-images.githubusercontent.com/55078043/156103071-ecf9ed4d-2c52-4120-b4c8-6c0894fcaa88.png)
