"""
There are a total of n courses you have to take, labeled from 0 to n - 1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

For example:
2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

2, [[1,0],[0,1]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
"""
import queue
from collections import OrderedDict


class CourseSchedule:
    @staticmethod
    def solve(edges):
        """
        Check if we can complete complete all the courses

        :param edges: graph edges in format of pairs
        :return: True if we can traverse all edges exactly once.
        """

        """
        Problem: Cycle Detection / Topological Sort
        Solution: DFS
            let U be the queue of unvisited nodes
            let V be the set of visited nodes
            for each node N in U:
                add N to V
                for each node M that has an edge from N to M:
                    if M is visited (cycle detected)
                        return False
                    add M to the queue
            return True
            
        """
        unvisited = queue.Queue()
        visited, graph = {}, {}
        # Constructing the graph from pairs. A pair is [course, required_course]
        for pair in edges:
            print(pair)
            if pair[1] in graph:
                graph[pair[1]] += (graph[pair[0]])  # required course -> course
            else:
                graph[pair[1]] = [pair[0]]

        for key in graph.keys():
            unvisited.put(key)
        print(list(unvisited.queue))
        while not unvisited.empty():
            node = unvisited.get()
            visited[node] = True

            for next_node in graph[node]:
                if next_node in visited:
                    return False  # cycle detected
                unvisited.put(next_node)

        return True


graph1 = [["A", "B"], ["B", "A"]]
graph2 = [["A", "B"]]
graph3 = [["A", "B"], ["B", "C"], ["C", "D"], ["C", "E"]]
graph4 = [["A", "B"], ["B", "C"], ["C", "D"], ["D", "B"]]  # A <-- B <-- C <-- D <--- B: False
graph5 = []

# print(CourseSchedule.solve(graph1))  # expect False
# print(CourseSchedule.solve(graph2))  # expect True
print(CourseSchedule.solve(graph3))  # expect True
#print(CourseSchedule.solve(graph4))  # expect False
# print(CourseSchedule.solve(graph5))  # expect True
