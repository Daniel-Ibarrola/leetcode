class Solution:
    @staticmethod
    def count_distinct_colors(limit: int, queries: list[list[int]]) -> list[int]:
        query_results: list[int] = []
        ball_colors: dict[int, int] = {}
        color_count: dict[int, int] = {}

        for query in queries:
            [ball, color] = query

            # Ball doesn't have color
            if ball not in ball_colors:
                ball_colors[ball] = color
                color_count[color] = color_count.get(color, 0) + 1

            else:
                # Color changed, then previous color count is reduced by 1
                previous_color = ball_colors[ball]
                if previous_color != color:
                    color_count[previous_color] -= 1
                    if color_count[previous_color] == 0:
                        del color_count[previous_color]

                    color_count[color] = color_count.get(color, 0) + 1
                    ball_colors[ball] = color

                # Color is the same, then nothing changes

            query_results.append(len(color_count))

        return query_results
