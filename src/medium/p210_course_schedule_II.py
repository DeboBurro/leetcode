class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = dict()
        requirements = dict()
        que = []
        res = []
        for dest, start in prerequisites:
            if start not in requirements:
                requirements[start] = set()
            if dest not in indegree:
                indegree[dest] = 0
            requirements[start].add(dest)
            indegree[dest] += 1
        
        for i in range(numCourses):
            if i not in indegree:
                que.append(i)
        
        while que:
            start = que.pop()
            res.append(start)
            if start in requirements:
                for dest in requirements[start]:
                    indegree[dest] -= 1
                    if indegree[dest] == 0:
                        que.append(dest)

        if len(res) != numCourses:
            return []
        return res