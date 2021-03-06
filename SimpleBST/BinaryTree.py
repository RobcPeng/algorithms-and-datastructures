from node import Node

class BinaryTree(object):

	def __init__(self, root = None):
		self.root = None

	def add(self, root, cargo):
		node = Node(cargo)
		if not root:
			root = node
		elif cargo <= root.cargo:
			root.left = self.add(root.left, cargo)
		elif cargo >= root.cargo:
			root.right = self.add(root.right, cargo)
		return root

	def print_node(self, root):
		if not root:
			pass
		else:
			self.print_node(root.left)
			print(root.cargo)
			self.print_node(root.right)

	def search(self, root, number):
		if not root:
			pass
		else:
			if root.cargo == number:
				return "found"
			elif root.cargo > number:
				self.search(root.left, number)
			else:
				self.search(root.right, number)


# a = BinaryTree(0)
# a.root = Node(5)
# a.add(a.root,3)
# a.add(a.root,2)
# a.add(a.root,1)
# a.add(a.root,4)
# a.add(a.root,5)
# a.add(a.root,6)
# a.add(a.root,7)
# a.print_node(a.root)
# a.search(a.root,5)
# a.search(a.root,15)
