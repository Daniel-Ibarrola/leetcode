class Solution:

    @staticmethod
    def is_isomorphic(this_string: str, that_string: str) -> bool:
        if len(this_string) != len(that_string):
            return False

        first_occurrences_this_string: dict[str, int] = {}
        first_occurrences_that_string: dict[str, int] = {}

        this_string_encoded: list[int] = [0] * len(this_string)
        that_string_encoded: list[int] = [0] * len(that_string)

        for ii in range(len(this_string)):
            this_string_encoded[ii] = first_occurrences_this_string.setdefault(
                this_string[ii], len(first_occurrences_that_string)
            )
            that_string_encoded[ii] = first_occurrences_that_string.setdefault(
                that_string[ii], len(first_occurrences_that_string)
            )

            if this_string_encoded[ii] != that_string_encoded[ii]:
                return False

        return True
