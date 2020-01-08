
#Reporting Graph structure
# Use depth first search keep track of if a reportis found passing it back up the chain
#on the way back up if 2 reports are found the lcm is set
# check the if lcm is found as going back up chain
# 
# Time O(N) traverse each node
# Space O(d) for depth first search 
def getLowestCommonManager(topManager, reportOne, reportTwo):

    lcm,_ = lcmHelper(topManager, reportOne, reportTwo)
    return lcm

def lcmHelper(manager, reportOne, reportTwo):
    
    lcm = None
    allReportsFound = 0
    #depth first search
    for report in manager.directReports:
        lcm, reportsFound = lcmHelper(report, reportOne, reportTwo)
        allReportsFound += reportsFound
        if lcm is not None:
            return lcm, allReportsFound
    if manager == reportOne or manager == reportTwo:
        allReportsFound += 1
    if reportsFound == 2:
        lcm = manager
    return lcm, allReportsFound

