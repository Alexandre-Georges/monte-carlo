# Monte Carlo Simulation

## Installation

```bash
npm install
npm run webpack
```

```bash
pip install flask
```

## Start the server

```python
npm run python
```

## Examples

### Basic example

The defaults provide a decent example that uses 2 different distributions and a simple formula.

### Monty Hall Problem

#### Stick to the same door

```python
from random import randint

door = randint(1, 3)
choosen = randint(1, 3)

output = 1 if door == choosen else 0
```

#### Switch to another door

```python
from random import randint

winning_door = randint(1, 3)
first_chosen = randint(1, 3)

options = [1, 2, 3]
options.remove(first_chosen)

if options.count(winning_door) == 1:
  output = 1
else:
  output = 0
```
