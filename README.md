# PowerGrid - TSO Finder

[![PyPI Version](https://img.shields.io/pypi/v/powergrid.svg)](https://pypi.org/project/powergrid/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python Versions](https://img.shields.io/pypi/pyversions/powergrid.svg)](https://pypi.org/project/powergrid/)
[![Tests](https://github.com/cameraink/powergrid/actions/workflows/tests.yml/badge.svg)](https://github.com/cameraink/powergrid/actions)

PowerGrid is a **high-performance Python library** for looking up **Transmission System Operators (TSOs)** based on **ISO country-region codes**.

## 🚀 Features

✅ **Blazing-fast in-memory lookup**  
✅ **Search by**:
- **Region code** (ISO 3166-2)
- **TSO ID**
- **ENTSO-E Code**
✅ **Case-insensitive searches**  
✅ **Optimized for REST APIs and large-scale queries**  
✅ **Multi-threaded for high-performance lookups**  

---

## 📦 Installation

### **Using PyPI**
PowerGrid is available on PyPI. Install it with:
```sh
uv pip install powergrid
```

## 📖 Usage
### Initialize the Finder
```python
from tso_finder import TsoFinder
finder = TsoFinder()
```
### Lookup by Region Code
```python
print(finder.by_region("FR-IDF"))  # Output: "TSO_FR_001"
```

### Lookup by TSO ID
```python
print(finder.by_tsoid("TSO_FR_001"))  # Output: ["FR-IDF", "FR-ARA", ...]
```

### Lookup by ENTSO-E Code
```python
print(finder.by_entsoe("10YFR-RTE------C"))  # Output: <Tso object for RTE>
```

## 🛠 API Reference
### TsoFinder
```python
finder = TsoFinder()
```
- Loads TSO data from ../data/tso_data.json
- Precomputes reverse lookup mappings for fast queries.

Finds the TSO ID for a given region.
```python
finder.by_region("FR-IDF")  # "TSO_FR_001"
```

Finds all regions managed by a given TSO.
```python
finder.by_tsoid("TSO_FR_001")  # ["FR-IDF", "FR-ARA", ...]
```

Finds a TSO object using an ENTSO-E code.
```python
finder.by_entsoe("10YFR-RTE------C")
```

## 🏗 Contributing
👥 We welcome contributions!
To contribute:

1. Fork the repo and create a branch.
2. Add your feature or fix a bug.
3. Submit a pull request.

## 📜 License
PowerGrid is MIT Licensed. See the LICENSE file for details.

## 💡 Why Use PowerGrid?
- Fast: Precomputes mappings for instant lookups.
- Scalable: Can handle large-scale queries efficiently.
- Reliable: Designed for TSO data accuracy.

