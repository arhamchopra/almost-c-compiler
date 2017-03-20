from symbol_table import SymbolTable as ST

a = ST("A")
a.makeNewTable(None)
a.addEntry("a", "int")
a.addEntry("b", "int")
a.addEntry("c", "int")
a.addEntry("d", "int")
a.addEntry("e", "int")
a.addEntry("f", "int")
b = ST("B")
b.makeNewTable(a)
b.addEntry("a", "int")
b.addEntry("b", "int")
b.addEntry("c", "int")
print(b.lookupCurrentScope( "a"))
print(b.lookupCurrentScope( "c"))
print(b.lookupCurrentScope( "b"))
print(b.lookupFullScope( "a"))
print(b.lookupFullScope( "b"))
print(b.lookupFullScope( "c"))
print(b.lookupFullScope( "d"))
