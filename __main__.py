#!/usr/bin/python
# -*- coding: utf-8 -*-

import AvlTree
import random

if __name__ == "__main__":
	nodes = input("Quanti nodi deve contenere l'albero AVL? ")
	nodes = int(nodes)

	print

	#
	# Costruisci un albero AVL vuoto.
	#
	tree = AvlTree.Tree()
	random.seed()

	for i in range(nodes):
		#
		# Inserisci l'indice attuale come nuovo nodo dell'albero.
		#
		n = random.randint(0, (nodes ** 2))
		tree.insert(n)

		#
		# Stampa a schermo una rappresentazione dell'albero.
		#
		index = "%d" % (i)

		print "-- [%s]" % (index) , "-" * (74 - len(index))
		print
		print tree
