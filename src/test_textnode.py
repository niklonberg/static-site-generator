import unittest

from textnode import TextNode, TextType, text_node_to_html_node

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


class TestTextNodeToHTMLNode(unittest.TestCase):
  def test_text(self):
    node = TextNode("This is a text node", TextType.TEXT)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, None)
    self.assertEqual(html_node.value, "This is a text node")

  def test_bold(self):
    node = TextNode('Bold text', TextType.BOLD)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, 'b')
    self.assertEqual(html_node.value, "Bold text")

  def test_italic(self):
    node = TextNode('Italic text', TextType.ITALIC)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, 'i')
    self.assertEqual(html_node.value, "Italic text")

  def test_code(self):
    node = TextNode('Code text', TextType.CODE)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, 'code')
    self.assertEqual(html_node.value, "Code text")

  def test_link(self):
    node = TextNode('Go to support', TextType.LINK, "https://www.example.com")
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, 'a')
    self.assertEqual(html_node.value, 'Go to support')
    self.assertEqual(html_node.props, {'href': 'https://www.example.com'})

  def test_image(self):
    node = TextNode('Cute cat', TextType.IMAGE, "/cute-cat.jpg")
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, 'img')
    self.assertEqual(html_node.value, '')
    self.assertEqual(html_node.props, {'src': "/cute-cat.jpg", 'alt': 'Cute cat'})

  def test_invalid_texttype(self):
    node = TextNode("This won't work", TextType.TEXT)
    node.text_type = "invalid_type"
    with self.assertRaises(Exception):
      text_node_to_html_node(node)

if __name__ == "__main__":
  unittest.main()