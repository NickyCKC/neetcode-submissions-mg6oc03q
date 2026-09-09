class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(course, visited):
            if course in visited:
                return False
            if path[course] == []:
                return True
            visited.add(course)
            for prereq in path[course]:
                if not dfs(prereq, visited):
                    return False
            visited.remove(course)
            path[course] = []
            return True
        
        path = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            path[course].append(prereq)
        
        visited = set()
        for key in path:
            if not dfs(key, visited):
                return False
        return True