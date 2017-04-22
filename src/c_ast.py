#-----------------------------------------------------------------
# ** ATTENTION **
# This code was automatically generated from the file:
# _c_ast.cfg
#
# Do not modify it directly. Modify the configuration file and
# run the generator again.
# ** ** *** ** **
#
# pycparser: c_ast.py
#
# AST Node classes.
#
# Eli Bendersky [http://eli.thegreenplace.net]
# License: BSD
#-----------------------------------------------------------------


import sys
from parse_tree import *
from symbol_table import *
#  from code_gen import *
import re

# TODO In this file 

code_list = []

# In if statement we are checking whether the tmp has value non zero if so then we take goto else if tmp is 0 we take else


user_debug = False 
    
def printDebug(s):
    if user_debug:
        print(s)

def getType(v):
    if isinstance(v, Constant):
        return v.type
    elif isinstance(v, IdentifierType):
        return v.names
    elif isinstance(v, PtrDecl):
        return "ptr"
    elif isinstance(v, ArrayDecl):
        return "array"
    elif isinstance(v, TypeDecl):
        p1_type = v.type        
    elif isinstance(v, BinaryOp):
        p1_type = v.type
    elif isinstance(v, UnaryOp):
        p1_type = v.type
    elif isinstance(v, ArrayRef):
        p1_type = v.type
    elif isinstance(v, Cast):
        p1_type = v.type 
        if isinstance(p1_type, Typename):
            p1_type = p1_type.type 
    return getType(p1_type)

class Node(object):
    __slots__ = ()
    """ Abstract base class for AST nodes.
    """
    def children(self):
        """ A sequence of all children that are Nodes
        """
        pass

    def show(self, buf=sys.stdout, offset=0, attrnames=False, nodenames=False, showcoord=False, _my_node_name=None):
        """ Pretty print the Node and all its attributes and
            children (recursively) to a buffer.

            buf:
                Open IO buffer into which the Node is printed.

            offset:
                Initial offset (amount of leading spaces)

            attrnames:
                True if you want to see the attribute names in
                name=value pairs. False to only see the values.

            nodenames:
                True if you want to see the actual node names
                within their parents.

            showcoord:
                Do you want the coordinates of each Node to be
                displayed.
        """
        lead = ' ' * offset
        if nodenames and _my_node_name is not None:
            buf.write(lead + self.__class__.__name__+ ' <' + _my_node_name + '>: ')
        else:
            buf.write(lead + self.__class__.__name__+ ': ')

        if self.attr_names:
            if attrnames:
                nvlist = [(n, getattr(self,n)) for n in self.attr_names]
                attrstr = ', '.join('%s=%s' % nv for nv in nvlist)
            else:
                vlist = [getattr(self, n) for n in self.attr_names]
                attrstr = ', '.join('%s' % v for v in vlist)
            buf.write(attrstr)

        if showcoord:
            buf.write(' (at %s)' % self.coord)
        buf.write('\n')

        child_list = []
        for (child_name, child) in self.children():
            n = child.show(
                buf,
                offset=offset + 2,
                attrnames=attrnames,
                nodenames=nodenames,
                showcoord=showcoord,
                _my_node_name=child_name)
            for i in n:
                child_list.append(i)
            #  child_list.append(n)

        #  if self.__class__.__name__ != "PtrDecl" and self.__class__.__name__ != "IdentifierType" and  self.__class__.__name__ != "TypeDecl"and self.__class__.__name__ != "ArrayDecl" and self.__class__.__name__ != "FuncDecl" and self.__class__.__name__ != "ArrayRef":
        if self.__class__.__name__ != "Decl" and self.__class__.__name__ != "IdentifierType":
            if hasattr(self, 's'):

                if hasattr(self, 'stpointer'):
                    a = self.stpointer
                    if a is None:
                        stp = a
                    else:
                        stp = (a[0], a[1])
                    if self.__class__.__name__ == "TypeDecl":
                        k = addNodes(" "+str(self.s or "No S")+" "+str(self.type.names or "No Type Found")+" "+str(stp or ""), child_list)

                    elif self.__class__.__name__ == "Cast":
                        k = addNodes(" "+str(self.s or "No S")+" "+str(self.type.names or "No Type Found")+" "+str(stp or ""), child_list)

                    elif self.__class__.__name__ == "ID":
                            k = addNodes(" "+str(self.s or "No S")+" "+str(stp or ""), child_list)
                    elif self.__class__.__name__ == "FuncCall":
                            k = addNodes(" "+str(self.s or "No S")+" "+str(stp or ""), child_list)
                    else:
                        k = addNodes(" "+str(self.s or "No S")+" "+str(stp or ""), child_list)

                elif self.__class__.__name__ == "BinaryOp":
                        k = addNodes(" "+str(self.s or "No S")+" "+str(getType(self) or ""), child_list)
            
                elif self.__class__.__name__ == "UnaryOp":
                    k = addNodes(" "+str(self.s or "No S")+" "+str(getType(self) or ""), child_list)

                else:
                    k = addNodes(" "+str(self.s)+" ", child_list)

            else:
                k = addNodes(" "+str(self.__class__.__name__)+" ", child_list)

            return [k]
        else:
            return child_list
        return addNodes(self.__class__.__name__, child_list)


class NodeVisitor(object):
    """ A base NodeVisitor class for visiting c_ast nodes.
        Subclass it and define your own visit_XXX methods, where
        XXX is the class name you want to visit with these
        methods.

        For example:

        class ConstantVisitor(NodeVisitor):
            def __init__(self):
                self.values = []

            def visit_Constant(self, node):
                self.values.append(node.value)

        Creates a list of values of all the constant nodes
        encountered below the given node. To use it:

        cv = ConstantVisitor()
        cv.visit(node)

        Notes:

        *   generic_visit() will be called for AST nodes for which
            no visit_XXX method was defined.
        *   The children of nodes for which a visit_XXX was
            defined will not be visited - if you need this, call
            generic_visit() on the node.
            You can use:
                NodeVisitor.generic_visit(self, node)
        *   Modeled after Python's own AST visiting facilities
            (the ast module of Python 3.0)
    """
    def visit(self, node):
        """ Visit a node.
        """
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        """ Called if no explicit visitor function exists for a
            node. Implements preorder visiting of the node.
        """
        for c_name, c in node.children():
            self.visit(c)


class ArrayDecl(Node):
    # __slots__ = ('type', 'dim', 'dim_quals','size', 'coord', '__weakref__')
    __slots__ = ('stpointer', 'type', 'dim', 'dim_quals','coord', '__weakref__')

    # def __init__(self, type, dim, size, dim_quals, coord=None):
    def __init__(self, type, dim,  dim_quals, coord=None):
        self.type = type
        self.dim = dim
        self.dim_quals = dim_quals
        # self.size = size
        self.coord = coord
        self.stpointer = None

    def children(self):
        nodelist = []
        if self.type is not None: nodelist.append(("type", self.type))
        if self.dim is not None: nodelist.append(("dim", self.dim))
        
        return tuple(nodelist)

    attr_names = ('dim_quals', )

class ArrayRef(Node):
    __slots__ = ('name', 'subscript', 'refer', 'type', 'coord', '__weakref__')
    def __init__(self, name, subscript, type="void", coord=None):
        self.name = name
        self.subscript = subscript
        self.coord = coord
        self.type = type
        self.refer = emit("ArrayRef", "[]", (type, name.refer, subscript))

    def children(self):
        nodelist = []
        if self.name is not None: nodelist.append(("name", self.name))
        if self.subscript is not None: nodelist.append(("subscript", self.subscript))
        return tuple(nodelist)

    attr_names = ()

class Assignment(Node):
    __slots__ = ('s', 'op', 'lvalue', 'rvalue', 'refer', 'coord', '__weakref__')
    def __init__(self, op, lvalue, rvalue, coord=None):
        self.op = op
        self.lvalue = lvalue
        self.rvalue = rvalue
        self.coord = coord
        self.s = op
        #There might be a problem here
        printDebug("[Assignment]"+str(rvalue.type)+" "+str(lvalue.type))
        self.refer = emit("Assignment", op, (rvalue.type, lvalue.refer, rvalue.refer))

    def children(self):
        nodelist = []
        if self.lvalue is not None: nodelist.append(("lvalue", self.lvalue))
        if self.rvalue is not None: nodelist.append(("rvalue", self.rvalue))
        return tuple(nodelist)

    attr_names = ('op', )

class BinaryOp(Node):
    __slots__ = ('s', 'op', 'left', 'right', 'type', 'refer', 'coord', '__weakref__')
    def __init__(self, op, left, right, type='void', coord=None):
        self.op = op
        self.left = left
        self.right = right
        self.type = type 
        self.coord = coord
        self.s = op
        printDebug("In BinaryOp")
        printDebug("Left:"+str(left))
        printDebug("Right:"+str(right))
        self.refer = emit("BinaryOp", op, (type, left.refer, right.refer)) 

    def children(self):
        nodelist = []
        if self.left is not None: nodelist.append(("left", self.left))
        if self.right is not None: nodelist.append(("right", self.right))
        return tuple(nodelist)

    attr_names = ('op', )

class Break(Node):
    __slots__ = ('coord', 'refer', '__weakref__')
    def __init__(self, coord=None):
        self.coord = coord
        self.refer = TAC((0,0,0), makeNewData()) 


    def children(self):
        return ()

    attr_names = ()

class Case(Node):
    __slots__ = ('expr', 'stmts', 'coord', '__weakref__')
    def __init__(self, expr, stmts, coord=None):
        self.expr = expr
        self.stmts = stmts
        self.coord = coord

    def children(self):
        nodelist = []
        if self.expr is not None: nodelist.append(("expr", self.expr))
        for i, child in enumerate(self.stmts or []):
            nodelist.append(("stmts[%d]" % i, child))
        return tuple(nodelist)

    attr_names = ()

class Cast(Node):
    __slots__ = ('s', 'to_type', 'expr', 'type', 'refer', 'coord', '__weakref__')
    def __init__(self, to_type, expr, type="void", coord=None):
        self.to_type = to_type
        self.expr = expr
        self.coord = coord
        self.type = type 
        #  printDebug("Got ToTypes : {}".format(to_type))
        if isinstance(to_type, Typename):
            self.s = "cast:"+str(to_type.type.type.names)
        else:
            self.s = "cast:"+str(to_type.names)

        self.refer = emit("Cast", to_type, (to_type, expr.refer))

    def children(self):
        nodelist = []
        if self.to_type is not None: nodelist.append(("to_type", self.to_type))
        if self.expr is not None: nodelist.append(("expr", self.expr))
        return tuple(nodelist)

    attr_names = ()

class Compound(Node):
    __slots__ = ('s', 'block_items', 'refer', 'coord', '__weakref__')
    def __init__(self, block_items, coord=None):
        self.block_items = block_items
        self.coord = coord
        self.s = "compound"
        self.refer = TAC((0,0,0), makeNewData())

    def children(self):
        nodelist = []
        for i, child in enumerate(self.block_items or []):
            nodelist.append(("block_items[%d]" % i, child))
        return tuple(nodelist)

    attr_names = ()

class CompoundLiteral(Node):
    __slots__ = ('type', 'init', 'coord', '__weakref__')
    def __init__(self, type, init, coord=None):
        self.type = type
        self.init = init
        self.coord = coord

    def children(self):
        nodelist = []
        if self.type is not None: nodelist.append(("type", self.type))
        if self.init is not None: nodelist.append(("init", self.init))
        return tuple(nodelist)

    attr_names = ()

class Constant(Node):
    __slots__ = ('s', 'type', 'value', 'refer', 'coord', '__weakref__')
    def __init__(self, type, value, coord=None):
        self.type = type
        self.value = value
        self.coord = coord
        self.s = value
        self.refer = TAC(value, makeNewData())

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('type', 'value', )

class Continue(Node):
    __slots__ = ('coord', 'refer', '__weakref__')
    def __init__(self, coord=None):
        self.coord = coord
        self.refer = TAC((0,0,0), makeNewData())

    def children(self):
        return ()

    attr_names = ()

class Decl(Node):
    __slots__ = ('s', 'stpointer', 'name', 'quals', 'storage', 'funcspec', 'type', 'init', 'bitsize', 'refer', 'coord', '__weakref__')
    def __init__(self, name, quals, storage, funcspec, type, init, bitsize, coord=None):
        self.name = name
        self.quals = quals
        self.storage = storage
        self.funcspec = funcspec
        self.type = type
        self.init = init
        self.bitsize = bitsize
        self.coord = coord
        self.s = "NAME" 
        self.stpointer = None
        self.refer = TAC((0,0,0), makeNewData())

    def children(self):
        nodelist = []
        if self.type is not None: nodelist.append(("type", self.type))
        if self.init is not None: nodelist.append(("init", self.init))
        if self.bitsize is not None: nodelist.append(("bitsize", self.bitsize))
        return tuple(nodelist)

    attr_names = ('name', 'quals', 'storage', 'funcspec', )

class DeclList(Node):
    __slots__ = ('s', 'decls', 'coord', '__weakref__')
    def __init__(self, decls, coord=None):
        self.decls = decls
        self.coord = coord
        self.s = 'decls'

    def children(self):
        nodelist = []
        for i, child in enumerate(self.decls or []):
            nodelist.append(("decls[%d]" % i, child))
        return tuple(nodelist)

    attr_names = ()

class Default(Node):
    __slots__ = ('stmts', 'coord', '__weakref__')
    def __init__(self, stmts, coord=None):
        self.stmts = stmts
        self.coord = coord

    def children(self):
        nodelist = []
        for i, child in enumerate(self.stmts or []):
            nodelist.append(("stmts[%d]" % i, child))
        return tuple(nodelist)

    attr_names = ()

class DoWhile(Node):
    __slots__ = ('s', 'cond', 'stmt', 'refer', 'coord', '__weakref__')
    def __init__(self, cond, stmt, coord=None):
        self.cond = cond
        self.stmt = stmt
        self.coord = coord
        self.s = 'dowhile'
        self.refer = TAC((0,0,0), makeNewData())

    def children(self):
        nodelist = []
        if self.cond is not None: nodelist.append(("cond", self.cond))
        if self.stmt is not None: nodelist.append(("stmt", self.stmt))
        return tuple(nodelist)

    attr_names = ()

class EllipsisParam(Node):
    __slots__ = ('s', 'coord', '__weakref__')
    def __init__(self, coord=None):
        self.coord = coord
        self.s = '...'

    def children(self):
        return ()

    attr_names = ()

class EmptyStatement(Node):
    __slots__ = ('coord', 'refer', '__weakref__')
    def __init__(self, coord=None):
        self.coord = coord
        self.refer = TAC((0,0,0), makeNewData())

    def children(self):
        return ()

    attr_names = ()

class Enum(Node):
    __slots__ = ('name', 'values', 'coord', '__weakref__')
    def __init__(self, name, values, coord=None):
        self.name = name
        self.values = values
        self.coord = coord

    def children(self):
        nodelist = []
        if self.values is not None: nodelist.append(("values", self.values))
        return tuple(nodelist)

    attr_names = ('name', )

class Enumerator(Node):
    __slots__ = ('name', 'value', 'coord', '__weakref__')
    def __init__(self, name, value, coord=None):
        self.name = name
        self.value = value
        self.coord = coord

    def children(self):
        nodelist = []
        if self.value is not None: nodelist.append(("value", self.value))
        return tuple(nodelist)

    attr_names = ('name', )

class EnumeratorList(Node):
    __slots__ = ('enumerators', 'coord', '__weakref__')
    def __init__(self, enumerators, coord=None):
        self.enumerators = enumerators
        self.coord = coord

    def children(self):
        nodelist = []
        for i, child in enumerate(self.enumerators or []):
            nodelist.append(("enumerators[%d]" % i, child))
        return tuple(nodelist)

    attr_names = ()

class ExprList(Node):
    __slots__ = ('exprs', 'type', 'coord', '__weakref__')
    def __init__(self, exprs, type=[], coord=None):
        self.exprs = exprs
        self.coord = coord
        self.type = type

    def children(self):
        nodelist = []
        for i, child in enumerate(self.exprs or []):
            nodelist.append(("exprs[%d]" % i, child))
        return tuple(nodelist)

    attr_names = ()

class FileAST(Node):
    __slots__ = ('ext', 'coord', '__weakref__')
    def __init__(self, ext, coord=None):
        self.ext = ext
        self.coord = coord

    def children(self):
        nodelist = []
        for i, child in enumerate(self.ext or []):
            nodelist.append(("ext[%d]" % i, child))
        return tuple(nodelist)

    attr_names = ()

class For(Node):
    __slots__ = ('s', 'init', 'cond', 'next', 'stmt', 'refer', 'coord', '__weakref__')
    def __init__(self, init, cond, next, stmt, coord=None):
        self.init = init
        self.cond = cond
        self.next = next
        self.stmt = stmt
        self.coord = coord
        self.s = 'for'
        self.refer = TAC((0,0,0), makeNewData())

    def children(self):
        nodelist = []
        if self.init is not None: nodelist.append(("init", self.init))
        if self.cond is not None: nodelist.append(("cond", self.cond))
        if self.next is not None: nodelist.append(("next", self.next))
        if self.stmt is not None: nodelist.append(("stmt", self.stmt))
        return tuple(nodelist)

    attr_names = ()

class FuncCall(Node):
    __slots__ = ('s', 'name', 'args','type','stpointer', 'refer', 'coord', '__weakref__')
    def __init__(self, name, args, type='void', coord=None):
        self.name = name
        self.args = args
        self.coord = coord
        self.type = type
        self.stpointer = None
        self.refer = emit("FuncCall", "f()", (type, name, args.exprs))
        self.s ="FuncCall" 

    def children(self):
        nodelist = []
        if self.name is not None: nodelist.append(("name", self.name))
        if self.args is not None: nodelist.append(("args", self.args))
        return tuple(nodelist)

    attr_names = ()

class FuncDecl(Node):
    __slots__ = ('stpointer', 's', 'args', 'type', 'coord', '__weakref__')
    def __init__(self, args, type, coord=None):
        self.args = args
        self.type = type
        self.coord = coord
        self.stpointer = None
        self.s = "FuncDecl"

    def children(self):
        nodelist = []
        if self.type is not None: nodelist.append(("type", self.type))
        if self.args is not None: nodelist.append(("args", self.args))
        return tuple(nodelist)

    attr_names = ()

class FuncDef(Node):
    __slots__ = ('decl', 'param_decls', 'body', 'refer', 'coord', '__weakref__')
    def __init__(self, decl, param_decls, body, coord=None):
        self.decl = decl
        self.param_decls = param_decls
        self.body = body
        self.coord = coord
        self.refer = emit('FuncDef', 'FuncDef', (TAC(decl.type.stpointer, makeNewData())))

    def children(self):
        nodelist = []
        if self.decl is not None: nodelist.append(("decl", self.decl))
        if self.body is not None: nodelist.append(("body", self.body))
        for i, child in enumerate(self.param_decls or []):
            nodelist.append(("param_decls[%d]" % i, child))
        return tuple(nodelist)

    attr_names = ()

class Goto(Node):
    __slots__ = ('name', 'coord', '__weakref__')
    def __init__(self, name, coord=None):
        self.name = name
        self.coord = coord

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('name', )

class ID(Node):
    __slots__ = ('s', 'stpointer', 'name', 'refer', 'type', 'coord', '__weakref__')
    def __init__(self, name, type=None, coord=None):
        printDebug("ID HERE:"+ str(name))
        self.name = name
        self.coord = coord
        if type:
            self.type = type 
        else:
            CST = getCST()
            entry = CST.lookupFullScope(name)
            if(entry[-1]=="ST"):
                type = entry[1];
            else:
                type= None
        self.s = name
        self.stpointer = None
        self.refer = getReference(name)

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('name', )

class IdentifierType(Node):
    __slots__ = ('s', 'names', 'type', 'coord', '__weakref__')
    def __init__(self, names, coord=None):
        self.names = names
        self.coord = coord
        self.type = names
        self.s = names

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('names', )

class If(Node):
    __slots__ = ('s', 'cond', 'iftrue', 'iffalse', 'refer', 'coord', '__weakref__')
    def __init__(self, cond, iftrue, iffalse, coord=None):
        self.cond = cond
        self.iftrue = iftrue
        self.iffalse = iffalse
        self.coord = coord
        self.s = 'if'
        self.refer = TAC((0,0,0), makeNewData())

    def children(self):
        nodelist = []
        if self.cond is not None: nodelist.append(("cond", self.cond))
        if self.iftrue is not None: nodelist.append(("iftrue", self.iftrue))
        if self.iffalse is not None: nodelist.append(("iffalse", self.iffalse))
        return tuple(nodelist)

    attr_names = ()

class InitList(Node):
    __slots__ = ('exprs', 'coord', '__weakref__')
    def __init__(self, exprs, coord=None):
        self.exprs = exprs
        self.coord = coord

    def children(self):
        nodelist = []
        for i, child in enumerate(self.exprs or []):
            nodelist.append(("exprs[%d]" % i, child))
        return tuple(nodelist)

    attr_names = ()

class Label(Node):
    __slots__ = ('name', 'stmt', 'coord', '__weakref__')
    def __init__(self, name, stmt, coord=None):
        self.name = name
        self.stmt = stmt
        self.coord = coord

    def children(self):
        nodelist = []
        if self.stmt is not None: nodelist.append(("stmt", self.stmt))
        return tuple(nodelist)

    attr_names = ('name', )

class NamedInitializer(Node):
    __slots__ = ('name', 'expr', 'coord', '__weakref__')
    def __init__(self, name, expr, coord=None):
        self.name = name
        self.expr = expr
        self.coord = coord

    def children(self):
        nodelist = []
        if self.expr is not None: nodelist.append(("expr", self.expr))
        for i, child in enumerate(self.name or []):
            nodelist.append(("name[%d]" % i, child))
        return tuple(nodelist)

    attr_names = ()

class ParamList(Node):
    __slots__ = ('params', 'coord', '__weakref__')
    def __init__(self, params, coord=None):
        self.params = params
        self.coord = coord

    def children(self):
        nodelist = []
        for i, child in enumerate(self.params or []):
            nodelist.append(("params[%d]" % i, child))
        return tuple(nodelist)

    attr_names = ()

class PtrDecl(Node):
    __slots__ = ('s', 'stpointer', 'quals', 'type', 'coord', '__weakref__')
    def __init__(self, quals, type, coord=None):
        self.quals = quals
        self.type = type
        self.coord = coord
        self.stpointer = None
        self.s = "ptr"

    def children(self):
        nodelist = []
        if self.type is not None: nodelist.append(("type", self.type))
        return tuple(nodelist)

    attr_names = ('quals', )

class Return(Node):
    __slots__ = ('expr', 'coord', 'refer', '__weakref__')
    def __init__(self, expr, coord=None):
        self.expr = expr
        self.coord = coord
        self.refer = TAC((0,0,0), makeNewData())

    def children(self):
        nodelist = []
        if self.expr is not None: nodelist.append(("expr", self.expr))
        return tuple(nodelist)

    attr_names = ()

class Struct(Node):
    __slots__ = ('name', 'decls', 'coord', '__weakref__')
    def __init__(self, name, decls, coord=None):
        self.name = name
        self.decls = decls
        self.coord = coord

    def children(self):
        nodelist = []
        for i, child in enumerate(self.decls or []):
            nodelist.append(("decls[%d]" % i, child))
        return tuple(nodelist)

    attr_names = ('name', )

class StructRef(Node):
    __slots__ = ('name', 'type', 'field', 'coord', '__weakref__')
    def __init__(self, name, type, field, coord=None):
        self.name = name
        self.type = type
        self.field = field
        self.coord = coord

    def children(self):
        nodelist = []
        if self.name is not None: nodelist.append(("name", self.name))
        if self.field is not None: nodelist.append(("field", self.field))
        return tuple(nodelist)

    attr_names = ('type', )

class Switch(Node):
    __slots__ = ('cond', 'stmt', 'coord', '__weakref__')
    def __init__(self, cond, stmt, coord=None):
        self.cond = cond
        self.stmt = stmt
        self.coord = coord

    def children(self):
        nodelist = []
        if self.cond is not None: nodelist.append(("cond", self.cond))
        if self.stmt is not None: nodelist.append(("stmt", self.stmt))
        return tuple(nodelist)

    attr_names = ()

class TernaryOp(Node):
    __slots__ = ('cond', 'iftrue', 'iffalse', 'coord', '__weakref__')
    def __init__(self, cond, iftrue, iffalse, coord=None):
        self.cond = cond
        self.iftrue = iftrue
        self.iffalse = iffalse
        self.coord = coord

    def children(self):
        nodelist = []
        if self.cond is not None: nodelist.append(("cond", self.cond))
        if self.iftrue is not None: nodelist.append(("iftrue", self.iftrue))
        if self.iffalse is not None: nodelist.append(("iffalse", self.iffalse))
        return tuple(nodelist)

    attr_names = ()

class TypeDecl(Node):
    __slots__ = ('s', 'stpointer', 'declname', 'quals', 'type', 'refer', 'coord', '__weakref__')
    def __init__(self, declname, quals, type, coord=None):
        self.declname = declname
        self.quals = quals
        self.type = type
        self.coord = coord
        self.s = declname
        self.stpointer = None
        self.refer = TAC(None, makeNewData()) 

    def children(self):
        nodelist = []
        if self.type is not None: nodelist.append(("type", self.type))
        return tuple(nodelist)

    attr_names = ('declname', 'quals', )

class Typedef(Node):
    __slots__ = ('name', 'quals', 'storage', 'type', 'coord', '__weakref__')
    def __init__(self, name, quals, storage, type, coord=None):
        self.name = name
        self.quals = quals
        self.storage = storage
        self.type = type
        self.coord = coord

    def children(self):
        nodelist = []
        if self.type is not None: nodelist.append(("type", self.type))
        return tuple(nodelist)

    attr_names = ('name', 'quals', 'storage', )

class Typename(Node):
    __slots__ = ('name', 'quals', 'type', 'coord', '__weakref__')
    def __init__(self, name, quals, type, coord=None):
        self.name = name
        self.quals = quals
        self.type = type
        self.coord = coord

    def children(self):
        nodelist = []
        if self.type is not None: nodelist.append(("type", self.type))
        return tuple(nodelist)

    attr_names = ('name', 'quals', )

class UnaryOp(Node):
    __slots__ = ('s', 'op', 'expr', 'refer', 'type', 'coord', '__weakref__')
    def __init__(self, op, expr, type="void", coord=None):
        self.op = op
        self.expr = expr
        self.coord = coord
        self.type = type
        self.s = op
        self.refer = emit("UnaryOp", op, (type, expr.refer))

    def children(self):
        nodelist = []
        if self.expr is not None: nodelist.append(("expr", self.expr))
        return tuple(nodelist)

    attr_names = ('op', )

class Union(Node):
    __slots__ = ('name', 'decls', 'coord', '__weakref__')
    def __init__(self, name, decls, coord=None):
        self.name = name
        self.decls = decls
        self.coord = coord

    def children(self):
        nodelist = []
        for i, child in enumerate(self.decls or []):
            nodelist.append(("decls[%d]" % i, child))
        return tuple(nodelist)

    attr_names = ('name', )

class While(Node):
    __slots__ = ('cond', 'stmt', 'coord', 'refer', '__weakref__')
    def __init__(self, cond, stmt, coord=None):
        self.cond = cond
        self.stmt = stmt
        self.coord = coord
        self.refer = TAC((0,0,0), makeNewData())

    def children(self):
        nodelist = []
        if self.cond is not None: nodelist.append(("cond", self.cond))
        if self.stmt is not None: nodelist.append(("stmt", self.stmt))
        return tuple(nodelist)

    attr_names = ()

class Pragma(Node):
    __slots__ = ('string', 'coord', '__weakref__')
    def __init__(self, string, coord=None):
        self.string = string
        self.coord = coord

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('string', )


class TAC():
    def __init__(self, refer, data):
        self.refer = refer
        self.data = data

    def addToFalselist(self, id):
        self.data["falselist"].append(id)
    
    def addToTruelist(self, id):
        self.data["truelist"].append(id)
    
    def addToBreaklist(self, id):
        self.data["breaklist"].append(id)
    
    def addToContlist(self, id):
        self.data["contlist"].append(id)

    def transferData(self, TAC_object):
        TAC_object.data = self.data


    def __str__(self):
        if type(self.refer) == tuple:
            entry = getSTEntry(self.refer)
            return str(entry[0])
        else:
            return str(self.refer)

        


def emit(key, op, var_tuple):
    printDebug("[emit]In Emit")
    printDebug("[emit]"+str((key, op, var_tuple)))
    CST = getCST()
    #  if len(var_tuple) == 3 and not isinstance(var_tuple[2], tuple):
    #      printDebug("HAGGA 1")
    #      temp = CST.provideTemp(var_tuple[0])
    #
    #  if not isinstance(var_tuple[1], tuple):
    #      printDebug("HAGGA HAGGA HAGGA HAGGAPA")
    #      temp = CST.provideTemp(var_tuple[0])
        
    #  printDebug(CST.printDebug())
    if key == "BinaryOp":
        #  assert len(var_tuple) == 3
        # Have to separate the operator based on the true list and false list
        # -,+,*,/,^,&,|,~,<<,>>,
        # [TODO]
        if re.match(r"\-|\+|\*|\/|\||\&|\^", op) or op == "<<" or op == ">>":
            printDebug("[emit]In BinaryOp"+op)
            temp = TAC(CST.provideTemp(var_tuple[0]), makeNewData())

            code_list.append((op, temp, var_tuple[1], var_tuple[2]))

            temp.addToTruelist(getNextInstr())
            code_list.append(('if', temp, None, None))

            temp.addToFalselist(getNextInstr())
            code_list.append(('goto', None, None, None))
            
        elif op == "%":
            temp1 = TAC(CST.provideTemp(var_tuple[0]), makeNewData())
            temp2 = TAC(CST.provideTemp(var_tuple[0]), makeNewData())
            temp3 = TAC(CST.provideTemp(var_tuple[0]), makeNewData())
            code_list.append(("/", temp1, var_tuple[1], var_tuple[2]))
            code_list.append(("*", temp2, temp1, var_tuple[2]))
            code_list.append(("-", temp3, var_tuple[1], temp2))
            temp = temp3 

            temp.addToTruelist(getNextInstr())
            code_list.append(('if', temp, None, None))

            temp.addToFalselist(getNextInstr())
            code_list.append(('goto', None, None, None))

        elif re.match(r"<=|>=|==|!=|<|>", op):
            printDebug("[emit]In RelOp")
            printDebug("[emit]"+str(var_tuple))
            temp = TAC(CST.provideTemp(var_tuple[0]), makeNewData())

            code_list.append(('if'+op, var_tuple[1], var_tuple[2], getNextInstr()+3))
            code_list.append(('=', temp, 0, None))
            code_list.append(('goto', None, None, getNextInstr()+2))
            code_list.append(('=', temp, 1, None))

            temp.addToTruelist(getNextInstr())
            code_list.append(('if', temp, None, None))

            temp.addToFalselist(getNextInstr())
            code_list.append(('goto', None, None, None))

        # Assignment of logical operators is not handled
        elif op == "||":
            temp = TAC(CST.provideTemp(var_tuple[0]), makeNewData())

            code_list.append(('||', temp, var_tuple[1], var_tuple[2]))

        elif op == "&&":

            temp = TAC(CST.provideTemp(var_tuple[0]), makeNewData())

            code_list.append(('&&', temp, var_tuple[1], var_tuple[2]))

    elif key == "Cast":
        #  assert len(var_tuple) == 3
        temp = TAC(CST.provideTemp(var_tuple[0]), var_tuple[1].data)
        code_list.append(("Cast", temp, var_tuple[0], var_tuple[1]))

    elif key == "UnaryOp":
        #  assert len(var_tuple) == 3
        if op == "&":
            temp = TAC(CST.provideTemp(var_tuple[0]), makeNewData())

            code_list.append(('&', temp, var_tuple[1], None))
            temp.addToTruelist(getNextInstr())
            code_list.append(('goto', None, None, None))
                
        elif op == "*":
            temp = TAC(CST.provideTemp(var_tuple[0]), makeNewData())

            code_list.append(("deref", temp, var_tuple[1], None))
            
            temp.addToTruelist(getNextInstr())
            code_list.append(('if', temp, None, None))

            temp.addToFalselist(getNextInstr())
            code_list.append(('goto', None, None, None))
        
        elif op == "+":
            temp = var_tuple[1]
        
        elif op == "-":
            temp = TAC(CST.provideTemp(var_tuple[0]), var_tuple[1].data)
            code_list.append(("-", temp, 0, var_tuple[1]))

        # [TODO]
        elif op == "~":
            temp = TAC(CST.provideTemp(var_tuple[0]), makeNewData())

            code_list.append(("~", temp, var_tuple[1], None))

            temp.addToTruelist(getNextInstr())
            code_list.append(('if', temp, None, None))

            temp.addToFalselist(getNextInstr())
            code_list.append(('goto', None, None, None))

        elif op == "!":
            temp = TAC(CST.provideTemp(var_tuple[0]), var_tuple[1].data)

            #  Not storing the assignments of logical operators
            #  code_list.append(("!", temp, var_tuple[1], None))
        
            temp.data["truelist"] = var_tuple[1].data["falselist"]
            temp.data["falselist"] = var_tuple[1].data["truelist"]

        elif op == "++":
            temp = TAC(CST.provideTemp(var_tuple[0]), makeNewData())

            code_list.append(("+", temp, var_tuple[1], 1 ))
            code_list.append(("=", var_tuple[1], temp, None))

            temp.addToTruelist(getNextInstr())
            code_list.append(('if', temp, None, None))

            temp.addToFalselist(getNextInstr())
            code_list.append(('goto', None, None, None))

        elif op == "--":
            temp = TAC(CST.provideTemp(var_tuple[0]), makeNewData())

            code_list.append(("-", temp, var_tuple[1], 1 ))
            code_list.append(("=", var_tuple[1], temp, None))
            
            temp.addToTruelist(getNextInstr())
            code_list.append(('if', temp, None, None))

            temp.addToFalselist(getNextInstr())
            code_list.append(('goto', None, None, None))

        elif op == "p++":
            temp1 = TAC(CST.provideTemp(var_tuple[0]), makeNewData())
            temp2 = TAC(CST.provideTemp(var_tuple[0]), makeNewData())
            code_list.append(("=", temp2, var_tuple[1], None ))
            code_list.append(("+", temp1, var_tuple[1], 1 ))
            temp = temp2

            var_tuple[1].addToTruelist(getNextInstr())
            code_list.append(('if', var_tuple[1], None, None))

            var_tuple[1].addToFalselist(getNextInstr())
            code_list.append(('goto', None, None, None))
            
            code_list.append(("=", var_tuple[1], temp1, None))

        elif op == "p--":
            temp1 = TAC(CST.provideTemp(var_tuple[0]), makeNewData())
            temp2 = TAC(CST.provideTemp(var_tuple[0]), makeNewData())
            code_list.append(("=", temp2, var_tuple[1], None ))
            code_list.append(("-", temp1, var_tuple[1], 1 ))
            temp = temp2           
            
            var_tuple[1].addToTruelist(getNextInstr())
            code_list.append(('if', var_tuple[1], None, None))

            var_tuple[1].addToFalselist(getNextInstr())
            code_list.append(('goto', None, None, None))
            
            code_list.append(("=", var_tuple[1], temp1, None))
    # [TODO] might be error prone
    elif key == "Assignment":
        printDebug("[Assignment]IN Assignemnt")
        if op == "=":
            temp = var_tuple[2]
            code_list.append(("=", var_tuple[1], temp, None))

            temp.addToTruelist(getNextInstr())
            code_list.append(('if', temp, None, None))

            temp.addToFalselist(getNextInstr())
            code_list.append(('goto', None, None, None))
            
        else:
            op_equal = op[-1]
            op_exp = op[:-1]

            temp1 = TAC(CST.provideTemp(var_tuple[0]), makeNewData())

            code_list.append((op_exp, temp1, var_tuple[1], var_tuple[2]))
            code_list.append((op_equal, var_tuple[1], temp1))
            temp = temp1 
            
            temp.addToTruelist(getNextInstr())
            code_list.append(('if', temp, None, None))

            temp.addToFalselist(getNextInstr())
            code_list.append(('goto', None, None, None))

    elif key == "ArrayRef":
        printDebug("In Array Ref")
        temp1 = TAC(CST.provideTemp(var_tuple[0]), makeNewData())
        type = var_tuple[1][2].getElementAtIndex(var_tuple[1][1])[1]
        size = getSize(var_tuple[0])
        code_list.append(("*", temp1, var_tuple[2], size))
        
        temp1 = TAC(CST.provideTemp(var_tuple[0]), makeNewData())
        code_list.append(("+", temp2, temp1, var_tuple[1]))

        temp3 = TAC(CST.provideTemp(var_tuple[0]), makeNewData())
        code_list.append(("deref", temp3, temp2, None))
        temp = temp3

        temp.addToTruelist(getNextInstr())
        code_list.append(('if', temp, None, None))

        temp.addToFalselist(getNextInstr())
        code_list.append(('goto', None, None, None))

    elif key == "FuncCall":
        printDebug("[emit]FuncCall")
        temp1 = TAC(CST.provideTemp(var_tuple[0]), makeNewData())
        for var in var_tuple[2]:
            printDebug("[emit]Pushing the tuple "+str(var))
            code_list.append(('push', None, var.refer, None))
        #[TODO] Check if the length of function list should be passed or not
        code_list.append(('call',temp1, var_tuple[1],len(var_tuple[2])))
        
        #[TODO] Add code for activation records here
        temp = temp1
        
        temp.addToTruelist(getNextInstr())
        code_list.append(('if', temp, None, None))

        temp.addToFalselist(getNextInstr())
        code_list.append(('goto', None, None, None))

    elif key == "FuncDef":
        code_list.append(("begin", None, var_tuple, None))
        temp = var_tuple 

    elif key == "JMP":
        code_list.append(("goto", None, None, var_tuple))
        temp = None

    return temp

def makeNewData():
    data = {
            "truelist":[],
            "falselist":[],
            "contlist":[],
            "breaklist":[],
            "nextlist":[],
            }
    return data


def PrintCode():
    print("We are now printing the 3AC Code .........") 
    for line in range(len(code_list)):
        #  printDebug("[PrintCode]"+str(code_list[line]))
        if ( code_list[line][0][:2] =='if' or code_list[line][0]=='goto' ) and not code_list[line][-1]:
            pass
        else:
            s = "Line:"+str(line)+"\t{0: >5}"+"\t{1: >5}"+"\t{2: >5}"+"\t{3: >5}"
            v = []
            for i in range(len(code_list[line])):
                if code_list[line][i] == None:
                    v.append(" ")
                elif isinstance(code_list[line][i], IdentifierType):
                    v.append(code_list[line][i].type)
                else:
                    v.append(code_list[line][i])
            #  printDebug(v)
            #  print(v)
            print(s.format(v[0],v[1],v[2],v[3]))


def getReference(name):
    printDebug("In getReference")
    CST = getCST()
    entry = CST.lookupFullScope(name)
    if(entry[-1] == "ST"):
        return TAC(entry[5], makeNewData())
    else:
        return None 

def getNextInstr():
    return len(code_list)

#         if re.match(r"\-|\+|\*|\/|<=|>=|==|!=|\|\||\&\&|\||\&|\^|<|>|!", op) or op == "<<" or op == ">>":

def backpatch(c_list, index):
    printDebug("[backpatch]In backpatch")
    for i in c_list:
        if code_list[i][0][:2] == 'if' or code_list[i][0] == 'goto':
            printDebug(i)
            l = list(code_list[i])
            l[-1] = index
            code_list[i] = tuple(l) 
        else:
            printDebug("[backpatch]We are in serious trouble")

