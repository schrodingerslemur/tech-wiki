# Setup
```
uv init
```

## Adding modules
```
uv add <module_names>
```
Note: always use `uv add` instead of `uv pip install`

## Running jupyter
```
uv run jupyter lab
```
Note: restart kernel after downloading modules

### Cache directories
```
uv add <module_names> --cache-dir [path_to_cache_directory]
```
Use this to set different cache directories (e.g. if running out of space in AFS)
