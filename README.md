<h1 align="center">Calc CLI - desenvolvido em Python</h1>

<p align="center">
    <img loading="lazy" src="https://img.shields.io/badge/Python-V3.12.0-green" />
    <img loading="lazy" src="https://img.shields.io/badge/Python-V3.12.0-green" />
</p>

<p>
Este é o meu primeiro projeto prático com Python, uma Calculadora CLI, que surge da minha curiosidade em explorar a criação de interfaces de linha de comando (CLI) após utilizar extensivamente o terminal do Linux. Neste projeto, utilizei algumas bibliotecas úteis, como 'rich', 'argparse' e 'setuptools', para criar uma experiência de usuário amigável e eficiente.
</p>

<p>
Esta aplicação é uma demonstração do potencial do Python na criação de utilitários de linha de comando para simplificar tarefas cotidianas.
</p>

<h3 align="center">Estrutura do projeto:</h3>

```
calulator/
├── README.md
├── calculator
  ├── __init__.py
  ├── __main__.py
  └── formula.py
└── setup.py
```

<h3 align="center">Como instalar:</h3>
<p>
Para instalar é simples, basta fazer o clone deste repositório, acessar a pasta via terminal e digitar o comando:
</p>

```
pip install .
```

<h3 align="center">Comandos disponíveis:</h3>

```
mycalc -flag <números de sua escolha>
```

- `-a` ou `--addition`: Realiza a adição de vários números.
- `-s` ou `--subtraction`: Realiza a subtração de diversos números.
- `-m` ou `--multiplication`: Realiza a multiplicação de diversos números.
- `-d` ou `--division`: Realiza a divisão de dois números.

<p>Por enquanto, esses são os comandos disponíveis. Em futuras atualizações, planejo aprimorar o projeto.</p>

<h3 align="center">Contribuição:</h3>

<p>Este projeto é uma ótima introdução ao desenvolvimento de CLIs em Python e à utilização de bibliotecas como 'rich' e 'argparse'. Fique à vontade para contribuir, relatar problemas ou propor melhorias. Estou entusiasmado em continuar explorando a criação de CLIs e expandir este projeto no futuro.</p>
<h3 align="center">Licença:</h3>

<p>Este projeto é distribuído sob a Sua Licença. Sinta-se à vontade para utilizá-lo e modificá-lo de acordo com suas necessidades.</p>

<h3 align="center">Bibliografia:</h3>

<p>
Esse projeto foi baseado nos artigos:

- https://itanuromero.medium.com/como-criar-uma-cli-em-python-fd80320f7968
- https://trstringer.com/easy-and-nice-python-cli/

E alguns leves pitacos do nosso querido ChatGPT!

</p>

```

8 8888888888   b.             8 8 888888888o.
8 8888         888o.          8 8 8888    `^888.
8 8888         Y88888o.       8 8 8888        `88.
8 8888         .`Y888888o.    8 8 8888         `88
8 888888888888 8o. `Y888888o. 8 8 8888          88
8 8888         8`Y8o. `Y88888o8 8 8888          88
8 8888         8   `Y8o. `Y8888 8 8888         ,88
8 8888         8      `Y8o. `Y8 8 8888        ,88'
8 8888         8         `Y8o.` 8 8888    ,o88P'
8 888888888888 8            `Yo 8 888888888P'

```
