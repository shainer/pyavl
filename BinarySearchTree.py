# -*- coding: utf-8 -*-

import exceptions

class Node:
	def __init__(self, value):
		self.m_Parent = None
		self.m_LeftChild = None
		self.m_RightChild = None
		self.m_Value = value

	def getLeftChild(self):
		return self.m_LeftChild

	def setLeftChild(self, node):
		self.m_LeftChild = node

	def getRightChild(self):
		return self.m_RightChild

	def setRightChild(self, node):
		self.m_RightChild = node

	def getParent(self):
		return self.m_Parent

	def setParent(self, node):
		self.m_Parent = node

	def getValue(self):
		return self.m_Value

	def setValue(self, value):
		self.m_Value = value

	def getSubtreeMinimum(self):
		temp = self

		while (temp.getLeftChild() != None):
			temp = temp.getLeftChild()

		return temp

	def getSubtreeMaximum(self):
		temp = self

		while (temp.getRightChild() != None):
			temp = temp.getRightChild()

		return temp

	def __cmp__(self, other):
		if isinstance(other, Node):
			return cmp(self.getValue(), other.getValue())

		return cmp(self.getValue(), other)

class Tree:
	def __init__(self):
		self.m_Root = None

	def getRootNode(self):
		return self.m_Root

	def setRootNode(self, node):
		self.m_Root = node

	def insert(self, value):
		prev = None
		temp = self.m_Root

		while (temp != None):
			prev = temp
			temp = temp.getLeftChild() if (value < temp) else temp.getRightChild()

		node = Node(value)

		if (prev == None):
			self.m_Root = node
		else:
			node.setParent(prev)

			if (value < prev):
				prev.setLeftChild(node)
			else:
				prev.setRightChild(node)

	def search(self, value):
		temp = self.m_Root

		while (temp != None) and (temp != value):
			temp = temp.getLeftChild() if (value < temp) else temp.getRightChild()

		return temp

	def deleteValue(self, value):
		node = self.search(value)

		if (node != None):
			self.deleteNode(node)

	def deleteNode(self, node):
		nodeToDelete = node
		nodeToLink = None
		parent = None

		if (node.getLeftChild() != None) or (node.getRightChild() != None):
			if (node.getLeftChild() != None):
				nodeToLink = node.getLeftChild()
			elif (node.getRightChild() != None):
				nodeToLink = node.getRightChild()
			else:
				nodeToDelete = node.getSuccessor()

		parent = nodeToDelete.getParent()

		if (parent != None):
			if (parent.getRightChild() == nodeToDelete):
				parent.setRightChild(nodeToLink)
			else:
				parent.setLeftChild(nodeToLink)

		if (nodeToLink != None):
			nodeToLink.setParent(parent)

		if (nodeToDelete != node):
			node.setValue(nodeToDelete.getValue())

		if (nodeToDelete == self.m_Root):
			self.m_Root = None

	def getMinimum(self):
		if (self.m_Root != None):
			self.m_Root.getSubtreeMinimum().getValue()

		raise RuntimeError()

	def getMaximum(self):
		if (self.m_Root != None):
			self.m_Root.getSubtreeMinimum().getValue()

		raise RuntimeError()

	def subtreeToString(self, node, level):
		s = ""

		if (node != None):
			s += self.subtreeToString(node.getLeftChild(), (level + 1))

		for i in range(level):
			s += "\t"

		s += str(node.getValue()) if (node != None) else "[--]"
		s += "\n"

		if (node != None):
			s += self.subtreeToString(node.getRightChild(), (level + 1))

		return s

	def __str__(self):
		return self.subtreeToString(self.getRootNode(), 0)
