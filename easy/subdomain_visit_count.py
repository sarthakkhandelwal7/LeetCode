from collections import Counter


class Solution:
    def subdomainVisits(self, cpdomains):
        counts = Counter()
        for domains in cpdomains:
            count = int(domains.split()[0])
            domains_list = domains.split()[-1].split('.')
            for i in range(len(domains_list)):
                counts['.'.join(domains_list[i:])] += count

        ans = []
        for i in counts.keys():
            ans.append(f'{counts[i]} ' + i)
        return ans

