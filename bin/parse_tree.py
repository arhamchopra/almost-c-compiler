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
        print(child)
        if child[0] is None and child[1] is not None:
            cnode = pd.Node("id{}".format(i),label = child[1])
            i+=1
            graph.add_node(cnode)
            #  print("CHILD IS NONE")
            graph.add_edge(pd.Edge(rnode,cnode))

        elif child[0] is not None :
            cnode = child[0]
            graph.add_edge(pd.Edge(rnode,cnode))

            #  print("CHILD IS NOT NONE")
        #  print("RNODE:{} CNODE:{}".format(rnode, cnode))

    return rnode

def createTypeNode(type):
    global i
    global graph
    t_node = addNodes(type,[])
    type_node = addNodes("type_specifier", [(t_node, None)])
    decl_spec_node = addNodes("declaration_specifier",[(type_node, None)])
    return decl_spec_node
    
def saveGraph(fname = "ParseTree.png"):
    graph.write_png(fname)
    

