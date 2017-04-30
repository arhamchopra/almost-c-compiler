
# Table : PP, current_offset, current_scope
# Entry : Tuple -- ( lexeme, type, size, offset )
import c_ast

user_debug = False 

def printDebug(s):
    if user_debug:
        print(s)

def getSize(type):
    print("[getSize]IN GET SIZE")
    print("[getSize]"+str(type))
    if isinstance(type, c_ast.TypeDecl):
        return getSize(type.type)
    if isinstance(type, c_ast.IdentifierType):
        return getSize(type.names[-1])
    if type == "void":
        return 0
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
    if isinstance(type, c_ast.PtrDecl):
        return 8
    if isinstance(type, c_ast.ArrayDecl):        
        printDebug(type.dim)
        print("[getSize]")
        print(type)
        print(type.dim)
        return int(type.dim.value)*getSize(type.type)
    if isinstance(type, c_ast.FuncDecl):
        return 0
    if isinstance(type, c_ast.Struct):
        st = SymbolTable()
        entry = st.lookupStructT(type.name)
        print(entry)
        if entry:
            return entry[1]
        else:
            assert False


# This class include all the functionality of SymbolTable 
class SymbolTable(object):
    GID = 0             #SymbolTable Id for indetification purpose
    GST=None
    FT=[]
    StructT=[]

    # Initialize the SymbolTable
    def __init__(self, name=None):
        self.id = SymbolTable.GID
        self.temp_id = 1
        SymbolTable.GID += 1
        printDebug("Name = "+str(name))
        if name is None:
            self.name = "ID"+str(self.id)
        else:
            self.name = name

    def makeNewTable(self, PP):
        if PP == None:
            self.table = { 'PP': None, 'cur_offset': 0, 'cur_scope': [], 'nesting': 0 }
            SymbolTable.GST=self
            printDebug("Creating Root SymbolTable:{}".format(self.id))
        else:
            self.table = { 'PP': PP, 'cur_offset': 0, 'cur_scope': [], 'nesting': PP.getNesting()+1 }
            PP.addEntry(self.name, "SymbTab", self)
            printDebug("Creating a new SymbolTable:{} name:{}".format(self.id, self.name))
        return self

    def addEntry(self, lexeme, type, child=None):
        try:
            print("[addEntry]Adding the entry to ST " + str((lexeme, type.type)))
        except:
            print("[addEntry]Adding the entry to ST " + str((lexeme, type)))
            pass
        if isinstance(type, c_ast.FuncDecl):
            if child:
                size = child.table['cur_offset']
            else:
                size = 0
        else:
            if lexeme[0] == "#" and isinstance(type, c_ast.ArrayDecl):
                size = 8
            else:
                size = getSize(type)
        offset = self.table['cur_offset']
        self.table['cur_offset'] += size
        pointer = (offset, len(self.table['cur_scope']), self)
        printDebug("Adding entry : {} to SymbolTable: {}".format((lexeme, type, size, offset, child, pointer), self.id))
        self.table['cur_scope'].append((lexeme, type, offset, size, child, pointer))
        return pointer

    def addToFT(self, lexeme, type, status, child=None, p_list=None):
        for entry in SymbolTable.FT:
            if lexeme == entry[0]:
                adderror("Reusing a used name")
                return
        SymbolTable.FT.append((lexeme, type, status, child, p_list))

    def lookupElemFT(self, name, fscope):
        if fscope[3]:
            print(fscope[3])


    def popEntry(self):
        printDebug("Popping entry from SymbolTable: {}".format(self.id))
        e = self.table['cur_scope'].pop()
        if e[1] == "SymbTab":
            self.table['cur_offset'] -= e[4].table['cur_offset']
        else:
            self.table['cur_offset'] -= getSize(e[1])
        printDebug("{} was popped".format(e))
        return e

    def removeEntry(self, name):
        printDebug("IN removeEntry")
        for entry in SymbolTable.FT:
            if name == entry[0]:
                ret = entry
                SymbolTable.FT.remove(ret)
                printDebug(ret)
                return ret 


    def popFT(self):
        printDebug("Popping entry from FT: ")
        e = SymbolTable.FT.pop()
        printDebug("{} was popped".format(e))
        return e


# StructEntry : (lexeme, size,  entries)
# Object of StructEntry : (lexeme, type, size, offset)
#  Entries will be a list of Decl Objects and we will extract the type of the them and add them to ST.
    def addToStructT(self, name, entries):
        printDebug(name)
        offset = 0
        entries_template = []
        for var in entries:
            elem = var.type
            printDebug(elem.declname)
            printDebug(elem.type.type)
            elem_size = getSize(elem.type.type[-1])
            entries_template.append((elem.declname, elem.type.type[-1], elem_size, offset))
            offset = offset + elem_size 

        SymbolTable.StructT.append((name, offset, entries_template))
        return (name, offset, entries_template)

    def popStructT(self, name):
        return SymbolTable.StructT.pop()

    def lookupStructT(self, name):
        printDebug("[lookupStructT]In lookupStructT looking for " +str(name))
        for entry in SymbolTable.StructT:
            printDebug("[lookupStructT]Found " + entry[0])
            if entry[0] == name:
                printDebug("[lookupStructT]Found Entry " +str(name)+" in StructT")
                return entry

        printDebug("[lookupStructT]DId not find Entry " +str(name)+" in StructT")
        return None

    def getStructTentry(self, struct_name, elem_name):
        printDebug("[getStructTentry]In getStructTentry looking for " +str(elem_name))
        struct = self.lookupStructT(struct_name)
        for elem in struct[2]:
            if elem[0] == elem_name:
                printDebug("[getStructTentry]Found Elem " +str(elem_name))
                return elem

        printDebug("[getStructTentry]Did not find Elem " +str(elem_name))
        return None

    def getLastElemFT(self):
        return SymbolTable.FT[-1]

    def setLastLexeme(self, lexeme):
        printDebug("Setting last lexeme: {} to {}".format(e, lexeme))
        e = self.table["cur_scope"].pop()
        e[0] = lexeme
        self.table["cur_scope"].append(e)

    def setOffset(self, offset):
        self.table['cur_offset'] = offset

    def getCurOffset(self):
        return self.table['cur_offset']

    def getPP(self):
        return self.table["PP"]

    def getNesting(self):
        return self.table["nesting"]

    def getElementAtIndex(self, index):
        return self.table['cur_scope'][index]

    def lookupCurrentScope(self, name):
        for entry in self.table['cur_scope']:
            if entry[0] == name:
                return entry
        return None

    def lookupFT(self, name):
        printDebug("Looking for {}".format(name))
        for entry in SymbolTable.FT:
            if entry[0] == name:
                printDebug("Entry Found in FT")
                return entry
            printDebug("Not Looking for but Found Entry: {} ".format(entry))
        printDebug("Not Found in FT")
        return None

    def lookupFullScope(self,  name):
        printDebug("[lookupFullScope]Looking for " + name)
        entry = self._lookupFullScope(name)
        printDebug(entry)
        if entry:
            printDebug("Found in ST")
            printDebug(name)
            l = list(entry)
            l.append("ST")
            entry = tuple(l)
            return entry
        else:
            entry = self.lookupFT(name)
            if entry:
                printDebug("Found in function")
                printDebug(name)
                l = list(entry)
                l.append("FT")
                entry = tuple(l)
                return entry
            else:
                return None


    def _lookupFullScope(self,  name):
        found = self.lookupCurrentScope(name)
        if found:
            return found
        else:
            PP = self.table['PP']
            if PP:
                self = PP
                return self._lookupFullScope(name)
            else:
                return None

    def Print(self):
        print("Printing SymbolTable:"+ str(self.id))
        for entry in self.table['cur_scope']:
            if entry[4]:
                print(entry)
                entry[4].Print()
            else:
                print(entry)
        print("Finished SymbolTable:"+ str(self.id))

    def PrintFT(self):
        print("Printing Function Table")
        for i in SymbolTable.FT:
           print(i)

    def PrintStructT(self):
        printDebug("Printing Struct Table")
        for i in SymbolTable.StructT:
            printDebug(i)

    def provideTemp(self, type):
        printDebug("[provideTemp]Making a tmp of type "+str(type))
        lexeme = "#temp" + str(self.temp_id)
        self.temp_id += 1
        return self.addEntry(lexeme, type, None)

CST = SymbolTable().makeNewTable(None)
GST = CST

def getNewST():
    global CST, GST
    new_st = SymbolTable()
    new_st.makeNewTable(CST)
    CST = new_st
    return CST 

def popST():
    global CST, GST
    PST = CST.getPP()
    assert PST is not None
    off = CST.getCurOffset()
    PST.setOffset(off+PST.getCurOffset()) 
    CST = PST
    return CST

def getCST():
    return CST;

def getGST():
    return GST;

def getSTEntry(refer):
    ST = refer[2]
    return ST.table["cur_scope"][refer[1]]
