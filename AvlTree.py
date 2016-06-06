# -*- coding: utf-8 -*-

import BinarySearchTree

class Node(BinarySearchTree.Node):
	def __init__(self, value):
		BinarySearchTree.Node.__init__(self, value)
		self.m_Balance = 0

	def getBalance(self):
		return self.m_Balance

	def setBalance(self, balance):
		self.m_Balance = balance

	def decreaseBalance(self):
		self.m_Balance -= 1

	def increaseBalance(self):
		self.m_Balance += 1

	def isCritical(self):
		return not (-1 <= self.m_Balance <= +1)

	def doSingleLeftRotation(self):
		rightChild = self.getRightChild()

		self.setRightChild(rightChild.getLeftChild())
		self.setBalance(0)

		rightChild.setLeftChild(self)
		rightChild.setBalance(0)

		if (self.getParent() != None):
			if (self == self.getParent().getLeftChild()):
				self.getParent().setLeftChild(rightChild)
			else:
				self.getParent().setRightChild(rightChild)

		rightChild.setParent(self.getParent())
		self.setParent(rightChild)

		return rightChild

	def doSingleRightRotation(self):
		leftChild = self.getLeftChild()

		self.setLeftChild(leftChild.getRightChild())
		self.setBalance(0)

		leftChild.setRightChild(self)
		leftChild.setBalance(0)

		if (self.getParent() != None):
			if (self == self.getParent().getLeftChild()):
				self.getParent().setLeftChild(leftChild)
			else:
				self.getParent().setRightChild(leftChild)

		leftChild.setParent(self.getParent())
		self.setParent(leftChild)

		return leftChild

	def doLeftRightRotation(self):
		self.getLeftChild().doSingleLeftRotation()
		return self.doSingleRightRotation()


	def doRightLeftRotation(self):
		self.getRightChild().doSingleRightRotation()
		return self.doSingleLeftRotation()

	def rebalance(self):
		if (self.getBalance() == +2):
			if (self.getLeftChild().getBalance() == +1):
				return self.doSingleRightRotation()
			elif (self.getLeftChild().getBalance() == -1):
				return self.doLeftRightRotation()
		elif (self.getBalance() == -2):
			if (self.getRightChild().getBalance() == -1):
				return self.doSingleLeftRotation()
			elif (self.getRightChild().getBalance() == +1):
				return self.doRightLeftRotation()

class Tree(BinarySearchTree.Tree):
	def insert(self, value):
		prev = None
		temp = self.m_Root

		#
		# Go down the tree to see where should the node be added.
		#
		while (temp != None):
			prev = temp
			temp = temp.getLeftChild() if (value < temp) else temp.getRightChild()

		#
		# Insert the new node: replacing the root if the tree was empty,
		# adding it to the last node encountered otherwise.
		#
		node = Node(value)

		if (prev == None):
			self.m_Root = node
		else:
			node.setParent(prev)

			if (value < prev):
				prev.setLeftChild(node)
			else:
				prev.setRightChild(node)

		#
		# Go up the tree again to adjust balance factor: we stop if we get a
		# node with a balance factor of 0 -- where its parents need no more
		# adjustments -- or when one becomes a "critical node", case in which
		# we rebalance its subtree by performing a single or double rotation.
		#
		temp = prev
		prev = node

		while (temp != None):
			if (prev < temp):
				temp.increaseBalance()
			else:
				temp.decreaseBalance()

			if (temp.getBalance() == 0):
				break

			if (temp.isCritical()):
				newNode = temp.rebalance()

				if (newNode != None) and (newNode.getParent() == None):
					self.setRootNode(newNode)

				break

			prev = temp
			temp = temp.getParent()
