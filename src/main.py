from textnode import TextNode, TextType

def main():
  test = TextNode('Some text', TextType.BOLD, 'https://www.ducksarecool.com')
  print(test)

main()