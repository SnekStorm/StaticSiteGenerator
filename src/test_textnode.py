import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_eq2(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        node2 = TextNode("This is a text node", TextType.BOLD, None)
        self.assertEqual(node, node2)
    
    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD, "www.boot.dev")
        self.assertEqual(node, node2)
    
    # ----------------------------------------
    def test_not_eq1(self):
        node = TextNode("This is not a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_eq2(self):
        node1 = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_not_eq3(self):
        node1 = TextNode("This is a text node", TextType.BOLD, None)
        node2 = TextNode("This is a text node", TextType.BOLD, "www.boot.dev")
        self.assertNotEqual(node1, node2)

    def test_not_eq4(self):
        node1 = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is not a text node", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    


if __name__ == "__main__":
    unittest.main()