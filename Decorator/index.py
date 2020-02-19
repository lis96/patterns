import decorator

class printLogger(decorator.ConcreteComponent):
	def logging(self, msg):
		super().logging(msg)
		print(msg)

class SaveToFile(decorator.Decorator):
	def logging(self, msg):
		super().logging(msg)
		print('save to file: "' + msg + '"')
	def __init__(self, wrapped):
		super().__init__(wrapped)

class SendToServer(decorator.Decorator):
	def logging(self, msg):
		super().logging(msg)
		print('send to server: "' + msg + '"')
	def __init__(self, wrapped):
		super().__init__(wrapped)

printer = printLogger()
printer = SaveToFile(printer)
printer = SendToServer(printer)
printer.logging('Hello, world')