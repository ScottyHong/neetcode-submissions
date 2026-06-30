class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = []
        for pos, spd in zip(position,speed):
            pos_speed.append((pos,spd))
        pos_speed.sort(reverse = True)
        stack = []

        times = []
        for tup in pos_speed:
            time = (target-tup[0])/tup[1]
            times.append(time)

        print(times)
        for time in times:
            if not stack: 
                stack.append(time)
            else:
                if time <= stack[-1]:
                    continue
                else:
                    stack.append(time)



        return len(stack)