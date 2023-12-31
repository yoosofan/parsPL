
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = b'\xb0\xb6\xba\xa8\xf2C\xbd^\xa3\xd9\xdaY\xdf\xd2\xe7g'
    
_lr_action_items = {'PLUS':([10,12,13,17,23,25,26,27,28,29,30,],[-20,-21,21,21,-18,21,-19,-17,-16,-14,-15,]),'RPAREN':([10,12,17,23,26,27,28,29,30,],[-20,-21,26,-18,-19,-17,-16,-14,-15,]),'DIVIDE':([10,12,13,17,23,25,26,27,28,29,30,],[-20,-21,18,18,-18,18,-19,-17,-16,18,18,]),'NEWLINE':([0,1,2,3,4,8,9,10,12,13,15,19,23,24,25,26,27,28,29,30,31,],[2,2,-7,9,-2,-1,-6,-20,-21,19,24,-4,-18,-5,31,-19,-17,-16,-14,-15,-3,]),'NUMBER':([5,11,14,16,18,20,21,22,],[10,10,10,10,10,10,10,10,]),'MINUS':([5,10,11,12,13,14,16,17,18,20,21,22,23,25,26,27,28,29,30,],[14,-20,14,-21,22,14,14,22,14,14,14,14,-18,22,-19,-17,-16,-14,-15,]),'EQUALS':([7,],[16,]),'EXIT':([0,1,2,4,8,9,19,24,31,],[3,3,-7,-2,-1,-6,-4,-5,-3,]),'LPAREN':([5,11,14,16,18,20,21,22,],[11,11,11,11,11,11,11,11,]),'PRINT':([0,1,2,4,8,9,19,24,31,],[5,5,-7,-2,-1,-6,-4,-5,-3,]),'INPUT':([0,1,2,4,8,9,19,24,31,],[6,6,-7,-2,-1,-6,-4,-5,-3,]),'TIMES':([10,12,13,17,23,25,26,27,28,29,30,],[-20,-21,20,20,-18,20,-19,-17,-16,20,20,]),'ID':([0,1,2,4,5,6,8,9,11,14,16,18,19,20,21,22,24,31,],[7,7,-7,-2,12,15,-1,-6,12,12,12,12,-4,12,12,12,-5,-3,]),'$end':([1,2,4,8,9,19,24,31,],[0,-7,-2,-1,-6,-4,-5,-3,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'stmts':([0,],[1,]),'expression':([5,11,14,16,18,20,21,22,],[13,17,23,25,27,28,29,30,]),'statement':([0,1,],[4,8,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> stmts","S'",1,None,None,None),
  ('stmts -> stmts statement','stmts',2,'p_stmts','/home/ahmad/other/backup_dates/911205/parsPL/backup/2013_02_21_16_06_56/parser.py',93),
  ('stmts -> statement','stmts',1,'p_stmts','/home/ahmad/other/backup_dates/911205/parsPL/backup/2013_02_21_16_06_56/parser.py',94),
  ('statement -> ID EQUALS expression NEWLINE','statement',4,'p_statement_assign','/home/ahmad/other/backup_dates/911205/parsPL/backup/2013_02_21_16_06_56/parser.py',107),
  ('statement -> PRINT expression NEWLINE','statement',3,'p_statement_print','/home/ahmad/other/backup_dates/911205/parsPL/backup/2013_02_21_16_06_56/parser.py',110),
  ('statement -> INPUT ID NEWLINE','statement',3,'p_statement_input','/home/ahmad/other/backup_dates/911205/parsPL/backup/2013_02_21_16_06_56/parser.py',113),
  ('statement -> EXIT NEWLINE','statement',2,'p_statement_exit','/home/ahmad/other/backup_dates/911205/parsPL/backup/2013_02_21_16_06_56/parser.py',116),
  ('statement -> NEWLINE','statement',1,'p_statement_newline','/home/ahmad/other/backup_dates/911205/parsPL/backup/2013_02_21_16_06_56/parser.py',119),
  ('comparison -> expression EQ expression','comparison',3,'p_comparison','/home/ahmad/other/backup_dates/911205/parsPL/backup/2013_02_21_16_06_56/parser.py',122),
  ('comparison -> expression NE expression','comparison',3,'p_comparison','/home/ahmad/other/backup_dates/911205/parsPL/backup/2013_02_21_16_06_56/parser.py',123),
  ('comparison -> expression GT expression','comparison',3,'p_comparison','/home/ahmad/other/backup_dates/911205/parsPL/backup/2013_02_21_16_06_56/parser.py',124),
  ('comparison -> expression GE expression','comparison',3,'p_comparison','/home/ahmad/other/backup_dates/911205/parsPL/backup/2013_02_21_16_06_56/parser.py',125),
  ('comparison -> expression LT expression','comparison',3,'p_comparison','/home/ahmad/other/backup_dates/911205/parsPL/backup/2013_02_21_16_06_56/parser.py',126),
  ('comparison -> expression LE expression','comparison',3,'p_comparison','/home/ahmad/other/backup_dates/911205/parsPL/backup/2013_02_21_16_06_56/parser.py',127),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','/home/ahmad/other/backup_dates/911205/parsPL/backup/2013_02_21_16_06_56/parser.py',135),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','/home/ahmad/other/backup_dates/911205/parsPL/backup/2013_02_21_16_06_56/parser.py',136),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','/home/ahmad/other/backup_dates/911205/parsPL/backup/2013_02_21_16_06_56/parser.py',137),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','/home/ahmad/other/backup_dates/911205/parsPL/backup/2013_02_21_16_06_56/parser.py',138),
  ('expression -> MINUS expression','expression',2,'p_expression_uminus','/home/ahmad/other/backup_dates/911205/parsPL/backup/2013_02_21_16_06_56/parser.py',145),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','/home/ahmad/other/backup_dates/911205/parsPL/backup/2013_02_21_16_06_56/parser.py',148),
  ('expression -> NUMBER','expression',1,'p_expression_number','/home/ahmad/other/backup_dates/911205/parsPL/backup/2013_02_21_16_06_56/parser.py',151),
  ('expression -> ID','expression',1,'p_expression_id','/home/ahmad/other/backup_dates/911205/parsPL/backup/2013_02_21_16_06_56/parser.py',154),
]
