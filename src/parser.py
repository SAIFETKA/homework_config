from lark import Lark

grammar = r"""
start: statement*

?statement: var_decl ";"

var_decl: "var" NAME ":=" value

?value: NUMBER
      | STRING
      | array
      | dict
      | const_expr
      | var_ref

array: "#(" [value*] ")"
dict: "{" [pair ("," pair)*] "}"
pair: NAME "=" value

var_ref: NAME ("." NAME)*

const_expr: "?" "(" OP value (value)? ")"
OP: "+" | "-" | "*" | "len"

STRING: ESCAPED_STRING
%import common.ESCAPED_STRING
%import common.CNAME -> NAME
%import common.SIGNED_NUMBER -> NUMBER
%import common.WS

%ignore WS
%ignore "::" /[^\n]/*
%ignore "/*" /(.|\n)*?/ "*/"
"""

parser = Lark(grammar, start='start', parser='lalr')
