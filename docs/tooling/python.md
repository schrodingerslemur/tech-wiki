# CLI building
## Typer and Annotated
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

  
