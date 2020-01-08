
class Airport:
    def __init__(self, name):
        self.name = name
        #list of airports nodes
        self.connections = []

class AirportGraph:
    
    #Time   O(a + r)
    #Space  O(a + r)
    def __init__(self, airports, routes):
        self.airports = {name : Airport(name) for name in airports}
        for start, destination in routes:
            self.airports[start].connections.append(self.airports[destination])
    
    #Time   worst O(a+r)    if every airport can be reached   
    #Space  worst O(a+r)    if all airports are only connected by one route in a circle/line
    def reachableAirports(self, airport, visited=None):
        #depth first search with loop prevention
        if visited is None:
            visited = {}
        if airport in visited:
            return visited
        visited[airport] = True 
        node = self.airports[airport]
        if not len(node.connections):
            return visited
        for ap in node.connections:
            visited = self.reachableAirports(ap.name, visited = visited)
        return visited

    # Time worst (a+r)
    #space worst (a+r)
    def unreachableAirports(self, airport):
        aps = self.airports.copy()
        reachable = self.reachableAirports(airport)
        for ap in reachable:
            del(aps[ap])
        return aps     

    def getValueOfAirports(self, airports):
        airports = list(airports.keys())
        apVals = {}
        for ap in airports:
            val = len(self.reachableAirports(ap))
            if val in apVals:
                apVals[val][ap] = True
            else:
                apVals[val] = {ap:True}
        return apVals
    

def airportConnections(airports, routes, startingAirport):
    graph = AirportGraph(airports, routes)
    unreachableAirports = graph.unreachableAirports("PERTH")
    valToAp = graph.getValueOfAirports(unreachableAirports)
    # create mirror dict
    apToVal = {}
    for val, aps in valToAp.items():
        for ap in aps:
            apToVal[ap] = val 
    priorityVals = sorted(list(valToAp.keys()))

    n = 0
    while len(unreachableAirports):
        n += 1
        
        j = -1
        while not len(valToAp[priorityVals[j]]):
            j -=1
        curVal = priorityVals[j]
        reachableAps = graph.reachableAirports(list(valToAp[curVal].keys())[-1])
        for key, val in reachableAps.items():
            if key in unreachableAirports:
                del(unreachableAirports[key])
            if key in apToVal:
                del(valToAp[apToVal[key]][key])
        # apVals = graph.getValueOfAirports(unreachableAirports)
        # priorityVals = sorted(list(apVals.keys()))
    return n
    #setup graph
    #get unreachable airports
    #get values of unreachable airports
    # num = 0
    # while len(unreachableAps):
    #     curAp = unreachableAps[-1]
    #     curReachable = graph.reachableAps(curAp)
    #     for delAp in curReachable:
    #         del(unreachableAps[delAp])


if __name__ == "__main__":
    airports = ["SYD", "MELB", "BRIS", "PERTH"]
    flights = [
        # ["SYD", "MELB"], 
        # ["SYD", "BRIS"],
        # ["MELB", "PERTH"],
        # ["PERTH", "BRIS"],
        #["MELB", "SYD"]
        ]
    n = airportConnections(airports, flights, "PERTH")
    print(n)


#Dump all aiports into a graph
#create list of airports
#From starting airpot remove all reachable airports from list
#now have list of unreachable airports

#asign a number to each airport by how many unreachable airports it can access
#depth first search the airport terminating at any airport not in unreachable list
#to get the number of unreachable airports it can access 
#NOTE: handle loops

# go through each airport from greatest amount of unreachable airports to least
# depth first traverse to remove all reachable airports
# for each airport needed increment counter

#return counter when no unreachable airports left