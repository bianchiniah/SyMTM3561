from sympy import *
from data import *

def num_solv(oper):
    copia = oper[0].copy()
    expr = oper[1]
    while True:
        var = input('Escolha a variavel: {} '.format(copia))
        if var == 'quit':
            return
        if var in copia:
            copia[var] = Symbol(var)
            break
    for i in copia.keys():
        if i == var:
            continue
        else:
            copia[i] = input('{} = '.format(i))
            if copia[i] in memoria:
                copia[i] = memoria[copia[i]]
            try:
                copia[i] = float(copia[i])
                if copia[i] <= 0:
                    raise Exception()
            except:
                print('Erro: valor invalido.')
                return
    eq = sympify(expr, locals = copia)
    try:
        result = solve(eq, dict = True)
    except:
        print('Erro: nao foi possivel resolver.')
        return
    if result == []:
        print('Erro: sem solucoes.')
        return
    res_final = result[0][Symbol(var)]
    try:
        float(res_final)
    except:
        print('Erro: resultado fora do dominio dos reais.')
        return
    print(var, '=', res_final)
    memi = input('Salvar na memoria? {} '.format(memoria))
    if memi in memoria:
        memoria[memi] = res_final

print('''SyMTM3561, 15/08/2022.
Digite 'help' para ajuda.''') 
while True:
    op = input('>>> ')
    if op == 'esc':
        break
    elif op == 'help': 
        print(ajuda)
    elif op == 'list': 
        print(listaop)
    elif op in op_dict:
        num_solv(op_dict[op])
    elif op in memoria:
        try:
            memoria[op] = float(input('{} = '.format(op)))
        except:
            print('Erro: valor invalido.')
            continue
    elif op == 'rcl':
        print(memoria)
    elif op == 'clear':
        certeza = input("Tem certeza? {'1' : 'Sim', '2' : 'Nao'} ")
        if certeza == '1':
            memoria = {'x' : 0, 'y' : 0, 'z' : 0, 't' : 0, 'a' : 0, 'b' : 0, 'c' : 0, 'd' : 0}
