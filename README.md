# API Simples em Flask

## 🎯 Objetivos de Aprendizagem

1. Consolidar o aprendizado de **Python** com **APIs**, **JSON** e **Flask**.  
2. Compreender a relação entre **Python** e **Cloud Computing**.  
3. Praticar **versionamento** com **Git e GitHub** (commit, push, pull).  
4. Desenvolver autonomia na **documentação de projetos**.

---

### ⚠️ AVISO
Este repositório foi criado como ambiente de estudos. Ele não possui implementações de segurança e apresenta diversas vulnerabilidades. Use-o apenas para fins educacionais.

---

## 📌 Rotas da API

- **`alunos.py`**
  - `GET /alunos` → lista estudantes
  - **Parâmetros**:
    - **`aluno`** _(opcional)_: Filtrar por nome de estudante.
      - **Ex**: `?aluno=João`
  - `POST /alunos` → cria novos alunos  
  - `PUT /alunos/` → atualiza informações de alunos  
  - `DELETE /alunos/` → remove alunos

- **`curso.py`**
  - `GET /curso` → retorna o curso de uma aluno

- **`gitrepo.py`**
  - `GET /github-repo` → retorna informações do repositório do aluno(exemplo de integração com GitHub API)  

- **`saudacao.py`**
  - `GET /saudacao` → retorna uma mensagem de saudação simples para o aluno 

- **`weather.py`**
  - `GET /weather` → retorna dados de clima sobre a cidade do usuário

---

## Exemplos de uso para cada rota:
### GET rota alunos
![GET rota alunos](examples/image.png)
### GET rota curso
![GET rota curso](examples/image-1.png)
### GET rota github-repo
![GET rota github-repo](examples/image-2.png)
### GET rota saudacao
![GET rota saudacao](examples/image-3.png)
### GET rota weather
![GET rota weather](examples/image-4.png)