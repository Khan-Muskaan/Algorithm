v=4
inf=99999
def floydWarshall(graph):
    dist=list(map(lambda i: list(map(lambda j:j,i)),graph))
    for k in range(v):
        for i in range(v):
            for j in range(v):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    printSolution(dist)

def printSolution(dist):
    print ("Following matrix shows the shortest distance/ between every pair of vertices")
    for i in range(v):
        for j in range(v):
            if(dist[i][j] == inf):
                print ("%7s" %("inf")),
            else:
                print("%7d\t" %dist[i][j]),
            if j==v-1:
                print ("")

graph = [[0,5,inf,10],         [inf,0,3,inf],
         [inf,inf,0,1],
         [inf,inf,inf,0]]
floydWarshall(graph)
                
