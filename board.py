
# class Board_Class:
#     def __init__(self) -> None:
#         self.board_state=["*","*","*","*","*","*","*","*","*"]

#     def change_board_state(self,number:int,string:str):
#         self.board_state[number-1]=string 
#         self.print_board( )

#     def print_board(self):
#         for row in range(3):
#             for column in range(3):
#                 print(self.board_state[row*3+column],end=" ")
#             print()

#     def get_free_slots(self):
#         free_slots=[]
#         for index,value in enumerate(self.board_state):
#             if value=="*":
#                 free_slots.append(index+1)
#         return free_slots        



# if __name__=="__main__":
#     b=Board_Class()
#     b.change_board_state(1,"X")
#     b.change_board_state(5,"0")
#     b.print_board()
#     print(b.get_free_slots())




        