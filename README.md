# aiojarm

![CI](https://github.com/ninoseki/aiojarm/workflows/CI/badge.svg)
[![PyPI version](https://badge.fury.io/py/aiojarm.svg)](https://badge.fury.io/py/aiojarm)

Async version of [JARM](https://github.com/salesforce/jarm).

## Installation

```bash
pip install aiojarm
```

## Usage

```python
import asyncio
import aiojarm

loop = asyncio.get_event_loop()
fingerprints = loop.run_until_complete(
    asyncio.gather(
        aiojarm.scan("www.salesforce.com"),
        aiojarm.scan("www.google.com"),
        aiojarm.scan("www.facebook.com"),
        aiojarm.scan("github.com"),
    )
)
print(fingerprints)
# [
#     (
#         "www.salesforce.com",
#         443,
#         "23.42.156.194",
#         "2ad2ad0002ad2ad00042d42d00000069d641f34fe76acdc05c40262f8815e5",
#     ),
#     (
#         "www.google.com",
#         443,
#         "172.217.25.228",
#         "27d40d40d29d40d1dc42d43d00041d4689ee210389f4f6b4b5b1b93f92252d",
#     ),
#     (
#         "www.facebook.com",
#         443,
#         "31.13.82.36",
#         "27d27d27d29d27d1dc41d43d00041d741011a7be03d7498e0df05581db08a9",
#     ),
#     (
#         "github.com",
#         443,
#         "52.192.72.89",
#         "29d29d00029d29d00041d41d0000008aec5bb03750a1d7eddfa29fb2d1deea",
#     ),
# ]
```

## License

JARM is created by Salesforce's JARM team and it is licensed with 3-Clause "New" or "Revised" License.

- https://github.com/salesforce/jarm/blob/master/LICENSE.txt
