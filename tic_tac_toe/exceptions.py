class InvalidMovement(Exception):
    def __init__(self,*args,**kwargs):
        Exception.__init__(self,*args,**kwargs)

class GameOver(Exception):
    pass
