class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

def earliest_ancestor(ancestors, starting_node):
    q = Queue()
    tree = dict()
    current = starting_node

    for pair in ancestors:
        if pair[1] not in tree:
            tree[pair[1]] = set()
        tree[pair[1]].add(pair[0])

    if starting_node in tree:
        q.enqueue(tree[current])
    else:
        return -1
    
    while True:
        relation = q.dequeue()
        current = min(relation)
        if current not in tree:
            return current
        else:
            q.enqueue(tree[current])



