# Primeiros passos

Clone o repositório e abra o terminal.

```bash
git clone https://github.com/robert-the-freaking-victor/teste_python_backend.git
cd teste_python_backend
```

Agora no terminal, execute o comando abaixo.

```bash
pip3 -r install requirements
```

Agora crie um arquivo .env, de acordo com o .env.example.

No banco de dados, é importante que o banco de dados tenha sido criado. Apenas o banco, pois as tabelas são criadas automaticamente.

Execute o arquivo index.py para rodar o servidor.

```bash
python index.py
```

| Endpoint                 | Método | Body                                   | Descrição
| ------------------------ | ------ | -------------------------------------- | -------------------------------------------------------- |
| /Users                   | POST   | { username: string, password: string } | Cria um usuário                                          |
| /Auth                    | POST   | { username: string, password: string } | Autentica um usuario e retorna o token JWT               |
| /Users/<int:id>          | PUT    | { username: string, password: string } | Altera o usernmae e/ou senha do usuário.                 |
| /Users/<int:id>          | DELETE | None                                   | Deleta o usuário                                         |
| /Megasena                | POST   | { unities: integer }                   | Cria um novo jogo na megasena                            |
| /Megasena/Results        | GET    | None                                   | Pega o resultado da última megasena                      |
| /Megasena/CorrectNumbers | GET    | None                                   | Confere quantos números o usuário acertou no último jogo |
| /Megasena                | GET    | None                                   | Retorna os jogos feitos por esse usuário                 |
