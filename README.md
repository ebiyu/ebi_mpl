# Someya-lab style for Matplotlib

## Installation

Open this folder in terminal and run the following command:

```bash
pip install .
```

## Usage

You can use the style by inserting line `plt.style.use("mpl_someyalab.presentation")` at the beginning of your script.

Example:

```python
import matplotlib.pyplot as plt
plt.style.use("mpl_someyalab.presentation")

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y, label='1')
plt.xlabel("X label")
plt.ylabel("Y label")
plt.legend()
plt.tight_layout()
plt.show()
```
