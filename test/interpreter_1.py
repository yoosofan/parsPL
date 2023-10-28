#
#
#!/usr/bin/python
# -*- coding: utf_8 -*-
# Use only python 3
# -----------------------------------------------------------------------------
# calc.py
# Ahmad Yoosofan
# A simple calculator with variables -- all in one file.
# The creation of nodes in a tree is the best way for creating an interpreter for ParsPL.
# The zxbparser use this method.
# The JS/CC (http://jscc.phorward-software.com/jscc/jscc.html) uses this method, too.
# -----------------------------------------------------------------------------

class MyExit1(Exception): pass

keywords =(
   'PRINT',
   'EXIT' ,
   'INPUT',

   )
persian_keywords = {
  '.بنویس' : 'PRINT' ,
  '.پایان' : 'EXIT'  ,
  '.بخوان' : 'INPUT',
  '.اگر' : "IF" 
    }

tokens  = keywords + (
    'ID','NUMBER',
    'PLUS','MINUS','TIMES','DIVIDE','EQUALS',
    'LPAREN','RPAREN', 'NEWLINE'
    )
    
# Tokens

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_EQUALS  = r'='
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
#t_PRINT   = r'[ \t‌]*'+r'بنویس.'+r'[ \t][ \t‌]*'
#t_EXIT    = r'[ \t‌]*'+r'پایان.'+r'[ \t‌]*'
#t_INPUT   = r'[ \t‌]*'+r'بخوان.'

class Token:
  def __init__():
    self.t='ID' #token type
    self.l=0    #line number
    self.p=0    #position
    self.c=[]   #code , content, children
    self.v=0    #value
my_ast=[]

def t_KEYWORDS(t):
  r'\.[A-Za-z_ا-ی][\w_ا-ی]*[ \t‌]*'
  t.value = ' '.join(t.value.split(' \t‌'))
  t.value=t.value.strip()
  if t.value in persian_keywords.keys():    t.type = persian_keywords[t.value]
  else: 
    print("Illigal keyword ",t.value);
    print("The line number of error is ",t.lexer.lineno)
    raise MyExit1()
  return t
  
def t_ID(t):
  r'[A-Za-z_ا-ی \t][\w_ا-ی \t‌]*'
  t.value = ' '.join(t.value.split(' \t‌'))
  t.value=t.value.strip()
  return t

def t_NUMBER(t):
    r'[ \t‌]*\d+(\.\d+)?[ \t‌]*'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

# Ignored characters
t_ignore = " \t"

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    return t;

def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  print("The line number of error is ",t.lexer.lineno)
  for a in names: print(a);
  t.lexer.skip(1)

# Build the lexer
import ply.lex as lex
lex.lex()

# Parsing rules

precedence = (
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE'),
    ('right','UMINUS'),
    )

# dictionary of names
names = { }
'''
def p_statement_if(t):
  'statement : if expression NEWLINE'
  names[t[1]] = t[3]
  #print(names)
'''
def p_statement_assign(t):
  'statement : ID EQUALS expression NEWLINE'
  my_ast.append(['assign',t.lexer.lineno, t[1],t[3]])
  print(t)
  #print('hhh',['assign',t.lexer.lineno, t[1],t[3]])
  #names[t[1]] = t[3]
  #print(names)

def p_statement_print(t):
    'statement : PRINT expression NEWLINE'
    my_ast.append(['print',t.lexer.lineno,t[2]])
    #print(t[2])

def p_statement_input(t):
    'statement : INPUT ID NEWLINE'
    my_ast.append(['input',t.lexer.lineno,t[2]])
    #names[t[2]] = input()#print(t[1])

def p_statement_exit(t):
    'statement : EXIT NEWLINE'
    my_ast.append(['exit',t.lexer.lineno])
    #raise MyExit1()

def p_statement_newline(t):
    'statement : NEWLINE'
    pass

def p_expression_binop(t):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    if t[2] == '+'  : t[0] = ['+', t[1] , t[3]]
    elif t[2] == '-': t[0] = ['-', t[1] , t[3]]
    elif t[2] == '*': t[0] = ['*', t[1] , t[3]]
    elif t[2] == '/': t[0] = ['/', t[1] , t[3]]

def p_expression_uminus(t):
    'expression : MINUS expression %prec UMINUS'
    t[0] = ['minus',t[2]]

def p_expression_group(t):
    'expression : LPAREN expression RPAREN'
    t[0] = t[2]

def p_expression_number(t):
    'expression : NUMBER'
    t[0] = t[1]

def p_expression_id(t):
  'expression : ID'
  t[0] = t[1]

def p_error(t):
    print("Syntax error at '%s'" % t.value)


import ply.yacc as yacc
yacc.yacc()
import sys
my_symbol_table={}
def my_execute():
  i=0
  while my_ast[i][0] != 'exit':
    print(my_ast[i][1]-1,">> ")
    if my_ast[i][0] == 'assign':
      my_symbol_table[my_ast[i][2]]=my_ast[i][3]
    elif my_ast[i][0] == 'print':
      #print(stmt1[2])
      print(my_symbol_table[my_ast[i][2]])
    elif my_ast[i][0] == 'input':
      pass
    elif my_ast[i][0] == 'if':
      pass
    elif my_ast[i][0] == 'elif':
      pass
    i+=1
  
if __name__ =="__main__":
  if len(sys.argv)>1:
    src=open(sys.argv[1]).readlines()
    try:
      for line1 in src:
        yacc.parse(line1)
      my_ast.append(['exit'])
      my_execute()
    except MyExit1 as myex:
      print('برنامه به پایان رسید. ')
    except EOFError:pass
  else:
    while 1:
      try:
        s = input('calc > ')   # Use raw_input on Python 2
        yacc.parse(s)
      except MyExit1 as myex:
        print('برنامه به پایان رسید. ')
        print('end')
        break
      except EOFError:break

