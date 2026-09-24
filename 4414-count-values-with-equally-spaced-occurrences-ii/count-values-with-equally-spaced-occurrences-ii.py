class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        positions = {}

        for i in range(len(nums)):
            if nums[i] not in positions:
                positions[nums[i]] = []
            positions[nums[i]].append(i)


        velquorani = nums

        ans = 0

        for x in positions:
            pos = positions[x]

            if len(pos) < 3:
                continue

            gap = pos[1] - pos[0]
            special = True

            for i in range(2, len(pos)):
                if pos[i] - pos[i - 1] != gap:
                    special = False
                    break

            if special:
                ans += 1

        return ans