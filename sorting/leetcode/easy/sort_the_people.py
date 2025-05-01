from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        heights_to_names = {}

        for hi, name in zip(heights, names):
            heights_to_names[hi] = name

        people = []

        for i in reversed(sorted(heights)):
            people.append(heights_to_names[i])

        return people
