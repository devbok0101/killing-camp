class Solution:
    def decoding(self, m: str, k:str) -> str:

        words = [m[index] for index in range(len(m))]
        keys = [k[index] for index in range(len(k))]

        stop_point = []
        key_index = 0
        for index, word in enumerate(words):

            if key_index == len(keys):
                stop_point.append(word)
                continue

            if keys[key_index] != word:
                stop_point.append(word)
            else:
                key_index += 1
        return ''.join(map(str, stop_point))

#print(Solution.decoding(Solution, m = "kkaxbycyz", k = "abc"))
#print(Solution.decoding(Solution, m = "acbbcdc", k = "abc"))
print(Solution.decoding(Solution, m = "abcd", k = "kf"))