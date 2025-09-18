def checkmate(board: str):
    try:
        inp_board = board.replace(" ", "").upper() #เปลี่ยนเป็นตัวใหญ่และตัดช่องว่าง
        lst_board = inp_board.split("\n") #แยกบรรทัดเป็น list
        ob_point = {} #เก็บพิกัดและค่า
        check_point = []  #เก็บพิกัดที่ถูก check
        for y in range(len(lst_board)): #ลูปตามแถว
            for x in range(len(lst_board[y])): #ลูปตาม col
                ob_point[(x, y)] = lst_board[y][x]
                if lst_board[y][x] == "P": #เชค Pawn
                    check_point.extend([(x-1, y-1),(x+1, y-1)])
                elif lst_board[y][x] == "B": #เชค Bishop
                        for i in range(len(lst_board)):
                            for j in range(len(lst_board[i])):
                                if (i+j == y+x or i-j == y-x) and ((j, i) != (x, y)):
                                    check_point.append((j, i))
                elif lst_board[y][x] == "R": #เชค Rook
                        for i in range(len(lst_board)):
                            for j in range(len(lst_board[i])):
                                if (i == y or j == x) and ((j, i) != (x, y)):
                                    check_point.append((j, i))
                elif lst_board[y][x] == "Q": #เชค Queen
                        for i in range(len(lst_board)):
                            for j in range(len(lst_board[i])):
                                if ((i == y or j == x) or (i+j == y+x or i-j == y-x)) and ((j, i) != (x, y)):
                                    check_point.append((j, i))                              
            
        
        point = {coor: ("X" if coor in check_point and val in [".", "K"] else val) for coor, val in ob_point.items()} #เชคว่าพิกัดไหนถูก check
        
        
        
        
        if "K" in list(ob_point.values()) or "K" not in inp_board: 
            print("Fail")
        else:
            print("Success")
    except:
        print()