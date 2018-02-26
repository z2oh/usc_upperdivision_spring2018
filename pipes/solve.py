# With path compression and union by rank, performing N operations on the
# DisjointSet will result in a running time that is almost linear on N. While
# it is strictly superlinear, in the case of this problem the input constraints
# can be used to place a linear upper bound on the running time.
class DisjointSet:
    # We make sure that the node's parent is set to itself to start, and that
    # the rank of the node is 0.
    def make_set(x):
        x.p = x
        x.rank = 0

    # We link the two nodes that are representative of the set for x and y.
    def union(x, y):
        DisjointSet.link(DisjointSet.find_set(x), DisjointSet.find_set(y))

    # We link the two nodes x and y.
    def link(x, y):
        # Here we are using union by rank to keep the asymptotic complexity
        # as low as possible.
        # If x's rank is greater than y's, y is set as a child of x.
        if x.rank > y.rank:
            y.p = x
        else:
            x.p = y
            # If the ranks are equal, we must increase the rank of the new
            # parent (y).
            if x.rank == y.rank:
                y.rank = y.rank + 1

    # We find the representative node for x, which is the root node for the
    # tree of which x is a member.
    def find_set(x):
        if x != x.p:
            # Here we perform path compression by making sure that the root
            # node is the parent of as many nodes in the tree as possible,
            # which speeds up future accesses.
            x.p = DisjointSet.find_set(x.p)
        return x.p

# The Node object. This is a node in our DisjointSet, not a node in our input
# graph. It is initialized with the id of the vertex in our input graph.
class Node:
    def __init__(self, id):
        self.id = id

# T is the number of test cases.
T = int(input())

# Iterate over our test cases
for _ in range(T):
    # num is the number of vertices in our graph.
    num = int(input())

    # We maintain a set of the vertices, to make sure we have the ids for 
    # each one.
    vertices = set()

    # We also maintain a set of the edges in our graph.
    edges = set()

    # Our input gives us `num - 1` lines, with each line containing the leading
    # edge id, followed by the number of edges, and then a list of trailing
    # edge ids and the edge weights.
    # For example 5 2 7 11 9 10 means:
    # There are two edges connecting with vertex 5, an edge to vertex 7 (with
    # weight 11) and an edge to vertex 9 (with weight 10).
    for _ in range(num - 1):
        line = input().split(' ')
        leading = line[0]
        numEdges = int(line[1])
        # For each edge specified in our input line
        for i in range(numEdges):
            # We add 2 to all indices to account for the leading edge and
            # number of edges in our input line.
            trailing = line[2 + i * 2]
            # Add the leading and trailing edges to the set to make sure we get
            # every vertex.
            vertices.add(leading)
            vertices.add(trailing)
            # We add the edge to our edges set. An edge is represented by a
            # 3-tuple, (leading edge id, trailing edge id, weight)
            # Since each edge in specified in our line has two space separated
            # pieces, we can index to the edge specified with i * 2. We again
            # add 2 to index past the leading edge id and number of edges, then
            # add 1 to index to the weight.
            edges.add((leading, trailing , int(line[2 + i * 2 + 1])))

    # We will store our disjoint set forest in a dictionary. The keys of the
    # dictionary will be the vertex ids, and the values will be the nodes of
    # our disjoint-set trees.
    forests = {}
    for vertex in vertices:
        # Create a node with the vertex and assign it to the key `vertex`,
        # which is the id of the vertex.
        forests[vertex] = Node(vertex)
        # We call `make_set` on the node to assign its parent as itself and
        # set its rank to 0.
        DisjointSet.make_set(forests[vertex])

    # Now we convert our edges set into a list, and sort it by edge weight.
    edges = list(edges)
    edges.sort(key = lambda edge: edge[2])

    # We iterate over every edge. `total` keeps track of the sum total of all
    # the weights of the edges that we add to our MSP.
    total = 0
    while len(edges) > 0:
        edge = edges.pop(0)
        # We call find_set on the leading and trailing ids of the edge in
        # question.
        set_leading = DisjointSet.find_set(forests[edge[0]])
        set_trailing = DisjointSet.find_set(forests[edge[1]])

        # We have found an edge that connects two componenets of our graph.
        # This edge should be added to the MSP weight total.
        if set_leading != set_trailing:
            # We must now union the nodes for our leading and trailing ids for
            # this edge. Path compression and union by rank are used in this
            # implementation of disjoint set forests to ensure maximum
            # efficiency.
            DisjointSet.union(forests[edge[0]], forests[edge[1]])
            total += edge[2]

    # Print out our total. On to the next test case!
    print(total)
