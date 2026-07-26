import string
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0

        word_set = set(wordList)

        q = deque()
        q.append(beginWord)

        visited = set()
        visited.add(beginWord)

        steps = 1

        while q:

            size = len(q)

            for _ in range(size):

                key = q.popleft()

                if key == endWord:
                    return steps

                for i in range(len(key)):
                    for alpha in string.ascii_lowercase:

                        temp = key[:i] + alpha + key[i+1:]

                        if temp in word_set and temp not in visited:
                            visited.add(temp)
                            q.append(temp)

            steps += 1

        return 0