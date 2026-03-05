# 井字棋：alpha-beta算法

import copy


def isfinish(board):
    if board[0][0] == board[0][1] == board[0][2] == 1:
        return 1
    elif board[1][0] == board[1][1] == board[1][2] == 1:
        return 1
    elif board[2][0] == board[2][1] == board[2][2] == 1:
        return 1
    elif board[0][0] == board[1][0] == board[2][0] == 1:
        return 1
    elif board[0][1] == board[1][1] == board[2][1] == 1:
        return 1
    elif board[0][2] == board[1][2] == board[2][2] == 1:
        return 1
    elif board[0][0] == board[1][1] == board[2][2] == 1:
        return 1
    elif board[0][2] == board[1][1] == board[2][0] == 1:
        return 1
    
    if board[0][0] == board[0][1] == board[0][2] == 2:
        return 2
    elif board[1][0] == board[1][1] == board[1][2] == 2:
        return 2
    elif board[2][0] == board[2][1] == board[2][2] == 2:
        return 2
    elif board[0][0] == board[1][0] == board[2][0] == 2:
        return 2
    elif board[0][1] == board[1][1] == board[2][1] == 2:
        return 2
    elif board[0][2] == board[1][2] == board[2][2] == 2:
        return 2
    elif board[0][0] == board[1][1] == board[2][2] == 2:
        return 2
    elif board[0][2] == board[1][1] == board[2][0] == 2:
        return 2
    
    elif not any(0 in row for row in board):
        return 3

    else:
        return 0
    

def minumaxum(board, d, alpha, beta, ismax):
    board_copy = copy.deepcopy(board)
    # print(board_copy)
    # print(d)
    # print(isfinish(board_copy))
    # find all blank position
    blank = []
    for i, row in enumerate(board_copy):
        for j, value in enumerate(row):
            if value ==0:
                blank.append([i,j])
    # print(blank)
    # d = 9-len(blank)
    # print(d)
    if isfinish(board_copy) == 1:
        return 1
    if isfinish(board_copy) == 2:
        return -1
    if isfinish(board_copy) == 3:
        return 0
    else:
        # 迭代得到最高分
        if ismax:
            max_score = -1
            for index in blank:
                board_copy_2 = copy.deepcopy(board_copy)
                board_copy_2[index[0]][index[1]] = 1
                score = minumaxum(board_copy_2, d+1, alpha, beta, False)
                max_score = max(score, max_score)
                # 修建枝叶
                if score >= beta:
                    break
                alpha = max(alpha, score)
                # print(max_score)
            return max_score
        else:
            min_score = 1
            for index in blank:
                board_copy_2 = copy.deepcopy(board_copy)
                board_copy_2[index[0]][index[1]] = 2
                score = minumaxum(board_copy_2, d+1, alpha, beta, True)
                min_score = min(score, min_score)
                # 修建枝叶
                if score <= alpha:
                    break
                beta = min(beta, score)
                # print(min_score)
            return min_score
        
        
def step(board):
    # find all blank position
    blank = []
    alpha = -2
    beta = 2
    for i, row in enumerate(board):
        for j, value in enumerate(row):
            if value != 1 and value != 2:
                blank.append([i,j])
    # print(blank)
    # check which step gets higer score
    best_score = -2
    best_board = copy.deepcopy(board)
    index = blank[0]
    best_board[index[0]][index[1]] = 1
    for index in blank:
        board_copy = copy.deepcopy(board)
        # print(board)
        # print(board_copy)
        board_copy[index[0]][index[1]] = 1
        # print(board_copy)
        board_copy_2 = copy.deepcopy(board_copy)
        score = minumaxum(board_copy_2, 1, alpha, beta, False)
        # print(score)
        if score > best_score:
            best_board = board_copy
            best_score = score
    # print("board=",best_board)
    return best_board


def run():
    board = [[0,0,0],[0,0,0],[0,0,0]]
    print("欢迎来到井字棋")
    start = int(input("请选择谁先手(玩家0,电脑1):"))
    if start == 0:
        isplayer = True
    elif start == 1:
        isplayer = False
    else:
        print("wrong")

    while True:
        # find all blank position
        blank = []
        for i, row in enumerate(board):
            for j, value in enumerate(row):
                # print(value)
                if value == 0:
                    blank.append([i,j])
        # print(blank)

        if isplayer:
            # print(board)
            for i, row in enumerate(board):
                for j, sym in enumerate(row):
                    if sym == 0:
                        print(" ",end="    ")
                    elif sym == 1:
                        print("O",end="    ")
                    elif sym == 2:
                        print("X",end="    ")
                print("\n")
            position = int(input("请输入你的落子位置(1-9):"))
            i = int((position-1)/3)
            j = (position-1)%3
            index = [i, j]
            # print(index)
            if index not in blank:
                print("位置已被占用!")
                break
            else:
                board[index[0]][index[1]] = 2

            if isfinish(board) == 1:
                for i, row in enumerate(board):
                    for j, sym in enumerate(row):
                        if sym == 0:
                            print(" ",end="    ")
                        elif sym == 1:
                            print("O",end="    ")
                        elif sym == 2:
                            print("X",end="    ")
                    print("\n")
                print("抱歉，你输了")
                break
            elif isfinish(board) == 2:
                for i, row in enumerate(board):
                    for j, sym in enumerate(row):
                        if sym == 0:
                            print(" ",end="    ")
                        elif sym == 1:
                            print("O",end="    ")
                        elif sym == 2:
                            print("X",end="    ")
                    print("\n")
                print("恭喜，你赢了！")
                break
            elif isfinish(board) == 3:
                for i, row in enumerate(board):
                    for j, sym in enumerate(row):
                        if sym == 0:
                            print(" ",end="    ")
                        elif sym == 1:
                            print("O",end="    ")
                        elif sym == 2:
                            print("X",end="    ")
                    print("\n")
                print("平局")
                break
            isplayer = False

        else:
            # print(board)
            board = step(board)

            if isfinish(board) == 1:
                for i, row in enumerate(board):
                    for j, sym in enumerate(row):
                        if sym == 0:
                            print(" ",end="    ")
                        elif sym == 1:
                            print("O",end="    ")
                        elif sym == 2:
                            print("X",end="    ")
                    print("\n")
                print("抱歉，你输了")
                break
            elif isfinish(board) == 2:
                for i, row in enumerate(board):
                    for j, sym in enumerate(row):
                        if sym == 0:
                            print(" ",end="    ")
                        elif sym == 1:
                            print("O",end="    ")
                        elif sym == 2:
                            print("X",end="    ")
                    print("\n")
                print("恭喜，你赢了！")
                break
            elif isfinish(board) == 3:
                for i, row in enumerate(board):
                    for j, sym in enumerate(row):
                        if sym == 0:
                            print(" ",end="    ")
                        elif sym == 1:
                            print("O",end="    ")
                        elif sym == 2:
                            print("X",end="    ")
                    print("\n")
                print("平局")
                break
            isplayer = True


if __name__ == "__main__":
    run()