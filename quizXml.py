#!/usr/local/bin/python3
# -*- coding: utf-8 -*-  

import sys
import xml.dom.minidom
import random
from question import Question


def quiz_xml(xml_file):
	dom_tree = xml.dom.minidom.parse(xml_file)
	root = dom_tree.documentElement
	nodes = root.getElementsByTagName("node")
	probs = [Question(node.getAttribute("timu"), node.getAttribute("thisXX"), node.getAttribute("thisAnswer"), node.getAttribute("tixing")) for node in nodes]
	wrong_probs = []
	while len(probs) > 0:
		random.shuffle(probs)
		for prob in probs:
			hint = prob.show()
			while True:
				ans = input(hint)
				ret, ret_str = prob.check_ans(ans)
				if ret != None:
					print(ret_str+"\n")
					if not ret:
						wrong_probs.append(prob)
						input("Press 'Enter' to next question...")
						print("")
					break
		probs = wrong_probs


if __name__ == '__main__':
	quiz_xml(sys.argv[1])

