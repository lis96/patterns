from observer import Subject, Observer

class Sender(Subject):
	def __init__(self):
		self.observers = set()

	def addObserver(self, obs):
		self.observers.add(obs)
		return self

	def removeObserver(self, obj):
		self.observers.discard(obj)
		return self

	def notifyObservers(self, state):
		for observer in self.observers:
			observer.handleObserverEvent(state)
		return self
		

class Listener(object):
	def __init__(self, msgHandler):
		self.msgHandler = msgHandler

	def handleObserverEvent(self, state):
		print(self.msgHandler(state))

sender = Sender()

helloyer = Listener(lambda x: 'Hello, ' + x)
goOuter = Listener(lambda x: 'Go out ' + x)
howAreYou = Listener(lambda x: x + ', how are you!')
juster = Listener(lambda x: 'just ' + x)

sender.addObserver(helloyer).addObserver(goOuter).addObserver(howAreYou).notifyObservers('Gregor')
sender.removeObserver(goOuter).notifyObservers('Paul')