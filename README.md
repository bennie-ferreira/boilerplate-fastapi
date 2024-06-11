## 🚀 Um Boilerplate de backend python para Alta Performance! 🚀

Este boilerplate foi desenvolvido ao longos de varios anos, visando trazer performance, segurança, agilidade e qualidade nos projetos administrado por min, este boilerplate usa como padrão arquitetura hexagonal uma arquiterua de alta reusabilidade e baixa dependencia, assim mantendo a regra de negocio
como o nucleo principal da aplicação

O foco principal da arquitetura hexagonal é construir sistemas que favorecem reusabilidade de código, alta coesão, baixo acoplamento, independência de tecnologia e que são mais fáceis de serem testados, além de ser case de sucesso por varias empresas de tecnologia.

## ⚙️ O Core do boilerplate ⚙️

- Arquitetura hexagonal como padrão
  
- Poetry para gerenciamento de dependencias

- Fastapi o framework mais moderno em python

- Pydantic para tipagens de dados

- Pytest para testes unitarios e testes de integração

- Cobertura de testes em 100% em pipelines, além de lint

## ⭐ Implementações do boilerplate ⭐

- Suporte a Banco de Dados 🛢️

- Seeds 🌱

- Envio de Emails 📧

- Autenticação e Autorização via JWT ou Keycloak 🔐

- Upload de Arquivos 📂

- Swagger 📝

- Testes 🧪

- Docker 🐳

- Cron e Crontab para execução de jogs agendados 🕰️

- CI/CD 🔍

- Logger 📝

- Makefile 📝

- Pronto para Produção 📐


## 🔨 Instalação do projeto 🔨
### 1. Executar comando para verificar a versão do poetry
```sh
poetry --version
```

### 2. Configurar o ambiente virtual para ser criado dentro do projeto
```sh
poetry config virtualenvs.in-project true
```

### 3. Criar um ambiente virtual para instalar as dependencias e libs para o funcionamento do projeto
```sh
poetry env use python
```

### 4. Ativar ambiente virtual 
```sh
poetry shell
```
### 5. Instalar as dependencias do Poetry
```sh
poetry install
```

### 6. [Opcional] Para sair do ambiente virtual
```sh
exit
```

### 7. [Opcional] Makefile instação
No linux geralmente vem por padrão agora windows recomendo esse tutoras [aqui](https://leangaurav.medium.com/how-to-setup-install-gnu-make-on-windows-324480f1da69)
```sh
make --version
```

### 5. Iniciar servidor da aplicação
```sh
make run
```