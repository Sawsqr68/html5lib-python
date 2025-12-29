# html5lib Examples

This directory contains example scripts demonstrating various uses of html5lib.

## BeautifulSoup Integration

**File:** `beautifulsoup_example.py`

This example demonstrates how to use html5lib as a parser backend for BeautifulSoup. It compares the behavior of html5lib with Python's built-in html.parser and shows the advantages of using html5lib for HTML5-compliant parsing.

To run:
```bash
python beautifulsoup_example.py
```

Requirements:
- beautifulsoup4
- html5lib

## About html5lib

html5lib is a pure-Python library for parsing HTML. It is designed to conform to the WHATWG HTML specification, as implemented by all major web browsers. This makes it particularly useful when you need parsing behavior that matches what browsers do, rather than just parsing valid HTML.
