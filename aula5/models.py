class Aluno:
    def __init__(self , nome, sexo, telefone, email, data_nascimento, data_matricula, turma_fk, desconto , id_aluno = None):
        self.id_aluno = id_aluno
        self.nome = nome
        self.sexo = sexo
        self.telefone = telefone
        self.email = email
        self.data_nascimento = data_nascimento
        self.data_matricula = data_matricula
        self.turma_fk = turma_fk
        self.desconto = desconto


class Pagamento:
    def __init__(self, id, valor, data, aluno):
        self.id = id
        self.valor = valor
        self.data = data
        self.aluno = aluno


class Turma_fk:
    def __init__(self, id, nome, dia, hora, valor):
        self.id = id
        self.nome = nome
        self.dia = dia
        self.hora = hora
        self.valor = valor


class Aula:
    def __init__(self, id, data, turma_fk):
        self.id = id
        self.data = data
        self.turma_fk = turma_fk

class Aluno_aula:
    def __init__(self, aluno, aula):
        self.aluno = aluno
        self.aula = aula


class Usuario:
    def __init__(self, id, nome, senha):
        self.id = id
        self.nome = nome
        self.senha = senha
