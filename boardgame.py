# https://www.acmicpc.net/problem/17825

class Pawn:
    _id = 0

    def __init__(self):
        self.id = self._id
        self._id += 1
        self.bound_node = None

    def setBoundNode(self, node):
        self.bound_node = node
        node.bound_pawn = self

    def getBoundNode(self):
        return self.bound_node

class BoardNode:
    def __init__(self, score, prevs=[], next_red=None, next_blue=None, src=False, dst=False):
        self.score = score
        self.prevs = prevs
        self.next_red = next_red
        self.next_blue = next_blue

        self.src = src
        self.dst = dst

        self.bound_pawn = None

    def connectPrev(self, other):
        if other not in self.prevs:
            self.prevs.append(other)

    def connectNextRed(self, other):
        self.next_red = other
        other.connectPrev(self)

    def connectNextBlue(self, other):
        self.next_blue = other

    def getNextRed(self):
        return self.next_red

    def getNextBlue(self):
        return self.next_blue

    def isNextBlue(self):
        return self.next_blue != None

class Board:
    def __init__(self):
        self.src_node = BoardNode(0, src=True)
        self.pawns = []
        self.total_score = 0

        # Initialize pawns.
        for _ in range(4):
            pawn = Pawn()
            self.pawns.append(pawn)
            pawn.setBoundNode(self.src_node)
        
        # Form outer U shape line.
        prev = self.src_node
        for score in range(2, 42, 2):
            node = BoardNode(score)
            prev.connectNextRed(node)
            prev = node

        top_node = node
        assert top_node.score == 40

        # Get score 30 node on the right.
        prev = self.src_node
        for _ in range(15):
            prev = prev.getNextRed()
        assert prev.score == 30

        # Make connection to the middle from right.
        node = BoardNode(28)
        prev.connectNextBlue(node)
        prev = node
        node = BoardNode(27)
        prev.connectNextRed(node)
        prev = node
        node = BoardNode(26)
        prev.connectNextRed(node)
        prev = node
        middle_node = BoardNode(25)
        prev.connectNextRed(middle_node)

        # Get score 20 node on the bottom.
        prev = self.src_node
        for _ in range(10):
            prev = prev.getNextRed()
        assert prev.score == 20

        # Make connection to the middle from bottom.
        node = BoardNode(22)
        prev.connectNextBlue(node)
        prev = node
        node = BoardNode(24)
        prev.connectNextRed(node)
        prev = node
        prev.connectNextRed(middle_node)

        # Get score 10 node on the left.
        prev = self.src_node
        for _ in range(5):
            prev = prev.getNextRed()
        assert prev.score == 10

        # Make connection to the middle from left.
        node = BoardNode(13)
        prev.connectNextBlue(node)
        prev = node
        node = BoardNode(16)
        prev.connectNextRed(node)
        prev = node
        node = BoardNode(19)
        prev.connectNextRed(node)
        prev = node
        prev.connectNextRed(middle_node)

        # Make connection to the top from middle.
        prev = middle_node
        node = BoardNode(30)
        prev.connectNextRed(node)
        prev = node
        node = BoardNode(35)
        prev.connectNextRed(node)
        prev = node
        prev.connectNextRed(top_node)
        self.dst_node = BoardNode(0, dst=True)
        top_node.connectNextRed(self.dst_node)

    def init(self):
        for pawn in self.pawns:
            node = pawn.bound_node
            if node != None:
                node.bound_pawn = None

            pawn.setBoundNode(self.src_node)


    def canMovePawn(self, pawn_id, dice_roll):
        pawn = self.pawns[pawn_id]
        node = pawn.getBoundNode()

        if pawn.bound_node == None:
            return False

        # If node has blue connection.
        if node.isNextBlue():
            node = node.getNextBlue()
            for _ in range(dice_roll - 1):
                node = node.getNextRed()

                if node == self.dst_node:
                    return True
        # Else follow red connection.
        else:
            for _ in range(dice_roll):
                node = node.getNextRed()

                if node == self.dst_node:
                    return True

        end_node = node
        if end_node.bound_pawn == None:
            return True
        else:
            return False

    def movePawn(self, pawn_id, dice_roll):
        pawn = self.pawns[pawn_id]
        start_node = node = pawn.getBoundNode()

        # If node has blue connection.
        if node.isNextBlue():
            node = node.getNextBlue()
            for _ in range(dice_roll - 1):
                node = node.getNextRed()

                if node == self.dst_node:
                    start_node.bound_pawn = None
                    pawn.bound_node = None
                    return start_node, self.dst_node
        # Else follow red connection.
        else:
            for _ in range(dice_roll):
                node = node.getNextRed()

                if node == self.dst_node:
                    start_node.bound_pawn = None
                    pawn.bound_node = None
                    return start_node, self.dst_node

        end_node = node

        pawn.setBoundNode(end_node)
        start_node.bound_pawn = None

        self.total_score += end_node.score

        return start_node, end_node

    def reversePawn(self, pawn_id, start_node, end_node):
        pawn = self.pawns[pawn_id]

        pawn.setBoundNode(start_node)
        end_node.bound_pawn = None

        self.total_score -= end_node.score
    

    def getTotalScore(self):
        return self.total_score


dice_rolls = list(map(int, input().split()))

def dfs(i, pawn_id, board):
    if i == 10:
        return board.getTotalScore()
    else:
        score0, score1, score2, score3 = -1, -1, -1, -1
        dice_roll = dice_rolls[i]

        if board.canMovePawn(0, dice_roll):
            start, end = board.movePawn(0, dice_roll)
            score0 = dfs(i+1, 0, board)
            board.reversePawn(0, start, end)

        if board.canMovePawn(1, dice_roll):
            start, end = board.movePawn(1, dice_roll)
            score1 = dfs(i+1, 1, board)
            board.reversePawn(1, start, end)

        if board.canMovePawn(2, dice_roll):
            start, end = board.movePawn(2, dice_roll)
            score2 = dfs(i+1, 2, board)
            board.reversePawn(2, start, end)

        if board.canMovePawn(3, dice_roll):
            start, end = board.movePawn(3, dice_roll)
            score3 = dfs(i+1, 3, board)
            board.reversePawn(3, start, end)

        return max(score0, score1, score2, score3)

board = Board()
max_score = dfs(0, 0, board)
print(max_score)

