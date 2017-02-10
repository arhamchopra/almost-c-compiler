import pydot as pd

i=0

graph = pd.Dot(graph_type = "graph", ordering = "out" )

def addNodes(root, child_list):
    global i
    global graph
    rnode = pd.Node( "id{}".format(i) ,label = root)
    i+=1
    graph.add_node(rnode)
    for child in child_list:
        #  print(child)
        if child[0] is None:
            cnode = pd.Node("id{}".format(i),label = child[1])
            i+=1
            graph.add_node(cnode)
            #  print("CHILD IS NONE")
        else:
            cnode = child[0]
            #  print("CHILD IS NOT NONE")
        #  print("RNODE:{} CNODE:{}".format(rnode, cnode))
        graph.add_edge(pd.Edge(rnode,cnode))

    return rnode

def saveGraph():
    graph.write_png("ParseTree.png")
