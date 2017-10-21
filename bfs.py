def breadth_first_search_tuples(problem):
    """[Figure 3.11]"""
    node = Node(problem.initial)
    if problem.goal_test(node.state):
        return node
    frontier = FIFOQueue()
    frontier.append(node)
    explored = set()
    while frontier:
        node = frontier.pop()
        explored.add(tuple(node.state)) #tuples!
        for child in node.expand(problem):
            if tuple(child.state) not in explored and child not in frontier: #tuples tuples!
                if problem.goal_test(child.state):
                    return child
                frontier.append(child)
    return None

