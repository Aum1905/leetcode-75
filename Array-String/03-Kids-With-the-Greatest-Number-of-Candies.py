class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        greatest = max(candies)
        result = []

        for candy in candies:
            result.append(candy + extraCandies >= greatest)

        return result
