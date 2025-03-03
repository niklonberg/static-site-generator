from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
  TEXT = 'text'
  BOLD = 'bold'
  ITALIC = 'italic'
  CODE = 'code'
  LINK = 'link'
  IMAGE = 'image'

class TextNode():
  def __init__(self, text, text_type: TextType, url=None):
    if not isinstance(text_type, TextType):
      raise TypeError("text_type must be a TextType enum member")
    self.text = text
    self.text_type = text_type
    self.url = url

  def __eq__(self, other):
    return (self.text == other.text and
            self.text_type == other.text_type and
            self.url == other.url)
    
  def __repr__(self):
    url_str = f"'{self.url}'" if self.url is not None else "None"
    return f"TextNode('{self.text}', '{self.text_type.value}', '{url_str}')"


def text_node_to_html_node(text_node: TextNode):
  match text_node.text_type:
    case TextType.TEXT:
      return LeafNode(None, text_node.text)
    case TextType.BOLD:
      return LeafNode("b", text_node.text)
    case TextType.ITALIC:
      return LeafNode("i", text_node.text)
    case TextType.CODE:
      return LeafNode("code", text_node.text)
    case TextType.LINK:
      return LeafNode("a", text_node.text, {"href": text_node.url})
    case TextType.IMAGE:
      return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    case _:
      raise Exception("Invalid TextNode type")