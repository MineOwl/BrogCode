import shogi

def main():
    board = shogi.Board('+R+N+SGKG+S+N+R/+B+N+SG+LG+S+N+B/P+LPP+LPP+LP/9/9/9/9/1P2P2P1/6k2 b - 200')
    board.push( shogi.Move.from_usi('5e4d') )
    for i in range(10):
        moves = []
        for legal_move in board.legal_moves:
            moves.append(legal_move)
        print(board.kif_str())
        board.push( moves[0] )

if __name__ == "__main__":
    main()
