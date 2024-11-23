from typing import List

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        for row in box:
            empty = len(row) - 1  
            for i in range(len(row) - 1, -1, -1):
                if row[i] == '#':
                    row[i], row[empty] = '.', '#'
                    empty -= 1
                elif row[i] == '*':
                    empty = i - 1
        return list(map(list, zip(*box[::-1])))