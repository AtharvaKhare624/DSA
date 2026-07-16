import math

def print_board(s):
    for i in range(0, 9, 3):
        print(s[i], '|', s[i+1], '|', s[i+2])
        if i < 6: print('---------')
    print()

wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

def winner(s, p): return any(s[a]==s[b]==s[c]==p for a,b,c in wins)
def terminal(s): return winner(s,'X') or winner(s,'O') or ' ' not in s
def score(s): return 10 if winner(s,'X') else -10 if winner(s,'O') else 0

def moves(s): return [i for i,v in enumerate(s) if v==' ']

def alphabeta(s, d, a, b, maxp):
    if d==0 or terminal(s): return score(s), None
    best_move = None
    if maxp:
        val = -math.inf
        for m in moves(s):
            s[m]='X'; v,_=alphabeta(s,d-1,a,b,0); s[m]=' '
            if v>val: val, best_move=v,m
            a=max(a,v)
            if b<=a: break
    else:
        val = math.inf
        for m in moves(s):
            s[m]='O'; v,_=alphabeta(s,d-1,a,b,1); s[m]=' '
            if v<val: val, best_move=v,m
            b=min(b,v)
            if b<=a: break
    return val,best_move

def play():
    s=[' ']*9
    print("Positions:\n0|1|2\n-----\n3|4|5\n-----\n6|7|8\n")
    while True:
        print_board(s)
        if terminal(s):
            print("X wins!" if winner(s,'X') else "O wins!" if winner(s,'O') else "Draw!")
            break
        if s.count(' ')%2:
            try:
                m=int(input("Your move (0-8): "))
                if s[m]!=' ': print("Invalid!"); continue
                s[m]='X'
            except: print("Enter 0-8."); continue
        else:
            print("AI thinking...")
            _,m=alphabeta(s,9,-math.inf,math.inf,0)
            s[m]='O'

if __name__=="__main__":
    play()
