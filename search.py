# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from searchGeneric import genericSearch

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """

    return genericSearch(problem, util.Stack(), nullHeuristic, 0)


    current = (problem.getStartState(), [])  # Initialize current node to start state
    closed = set()  # Initialize 'closed' as an empty set
    open = util.Stack()  # Initialize 'open' as a stack

    while not problem.isGoalState(current[0]):  # while start state is not the goal state

        state = current[0] # Initialize state to be the current state
        actions = current[1] # Initialize actions to be the list of actions
        closed.add(state)  # add current state to closed set

        successors = problem.getSuccessors(state) # initialize successors to be tuple of successors of the current state

        for s in successors: # For loop to go through the tuple of successors
            if s[0] not in closed:  # if the successor's state is not in closed/visited 
                open.push((s[0], actions + [s[1]])) # then it will add it to open along with the actions already in actions list plus the new successor states action

        if open.isEmpty(): #if open is empty returns an empty path
            return []  

        current = open.pop()  # Updates current to be the successor that is not in closed

    return current[1]  # return the actions to reach the goal state

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    
    return genericSearch(problem, util.Queue(), nullHeuristic, 0)

    current = (problem.getStartState(), [])  # Initialize current node to start state
    closed = set()  # Initialize 'closed' as an empty set
    open = util.Queue()  # Initialize 'open' as a stack

    while not problem.isGoalState(current[0]):  # while start state is not the goal state

        state = current[0] # Initialize state to be the current state
        actions = current[1] # Initialize actions to be the list of actions
        closed.add(state)  # add current state to closed set

        successors = problem.getSuccessors(state) # initialize successors to be tuple of successors of the current state

        for s in successors: # For loop to go through the tuple of successors
            if s[0] not in closed:  # if the successor's state is not in closed/visited 
                open.push((s[0], actions + [s[1]])) # then it will add it to open along with the actions already in actions list plus the new successor states action

        if open.isEmpty(): #if open is empty returns an empty path
            return []  

        current = open.pop()  # Updates current to be the successor that is not in closed

    return current[1]  # return the actions to reach the goal state


def uniformCostSearch(problem):
    """Search the node of least total cost first."""

    return genericSearch(problem, util.PriorityQueue(), nullHeuristic, 0)


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    
    # return genericSearch(problem, util.PriorityQueueWithFunction(heuristic))

    current = (problem.getStartState(), [])
    visited = set()
    open = util.PriorityQueue()

    while not problem.isGoalState(current[0]):
        state = current[0]
        actions = current[1]

        if state not in visited:
            visited.add(state)

            children = problem.getSuccessors(state)

            for s in children:
                if s[0] not in visited:
                    cost = problem.getCostOfActions(actions + [s[1]]) + heuristic(s[0], problem)
                    open.push((s[0], actions + [s[1]]), cost)

        if open.isEmpty():
            return []

        current = open.pop()

    return current[1]
    



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
