#!/usr/bin/python3
# -*- coding: utf_8 -*-

keywords =('IF' , 'WHILE', 'ELSE', 'FUNCTION', 'RETURN' )
persian_keywords = {
  '.اگر' : "IF",
  '.وگرنه' : "ELSE",
  '.تا'   : "WHILE" ,
  '.برگرد'   : "RETURN" ,  
  '.تابع'   : "FUNCTION" ,  
    }

tokens  = keywords + (
    'ID','NUMBER',
    'PLUS','MINUS','TIMES','DIVIDE','EQUALS',
    'LPAREN','RPAREN', 'NEWLINE', 'EQ','LT','GT','LE','GE','NE',
    'LBRACE','RBRACE', 'LITERAL','COMMENT1', 'COMMA', 'RBRACKET','LBRACKET',
    )
    
# Tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'\\'
t_EQUALS  = r'='
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_EQ = r'=='
t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='
t_NE = r'!='
t_LBRACE=r'\{'
t_RBRACE=r'\}'
t_LBRACKET=r'\['
t_RBRACKET=r'\]'
t_COMMA=r'؛'
import common
def t_KEYWORDS(t):
  r'\.[A-Zپچژگکآa-z_ا-ی][A-Zپچژگکآ0-9a-z_ا-ی]*[ \t‌]'
  t.value = ' '.join(t.value.split(' \t‌'))
  t.value=t.value.strip()
  if t.value in persian_keywords.keys():    t.type = persian_keywords[t.value]
  else: 
    print("Illigal keyword ",t.value);
    print("The line number of error is ",t.lexer.lineno)
    raise common.MyExit1()
  return t
  
def t_ID(t):
  r'[A-Zپچژگکآa-z_ا-ی][A-Zپچژگکآ0-9۰۱۲۳۴۵۶۷۸۹a-z_ا-ی \t]*'
  t.value = ' '.join(t.value.split(' \t‌'))
  t.value=t.value.strip()
  return t

def t_NUMBER(t):
  r'\d+(\.\d+)?'
  try:
    t.value = float(t.value)
  except ValueError:
    print("Integer value too large %d", t.value)
    t.value = 0
  return t
def t_LITERAL(t):
  r'\«[^\n]*\»'
  t.value = t.value[1:-1]
  return t

def t_COMMENT1(t):
  r'//.*'
  pass
#def t_COMMENT2(t):  r'<<<[.|\n]*>>>'  t.lineno += t.value.count('\n')

# Ignored characters
t_ignore = " \t"
#t_ignore_COMMENT=r'(/\*[.|\n]*\*/)|(//.*)'

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    return t;

def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  print("The line number of error is ",t.lexer.lineno)
  t.lexer.skip(1)

# Build the lexer
import ply.lex as lex
import re
lex.lex(reflags=re.UNICODE)

# Parsing rules

precedence = (
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE'),
    ('right','UMINUS'),
    ('right', 'ELSE'),
    ('right','NEWLINE'),
    )
start = 'sourceOfaFile'
def p_sourceOfaFile(p):
  'sourceOfaFile : stmts'
  for m1 in p[1]:
    common.ast.append(m1)
def p_stmts(p):
    """stmts : stmt stmts
             | stmt"""
    if p[1] != None:
      p[0]=[p[1]]
    if len(p) == 3 and p[2]!= None:
      if p[0] : p[0] += p[2]
      else : p[0] = p[2]
def p_suite(p):
    """suite : NEWLINE statement
             | newLineOrEmpty LBRACE stmts RBRACE newLineOrEmpty"""
    if len(p) == 3:
        p[0] = [p[2]]
    else:
        p[0] = p[3]
def p_stmt(p):
  'stmt : newLineOrEmpty statement'
  p[0]=p[2]

def p_statement_if(p):
  'statement : IF comparison suite'
  p[0]=common.StmtCls('if',p.lexer.lineno, [p[2],p[3]])
def p_statement_ifelse(p):
  'statement : IF comparison suite ELSE suite'
  p[0]=common.StmtCls('ifelse',p.lexer.lineno, [p[2],p[3],p[5]])
def p_statement_while(p):
  'statement : WHILE comparison suite'
  p[0]=common.StmtCls('while',p.lexer.lineno, [p[2],p[3]])
def p_newLineOrEmpty(p):
  """newLineOrEmpty : NEWLINE  newLineOrEmpty
                    |"""
  pass;

def p_statement_definitionOfFunction(p):
  'statement : FUNCTION ID LPAREN paramList RPAREN suite'
  #p[0]=common.StmtCls('def_func',p.lexer.lineno, [p[4],p[6]],p[2])
  common.symt.insertFunction(p[2],p[4],p[6],p.lexer.lineno)
def p_statement_assign(p):
  'statement : lvalue EQUALS expression NEWLINE'
  p[0]=common.StmtCls('assign',p.lexer.lineno, [p[1],p[3]])
def p_statement_return(p):
  'statement : RETURN expression NEWLINE'
  p[0]=common.StmtCls('return',p.lexer.lineno,[p[2]])
def p_statement_exprs(p):
  'statement : expression NEWLINE'
  p[0]=common.StmtCls('exprs',p.lexer.lineno,[p[1]])

def p_paramList(p):
  """paramList : params
             |"""
  if len(p) == 2: p[0]=p[1]
  else: p[0]=[]
def p_params(p):
  """params : ID COMMA params
          | ID"""
  p[0]=[p[1]];
  if len(p) == 4:  p[0]+=p[3]

'''
def p_statement_newline(p):
    'statement : NEWLINE'
    pass
'''
def p_comparison(p):
  '''comparison : expression EQ expression
                | expression NE expression
                | expression GT expression
                | expression GE expression
                | expression LT expression
                | expression LE expression'''
  if p[2] == '=='  : p[0] = common.NodeCls('==',p.lineno(2),[ p[1] , p[3]])
  elif p[2] == '!=': p[0] = common.NodeCls('!=',p.lineno(2),[ p[1] , p[3]])
  elif p[2] == '>' : p[0] = common.NodeCls('>',p.lineno(2),[ p[1] , p[3]])
  elif p[2] == '>=': p[0] = common.NodeCls('>=',p.lineno(2),[ p[1] , p[3]])
  elif p[2] == '<' : p[0] = common.NodeCls('<',p.lineno(2),[ p[1] , p[3]])
  elif p[2] == '<=': p[0] = common.NodeCls('<=',p.lineno(2),[ p[1] , p[3]])
def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    if   p[2] == '+': p[0] = common.NodeCls('+',p.lineno(2),[ p[1] , p[3]])
    elif p[2] == '-': p[0] = common.NodeCls('-',p.lineno(2),[ p[1] , p[3]])
    elif p[2] == '*': p[0] = common.NodeCls('*',p.lineno(2),[ p[1] , p[3]])
    elif p[2] == '\\': p[0] = common.NodeCls('/',p.lineno(2),[ p[1] , p[3]])
    else: print('Unknown operation in an expersion ')

def p_expression_uminus(p):
    'expression : MINUS expression %prec UMINUS'
    p[0] = common.NodeCls('uminus',p.lineno(1),[p[2]])
def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_fcal(p):
  'expression : ID LPAREN argList RPAREN '
  p[0] = common.NodeCls('fcal',p.lineno(1),[p[3]],p[1])
def p_argList(p):
  """argList : args
             |"""
  if len(p) == 2: p[0]=p[1]
  else: p[0]=[]
def p_args(p):
  """args : expression COMMA args
          | expression"""
  p[0]=[p[1]];
  if len(p) == 4:  p[0]+=p[3]
def p_expression_number(p):
    'expression : NUMBER'
    p[0] = common.NodeCls('number',p.lineno(1),[], p[1])
def p_expression_id(p):
  'expression : lvalue'
  p[0] = p[1]
def p_expression_literal(p):
  'expression : LITERAL'
  p[0] = common.NodeCls('literal',p.lineno(1),[],p[1])
def p_lvalue(p):
  """lvalue : ID
            | ID LBRACKET indexList RBRACKET"""
  if len(p)==2:p[0] = common.NodeCls('id',p.lineno(1),[],p[1])
  elif len(p)==5:
    p[0] = common.NodeCls('array',p.lineno(1),[p[3]],p[1])
def p_indexList(p):
  """indexList : indexes
             |"""
  if len(p) == 2: p[0]=p[1]
  else: p[0]=[]
def p_indexes(p):
  """indexes : expression COMMA indexes
          | expression"""
  p[0]=[p[1]];
  if len(p) == 4:  p[0]+=p[3]
def p_error(p):
  st="Syntax error"+str(p)
  print(st)
  if p!= None: st+=" at line='"+ str(p.lineno(0))+'  '+str(p.lexpos(0))+ "' value='"+str(p.value)+"'"
  print(st)
import ply.yacc as yacc
yacc.yacc()



'''
def p_optitem(p):
    'optitem : item'
    '        | empty'
    ...

Normally, the first rule found in a yacc specification defines the starting grammar
   rule (top level rule). 
To change this, simply supply a start specifier in your file. 
For example:
start = 'foo'

def p_bar(p):
    'bar : A B'

# This is the starting rule due to the start specifier above
def p_foo(p):
    'foo : bar X'
...
 The use of a start specifier may be useful during debugging since you can use it to have yacc build a subset of a larger grammar. For this purpose, it is also possible to specify a starting symbol as an argument to yacc(). For example: 
yacc.yacc(start='foo')


In this case, %prec UMINUS overrides the default rule precedence--setting it to that of UMINUS in the precedence specifier. 

 At first, the use of UMINUS in this example may appear very confusing. UMINUS is not an input token or a grammer rule. Instead, you should think of it as the name of a special marker in the precedence table. When you use the %prec qualifier, you're simply telling yacc that you want the precedence of the expression to be the same as for this special marker instead of the usual precedence.

def p_expression(p):
    'expression : expression PLUS expression'
    p.lineno(1)        # Line number of the left expression
    p.lineno(2)        # line number of the PLUS operator
    p.lineno(3)        # line number of the right expression
    ...
    start,end = p.linespan(3)    # Start,end lines of the right expression
    starti,endi = p.lexspan(3)   # Start,end positions of right expression

 Note: The lexspan() function only returns the range of values up to the start of the last grammar symbol.


# Set up a logging object
import logging
logging.basicConfig(
    level = logging.DEBUG,
    filename = "parselog.txt",
    filemode = "w",
    format = "%(filename)10s:%(lineno)4d:%(message)s"
)
log = logging.getLogger()

lex.lex(debug=True,debuglog=log)
yacc.yacc(debug=True,debuglog=log)



lex.lex(errorlog=log)
yacc.yacc(errorlog=log)

'''    
