


# Time O(V + E) |Space O(V+E)
# Creates a graph of the jobs and edges to the dependancies
# for each node depth first search the graph, add dependancies on the way back up if all their
# dependancies have already been added
# if the node is part of the bredth search and it appears twice there is a cycle and return []
# go through all the rest of the nodes that havnt been visited

def topologicalSort(jobs, deps):
    jobGraph = createJobGraph(jobs, deps)
    return getOrderedJobs(jobGraph)


def createJobGraph(jobs, deps):
    graph = JobGraph(jobs)
    for prereq, job in deps:
        #add edges to graph
        graph.addPrereq(job, prereq)
    return graph

def getOrderedJobs(graph):
    orderedJobs = []
    nodes = graph.nodes
    while len(nodes):
        node = nodes.pop()
        containsCycle = depthFirstTraverse(node, orderedJobs)
        if containsCycle:
            return []
    return orderedJobs

def depthFirstTraverse(node, orderedJobs):
    if node.visited:
        return False
    if node.visiting:
        return True
    node.visiting = True
    for prereqNode in node.prereqs:
        containsCycle = depthFirstTraverse(prereqNode, orderedJobs)
        if containsCycle:
            return True
    node.visited = True
    node.visiting = False
    orderedJobs.append(node.job) 
    return False


class JobGraph():

    def __init__(self, jobs):
        self.nodes = []
        self.graph = {}

        for job in jobs:
            self.addNode(job)
    
    def addNode(self,job):
        self.graph[job] = JobNode(job)
        self.nodes.append(self.graph[job])

    def addPrereq(self, job, prereq):
        jobNode = self.getNode(job)
        prereqNode = self.getNode(prereq)
        jobNode.prereqs.append(prereqNode)

    def getNode(self, job):
        if job not in self.graph:
            self.addNode(job)
        return self.graph[job]

class JobNode():
    def __init__(self, job):
        self.job = job
        self.prereqs = []
        self.visited = False
        self.visiting = False


if __name__ == "__main__":
    jobs = [1,2,3,4,5]
    deps = [[1,2], [1,3], [2,3], [4,3]]
    k = topologicalSort(jobs, deps)
    print(k) 

[1,2_,3,4,5]
[
    1 : True
    2 : [1]
    3 : [1,2,3,4]
    4 : []
    5 : []
]

