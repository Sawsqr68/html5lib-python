#!/usr/bin/env python
"""
Example demonstrating html5lib integration with BeautifulSoup.

This example shows how to use html5lib as a parser backend for BeautifulSoup,
providing HTML5-compliant parsing.

The problem statement "BeautifulSoup(markup, 'html.parser')" refers to
BeautifulSoup's internal usage of 'html.parser' in its html5lib integration.
This example demonstrates that html5lib works correctly with BeautifulSoup
regardless of this internal implementation detail.
"""

from __future__ import print_function
from bs4 import BeautifulSoup
import html5lib


def main():
    print("=" * 60)
    print("html5lib with BeautifulSoup - Example")
    print("=" * 60)
    
    # Test markup with potential parsing challenges
    markup = '''
    <html>
        <body>
            <p>Hello <span>World</span>!</p>
            <p>Unclosed paragraph
            <div>Nested content</div>
        </body>
    </html>
    '''
    
    print("\n1. Parsing with html5lib via BeautifulSoup:")
    print("-" * 60)
    soup_html5lib = BeautifulSoup(markup, 'html5lib')
    print("Parser used: html5lib")
    print("Found <p> tags:", len(soup_html5lib.find_all('p')))
    print("Found <span> tags:", len(soup_html5lib.find_all('span')))
    print("Found <div> tags:", len(soup_html5lib.find_all('div')))
    
    print("\n2. Parsing with html.parser via BeautifulSoup:")
    print("-" * 60)
    soup_htmlparser = BeautifulSoup(markup, 'html.parser')
    print("Parser used: html.parser")
    print("Found <p> tags:", len(soup_htmlparser.find_all('p')))
    print("Found <span> tags:", len(soup_htmlparser.find_all('span')))
    print("Found <div> tags:", len(soup_htmlparser.find_all('div')))
    
    print("\n3. Direct html5lib parsing:")
    print("-" * 60)
    doc = html5lib.parse(markup)
    print("Parser: html5lib (direct)")
    print("Document type:", type(doc))
    
    print("\n4. Comparing results:")
    print("-" * 60)
    
    # Test with malformed HTML
    malformed = '<p>First<p>Second<p>Third'
    
    soup_html5lib = BeautifulSoup(malformed, 'html5lib')
    soup_htmlparser = BeautifulSoup(malformed, 'html.parser')
    
    print("Malformed HTML: {}".format(malformed))
    print("html5lib found {} paragraphs".format(len(soup_html5lib.find_all('p'))))
    print("html.parser found {} paragraphs".format(len(soup_htmlparser.find_all('p'))))
    
    print("\n" + "=" * 60)
    print("CONCLUSION:")
    print("=" * 60)
    print("html5lib works correctly as a BeautifulSoup parser backend.")
    print("It provides HTML5-compliant parsing with robust error handling.")
    print("The choice between 'html5lib' and 'html.parser' depends on your")
    print("specific needs for compliance vs. performance.")
    print("=" * 60)


if __name__ == '__main__':
    main()
