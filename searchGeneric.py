import util

def genericSearch(problem, dataStruct, heuristic, t):
    currNode = (problem.getStartState(), [])  
    visited = set()  
    open = dataStruct  

    while not problem.isGoalState(currNode[0]):  
        state = currNode[0] 
        actions = currNode[1] 

        # We only want to pop() after it's been visited
        if state not in visited:
            visited.add(state)  

            children = problem.getSuccessors(state) 

            for s in children: 
                if s[0] not in visited:  
                    if isinstance(open, util.Queue) or isinstance(open, util.Stack):
                        open.push((s[0], actions + [s[1]])) 
                    elif isinstance(open, util.PriorityQueue) or isinstance(open, util.PriorityQueueWithFunction):
                        cost = problem.getCostOfActions(actions + [s[1]])
                        open.update((s[0], actions + [s[1]]), cost)

        if open.isEmpty(): 
            return []  

        currNode = open.pop()  

    return currNode[1]