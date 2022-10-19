# Qing

Quantum Computing SDK

### Version

[![Version](https://badge.fury.io/py/qing.svg)](https://badge.fury.io/py/qing)

### Tutorial

https://github.com/Qing/Qing-tutorials

### Notice

The back end has been changed to tensor network. The previous backend environment can still be used with .run(backend="numpy").

### Install

```
git clone https://github.com/Qing/Qing
cd Qing
pip3 install -e .
```

or

```
pip3 install qing
```

### Circuit

```python
from qing import Circuit
import math

c = Circuit()

c = Circuit(50)
```

### Method Chain

```python
Circuit().h[0].x[0].z[0]

c = Circuit().h[0]
c.x[0].z[0]
```

### Slice

```python
Circuit().z[1:3] # Zgate on 1,2
Circuit().x[:3] # Xgate on (0, 1, 2)
Circuit().h[:] # Hgate on all qubits
Circuit().x[1, 2] # 1qubit gate with comma
```

### Rotation Gate

```python
Circuit().rz(math.pi / 4)[0]
```

### Run

```python
from qing import Circuit
Circuit(50).h[:].run()
```

### Run(shots=n)

```python
Circuit(100).x[:].run(shots=100)
# => Counter({'1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111': 100})
```

### Single Amplitude

```python
Circuit(4).h[:].run(amplitude="0101")
```

### Expectation value of hamiltonian

```python
from qing.pauli import Z
hamiltonian = 1*Z[0]+1*Z[1]
Circuit(4).x[:].run(hamiltonian=hamiltonian)
# => -2.0
```

### Qing to QASM

```python
Circuit().h[0].to_qasm()
```

### Hamiltonian

```python
from qing.pauli import *

hamiltonian1 = (1.23 * Z[0] + 4.56 * X[1] * Z[2]) ** 2
hamiltonian2 = (2.46 * Y[0] + 5.55 * Z[1] * X[2] * X[1]) ** 2
hamiltonian = hamiltonian1 + hamiltonian2
print(hamiltonian)
```

### Simplify the Hamiltonian

```python
hamiltonian = hamiltonian.simplify()
print(hamiltonian)
```

### QUBO Hamiltonian

```python
from qing.pauli import qubo_bit as q

hamiltonian = -3*q(0)-3*q(1)-3*q(2)-3*q(3)-3*q(4)+2*q(0)*q(1)+2*q(0)*q(2)+2*q(0)*q(3)+2*q(0)*q(4)
print(hamiltonian)
```

### Time Evolution

```python
hamiltonian = [1.0*Z(0), 1.0*X[0]]
a = [term.get_time_evolution() for term in hamiltonian]

time_evolution = Circuit().h[0]
for evo in a:
    evo(time_evolution, np.random.rand())

print(time_evolution)
```

### QAOA

```python
from qing import Circuit
from qing.utils import qaoa
from qing.pauli import qubo_bit as q
from qing.pauli import X,Y,Z,I

hamiltonian = q(0)-q(1)
step = 1

result = qaoa(hamiltonian, step)
result.circuit.run(shots=100)
```

### Circuit Drawing Backend

```python
from qing import vqe
from qing.pauli import *
from qing.pauli import qubo_bit as q

hamiltonian = Z[0]-3*Z[1]+2*Z[0]*Z[1]+3*Z[2]*Z[3]+Z[4]
step = 8

result = vqe.Vqe(vqe.QaoaAnsatz(hamiltonian, step)).run()
result.circuit.run(backend='draw')
```

### Document

https://qing.readthedocs.io/en/latest/

### Contributors

[Contributors](https://github.com/Qing/Qing/graphs/contributors)

### Disclaimer

Copyright 2022 The DeepRecommend Developers.

# Qing
