# xsltproc-py-lite

[![PyPI version](https://img.shields.io/pypi/v/xsltproc-py-lite.svg)](https://pypi.org/project/xsltproc-py-lite/)
[![Python versions](https://img.shields.io/pypi/pyversions/xsltproc-py-lite.svg)](https://pypi.org/project/xsltproc-py-lite/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

A lightweight Python reimplementation of `xsltproc`, supporting basic XSLT 1.0 transformations using `lxml`.

🔗 [View on PyPI](https://pypi.org/project/xsltproc-py-lite/)  
🔗 [GitHub Repository](https://github.com/takaakiaoki/xsltproc-py-lite)

---

## ✨ Features

- Apply XSLT 1.0 stylesheets to XML documents
- Outputs to file or standard output
- Zero-dependency CLI (except `lxml`)
- Simple and familiar `xsltproc`-like usage

---

## 📦 Installation

You can install this package from [PyPI](https://pypi.org/project/xsltproc-py-lite/):

```bash
pip install xsltproc-py-lite
```

---

## 🚀 Usage

```bash
xsltproc-py stylesheet.xsl input.xml -o output.xml
```

### Arguments
| Option           | Description                        |
| ---------------- | ---------------------------------- |
| `stylesheet.xsl` | Path to the XSLT file              |
| `input.xml`      | Path to the input XML file         |
| `-o output.xml`  | Output file path (default: stdout) |

---

## 🛠 Example
Given:

#### example.xsl
```xml
<xsl:stylesheet version="1.0"
 xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/">
    <hello>World</hello>
  </xsl:template>
</xsl:stylesheet>
```
#### input.xml

```xml
<root/>
```

Run:
```bash
xsltproc-py example.xsl input.xml -o result.xml
```

Output:
```xml
<hello>World</hello>
```

---

## ⚠ Limitations

* XSLT 1.0 only
* Does not support parameters (e.g., --stringparam)
* No support for chunking, profiling, or extensions

---

## 📄 License
This project is licensed under the [MIT License](LIiCENCE).

---
