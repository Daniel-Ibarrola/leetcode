class Solution:
    @staticmethod
    def final_string(string: str) -> str:
        buffer: list[str] = []
        for char in string:
            if char == "i":
                buffer.reverse()
            else:
                buffer.append(char)
        return "".join(buffer)
