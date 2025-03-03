from htmlnode import HTMLNode

class ParentNode(HTMLNode):
  def __init__(self, tag, children, props=None):
    super().__init__(tag, children, props)

  def to_html(self):
    if self.tag is None:
      raise ValueError("ParentNode must have a tag")
    if self.children is None:
      raise ValueError("ParentNode must have child node(s)")
    html_str = ""
    for child in self.children:
      html_str += child.to_html()
    return f"<{self.tag}>{html_str}</{self.tag}>"

