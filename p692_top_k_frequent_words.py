from collections import Counter, OrderedDict
from heapq import heappush, heappop

def topKFrequent(words, k):
    """
    :type words: List[str]
    :type k: int
    :rtype: List[str]
    """

    d = Counter(words)
    heap = []
    ordered_d = OrderedDict(sorted(d.items(), key=lambda x: -1 * x[1]))

    for key, val in ordered_d.items():
        heappush(heap, (-1 * val, key))

    output = []
    for i in range(k):
        output.append(heappop(heap)[1])

    return output


def main():
    input = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
    k = 4

    print (topKFrequent(input, k))


if __name__ == "__main__":
    main()