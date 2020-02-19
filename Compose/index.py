class msgSendBehaviour(object):
	def sendMsg():
		pass

class msgSendHello(msgSendBehaviour):
	def sendMsg():
		print('Hello')

class msgSendHi(msgSendBehaviour):
	def sendMsg():
		print('Hi')

class Sender(object):
	def __init__(self, behaviour = msgSendBehaviour):
		self.msgSendBehaviour = behaviour

	def sendMsg(self):
		self.msgSendBehaviour.sendMsg()

	def changeMsgSendBehaviour(self, behaviour):
		self.msgSendBehaviour = behaviour

sender = Sender()
sender.sendMsg()
sender.changeMsgSendBehaviour(msgSendHi)
sender.sendMsg()
sender.changeMsgSendBehaviour(msgSendHello)
sender.sendMsg()