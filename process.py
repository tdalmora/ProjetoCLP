import json
"""objs_teste = [
    {
        "Config": 1,        # Se 1, é um bloco lógico. Se 0, é um branch.
        
        "NA/NF" : True,     # Se TRUE --> NA
        "I/O" : True,       # Se TRUE --> Input
        "D/A" : True,       # Se TRUE --> Digital
        "PORT" : 1,         # Valor da porta
        
        "BI" : False,       # Se ele inicia uma branch
        "BF" : False        # Se finaliza uma branch
    },
    {
        "Config": 1,
        
        "NA/NF" : False,
        "I/O" : True,
        "D/A" : True,
        "PORT" : 2,
        
        "BI" : False,
        "BF" : False       
    },
    {
        "Config": 1,
        
        "NA/NF" : True,
        "I/O" : False,
        "D/A" : True,
        "PORT" : 0,
        
        "BI" : False,
        "BF" : False       
    }
]

# Usando uma string JSON.
# Transforma meu objeto python (objs_teste) em uma str json (objs_json).
objs_json = json.dumps(objs_teste)
print(objs_json)

# Transforma meu str json (objs_json) objeto python (objs_teste).
objs_teste = json.loads(objs_json)
print(objs_teste) """

# Lê valor da porta.
def PORT_STATUS(num):
    return (num/num)

# Seta uma saída.
def set_Status_Equation():
    ...

# Abrindo arquivo JSON e transormando em um obj python.
with open('teste_json.json') as arquivo_json:
    obj_python = json.load(arquivo_json)
    # json.dump  transforma em arquivo

# É aqui aonde eu crio a equação e faço as "variáveis".
# Cada variável vai ser uma das inputs.
# Não não não --> Fazer uma struct?
for obj in obj_python:
    if obj['Config']:
        if obj['NA/NF']:
            IN = PORT_STATUS(obj['PORT'])
        else:
            IN = not PORT_STATUS(obj['PORT'])
        equation.apend(IN)
            
# O while vai constantemente ver a mudança da equação, e setar a saída dependendo dela.
# OUT seria o bloco lógico de saída.        
while True:
     
    set_Status_Equation()
    
    if equation:
        SET_PORT(OUT['PORT'])