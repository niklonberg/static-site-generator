import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
  def test_eq(self):
    node = TextNode("This is a text node", TextType.BOLD)
    node2 = TextNode("This is a text node", TextType.BOLD)
    self.assertEqual(node, node2)
  
  def test_unequal_text(self):
    node = TextNode("This is a text node", TextType.BOLD)
    node2 = TextNode("This is a different text node", TextType.BOLD)
    self.assertNotEqual(node, node2)

  def test_unequal_text_type(self):
    node = TextNode("This is a text node", TextType.ITALIC)
    node2 = TextNode("This is a text node", TextType.BOLD)
    self.assertNotEqual(node, node2)

  def test_empty_url(self):
    node = TextNode("This is a text node", TextType.BOLD, 'https://www.coca-cola.com')
    node2 = TextNode("This is a text node", TextType.BOLD)
    self.assertNotEqual(node, node2)
  
  def test_different_urls(self):
    node = TextNode("This is a text node", TextType.BOLD, 'https://www.coca-cola.com')
    node2 = TextNode("This is a text node", TextType.BOLD, 'https://www.pepsi.com')
    self.assertNotEqual(node, node2)

  def test_all_props_equal(self):
    node = TextNode("This is a text node", TextType.BOLD, 'https://www.coca-cola.com')
    node2 = TextNode("This is a text node", TextType.BOLD, 'https://www.coca-cola.com')
    self.assertEqual(node, node2)


if __name__ == "__main__":
  unittest.main()