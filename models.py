from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy_utils.types import ChoiceType


# Cria a conexão com o banco de dados
db = create_engine('sqlite:///banco.db')

# Cria a base do banco de dados
base = declarative_base()

class Usuario(base):
    __tablename__ = 'usuarios'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    nome = Column('nome', String)
    email = Column('email', String, nullable=False, unique=True)
    senha = Column('senha', String)
    ativo = Column('ativo', Boolean)
    admin = Column('admin', Boolean, default=False)

    def __init__(self, nome, email, senha, ativo=True, admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin



class Pedido(base):
    __tablename__ = 'pedidos'

    # status_pedidos = [
    #     ('PENDENTE' , 'PENDENTE'),
    #     ('CANCELADO' , 'CANCELADO'),
    #     ('FINALIZADO' , 'FINALIZADO')
    # ]

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    status = Column('status', String, default='PENDENTE')
    usuario = Column('usuario', ForeignKey('usuarios.id'))
    preco = Column('preco', Float)
    itens = relationship('ItensPedido', cascade='all, delete')

    def __init__(self, usuario, status='PENDENTE', preco=0):
        self.usuario = usuario
        self.status = status
        self.preco = preco


    def calcular_preco(self):
        self.preco = sum(item.preco_unitario * item.quantidade for item in self.itens)


class ItensPedido(base):
    __tablename__ = 'itens_pedido'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    quantidade = Column('quantidade', Integer)
    sabor = Column('sabor', String)
    tamanho = Column('tamanho', String)
    preco_unitario = Column('preco_unitario', Float)
    pedido = Column('pedido', ForeignKey('pedidos.id'))

    def __init__(self, quantidade, sabor, tamanho, preco_unitario, pedido):
        self.quantidade = quantidade
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco_unitario = preco_unitario
        self.pedido = pedido
        


# Migrar banco de dados

# Criar a migração: alembic revision --autogenerate -m "mensagem"
# executar a migração: alembic upgrade head