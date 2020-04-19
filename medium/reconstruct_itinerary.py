from collections import defaultdict


class Solution:
    def findItinerary(self, tickets):
        targets = defaultdict(list)
        for i, j in sorted(tickets)[::-1]:
            targets[i] += j,

        result = []

        def visited(airports):
            while targets[airports]:
                visited(targets[airports].pop())

            result.append(airports)
        visited('JFK')
        return result[::-1]


if __name__ == '__main__':

    print(Solution().findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
    print(Solution().findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
    print(Solution().findItinerary([["JFK","NRT"],["JFK","KUL"], ["NRT","JFK"]]))
    print(Solution().findItinerary([["EZE","TIA"],["EZE","HBA"],["AXA","TIA"],["JFK","AXA"],["ANU","JFK"],["ADL","ANU"],["TIA","AUA"],["ANU","AUA"],["ADL","EZE"],["ADL","EZE"],["EZE","ADL"],["AXA","EZE"],["AUA","AXA"],["JFK","AXA"],["AXA","AUA"],["AUA","ADL"],["ANU","EZE"],["TIA","ADL"],["EZE","ANU"],["AUA","ANU"]]))
