
# Table : PP, current_offset, current_scope
# Entry : Tuple -- ( lexeme, type, size, offset )



def getSize(type):
    if type == "char":
        return 1
    if type == "int":
        return 4
    if type == "float":
        return 8
    if type == "double":
        return 8
    if type == "short":
        return 2
    if type == "long":
        return 8
    if type == "signed_int":
        return 4
    if type == "unsigned_int":
        return 4
    if type == "__int128":
        return 16
    if type == "_bool":
        return 1
    if type == "_complex":
        return 8
    if type == "SymbTab":
        return 0

class SymbolTable(object):
    GID = 0
    def __init__(self):
        self.id = SymbolTable.GID
        SymbolTable.GID += 1

    def makeNewTable(self, PP):
        if PP == None:
            self.table = { 'PP': None, 'cur_offset': 0, 'cur_scope': [], 'nesting': 0 }
            print("Creating Root SymbolTable:{}".format(self.id))
        else:
            PP.addEntry("ID"+str(self.id), "SymbTab")
            self.table = { 'PP': PP, 'cur_offset': 0, 'cur_scope': [], 'nesting': PP.getNesting()+1 }
            print("Creating a new SymbolTable:{}".format(self.id))
        return self

    def addEntry(self, lexeme, type):
        size = getSize(type)
        offset = self.table['cur_offset']
        self.table['cur_offset'] += size
        print("Adding entry : {} to SymbolTable: {}".format((lexeme, type, size, offset), self.id))
        self.table['cur_scope'].append((lexeme, type, size, offset))

    def popEntry(self):
        print("Popping entry from SymbolTable: {}".format(self.id))
        self.table['cur_scope'].pop()
        SymbolTable.GID -= 1
        
    def getCurOffset(self):
        return self.table['cur_offset']
    
    def getPP(self):
        return self.table["PP"]
    
    def getNesting(self):
        return self.table["nesting"]

