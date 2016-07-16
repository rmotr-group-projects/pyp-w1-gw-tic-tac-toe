class InvalidMovement(Exception):
	def __init__(self, message):
		super(InvalidMovement, self).__init__(message)


class GameOver(Exception):
    def __init__(self, message):
    	super(GameOver, self).__init__(message)
