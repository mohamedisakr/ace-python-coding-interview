from collections import Counter
from typing import List


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        table_num_set = set()
        food_item_set = set()
        table_map_food = Counter()

        for _, table_num, food_item in orders:
            table_num_set.add(int(table_num))
            food_item_set.add(food_item)
            table_map_food[f'{table_num}.{food_item}'] += 1

        sorted_table_num = sorted(list(table_num_set))
        sorted_food_item = sorted(list(food_item_set))

        display_table = [['Table'] + sorted_food_item]

        for table in sorted_table_num:
            row = [str(table)]
            for food_item in sorted_food_item:
                row.append(str(table_map_food[f'{str(table)}.{food_item}']))
            display_table.append(row)

        return display_table


orders = [
    ["David", "3", "Ceviche"],
    ["Corina", "10", "Beef Burrito"],
    ["David", "3", "Fried Chicken"],
    ["Carla", "5", "Water"],
    ["Carla", "5", "Ceviche"],
    ["Rous", "3", "Ceviche"]]
sol = Solution()
print(sol.displayTable(orders))
# table = [
#     ["Table", "Beef Burrito", "Ceviche", "Fried Chicken", "Water"],
#     ["3", "0", "2", "1", "0"],
#     ["5", "0", "1", "0", "1"],
#     ["10", "1", "0", "0", "0"]]
