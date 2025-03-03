import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
  def test_to_html_with_children(self):
    child = LeafNode('p', 'child text')
    parent = ParentNode('div', [child])
    self.assertEqual(parent.to_html(), '<div><p>child text</p></div>')

  def test_to_html_with_grandchildren(self):
    grandchild = LeafNode('b', 'grandchild')
    child = ParentNode("span", [grandchild])
    parent = ParentNode("div", [child])
    self.assertEqual(
        parent.to_html(),
        "<div><span><b>grandchild</b></span></div>",
    )
  
  def test_to_html_no_children(self):
    parent = ParentNode('div', None)
    with self.assertRaises(ValueError):
      parent.to_html()

  def test_parentnode_requires_children(self):
    with self.assertRaises(TypeError):
        ParentNode('div')
  
  def test_to_html_empty_children_list(self):
    parent = ParentNode('div', [])
    self.assertEqual(parent.to_html(), '<div></div>')
