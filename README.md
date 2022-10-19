# Deeq

Quantum Computing SDK

### Version

[![Version](https://badge.fury.io/py/deeq.svg)](https://badge.fury.io/py/deeq)

### Tutorial

https://github.com/Deeq/Deeq-tutorials

### Notice

The back end has been changed to tensor network. The previous backend environment can still be used with .run(backend="numpy").

### Install

```
git clone https://github.com/Deeq/Deeq
cd Deeq
pip3 install -e .
```

or

```
pip3 install deeq
```

### Circuit

```python
from deeq import QAOA, QML, QNN
```

### Method Chain

```python
Circuit().h[0].x[0].z[0]

c = Circuit().h[0]
c.x[0].z[0]
```

### Document


### Contributors

[Contributors](https://github.com/deep-recommend)

### Disclaimer

Copyright 2022 The DeepRecommend Developers.

# Deeq
