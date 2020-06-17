from fastapi import FastAPI
from pydantic import BaseModel
from time import sleep
from fastapi.middleware.cors import CORSMiddleware
import utils
app = FastAPI()


origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/cadastrar/")
def cadastrar(nome:str, usuario:str, senha:str):
    '''
        1 = usuario cadastrado
        2 = usuario e senha já existente
        3 = outros erros


    '''
    resultado = 0

    conexao = utils.conectar()

    #verifica se o usuario e senha já existe
    with conexao.cursor() as cursor:
        cursor.execute('select usuario, senha from usuarios')
        usuarios = cursor.fetchall()

    for i in usuarios:
        if i['usuario'] == usuario and i['senha'] == senha:
            resultado = 2

    #cadastra o usuario se ele já nao existe
    try:
        if not resultado == 2:

            with conexao.cursor() as cursor:
                cursor.execute(f"insert into usuarios (nome, usuario, senha) values ('{nome}', '{usuario}', '{senha}');")

            conexao.commit()

            resultado = 1
    except:
        resultado = 3



    return resultado



@app.post("/login/")
def logar(usuario: str, senha: str):
    conexao = utils.conectar()

    autenticado = False

    # verifica se o usuario e senha já existe
    with conexao.cursor() as cursor:
        cursor.execute('select * from usuarios')
        usuarios = cursor.fetchall()

    for i in usuarios:
        if i['usuario'] == usuario and i['senha'] == senha:
            autenticado = True

    return autenticado

