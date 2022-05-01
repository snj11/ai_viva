graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : ['G', 'H'],
    'F' : ['I', 'J'],
    'J' : ['K'],
    'H' : ['L']
}

def DLS(start,goal,path,level,maxD):
  #print('\nCurrent level-->',level)
  #print('Goal node testing for',start)
  path.append(start)
  if start == goal:
    return path
  #print('Goal node testing failed')
  if level==maxD:
    return False
  #print('\nExpanding the current node',start)
  for child in graph[start]:
    if DLS(child,goal,path,level+1,maxD):
      return path
    path.pop()
  return False

start = 'A'
goal = input('Enter the goal node:-')
maxD = int(input("Enter the maximum depth limit:-"))
print()
path = list()
res = DLS(start,goal,path,0,maxD)
if(res):
    print("Path found!!")
    print("Path = ",path)
else:
    print("No path available for the goal node in given depth limit")
