#!/usr/local/bin/python3
# -*- coding: utf-8 -*-  

import random

class Question(object):
	"""docstring for Question"""
	def __init__(self, main_prob, choices, ans, prob_type):
		super(Question, self).__init__()
		self.main_prob = main_prob
		if isinstance(choices, str) or isinstance(choices, unicode):
			self.choices = choices.split('#')
		else:
			self.choices = choices
		self.prob_type = int(prob_type)
		# 1: 单选， 2：多选， 3：判断
		self.multi_ans = prob_type == '2'
		if self.multi_ans:
			self.ans = ans.split('#')
		else:
			self.ans = ans

	def shuffle_choices(self):
		random.shuffle(self.choices)

	def show(self):
		if self.prob_type != 3:
			self.shuffle_choices()
		if self.multi_ans:
			print("\033[1;33m多选题\033[0m")
		print("- " + self.main_prob)
		for i in range(0, len(self.choices)):
			print("\t[{}] {}".format(i+1, self.choices[i]))
		hint = "Enter your answer (1~{}) ".format(len(self.choices))
		if self.multi_ans:
			return hint + " Use ',' to seperate multiple choices: "
		return hint

	def _check_multi(self, ans):
		ans_idxs = ans.split(",")
		try:
			ans_idxs = [int(idx) for idx in ans_idxs]
		except Exception:
			return (None, None)
		cans = ["[{}] {}".format(self.choices.index(a)+1, a) for a in self.ans]
		cans.sort()
		cans = "\n\t" + "\n\t".join(cans)
		wrong_ret = (False, "\033[1;31m Wrong!\033[0m The correct answer is: " + cans)
		if len(ans_idxs) != len(self.ans):
			return wrong_ret
		for idx in ans_idxs:
			if not self.choices[idx-1] in self.ans:
				return wrong_ret
		return (True, "\033[1;32m Correct!\033[0m")

	def _check(self, ans):
		try:
			ans_index = int(ans)
		except Exception:
			return (None, None)
		if ans_index < 1 or ans_index > len(self.choices):
			return (None, None)
		if self.choices[ans_index-1] == self.ans:
			return (True, "\033[1;32m Correct!\033[0m")
		else:
			return (False, "\033[1;31m Wrong!\033[0m The correct answer is: [{}] {}".format(self.choices.index(self.ans)+1, self.ans))

	def check_ans(self, ans):
		if self.multi_ans:
			return self._check_multi(ans)
		else:
			return self._check(ans)

