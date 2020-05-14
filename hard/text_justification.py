class Solution:
    def fullJustify(self, words, maxWidth):
        ans, line, number_of_letters = [], [], 0
        for word in words:
            if number_of_letters + len(word) + len(line) > maxWidth:
                for i in range(maxWidth - number_of_letters):
                    line[i % (len(line) - 1 or 1)].append(' ')

                for i in range(len(line)):
                    line[i] = ''.join(line[i])

                ans.append(''.join(line))
                number_of_letters, line = 0, []

            number_of_letters += len(word)
            line.append([word])

        ans.append(' '.join([word[0] for word in line]).ljust(maxWidth, ' '))
        return ans
