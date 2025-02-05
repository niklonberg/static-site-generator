from enum import Enum

class TextType(Enum):
  NORMAL = 'text'
  BOLD = 'bold'
  ITALIC = 'italic'
  CODE = 'code'
  LINK = 'link'
  IMAGE = 'image'