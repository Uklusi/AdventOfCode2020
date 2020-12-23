result = 0
MAXCUP = 1000000
MAXITER = 10000000


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        return str(self.data)

    def __eq__(self, node):
        return self.data == node.data

    def __ne__(self, node):
        return not self == node


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        self.tail = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                prevnode = node
                node = node.next
                node.prev = prevnode
            node.next = self.head
            self.tail = node
            self.head.prev = node

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        if self.head is not None:
            yield self.head
            node = self.head.next
            while node is not None and node != self.head:
                yield node
                node = node.next


with open("input.txt", "r") as input:
    fileContent = input.read().strip()
    cups = [int(n) for n in fileContent]

cups += list(range(max(cups) + 1, MAXCUP + 1))

cups = LinkedList(nodes=cups)

nodes = [node for node in cups]
nodes.sort(key=(lambda node: node.data))

nodes = [None] + nodes

currCup = cups.head
for i in range(MAXITER):
    crab = [currCup.next, currCup.next.next, currCup.next.next.next]
    n = currCup.data - 1
    while n <= 0 or nodes[n] in crab:
        n = n - 1
        if n <= 0:
            n = MAXCUP
    crab[0].prev.next = crab[2].next
    crab[2].next.prev = crab[0].prev
    nbefore = nodes[n]
    nafter = nbefore.next
    nbefore.next = crab[0]
    crab[0].prev = nbefore
    nafter.prev = crab[2]
    crab[2].next = nafter
    currCup = currCup.next

i1 = nodes[1]

result = i1.next.data * i1.next.next.data

with open("output2.txt", "w") as output:
    output.write(str(result))
    print(str(result))
