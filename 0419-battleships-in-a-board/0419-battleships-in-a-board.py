class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        answer = 0
        n, m = len(board), len(board[0])
        for row in range(n):
            for col in range(m):
                if board[row][col] == "X":
                    add = 1
                    if 0 <= col - 1 < m and board[row][col - 1] == "X":
                        add = 0
                    elif 0 <= row - 1 < n and board[row - 1][col] == "X":
                        add = 0
                    answer += add
                            
        return answer