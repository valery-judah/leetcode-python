# Import Formatting Example

This document demonstrates the correct import formatting that will be used in all generated Python code, following the `RuffI001` rule.

## Example

```python
from __future__ import annotations

from typing import List, Dict
import os
import sys

from my_package import my_module
```

As you can see, there is a blank line separating the `__future__` import from the standard library imports, and another blank line separating the standard library imports from the third-party imports. This is the correct way to format imports according to the `RuffI001` rule.
