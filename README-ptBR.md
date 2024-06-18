# Pytest

## Índice
- [Introdução](#introdução)
- [Aplicações](#aplicações)
- [Processo de Instalação](#processo-de-instalação)
- [Como Criar e Executar um Teste](#como-criar-e-executar-um-teste)
  - [Convenção para Diretório de Testes](#convenção-para-diretório-de-testes)
  - [Exemplo](#exemplo)
- [Pytest + Relatório HTML](#pytest--relatório-html)
- [Recursos Futuros](#recursos-futuros)
- [Recomendações e Referências](#recomendações-e-referências)


## Introdução
Pytest é um framework de código aberto para testes em Python que facilita a escrita de testes pequenos e legíveis, e pode escalar para suportar testes funcionais complexos para aplicações e bibliotecas.

[Ele tem integração com o framework `unittest`.](https://docs.pytest.org/en/7.1.x/how-to/unittest.html#:~:text=pytest%20supports%20running%20Python%20unittest%20%2Dbased%20tests%20out%20of%20the%20box.)


## Aplicações
Pytest é usado para todos os tipos de testes em Python quando:
- Testes unitários (Componentes individuais)
- Testes de integração (Interação entre dois ou mais componentes)
- Testes de aceitação (Verificar se o sistema atende aos requisitos especificados pelo usuário ou cliente)
- Testes de carga (Verificar o desempenho do sistema)
- Testes de regressão (Se o sistema ainda funciona após uma mudança)


## Processo de Instalação
O processo de execução será explicado antes

1. Crie um ambiente virtual:
```bash
python -m venv ./.venv
```

2. Ative o ambiente virtual no Windows:
```bash
./.venv/Scripts/ativar
```
  a. No Linux, o caminho é `./.venv/bin/activate`.
  b. No Windows, não esqueça de permitir a execução de scripts com o comando `Set-ExecutionPolicy Unrestricted -Scope Process`.

3. Instale o Pytest:
```bash
pip install pytest
```

4. (OPCIONAL) Instale o Pytest-html para gerar um relatório em HTML:
```bash
pip install pytest-html
```


## Como criar e executar um teste

### Convenção para testar o diretório
Quando `pytest` for executado, ele procurará arquivos que começam com `test_` ou terminam com `_test.py` e o executará.

É altamente recomendado criar um arquivo chamado `__init__.py` na pasta de módulos para que o pytest reconheça a pasta como um módulo.

### Exemplo
Criando um arquivo de teste e executando-o:

```python
# testes/test_sample.py
def teste_amostra():
  afirmar 1 == 1
```
```bash
pytest testes/test_sample.py
```
Ou apenas execute o comando abaixo para executar todos os testes do projeto:
```bash
pytest
```


## Pytest + Relatório HTML
Para gerar um relatório HTML, execute o comando abaixo:
1. Instale o pacote `pytest-html`:
```bash
pip install pytest-html
```
2. Execute o comando abaixo:
```bash
pytest --html=test_report/report.html
```


## Recursos Futuros
- Criar casos para comparar o Pytest com o Unittest usando o segundo link em Recomendações e Referências.
- Criar um tópico explicando como containerizar os testes com Docker.
- Remover a pasta `Foo` e a segunda linha no arquivo `.env`, pois não são necessárias para o projeto, apenas para fins acadêmicos.


## Recomendações e referências
- Crie [arquivos de configuração](https://docs.pytest.org/en/stable/reference/reference.html#configuration-options) para seus testes, como `pytest.ini` ou `setup.cfg`.
- [Documentação](https://docs.pytest.org/en/stable/index.html)
- [Pytest vs Unittest](https://docs.pytest.org/en/7.1.x/how-to/unittest.html#:~:text=pytest%20supports%20running%20Python%20unittest%20%2Dbased% 20testes%20out%20of%20the%20box.)
- [Médio](https://medium.com/assertqualityassurance/tutorial-de-pytest-para-iniciantes-cbdd81c6d761)
- [História do Pytest](https://docs.pytest.org/pt/stable/history.html)
