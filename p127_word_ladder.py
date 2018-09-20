from collections import deque
from collections import Counter


def ladderLength(beginWord, endWord, wordList):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: List[str]
    :rtype: int
    """

    counter = Counter(wordList)

    if len(beginWord) != len(endWord):
        return 0


    q = deque()
    visited = {}
    q.append((beginWord,1))

    while len(q) > 0:
        word, count = q.popleft()
        if word == endWord:
            return count

        if word in visited:
            continue

        for i in range(len(word)):
            for j in range(0, 26):
                char = chr(ord('a') + j)
                new_word = word[:i] + char + word[i+1:]
                if new_word in counter:
                    q.append((new_word, count + 1))
        visited[word] = 1

    return 0


def main():
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

    x = ladderLength(beginWord, endWord, wordList)
    print (x)


if __name__ == "__main__":
    main()
