# GitHub Flavored Markdown (GFM) Examples

> Taken from: [GitHub Flavored Markdown Spec](https://github.github.com/gfm/)

## Leaf Block Examples

### Thematic Breaks

***

---

___

### ATX Headings

# H1
## H2
### H3
#### H4
##### H5
###### H6

### Setext Headings

Foo *bar*
=========

Foo *bar*
---------

### Indented Code Blocks

    This is a simple
        indented code block.

### Fenced Code Blocks

```python
def main():
    print("Hello, World!")
```

### HTML Block

<html>
  <body>
    <p>This is a paragraph inside an HTML block.</p>
  </body>
</html>

### Line Reference Definitions

[foo]: /url "title"

[foo]

### Paragraph

aaa

bbb

### Table

| foo | bar |
| --- | --- |
| baz | bim |

## Container Block Examples

### Block Quotes

> This is a block quote.
>
> It has two paragraphs.

> This is another block quote.
>
> It has a list:
> - item one
> - item two
>
> > This is a nested block quote.

### Lists

* One
* Two
* Three

1. One
2. Two
3. Three
    - One
    - Two
    - Three
