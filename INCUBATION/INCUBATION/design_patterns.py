# templates that describe how to solve a particular problem with great efficiency.
# They are broadly of 3 types: 1) creational, 2) structural, 3) behavioural
#
#1. Singleton: Allows only one instance of a class.
# Example - connection to a database.

# classic implementation of Singleton Design pattern
class Singleton:

	__shared_instance = 'GeeksforGeeks'

	@staticmethod
	def getInstance():
		"""Static Access Method"""
		if Singleton.__shared_instance == 'GeeksforGeeks':
			Singleton()
		return Singleton.__shared_instance

	def __init__(self):
		"""virtual private constructor"""
		if Singleton.__shared_instance != 'GeeksforGeeks':
			raise Exception("This class is a singleton class !")
		else:
			Singleton.__shared_instance = self


# main method
if __name__ == "__main__":

	# create object of Singleton Class
	obj = Singleton()
	print(obj)

	# pick the instance of the class
	obj = Singleton.getInstance()
	print(obj)

#2. Factory : creational type design pattern that allows parameterized object instantiation.
# Example: A site is rendered in various languages. So depending upon the parameter language,
# The page object type must be decided. Say if language is choosen as Spanish, Fctaory pattern
# # Will return page_object = collection['Spanish']()

# Python Code for factory method
# it comes under the creational
# Design Pattern

class FrenchLocalizer:

	""" it simply returns the french version """

	def __init__(self):

		self.translations = {"car": "voiture", "bike": "bicyclette",
							"cycle":"cyclette"}

	def localize(self, msg):

		"""change the message using translations"""
		return self.translations.get(msg, msg)

class SpanishLocalizer:
	"""it simply returns the spanish version"""

	def __init__(self):
		self.translations = {"car": "coche", "bike": "bicicleta",
							"cycle":"ciclo"}

	def localize(self, msg):

		"""change the message using translations"""
		return self.translations.get(msg, msg)

class EnglishLocalizer:
	"""Simply return the same message"""

	def localize(self, msg):
		return msg

def Factory(language ="English"):

	"""Factory Method"""
	localizers = {
		"French": FrenchLocalizer,
		"English": EnglishLocalizer,
		"Spanish": SpanishLocalizer,
	}

	return localizers[language]()

if __name__ == "__main__":

	f = Factory("French")
	e = Factory("English")
	s = Factory("Spanish")

	message = ["car", "bike", "cycle"]

	for msg in message:
		print(f.localize(msg))
		print(e.localize(msg))
		print(s.localize(msg))

#3. Builder: Creational type design pattern that lets you construct complex objects step by step.
# Example: We want to make a phone. It has various features -
# Classical way - to call parameterised constructor

#phone_obj = phone(os, ram screen_size, cost, color)
# we may want to keep all features configurable(may or may not specify.
# This is provided by builder design pattern, through a class say PhoneBuilder
# Where we have setter for each parameter, and all the setter methods return the object of type,PhoneBuilder
# def set_os(os):
#   self.os = os
#   return self
#
#and we provide 1 get_phone method that returns object of type Phone.
# def get_phone():
#    return self.phone
#
# Then a peculiar phone instantiation would look like follows:
# phone = PhoneBuilder.set_os(os).set_ram(ram)........get_phone()
# Example 2: making a course



#4. Composite: is a structural design pattern.
# that lets you compose objects into tree structures
# and then work with these structures as if they were individual objects.
# Example: Let us say we want to build an object of type Computer.
# It has various parts - like HD,MB(RAM,CPU),....So its tree structure.
# Also each part has a price and so does the parent of that part also has the price.
# Composite dp is used to construct such objects.

#5. DECORATOR: decorates the object at run time.
#It helps to extend our classes to add more functionalities without disturbing the existing
# client code because we have to maintain the Single Responsibility Principle.

class WrittenText:

	"""Represents a Written text """

	def __init__(self, text):
		self._text = text

	def render(self):
		return self._text

class UnderlineWrapper(WrittenText):

	"""Wraps a tag in <u>"""

	def __init__(self, wrapped):
		self._wrapped = wrapped

	def render(self):
		return "<u>{}</u>".format(self._wrapped.render())

class ItalicWrapper(WrittenText):

	"""Wraps a tag in <i>"""

	def __init__(self, wrapped):
		self._wrapped = wrapped

	def render(self):
		return "<i>{}</i>".format(self._wrapped.render())

class BoldWrapper(WrittenText):

	"""Wraps a tag in <b>"""

	def __init__(self, wrapped):
		self._wrapped = wrapped

	def render(self):
		return "<b>{}</b>".format(self._wrapped.render())

""" main method """

if __name__ == '__main__':

	before_gfg = WrittenText("GeeksforGeeks")
	after_gfg = ItalicWrapper(UnderlineWrapper(BoldWrapper(before_gfg)))

	print("before :", before_gfg.render())
	print("after :", after_gfg.render())
