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
    def __init__(self, valor, data, aluno, id_pagamento = None):
        self.id = id_pagamento
        self.valor = valor
        self.data = data
        self.aluno = aluno


class Turma_fk:
    def __init__(self, nome, dia, hora, valor, id_turma = None):
        self.id = id_turma
        self.nome = nome
        self.dia = dia
        self.hora = hora
        self.valor = valor


class Aula:
    def __init__(self, data, turma_fk, id_aula = None):
        self.id = id_aula
        self.data = data
        self.turma_fk = turma_fk

class Aluno_aula:
    def __init__(self, aluno, aula):
        self.aluno = aluno
        self.aula = aula


class Usuario:
    def __init__(self, nome, senha, id_usuario = None):
        self.id = id_usuario
        self.nome = nome
        self.senha = senha
