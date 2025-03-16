# PowerGrid - TSO Finder

[![PyPI Version](https://img.shields.io/pypi/v/powergrid.svg)](https://pypi.org/project/powergrid/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python Versions](https://img.shields.io/pypi/pyversions/powergrid.svg)](https://pypi.org/project/powergrid/)

PowerGrid is a **high-performance Python library** for looking up **Transmission System Operators (TSOs)** based on **ISO country-region codes**.

> **📝 Note:** This version currently supports **French region codes only**.  
> 🎯 **Contributors are welcome** to extend it to other countries!  


> 📝 **Version 0.2.1:**
> - ✅ **Now handle TSO for Germany and Corsica.
> 
> 📝 **Version 0.2.0:**
> - ✅ **Now returns full `Tso` objects** instead of just IDs.
> - ✅ **Uses a shared `constants.py` file** for managing data source paths.
> - ✅ **Case-insensitive searches for region codes & ENTSO-E codes.**

## 🚀 Features

✅ **Blazing-fast in-memory lookup**  
✅ **Search by**:
- **Region code** (ISO 3166-2)
- **TSO ID**
- **ENTSO-E Code**

✅ **Case-insensitive searches**  
✅ **Optimized for REST APIs and large-scale queries**

## 📦 Installation

### **Using PyPI**
PowerGrid is available on PyPI at https://pypi.org/project/powergrid/

Install it with:
```sh
uv pip install powergrid
```

## 🛠 API Reference

### TsoFinder

#### Initialize the Finder
```python
from tso_finder import TsoFinder
finder = TsoFinder()
```

#### Lookup by Region Code
```python
print(finder.by_region("FR-IDF"))  # Output: "TSO_FR_001"
```

#### Lookup by TSO ID
```python
print(finder.by_tsoid("TSO_FR_001"))  # Output: ["FR-IDF", "FR-ARA", ...]
```

#### Lookup by ENTSO-E Code
```python
print(finder.by_entsoe("10YFR-RTE------C"))  # Output: <Tso object for RTE>
```

## 🏗 Contributing
We welcome contributions!

To contribute:

1. Fork the repo and create a branch.
2. Add your feature or fix a bug.
3. Submit a pull request.

## 📜 License
PowerGrid is MIT Licensed.

See the LICENSE file for details.

## 💡 Why Use PowerGrid?
- Fast: Precomputes mappings for instant lookups.
- Scalable: Can handle large-scale queries efficiently.
- Reliable: Designed for TSO data accuracy.

