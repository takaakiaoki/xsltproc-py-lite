# xsltproc-py-lite

A lightweight Python+lxml implementation of `xsltproc` command-line tool.

## Features

- Apply XSLT 1.0 stylesheets to XML documents
- Output to file (`-o`) or stdout

## Installation

```
pip install xsltproc-py-lite
```


## Usage

```
xsltproc-py style.xsl input.xml -o output.xml
```

Use `-o -` or omit `-o` to output to stdout.

## Limitations

- Only a subset of xsltproc's features (no chunking, no profiling, etc.)
- Based on lxml and XSLT 1.0

## License

MIT
