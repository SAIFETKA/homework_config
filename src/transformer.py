from lark import Transformer

class ConfigTransformer(Transformer):
    def __init__(self):
        self.vars = {}

    def var_decl(self, items):
        name = str(items[0])
        value = items[1]
        self.vars[name] = value
        return (name, value)

    def NUMBER(self, token):
        return float(token) if '.' in token else int(token)

    def STRING(self, token):
        return str(token)[1:-1]

    def array(self, items):
        return list(items)

    def dict(self, items):
        return dict(items)

    def pair(self, items):
        return (str(items[0]), items[1])

    def var_ref(self, items):
        val = self.vars.get(str(items[0]))
        for field in items[1:]:
            if val is None:
                raise ValueError(f"Переменная или поле '{'.'.join([str(i) for i in items])}' не найдено")
            val = val.get(str(field))
        return val

    def const_expr(self, items):
        op = str(items[0])
        if op == 'len':
            arg = items[1]
            return len(arg)
        else:
            a = items[1]
            b = items[2]
            return {'+': a + b, '-': a - b, '*': a * b}[op]
