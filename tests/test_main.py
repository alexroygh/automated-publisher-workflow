import pytest
from main import extract_text_from_html

def test_extract_text_from_html_removes_scripts_and_styles():
    html = """
    <html><head><style>body {color: red;}</style><script>alert('hi');</script></head>
    <body><h1>Title</h1><p>Some text.</p></body></html>
    """
    result = extract_text_from_html(html)
    assert "alert" not in result
    assert "body {color: red;}" not in result
    assert "Title" in result
    assert "Some text." in result 