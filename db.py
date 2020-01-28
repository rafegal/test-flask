def create_tech_db(nome, descricao):
    file = open('db.txt', 'a')
    dados = f'{nome}, {descricao}\n'
    file.write(dados)
    file.close()

def get_tech_db(nome):
    return {"nome": nome, "descricao": "descricao generica"}