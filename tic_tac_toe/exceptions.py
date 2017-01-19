class InvalidMovement(Exception):
    """
    Invalid Movement Exceptions:
    msg1: The wrong player took a turn. Raises InvalidMovement: ___ moves next
    msg2: The position is taken. Raises InvalidMovement: Position already taken.
    msg3: The position is out of range. Raises InvalidMovement: Position out of range.
    """
    pass
class GameOver(Exception):
    pass
