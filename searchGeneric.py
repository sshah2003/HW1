import queue

def genericSearch(problem, struct):
    currNode = problem.getStartState()
    goal = problem.getGoalState()
    closed = []
    # open = getDataStructure(struct)
    open = queue.PriorityQueue
    while not currNode['state'] is goal:
        closed.append(currNode['state'])
        children = currNode['state'].getChildren()
        for child in children:
            if not (child['state'] in closed):
                open.put(child)
        currNode = open.get
    
def getDataStructure(struct):
    if struct == "ucs":
        return queue.PriorityQueue
    if struct == "dfs":
        return queue.SimpleQueue
    if struct == "bfs":
        return queue.LifoQueue