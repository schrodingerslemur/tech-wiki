# Python modules which have helped me
## Typer (and Annotated)
This is used for CLIs.

1) Import modules
```python
import typer
from typing import Annotated
```
Note: `Annotated` is optional

2) Create app
```python
app = typer.Typer(add_completion=False)
```

3) Append `@app.command()` to `main()` function
```python
@app.command()
def main(
  arg1: Annotated[int, typer.argument(help="Input arg1")],
  arg2: Annotated[str, typer.argument(help="Input arg1")]
):
```
Note: you can do this to multiple functions

4) Define script entry point
```python
if __name__ == "__main__":
  app()
```

5) Using CLI
If you have one entry function:
```bash
python <script.py> [arg1] [arg2]
```

If you have multiple entry functions:
```bash
python <script.py> <function> [arg1] [arg2]
```

## Dataclass
This allows you to not have to define `__init__`, `__str__`, and `__eq__` functions, and to treat methods as properties.

### @dataclass
1) Import module
```python
import dataclasses from dataclass
```

2) Define class
```python
@dataclass
class Dog:
  name: str 
  age: int = 0
```
Hence, to create a class you can do `Max = Dog("Max", 2)`.

### @property
Define method
```python
class C:
  @property
  def x(self):
    return 42
```

Make class isntance
```python
c = C()
```

Now instead of doing `c.x()`, you can simply treat it like a property and do
```python
c.x
```


  
