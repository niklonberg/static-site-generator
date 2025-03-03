import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
  def test_leaf_to_html_p(self):
    node = LeafNode("p", 'Hello world!')
    self.assertEqual(node.to_html(), "<p>Hello world!</p>")

  def test_leaf_to_html_a(self):
    node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')
  
  def test_leaf_to_html_no_tag(self):
    node = LeafNode(None, 'Raw text here.')
    self.assertEqual(node.to_html(), 'Raw text here.')

  def test_leaf_to_html_no_value(self):
    node = LeafNode('p', None)
    with self.assertRaises(ValueError):
      node.to_html()

  def test_leaf_to_html_multi_props(self):
    node = LeafNode('a', 'Click here', {"href": "https://example.com", "target": "_blank", "class": "link-button"})
    self.assertEqual(node.to_html(), '<a href="https://example.com" target="_blank" class="link-button">Click here</a>')