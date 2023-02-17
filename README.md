# batch-apply

Given a function and a pandas.DataFrame, execute the function with each row of DataFrame as kwargs.

Successful status and error messages are appened as columns of the pandas.DataFrame

## Install

```bash
pip install batch_apply
```

## Usage

```python
import pandas as pd
from batch_apply import batch_apply

def function(var1,var2,...):
    # calculte with var1, va2, etc...
    # results output with side effects
    return None

args = pd.DataFrame({
    "var1": array1,
    "var2": array2,
    ...
})

batch_apply(function, args)
```
