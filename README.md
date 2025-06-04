# ebi's style for Matplotlib

[ja](./README_ja.md)

![](./doc/lab.png)

## Installation

```bash
pip install ebi_mpl
```

## Usage

You can use the style by inserting line `plt.style.use("ebi_mpl.lab")` at the beginning of your script.

Example:

```python
import matplotlib.pyplot as plt
plt.style.use("ebi_mpl.lab")

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y, label='1')
plt.xlabel("X label")
plt.ylabel("Y label")
plt.legend()
plt.tight_layout()
plt.show()
```

## For developer

Download this repository and open this folder in terminal and run the following command:

```bash
pip install .
```

Or if you computer has git, you can install it by the following command:

```bash
pip install git+https://github.com/ebiyu/ebi_mpl.git
```
