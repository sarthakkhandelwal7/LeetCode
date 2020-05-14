class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if not trust:
            return N
        _set = set()
        graph = collections.defaultdict(set)
        for a, b in trust:
            graph[a].add(b)
            _set.add(b)
            if a in _set:
                _set.remove(a)

        print(_set)
        for i in graph.keys():
            for j in _set.copy():
                if j not in graph[i]:
                    _set.remove(j)

                if not _set:
                    return -1
        return -1 if len(_set) != 1 else next(iter(_set))
