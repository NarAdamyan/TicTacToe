from board import Board_Class
from Player import Player

class HumanPlayer(Player):
    def move(self):
        while True:    
            number=input("Enter your step: ")
            
            if number.isdigit():
                number=int(number)
            else:
                print("Enter the number 1 to 9!!!")   
                continue
            if number not in self.board.get_free_slots():
                print(f"Chosen slot is not empaty!!! Enter the other from{self.board.get_free_slots()}!!!")   
                continue
            break
        print("number = ",number)
        self.board.change_board_state(number,self.value)
        