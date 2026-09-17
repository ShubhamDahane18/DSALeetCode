class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        n = len(numbers)
        i, j = 0, n - 1

        while i < j:
            s = numbers[i] + numbers[j]

            if s < target:
                i+=1
            elif s > target:
                j -= 1
            else:
                return [i + 1, j + 1]