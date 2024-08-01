from _typeshed import ExcInfo
from typing import List


class Solution:
    """
    The idea to solve this question is:
        if the time to take the further position to the target is less than
        the time to take the closer position to the target, we consider that they are the same fleet
        cause at some point, the car in the further postion will catch the car in the closer position, and they will be in the same speed afterward

        The time for the further position to catch the closer position does not need to be a whole number of hour i.e 1 hour, or 2 hours, it could be in fraction of hours i.e 30 minutes, or 2 hours 1 minute


        Because of this, we could use the stack, try to matain the stack in the increasing order in term of time to reach to the target, and increasing in distance also

         1 hour to reach the target, 3 hours to reach the target, 5 hours to reach the target
        [1 , 3, 5]
         ^
         at closest position than the one with 3 hours

    """

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # this stack is used to keep track the time to target in decreasing position (closer to target in distance to further position to target in distance)
        stack = []
        position_speed_pair = sorted(zip(position, speed), reverse=True)
        for current_position, current_speed in position_speed_pair:
            time_to_target = (target - current_position) / current_speed

            try:
                if stack[-1] < time_to_target:
                    # it means the closer position has less time to target so this current position never be the same fleet
                    stack.append(time_to_target)
            except Exception:
                stack.append(time_to_target)
        return len(stack)


position = [10, 8, 0, 5, 3]
speed = [2, 4, 1, 1, 3]
target = 12

print(Solution().carFleet(target, position, speed))
