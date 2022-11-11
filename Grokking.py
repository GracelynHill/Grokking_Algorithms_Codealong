#chapter 1: Introduction

#binary search
list = [i for i in range(100)]
def binary_search(list, item):
  low = 0
  high = len(list) - 1
  #101 items in list so have to minus 1
  mid = 0
  while low <= high: 
    #as long as we have items in the list,
    mid = (low + high) // 2 
    #take the number in the middle
    guess = list[mid] 
    #make that our guess
    if guess == item: 
      #if we're right we're done!
      return mid  
    elif guess > item: 
      #if it's less, then that's our new upper bound
      high = mid - 1
    elif guess < item: 
      #if it's more, that's our new lower bound
      low = mid + 1
  return None 
  #if we exit out of the while loop that means it's not in the list
print(binary_search(list, 47))
print(binary_search(list, 102))



#Chapter 2: selection sort

def findSmallest(arr):
  #we start by guessing that the first item is the smallest one
  smallest = arr[0] 
  smallest_index = 0
  for i in range(1, len(arr)): 
    #go through the list
    if arr[i] < smallest: 
      #if the item we find is smaller than the first item,
      smallest = arr[i] 
      smallest_index = i
      #we make it our new smallest
  return smallest_index

def selectionSort(arr):
  newArr = []
  for i in range(len(arr)):
    #find the smallest item in the list
    smallest = findSmallest(arr)
    #remove it from our first list and put it at the front of our new list
    newArr.append(arr.pop(smallest))
  return newArr
arr = [5, 3, 6, 2, 10]
print(selectionSort(arr))


#Chapter 3: Recursion

def fact(x):
  if x == 1:
    return 1
  else:
    return x * fact(x-1)
  #What's happening in the call stack here?
  #fact(3) calls fact(2) which calls fact(1)
  #fact(1) = 1, which returns to fact(2).
  # 2 * 1 = 2, which returns to fact(3)
  # 3 * 2 = 6, which returns to our original print function so we only see 6. Wow!
print(fact(3))


#Chapter 4: Quicksort

#basic sum function
def sum(arr):
  total = 0
  for x in arr:
    total += x
  return total
print(sum([1, 2, 3, 4]))

def recursivelen(arr):
  if not arr:
    return 0
  else:
    return 1 + recursivelen(arr[1:])
  #recursivelen(1, 2, 3) calls recursivelen(2, 3) calls recursivelen(3)
  #recursivelen(3) = 0 + 1 = 1
  #recursivelen(2, 3) = 1 + 1 = 2
  #recursivelen(1, 2, 3) = 1 + 2 = 3
print(recursivelen([1,2,3]))

def findLargest(arr):
  largest = arr[0] 
  for i in range(1, len(arr)): 
    if arr[i] > largest: 
      largest = arr[i]
  return largest
print(findLargest([1,2,3]))

def quicksort(arr):
  #base case: arrays of 1 and 0 don't need sorting
  if len(arr) < 2:
    return arr
  else:
    #first item in the list becomes a dividing line - aka pivot
    pivot = arr[0]
    #goes in less if the items are less or equal to pivot
    less = [i for i in arr[1:] if i <= pivot]
    #goes in more if more
    greater = [i for i in arr[1:] if i > pivot]
    #then sort the greater and less - will recursively go through the sublists and divide into greater or less until it reaches divisions less than 2
    return quicksort(less) + [pivot] + quicksort(greater)
print(quicksort([5, 7, 3, 2]))
#this is a bad quicksort implementation because it doesn't use a random value as the pivot, but whatever.

#chapter 5: hash tables
#idk why this chapter is in here, I know what a dictionary is
#simple voting system
voted = {}
def check_voter(name):
  if voted.get(name):
    print("get out, " + name + "!")
  else:
    voted[name] = True
    print("go to the polls, " + name + "!")
check_voter("Grace")
check_voter("Ben")
check_voter("Ben")


#chapter 6: breadth first search

#setting up a directed graph
friends = {}
friends["Me"] = ["Ben", "Kyler", "Lein"]
friends ["Lein"] = ["Adler"]
friends["Ben"] = ["Adler", "Amery"]
friends["Kyler"] = ["Connor", "Jamie"]
friends["Connor"] = []
friends["Jamie"] = []
friends["Adler"] = []
friends["Amery"] = []
#these people all have friends in real life i'm just using an example lol
from collections import deque
#double ended queue function
def bfs():
  search_queue = deque() #sets up queue object
  search_queue += friends["Me"] #add me to queue
  searched = [] #keeps track of our steps so we don't loop forever
  print(str(friends["Me"]) + " added to back of queue")
  while search_queue: #while there are objects on the queue
    person = search_queue.popleft() #pop name off the queue
    if person not in searched: #checks our steps
      print("checking " + person)
      if personY(person): #check if name ends in Y
        print(person + "'s name ends in Y!") #if so, we're done!
        return True
      else:
        print(str(friends[person]) + " added to back of queue")
        search_queue += friends[person] #if not, add all their friends to the queue
        searched.append(person)
  return False #base case: no names end in y
def personY(name):
  return name[-1] == "y" #name end in y checker

bfs()


#Dijkstra's Algorithm, but with printing
#All of the code for setting up the graph, and the algorithm itself, comes from chapter 6 of Grokking Algorithms by Aditya Bhargava
#The printing function is my own work (with help from stack overflow of course ^_^)

graph = {}
#weighted graph
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph ["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}

#table of lowest cost to reach each node
infinity = float("inf") # must be impossible to choose a node without an accessible edge
costs = {}
costs["start"] = 0
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

#parents hash
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None
processed = [] #make sure we dont recalculate nodes over and over

def dijkstra(graph, costs, parents):
  node = findCheapest(costs) #find cheapest node not yet processed
  while node is not None: #while we have nodes to process
    cost = costs[node] #take the node found
    neighbors = graph[node]
    for n in neighbors.keys(): #look at neighbors of the node
      new_cost = cost + neighbors[n] #check cost of path
      if costs[n] > new_cost: #if we've found a cheaper path
        costs[n] = new_cost #update that to be our new cost
        parents[n] = node #and our new best-guess path
    processed.append(node)
    node = findCheapest(costs) #add to processed and loop
  printPath(parents, costs, "start", "fin")

def findCheapest(costs):
  lowest_cost = float("inf")
  lowest_cost_node = None
  for node in costs:
    cost = costs[node]
    if cost < lowest_cost and node not in processed:
      lowest_cost = cost
      lowest_cost_node = node
  return lowest_cost_node

def printPath(path, costs, start, end): #takes dijkstra parents, costs, start node name, and end node names as input
  pathList = [start]
  step = start
  switchPath = {y: x for x, y in path.items()} #need to switch keys and values around. from https://stackoverflow.com/questions/8305518/switching-keys-and-values-in-a-dictionary-in-python
  finalPath = {}
  while end not in pathList: #"walks" through the path until it finds the end
    nextStep = switchPath[step]
    pathList.append(nextStep)
    step = nextStep
  for i in pathList:
    finalPath[i] = costs[i] #creates a dict with path as keys and costs as values, this time in the correct order
  result = "".join(str(key) + "(" + str(value) + ") -> " for key, value in finalPath.items()) #pretty dictionary string code from https://stackoverflow.com/questions/39578141/python-how-to-print-dictionary-in-one-line
  print(result.rstrip(" ->")) #clean up and print
  

dijkstra(graph, costs, parents)


#Chapter 8: Greedy Algorithms

#sets differ from lists b/c sets can't have duplicates
stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

def radioGreed():
  states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])
  final_stations = set([])
  while states_needed: #as long as there are still states to cover,
    best_station = None
    states_covered = set()
    for station, station_states in stations.items(): #look through each station
      covered = states_needed & station_states
      if len(covered) > len(states_covered): #if it covers more states than our last pick
        best_station = station #it becomes our new pick
        states_covered = covered
    states_needed -= states_covered #subtract from states to cover once you pick one
    final_stations.add(best_station) #and add to our list of stations to use
  print(final_stations)
#Station. 
radioGreed()


#Chapter 9: Dynamic Programming

def lcss(s1, s2):
  m = len(s1)
  n = len(s2)
  grid = [[0] * (n + 1) for x in range(m+1)] #init grid with zeros size of strings
  longest = 0
  lcs_set = set() 
  for i in range(m): #go through the grid
    for j in range(n):
      if s1[i] == s2[j]: #if we find a match,
        c = grid[i][j] + 1 #add 1 to the count
        grid[i+1][j+1] = c #at the spot 1 diagonally down
        if c > longest: #if the count is higher than before,
          lcs_set = set()
          longest = c #take note of that,
          lcs_set.add(s1[i-c+1:i+1]) #and make our lcss guess go from c+1 back from our match to 1 after the match (why is it offset by 1??)
        elif c == longest:
          lcs_set.add(s1[i-c+1:i+1]) #same if it's equal
  return lcs_set
ret = lcss("academy", "abracadabra")
for s in ret:
  print(s)
ret = lcss("AGCTGCTACACGTCA", "ACACAACTGGTCAGCTACGT")
for s in ret:
  print(s)