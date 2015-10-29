from collections import namedtuple
import itertools
import random

Link = namedtuple('Link', ['dest', 'cost'])

class Node:
  def __init__(self, id = None, name = None, links = None):
    self.id = id
    self.name = name
    self.links = []
    if links:
      self.links.extend(links)
  def __str__(self):
    return "<Node: %s>" % (self.name)
  def dfs(self, targets):
    paths = []
    self._dfs(targets, (), (), paths)
    return paths

  def _dfs(self, targets, visited, path, paths):
    visited = tuple(itertools.chain(visited, [self]))
    path = tuple(itertools.chain(path, [self]))
    if not targets:
      targets = self.links
    next_links = [link for link in self.links if link.dest not in visited and link.dest in targets]
    for link in next_links:
      newpath = link.dest._dfs(targets, visited, path, paths)
      if newpath:
        paths.append(newpath)
    if not next_links:
      return path

class Graph:
  def __init__(self, root = None, nodes = None):
    self.nodes = []
    if nodes:
      self.nodes.extend(nodes)
    if root:
      if root not in self.nodes:
        self.nodes.append(root)
      self.root = root

# Calculate inter-floor travel times
def calctime(d, a, v, j):
  t = None
  if d == 0:
    return 0
  if d >= ((a ** 2) + (v**2 * j) / (a * j)):
    t = (d / v) + (v / a) + (a / j)
  elif ((2 * a**3) / j**2) <= d*((a ** 2) + (v**2 * j) / (a * j)):
    t = (a / j) + (((4*d / a) + (a / j)**2) ** (1/2))
  return t

# Generate building data
def genFloorData(floors, fheight, accel, speed):
  jerk = accel*.8
  floor_nodes = [Node(i+1) for i in range(floors)]
  for i in range(floors):
    for j in range(floors):
      d = abs(j - i) * fheight
      floor_nodes[i].links.append(Link(floor_nodes[j], calctime(d, accel, speed, jerk)))
  return floor_nodes

def calc_lengths(paths):
  #Return format: [(path, path_length), ...]
  path_lengths = []
  for path in paths:
    length = 0
    for i, n in zip(range(len(path)), path):
      for l in n.links:
        if i < len(path)-1 and l.dest == path[i+1]:
          length += l.cost
    path_lengths.append((path, length))
  return path_lengths

class ElevatorData:
  def __init__(self, floors):
    self.floor_nodes = genFloorData(floors, 4.5, 1, 3)
  def find_route(self, current_floor, targets):
    root = self.floor_nodes[current_floor-1]
    paths = calc_lengths(root.dfs(targets))
    sp = sorted(paths, key=lambda x: x[1])[0]

    for n in sp[0]:
      print(n.id, end=' -> ')
    print('x')
    print(sp[1],'\n')

    return sp[0]
  def gen_scenario(self, length):
    return random.sample(self.floor_nodes, length)



#root = floor_nodes[0]

# Generate random test scenarios
#scenarios = []
#for i in range(10):
#  scenarios.append(random.sample(floor_nodes, 5))

#for sc in scenarios:
#  paths = calc_lengths(root.dfs(sc))
#  sp = sorted(paths, key=lambda x: x[1])[0]
#  for n in sp[0]:
#    print(n.name)
#  print(sp[1],'\n')
