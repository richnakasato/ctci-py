from collections import deque

def route_nodes(adj_dict, start, end):
    #TODO: error handling
    path = list()
    visited = set()
    to_visit = deque()
    to_visit.append((start, path))
    while len(to_visit):
        curr, path = to_visit.popleft()
        if curr not in visited:
            visited.add(curr)
            path.append(curr)
            if curr == end:
                return path
            for item in adj_dict[curr]:
                to_visit.append((item, path))
    return None

def has_path(adj_dict, start, end):
    path = route_nodes(adj_dict, start, end)
    print(path)
    return path != None


def main():
    graph1 = {'A': ['B', 'C'],
              'B': ['C', 'D'],
              'C': ['D'],
              'D': ['C'],
              'E': ['F'],
              'F': ['C'] }
    graph2 = {'A': ['B'],
              'B': ['A', 'C'],
              'D': ['A'] }
    print(has_path(graph1, 'A', 'F'))
    print(has_path(graph1, 'A', 'E'))
    print(has_path(graph1, 'A', 'D'))
    print(has_path(graph1, 'E', 'D'))

if __name__ == "__main__":
    main()

