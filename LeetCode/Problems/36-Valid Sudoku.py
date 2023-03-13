from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows={key:[] for key in range(9)}
        columns={key:[] for key in range(9)}
        grid={key:[] for key in range(9)}
        for i in range(9):
            for j in range(9):
                n=board[i][j]
                if n=='.':
                    continue
                if n in rows[i]:
                    return False
                rows[i].append(n)
                if n in columns[j]:
                    return False
                columns[j].append(n)
                gid=j//3+i//3*3
                if n in grid[gid]:
                    return False
                grid[gid].append(n)
        return True