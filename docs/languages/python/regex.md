# Regex (Regular Expressions)

## Usage (Python)
```python
import re
```

## Basic match
```python
re.search(r"abc", text)        # finds first match
re.match(r"abc", text)         # matches from start only
re.findall(r"abc", text)       # returns all matches
re.sub(r"abc", "def", text)    # replaces matches with "def"
```

## Character classes
```python
.       # any character except newline
\d      # digit [0-9]
\w      # word char [a-zA-Z0-9_]
\s      # whitespace

[abc]   # a or b or c
[a-z]   # range
[^0-9]  # not a digit
```

## Quantifiers
```python
*       # 0 or more
+       # 1 or more
?       # 0 or 1
{n}     # exactly n
{n,}    # n or more
{n,m}   # between n and m
```

## Anchors
```python
^       # start of string
$       # end of string
\b      # word boundary
```

## Groups and Alternation
```python
(abc)       # capture group
(?:abc)     # non-capturing group

# examples
m = re.search(r"(\d+)-(\d+)", "12-34")
m.group(1)      # "12"
m.group(2)      # "34"

# Alternation
re.search(r"cat|dog", text)   # matches "cat" or "dog"
```

## Examples
```python
# Check if string is a number
re.fullmatch(r"\d+", "12345")      # match
re.fullmatch(r"\d+", "12a45")      # no match

# Extract words from a string
re.findall(r"\w+", "Hello, world!")    # ["Hello", "world"]

# Replace multiple spaces with a single space
re.sub(r"\s+", " ", "a   b    c")   # "a b c"
```
