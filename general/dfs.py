def solvePackageDependency(array):
    order = len(array)
    for node in array:
        node.explored = False
    for node in array:
        if node.explored is False:
            order = DFS(node, order)

    array.sort(key=lambda node: node.order)
    return array


def DFS(node, order):
    node.explored = True
    for edge in node.dependencies:
        if edge.explored is False:
            order = DFS(edge, order)
    node.order = order
    order -= 1
    return order


class Package:
  def __init__(self, packageId, dependencies):
      self.packageId = packageId
      self.dependencies = dependencies
      self.explored = False
      self.order = -1
  def __repr__(self):
      return self.packageId

packageE = Package("E", [])
packageD = Package("D", [])
packageC = Package("C", [packageD, packageE])
packageB = Package("B", [])
packageA = Package("A", [packageB, packageC])

print "Solving package dependency"
print solvePackageDependency([packageD, packageC, packageA, packageB, packageE]), ["A", "B/C", "B/C", "D/E", "D/E"]


def BFS(array):
  for node in array:
      node.explored = False

  q = [array[0]]
    
  while q:
      node = q.pop()
      if node.explored is False:
          node.explored = True
          print node
          q += node.dependencies
                

print "Running BFS"
BFS([packageA, packageD, packageC, packageB, packageE])
