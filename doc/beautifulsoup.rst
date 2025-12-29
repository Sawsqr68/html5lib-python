BeautifulSoup Integration
=========================

html5lib can be used as a parser backend for `BeautifulSoup 4 <https://www.crummy.com/software/BeautifulSoup/>`_, 
providing HTML5-compliant parsing for your BeautifulSoup projects.

Using html5lib with BeautifulSoup
----------------------------------

To use html5lib as your BeautifulSoup parser, simply pass ``'html5lib'`` as the parser name:

.. code-block:: python

    from bs4 import BeautifulSoup
    
    markup = '<p>Hello <span>World</span>!</p>'
    soup = BeautifulSoup(markup, 'html5lib')
    
    print(soup.prettify())

This will output:

.. code-block:: html

    <html>
     <head>
     </head>
     <body>
      <p>
       Hello
       <span>
        World
       </span>
       !
      </p>
     </body>
    </html>

Key Differences from Other Parsers
-----------------------------------

When using html5lib with BeautifulSoup, there are some important differences compared to other parsers:

Document Structure
~~~~~~~~~~~~~~~~~~

html5lib always creates a complete HTML5 document structure, even when parsing fragments:

.. code-block:: python

    from bs4 import BeautifulSoup
    
    markup = '<p>Fragment</p>'
    
    # With html5lib - adds full document structure
    soup_html5lib = BeautifulSoup(markup, 'html5lib')
    print(soup_html5lib.html is not None)  # True
    print(soup_html5lib.body is not None)  # True
    
    # With html.parser - keeps it as a fragment
    soup_htmlparser = BeautifulSoup(markup, 'html.parser')
    print(soup_htmlparser.html is None)  # True
    print(soup_htmlparser.body is None)  # True

Error Handling
~~~~~~~~~~~~~~

html5lib follows the HTML5 specification's error handling rules, which means it will:

- Automatically close unclosed tags
- Fix misnested tags
- Handle invalid markup gracefully

.. code-block:: python

    from bs4 import BeautifulSoup
    
    # Malformed HTML with missing closing tags
    markup = '<p>Paragraph 1<p>Paragraph 2'
    soup = BeautifulSoup(markup, 'html5lib')
    
    # html5lib properly closes and structures the paragraphs
    paragraphs = soup.find_all('p')
    print(len(paragraphs))  # 2

Encoding Detection
~~~~~~~~~~~~~~~~~~

html5lib has sophisticated encoding detection capabilities and handles various character encodings correctly:

.. code-block:: python

    from bs4 import BeautifulSoup
    
    markup = '<p>Héllo Wörld</p>'
    soup = BeautifulSoup(markup, 'html5lib')
    
    print('Héllo' in soup.get_text())  # True
    print('Wörld' in soup.get_text())  # True

When to Use html5lib
--------------------

Consider using html5lib with BeautifulSoup when you need:

- **HTML5 compliance**: You want parsing that matches how modern web browsers handle HTML
- **Robust error handling**: You're dealing with malformed or broken HTML
- **Consistent behavior**: You need parsing that follows the HTML5 specification exactly
- **Encoding detection**: You're working with documents in various character encodings

Performance Considerations
--------------------------

html5lib prioritizes correctness and compliance over speed. If you're parsing large amounts of HTML and performance is critical, you might want to consider other parsers like lxml. However, if correctness and compliance with HTML5 standards are more important than raw speed, html5lib is an excellent choice.

Installation
------------

To use html5lib with BeautifulSoup, you need to install both packages:

.. code-block:: bash

    pip install beautifulsoup4 html5lib

Limitations
-----------

When using html5lib with BeautifulSoup, note these limitations:

- ``SoupStrainer`` is not supported - the entire document will be parsed
- Some BeautifulSoup features that depend on custom element types may not work
- html5lib is generally slower than other parsers

Example: Complete Workflow
---------------------------

Here's a complete example showing how to use html5lib with BeautifulSoup:

.. code-block:: python

    from bs4 import BeautifulSoup
    
    # Read HTML from a file or string
    html_content = '''
    <html>
        <head><title>Example Page</title></head>
        <body>
            <h1>Welcome</h1>
            <p>This is a <a href="/page1">link</a></p>
            <p>Another <a href="/page2">link</a></p>
        </body>
    </html>
    '''
    
    # Parse with html5lib for HTML5-compliant parsing
    soup = BeautifulSoup(html_content, 'html5lib')
    
    # Navigate the parse tree
    title = soup.find('title')
    print('Page title: {}'.format(title.get_text()))
    
    # Find all links
    links = soup.find_all('a')
    for link in links:
        href = link.get('href')
        text = link.get_text()
        print('{}: {}'.format(text, href))

See Also
--------

- `BeautifulSoup Documentation <https://www.crummy.com/software/BeautifulSoup/bs4/doc/>`_
- `HTML5 Specification <https://html.spec.whatwg.org/>`_
