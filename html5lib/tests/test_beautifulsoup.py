"""
Tests for html5lib integration with BeautifulSoup4.

These tests verify that html5lib works correctly as a parser backend for BeautifulSoup.
"""

from __future__ import absolute_import, division, unicode_literals

import pytest

# Check if BeautifulSoup is available
try:
    from bs4 import BeautifulSoup
    has_bs4 = True
except ImportError:
    has_bs4 = False

import html5lib


class TestBeautifulSoupIntegration:
    """Test html5lib's integration with BeautifulSoup4."""

    @pytest.mark.skipif(not has_bs4, reason="BeautifulSoup4 not installed")
    def test_html5lib_as_parser(self):
        """Test that html5lib can be used as a BeautifulSoup parser."""
        markup = '<p>Hello <span>World</span>!</p>'
        soup = BeautifulSoup(markup, 'html5lib')
        
        # html5lib adds full document structure
        assert soup.html is not None
        assert soup.body is not None
        assert soup.find('p') is not None
        assert soup.find('span') is not None
        assert 'World' in soup.get_text()

    @pytest.mark.skipif(not has_bs4, reason="BeautifulSoup4 not installed")
    def test_html5lib_vs_html_parser(self):
        """Compare html5lib and html.parser behavior with BeautifulSoup."""
        markup = '<p>Hello <span>World</span>!</p>'
        
        # Parse with html5lib
        soup_html5lib = BeautifulSoup(markup, 'html5lib')
        
        # Parse with html.parser
        soup_htmlparser = BeautifulSoup(markup, 'html.parser')
        
        # Both should find the same content
        assert soup_html5lib.find('p') is not None
        assert soup_htmlparser.find('p') is not None
        assert soup_html5lib.find('span').get_text() == soup_htmlparser.find('span').get_text()
        
        # html5lib adds full document structure
        assert soup_html5lib.html is not None
        assert soup_html5lib.body is not None
        
        # html.parser doesn't add document structure for fragments
        assert soup_htmlparser.html is None
        assert soup_htmlparser.body is None

    @pytest.mark.skipif(not has_bs4, reason="BeautifulSoup4 not installed")
    def test_html5lib_with_malformed_html(self):
        """Test that html5lib handles malformed HTML correctly with BeautifulSoup."""
        # Missing closing tags
        markup = '<p>Paragraph 1<p>Paragraph 2'
        soup = BeautifulSoup(markup, 'html5lib')
        
        # html5lib should properly close tags
        paragraphs = soup.find_all('p')
        assert len(paragraphs) == 2

    @pytest.mark.skipif(not has_bs4, reason="BeautifulSoup4 not installed")
    def test_html5lib_encoding(self):
        """Test encoding handling with html5lib and BeautifulSoup."""
        # UTF-8 content
        markup = '<p>Héllo Wörld</p>'
        soup = BeautifulSoup(markup, 'html5lib')
        
        assert 'Héllo' in soup.get_text()
        assert 'Wörld' in soup.get_text()

    @pytest.mark.skipif(not has_bs4, reason="BeautifulSoup4 not installed")
    def test_html5lib_attributes(self):
        """Test attribute handling with html5lib and BeautifulSoup."""
        markup = '<div id="test" class="foo bar">Content</div>'
        soup = BeautifulSoup(markup, 'html5lib')
        
        div = soup.find('div')
        assert div is not None
        assert div.get('id') == 'test'
        assert 'foo' in div.get('class', [])
        assert 'bar' in div.get('class', [])

    @pytest.mark.skipif(not has_bs4, reason="BeautifulSoup4 not installed")
    def test_html5lib_empty_document(self):
        """Test parsing empty or minimal documents with html5lib."""
        soup = BeautifulSoup('', 'html5lib')
        
        # Even empty input should have basic document structure
        assert soup.html is not None

    @pytest.mark.skipif(not has_bs4, reason="BeautifulSoup4 not installed")
    def test_direct_html5lib_vs_beautifulsoup(self):
        """Compare direct html5lib parsing with BeautifulSoup integration."""
        markup = '<p>Test content</p>'
        
        # Direct html5lib parsing
        doc = html5lib.parse(markup)
        
        # Through BeautifulSoup
        soup = BeautifulSoup(markup, 'html5lib')
        
        # Both should successfully parse the content
        assert doc is not None
        assert soup is not None
        assert soup.find('p') is not None
