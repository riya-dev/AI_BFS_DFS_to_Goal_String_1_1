# Name: Riya Dev
# Date: 9/26/20

import random
import queue

def getInitialState():
   x = "_12345678"
   l = list(x)
   random.shuffle(l)
   y = ''.join(l)
   return y
   
'''precondition: i<j
   swap characters at position i and j and return the new state'''
def swap(state, i, j):
   # ALL DONE
   return state[:i] + state[j] + state[i+1:j] + state[i] + state[j+1:] # rturn up to i, j, the char from i+1 to just before j, i, then the rest from j+1
   
'''Generate a list which hold all children of the current state
   and return the list'''
def generate_children(state):
   '''your code goes here'''
   children = []
   for char in range(0, len(state)): #loop through state
      # Down - "_12345678" -> "312_45678"
      if (state[char] == "_" and char <= 5): #if the position at char is _ and char is less than or equal to 5 _ can be moved down
         down = swap(state, char, char + 3)
         children.append(down)
      
      # Right
      if (state[char] == "_" and char % 3 != 2): # if the position at char is _ and char is not 2, 5, or 8
         right = swap(state, char, char + 1)
         children.append(right)
      
      # Up
      if (state[char] == "_" and char >= 3): # same logic as down except upwards
         up = swap(state, char - 3, char)
         children.append(up)
      
      # Left
      if(state[char] == "_" and char % 3 != 0): # same logic as moving right except char is not 0, 3, or 6
         left = swap(state, char - 1, char)
         children.append(left)
   return children
   
def display_path(n, explored): #key: current, value: parent
   l = []
   while explored[n] != "s": #"s" is initial's parent
      l.append(n)
      n = explored[n]
   print ()
   l = l[::-1]
   for i in l:
      print (i[0:3], end = "   ")
   print ()
   for j in l:
      print (j[3:6], end = "   ")
   print()
   for k in l:
      print (k[6:9], end = "   ")
   print ("\n\nThe shortest path length is :", len(l))
   return ""

'''goal test method'''
def Goal_Test(state):
   return True if state == "_12345678" else False #if state is the goal state return True

'''Find the shortest path to the goal state "_12345678" and
   returns the path by calling display_path() function to print all steps.
   You can make other helper methods, but you must use dictionary for explored.'''
def BFS(initial_state):
   '''Your code goes here'''
   Q = queue.Queue()
   Q.put(initial_state) #add initial state to the queue
   explored = {initial_state:"s"} #add the initial state to explored with s as the parent as a stopping point
   
   while not Q.empty(): #while q isn't empty
      s = Q.get()
      if Goal_Test(s):
         return display_path(s, explored) #call display_path if goal test is passed
      for a in generate_children(s):
         if a not in explored: #if a hasn't already been explored
            Q.put(a)
            explored[a] = s #add a to explored with s as the parent
   return ("No solution")

'''Find the shortest path to the goal state "_12345678" and
   returns the path by calling display_path() function to print all steps.
   You can make other helper methods, but you must use dictionary for explored.'''
def DFS(initial):
   '''Your code goes here'''
   Q = []
   Q.append(initial) #same logic as BFS except put replaced with append and get replaced with pop
   explored = {initial:"s"}
   
   while Q:
      s = Q.pop()
      if Goal_Test(s):
         return display_path(s, explored)
      for a in generate_children(s):
         if a not in explored:
            Q.append(a)
            explored[a] = s
   return ("No solution")

def main():
   initial = getInitialState()
   #initial = "_42135678"
   print ("BFS start with:\n", initial[0:3], "\n", initial[3:6], "\n", initial[6:], "\n")
   print (BFS(initial))
   print ("DFS start with:\n", initial[0:3], "\n", initial[3:6], "\n", initial[6:], "\n")
   print (DFS(initial))

if __name__ == '__main__':
   main()