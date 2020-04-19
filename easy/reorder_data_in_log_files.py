class Solution:
    def reorderLogFiles(self, logs):
        def sort_key(log):
            id_, content = log.split(' ', 1)
            # ASSIGNS TABLE OF VALUES AS KEY
            # First sort on basis of 0 or 1
            # Then sort on basis of content if their is a tie then uses id_
            # Finally sort on basis of id if their is a tie
            # CAN ALSO USE ITEMGETTER
            return (0, content, id_) if content[0].isalpha() else (1,)
        return sorted(logs, key=sort_key)


if __name__ == '__main__':
    print(Solution().reorderLogFiles(["dig1 8 1 5 1","let3 art can","dig2 3 6","let0 own kit dig","let1 art cant"]))


