#!/usr/bin/python3

class Person:
	def __init__(self, name):
		self.name = name

	def say_hi(self):
		print('Hello, my name is', self.name)
		print(f"Hello, my name is {self.name}")

p = Person("Kazzy")
p.say_hi()
