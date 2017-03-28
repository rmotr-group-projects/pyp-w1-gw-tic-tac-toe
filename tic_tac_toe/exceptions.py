class InvalidMovement(Exception):
    pass
    #validate player is next_turn 
    # _turn_is_valid    
    #check that the move is in range
    # _position_is_valid
    #determine whether that location is occupied
    # _position_is_empty_in_board

class GameOver(Exception):
    pass
    #Tied
    # _board_is_full
    #Winner
    # _is_winning_combination