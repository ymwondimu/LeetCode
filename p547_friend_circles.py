class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """

        n = len(M)
        m = len(M[0])

        visited = []

        outputs = []

        for i in range(len(M)):
            output = []
            if i not in visited:
                dfs(i, M, visited, output)
            if len(output) > 0:
                outputs.append(output)

        return len(outputs)


def dfs(i, M, visited, output):
    visited.append(i)
    output.append(i)

    for neighbor in get_neighbor(i, M):
        if neighbor not in visited:
            dfs(neighbor, M, visited, output)


def get_neighbor(i, M):
    output = []
    for j in range(len(M[i])):
        if i != j:
            if M[i][j] == 1:
                output.append(j)

    return output