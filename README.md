# ffi48

A Python package to classify SIC codes into Fama and French 48 industries.

## Installation

```bash
pip install ffi48
```

## Usage

```python
from ffi48 import ffi48

result = ffi48(2000)
print(result)  # Output: {'FFI48': 2, 'FFI48_desc': 'Food'}
```
