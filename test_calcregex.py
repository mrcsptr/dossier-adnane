# coding: utf-8

import unittest
from calc_regex import *


class MyFirstTests(unittest.TestCase):

	def testcalc(self):
		self.assertEqual(calc_regex('calc som 5 et 9'), 14)






