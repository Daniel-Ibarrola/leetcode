import enum
from collections import defaultdict

class State(enum.Enum):
    VISITED = 1
    VISITING = 2
    UNVISITED = 3

def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:
    """
    You have to take a total of numCourses courses, which are labeled from 0 to numCourses - 1.
    You are given a list of prerequisites pairs, where prerequisites[i] = [a, b] indicates
    that you must complete course b before course a.

    Given the total number of courses and a list of prerequisite pairs,
    write a function to determine if it is possible to finish all courses.
    """
    graph: dict[int, list[int]] = defaultdict(list)
    for course_a, course_b in prerequisites:
        graph[course_a].append(course_b)

    state: dict[int, State] = {c: State.UNVISITED for c in range(num_courses)}
    def has_cycle(course: int) -> bool:
         if state[course] == State.VISITED:
             return False

         if state[course] == State.VISITING:
             return True

         state[course] = State.VISITING
         for neighbor in graph[course]:
             if has_cycle(neighbor):
                 return True

         state[course] = State.VISITED
         return False

    for course in range(num_courses):
        if state[course] == State.UNVISITED:
            if has_cycle(course):
                return False

    return True

def find_order(num_courses: int, prerequisites: list[list[int]]) -> list[int]:
    """
    You have to take a total of numCourses courses, which are labeled from 0 to numCourses - 1.

    You are given a list of prerequisites pairs, where prerequisites[i] = [a, b] indicates that you must complete
    course b before course a.

    Given the total number of courses and a list of prerequisite pairs, write a function to return the
    ordering of courses you should take to finish all courses.

    If there are multiple valid orderings, return any valid ordering. If it is impossible to finish all courses,
    return an empty array.
    """
    graph: dict[int, list[int]] = defaultdict(list)
    for course_a, course_b in prerequisites:
        graph[course_a].append(course_b)

    state: dict[int, State] = {c: State.UNVISITED for c in range(num_courses)}
    order: list[int] = []

    def has_cycle(course: int) -> bool:
        if state[course] == State.VISITED:
            return False

        if state[course] == State.VISITING:
            return True

        state[course] = State.VISITING
        for neighbor in graph[course]:
            if has_cycle(neighbor):
                return True

        state[course] = State.VISITED
        order.append(course)
        return False

    for course in range(num_courses):
        if state[course] == State.UNVISITED:
            if has_cycle(course):
                return []

    return order
