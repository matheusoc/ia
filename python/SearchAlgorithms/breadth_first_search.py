'''
Created on Jun 15, 2016

@author: Edielson
'''
from SearchAlgorithms.queue import Queue
        
class breadth_first_search(object):
    '''
    This class implements the breadth first search algorithm
    '''

    def __init__(self, problem):
        '''
        Constructor
        Any object instance must receive an ``problem`` parameter that is responsible
        for controlling the problem evaluation and next possible solutions. This parameter
        have two required functions:
            
            ExpandSolution(current): function that returns all possible solutions from 
            ``current`` state
            TestObjective(current,target): function that evaluates if ``current`` state
            corresponds to the ``target`` state 
         
        '''
        self.problem = problem
        
    def __reconstruct_path(self,came_from, start, goal):
        '''
        The came_from list tells you where you came from, but not the direction you want to go. 
        That means it is backwards from what you want. The reconstructed path is backwards, 
        so I call reverse() at the end of reconstruct_path. (An alternative is to choose to store 
        the path backwards, and then when you implement object movement, tell the object to go to 
        the last location on the list instead of the first.)
        '''
        
        current = goal
        path = [current]
        edge=[]
        v=current
        while current != start:
            current = came_from[current]
            u=current
            path.append(current)
            edge.append((u,v))
            v=u
        path.reverse()
        
        return path,edge    
    
    
    def search(self,start,target):
        #start a empty queue
        frontier = Queue()
        #insert ``start`` state in the queue
        frontier.put(start)
          
        #initialize control variables
        path = []
        edges=[]
        came_from={}
        came_from[start]=None
        solution = False
          
        #repeat while there are not visited candidate solutions
        while not frontier.empty():
            #take the first candidate solution
            current = frontier.get()
            #add to the visited states
            path.append(current)
              
            #evaluate is this is the objective
            if self.problem.ObjectiveTest(current,target) == True:
                #if true, finish serach
                solution = True
                break
              
            #else
            print("Visiting %r" % current)
            #expand new candidate solutions from current 
            new_solutions = self.problem.ExpandSolution(current)
            #run over all expanded solutions 
            for next_item in new_solutions:
                #check if each expanded solution was already visited
                if next_item not in came_from:
                    #if not, add to the queue for evaluation
                    frontier.put(next_item)
                    came_from[next_item] = current
                      
        if solution == True:
            path,edges=self.__reconstruct_path(came_from, start, target)
        return solution,path,edges          