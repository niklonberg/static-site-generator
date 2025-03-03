from enum import Enum

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
    
