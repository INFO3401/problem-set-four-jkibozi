class Candidate:
	def __init__(self, name, data):
		self.candidate = name
		self.data = data.loc[data['endorsee'] == name]
	
	def countEndorsements(self):
		return len(self.data)
	
	def getScore(self):
		return self.data['points']