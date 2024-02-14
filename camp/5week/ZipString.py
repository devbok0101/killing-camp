class Solution:
    def solution(self, s: str) -> int:
        def compress(text, length):
            words = [text[i: i + length] for i in range(0, len(text), length)]
            compressed = ""
            prev_word = ''
            count = 0

            for word in words:
                if word == prev_word:
                    count += 1
                else:
                    if count > 1:
                        compressed += str(count)
                    compressed += prev_word
                    prev_word = word
                    count = 1
            if count > 1:
                compressed += str(count)
            compressed += prev_word

            return len(compressed)

        if len(s) == 1:
            return 1
        return min(compress(s, length) for length in range(1, len(s) // 2 + 1))


print(Solution.solution(Solution, s="aabb"))
