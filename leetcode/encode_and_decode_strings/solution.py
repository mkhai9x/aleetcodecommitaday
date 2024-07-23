from typing import List


class Codec:
    delimetter = "-"

    def encode(self, strs: List[str]) -> str:
        encoded_long_string = ""
        for each in strs:
            encoded_long_string += f"{len(each)}{self.delimetter}{each}"
        return encoded_long_string

    def decode(self, s: str) -> List[str]:
        decoded_strings = []

        i = 0
        while i < len(s):
            delimetter_index = find(self.delimetter, i)
            string_length = int(s[delimetter_index - 1])

            string = s[delimetter_index + 1 : delimetter_index + 1 + string_length]
            decoded_strings.append(string)

            i = delimetter_index + 1 + string_length
        return decoded_strings
