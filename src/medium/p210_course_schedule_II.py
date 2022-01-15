class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.numCourses = numCourses
        self.prerequisites = prerequisites

        self.que = []
        self.indegree = [0 for _ in range(self.numCourses)]
        self.neighbors = dict()
        self.helper()
        self.result = []
        self.topo_sort()
        if len(self.result) != numCourses:
            return []
        return self.result
        
    def helper(self):
        for dest, start in self.prerequisites:
            self.indegree[dest] += 1
            if start not in self.neighbors:
                self.neighbors[start] = set()
            self.neighbors[start].add(dest)
            
    def topo_sort(self):
        for i in range(len(self.indegree)):
            if self.indegree[i] == 0:
                self.que.append(i)
        self.result = [i for i in self.que]

        while self.que:
            node = self.que.pop()
            if node in self.neighbors:
                for dest in self.neighbors[node]:
                    self.indegree[dest] -= 1
                    if self.indegree[dest] == 0:
                        self.que.append(dest)
                        self.result.append(dest)