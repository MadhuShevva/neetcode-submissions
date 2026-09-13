class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[]
        cols=[]
        cell=[]
        for i in range(9):
            rows.append(set())
            cols.append(set())
            cell.append(set())
        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                    continue
                nums=board[i][j]
                x=(i//3)*3+(j//3)
                if nums in rows[i]:
                    return False
                if nums in cols[j]:
                    return False
                if nums in cell[x]:
                    return False
                rows[i].add(nums)
                cols[j].add(nums)
                cell[x].add(nums)
        return True

        