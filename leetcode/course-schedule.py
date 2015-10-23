# Time: O(|V|+|E|)
# Space: O(|E|)

# REVIEW

from collections import deque
from sets import Set

def canFinish(numCourses, prerequisites):
    zero_in_degree_queue, in_degree, out_degree = deque(), {}, {}

    for i, j in prerequisites:
        if i not in in_degree:
            in_degree[i] = Set()
        if j not in out_degree:
            out_degree[j] = Set()
        in_degree[i].add(j)
        out_degree[j].add(i)

    for i in xrange(numCourses):
        if i not in in_degree:
            zero_in_degree_queue.append(i)

    while zero_in_degree_queue:
        prerequisite = zero_in_degree_queue.popleft()
        if prerequisite in out_degree:
            for course in out_degree[prerequisite]:
                print course
                in_degree[course].discard(prerequisite)
                if not in_degree[course]:
                    zero_in_degree_queue.append(course)

            del out_degree[prerequisite]

    if out_degree:
        return False

    return True

print canFinish(2, [[1,0]]), True
print canFinish(2, [[1,0], [0,1]]), False
print canFinish(3, [[1,0], [1,2]]), True
print canFinish(3, [[1,0], [1,2], [1,2], [0,2]]), True
