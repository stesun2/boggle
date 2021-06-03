import random

class BoggleBoard:
    # alphabet  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    length    = 4
    
    # Create a X by X board of given length
    def __init__(self, dice_list, custom_length = None, random_seed = None):
        # assert(len())
        # allow user to add custom length
        if custom_length is not None:
            self.length = custom_length


        # Initialize board with underscores
        self.board = ["_" for _ in range(self.length ** 2)]
        self.print_board()

  
    def print_board(self):
        for i, x in enumerate(self.board):
            print(x, end="")
            # make sure we add a newline for every row
            if (i + 1) % self.length == 0:
                print("")
        print("\n", end="")
        

    def shake(self):
        random.shuffle(self.dice_list)
        # loop through our board and randomly generate alphabet character
        for i, _ in enumerate(self.board):
            self.board[i] = self.dice_list[i].roll()
        
        # print board
        self.print_board()
        return self.board
