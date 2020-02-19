class Componenet():
	def logging(self, msg):
		"""
		"""

class ConcreteComponent(Componenet):
	def logging(self, msg):
		"""
		"""

class Decorator(Componenet):
	def logging(self, msg):
		self.wrappedComponent.logging(msg)
	def __init__(self, wrapped):
		super().__init__()
		self.wrappedComponent = wrapped