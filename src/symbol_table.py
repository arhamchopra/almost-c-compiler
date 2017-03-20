
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
# This class include all the functionality of SymbolTable 
class SymbolTable(object):
    GID = 0             #SymbolTable Id for indetification purpose

    # Initialize the SymbolTable
    def __init__(self, name=None):
        self.id = SymbolTable.GID
        SymbolTable.GID += 1
        print("Name = "+str(name))
        if name is None:
            self.name = "ID"+str(self.id)
        else:
            self.name = name

    def makeNewTable(self, PP):
        if PP == None:
            self.table = { 'PP': None, 'cur_offset': 0, 'cur_scope': [], 'nesting': 0 }
            print("Creating Root SymbolTable:{}".format(self.id))
        else:
            self.table = { 'PP': PP, 'cur_offset': 0, 'cur_scope': [], 'nesting': PP.getNesting()+1 }
            PP.addEntry(self.name, "SymbTab", self)
            print("Creating a new SymbolTable:{} name:{}".format(self.id, self.name))
        return self

    def addEntry(self, lexeme, type, child=None):
        size = getSize(type)
        offset = self.table['cur_offset']
        self.table['cur_offset'] += size
        print("Adding entry : {} to SymbolTable: {}".format((lexeme, type, size, offset), self.id))
        if type == "SymbTab":
            self.table['cur_scope'].append((lexeme, type, child, offset))
        else:
            self.table['cur_scope'].append((lexeme, type, size, offset))


    def popEntry(self):
        print("Popping entry from SymbolTable: {}".format(self.id))
        e = self.table['cur_scope'].pop()
        print("{} was popped".format(e))

    def setLastLexeme(self, lexeme):
        print("Setting last lexeme: {} to {}".format(e, lexeme))
        e = self.table["cur_scope"].pop()
        e[0] = lexeme
        self.table["cur_scope"].append(e)

        
    def getCurOffset(self):
        return self.table['cur_offset']
    
    def getPP(self):
        return self.table["PP"]
    
    def getNesting(self):
        return self.table["nesting"]
    
    def lookupCurrentScope(self, name):
        for entry in self.table['cur_scope']:
            if entry[0] == name:
                return entry
        return None

    def lookupFullScope(self,  name):
        found = self.lookupCurrentScope(name)
        if found:
            return found
        else:
            PP = self.table['PP']
            if PP:
                self = PP
                return self.lookupFullScope(name)
            else:
                return None

    def Print(self):
        print("Printing SymbolTable:"+ str(self.id))
        for entry in self.table['cur_scope']:
            if entry[1] == "SymbTab":
                entry[2].Print()
            else:
                print(entry)
        print("Finished SymbolTable:"+ str(self.id))
                
