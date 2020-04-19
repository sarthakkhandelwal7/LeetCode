from collections import defaultdict


class Solution:
    def findDuplicate(self, paths):
        dictionary = defaultdict(list)
        duplicates = []
        for file in paths:
            path, files = file.split(' ', 1)
            files = files.split(' ')
            for i in files:
                i = i.split('(')
                dictionary[i[1]].append(path+'/'+i[0])

        for i in dictionary.values():
            if len(i) > 1:
                duplicates.append(i)

        return duplicates


if __name__ == '__main__':
    print(Solution().findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]))