from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = Solution.make_map(self, prerequisites)
        WHITE = 0
        GREY = 1
        BLACK = 2
        queue = deque()

        courses = {}
        for num in range(numCourses):
            courses[num] = WHITE
            queue.append(num)

        while(queue):
            curr = queue.pop()
            if courses[curr] == BLACK:
                continue
            elif courses[curr] == GREY:
                courses[curr] = BLACK
            else:
                courses[curr] = GREY
                queue.append(curr)

            for prereq in prereqs[curr]:
                if courses[prereq] == GREY:
                    return False

                if courses[prereq] == WHITE:
                    queue.append(prereq)


        
        return True

    def make_map(self, prerequisites):
        prereqs = defaultdict(set)
        for prereq in prerequisites:
            prereqs[prereq[0]].add(prereq[1])


        return prereqs