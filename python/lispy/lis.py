import math
import operator as op

Env = dict

def standard_env():
    env = Env()
    env.update(vars(math))
    env.update({
        '+':op.add, '-':op.sub, '*':op.mul, '/':op.div, 
        '>':op.gt, '<':op.lt, '>=':op.ge, '<=':op.le, '=':op.eq, 
        'abs':     abs,
        'append':  op.add,  
        'apply':   apply,
        'begin':   lambda *x: x[-1],
        'car':     lambda x: x[0],
        'cdr':     lambda x: x[1:], 
        'cons':    lambda x,y: [x] + y,
        'eq?':     op.is_, 
        'equal?':  op.eq, 
        'length':  len, 
        'list':    lambda *x: list(x), 
        'list?':   lambda x: isinstance(x,list), 
        'map':     map,
        'max':     max,
        'min':     min,
        'not':     op.not_,
        'null?':   lambda x: x == [], 
        'number?': lambda x: isinstance(x, Number),   
        'procedure?': callable,
        'round':   round,
        'symbol?': lambda x: isinstance(x, Symbol),        
    })
    return env

global_env = standard_env()

Symbol  = str           # A Scheme Symbol is implemented using a Python str
List    = list          # A Scheme List is implemented using a Python list
Number  = (int, float)  # A Scheme Numbers if implemented using either 
                        # a Python int or a Python float

def parse(program):
    "Read a scheme expression from a string"
    return read_from_tokens(tokenize(program))

def read_from_tokens(tokens):
    "Read an expression from a sequence of tokens"
    if len(tokens) == 0:
        raise SyntaxError('unexpected EOF while reading')
    token = tokens.pop(0)
    if '(' == token:
        L = []
        while tokens[0] != ')':
            L.append(read_from_tokens(tokens))
        tokens.pop(0)
        return L
    elif ')' == token:
        raise SyntaxError('unexpected )')
    else:
        return atom(token)

def atom(token):
    "Numbers are numbers. Every other token is a symbol"
    try: return int(token)
    except ValueError:
        try: return float(token)
        except ValueError:
            return Symbol(token)

def tokenize(chars):
    "Convert a string of chars into a list of tokens"
    return chars.replace('(', ' ( ').replace(')', ' ) ').split()

def eval(x, env=global_env):
    if isinstance(x, Symbol):
        return env[x]
    elif not isinstance(x, List):
        return x
    elif x[0] == 'if':
        (_, test, conseq, alt) = x
        exp = (conseq if eval(test, env) else alt)
        return eval(exp, env)
    elif x[0] == 'define':
        (_, var, exp) = x
        env[var] = eval(exp, env)
    else:
        proc = eval(x[0], env)
        args = [eval(arg, env) for arg in x[1:]]
        return proc(*args)

def repl(prompt='lis.py> '):
    while True:
        val = eval(parse(raw_input(prompt)))
        if val is not None:
            print(schemestr(val))

def schemestr(exp):
    if isinstance(exp, List):
        return '('+' '.join(map(schemestr, epx))+')'
    else:
        return str(exp)

if __name__ == '__main__':
    program_1 = ""
    program_2 = "()"
    program_3 = "(hello)"
    program_4 = "(hello world)"
    program_5 = "(begin (define r 10) (* pi (* r r)) )"

    parsed = parse(program_5)
    print parsed
    print eval(parsed)
    repl()
    

