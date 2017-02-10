import pydot as pd
from src.parse_tree import *

# a = 3
node1 = addNodes("a",[])
node3 = addNodes("EQUALS",[])
node2 = addNodes("3",[])
node4 = addNodes("EXPRESSION",[(node2, None)])
node5 = addNodes("ASSIGN", [(node1, None), (node3, None), (node4, None)])

# a = b*3
node1 = addNodes("a",[])
node3 = addNodes("EQUALS",[])
node2 = addNodes("3",[])
node4 = addNodes("b",[])
node5 = addNodes("EXPRESSION",[(node4, None),(None, "TIMES"),(node2, None)])
node6 = addNodes("ASSIGN", [(node1, None), (node3, None), (node5, None)])



saveGraph() 
