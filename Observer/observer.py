from abc import ABCMeta, abstractmethod, abstractproperty

class Subject():
	__metaclass__=ABCMeta

	@abstractmethod
	def addObserver(self, obj):
		"""
		"""

	@abstractmethod
	def removeObserver(self, obj):
		"""
		"""

	@abstractmethod
	def notifyObservers(self):
		"""
		"""


class Observer():
	__metaclass__=ABCMeta

	@abstractmethod
	def handleObserverEvent(self, state):
		"""
		"""
