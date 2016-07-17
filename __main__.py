#!/usr/bin/python
# -*- coding: utf-8 -*-

import AvlTree
import random

if __name__ == "__main__":
	nodes = input("How many nodes will the tree contain? ")
	nodes = int(nodes)

	print

	#
	# Build an empty tree.
    #
	tree = AvlTree.Tree()
	random.seed()

	for i in range(nodes):
		#
		# Insert the current index as a new node.
		#
		n = random.randint(0, (nodes ** 2))
		tree.insert(n)

		#
		# Print a representation of the tree.
		#
		index = "%d" % (i)

		print "-- [%s]" % (index) , "-" * (74 - len(index))
		print
		print tree
