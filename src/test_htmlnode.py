import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
  def test_props_is_none(self):
    node = HTMLNode('p', 'Test text')
    self.assertEqual(node.props_to_html(), '')

  def test_single_prop(self):
    node = HTMLNode('p', 'Test text', None, {"href": "https://www.google.com"})
    self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')

  def test_multiple_props(self):
    node = HTMLNode('p', 'Test text', None, {
      "href": "https://www.google.com", 
      "target": "_blank"
    })
    result = node.props_to_html()
    self.assertIn('href="https://www.google.com"', result)
    self.assertIn('target="_blank"', result)