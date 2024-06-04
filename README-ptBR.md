# Pytest

## Introdução
Pytest é uma estrutura de [código aberto](https://github.com/pytest-dev/pytest) para testes em Python que facilita a gravação de testes pequenos e legíveis e pode ser dimensionada para suportar testes funcionais complexos para aplicativos e bibliotecas.

[Possui integração com o framework `unittest`.](https://docs.pytest.org/en/7.1.x/how-to/unittest.html#:~:text=pytest%20supports%20running%20Python%20unittest%20%2Dbased%20tests%20out%20of%20the%20box.)


## Aplicações
Pytest é utilizado para todos os tipos de testes em Python quando:
- Testes unitários (Componentes individuais)
- Testes de integração (Interação entre dois ou mais componentes)
- Testes de aceitação (Verificar se o sistema atende aos requisitos especificados pelo usuário ou cliente)
- Testes de carga (Verificar o desempenho do sistema)
- Testes de regressão (Se o sistema ainda funciona após uma alteração)


## Processo de instalação
O processo de execução será explicado antes

1. Crie um ambiente virtual:
```bash
python -m venv ./.venv
```

2. Ative o ambiente virtual no windows:
```bash
./.venv/Scripts/activate
```
  1. No Linux, o caminho é `./.venv/bin/activate`.
  2. No Windows, não se esqueça de permitir a execução de scripts com o comando `Set-ExecutionPolicy Unrestricted -Scope Process`.

3. Instale o Pytest:
```bash
pip install pytest
```

4. (OPCIONAL) Instale o Pytest-html para gerar um relatório em HTML:
```bash
pip install pytest-html
```


## Como criar e executar um teste

### Convenção para o Diretório de Testes
Quando o `pytest` é executado, ele procurará por arquivos que começam com `test_` ou terminam com `_test.py` e os executará.

É altamente recomendável criar um arquivo chamado `__init__.py` na pasta de módulos para que o pytest reconheça a pasta como um módulo.

### Exemplo
Criando um arquivo de teste e executando-o:

```python
# tests/test_sample.py
def test_sample():
  assert 1 == 1
```
```bash
pytest tests/test_sample.py
```
Ou apenas execute o comando abaixo para executar todos os testes do projeto:
```bash
pytest
```


## Recomendações e Referências
- Crie [arquivos de configuração](https://docs.pytest.org/en/stable/reference/reference.html#configuration-options) para seus testes, como `pytest.ini` ou `setup.cfg`.
- [Documentação](https://docs.pytest.org/en/stable/index.html)
- [Pytest vs Unittest](https://docs.pytest.org/en/7.1.x/how-to/unittest.html#:~:text=pytest%20supports%20running%20Python%20unittest%20%2Dbased%20tests%20out%20of%20the%20box.)
- [Médio](https://medium.com/assertqualityassurance/tutorial-de-pytest-para-iniciantes-cbdd81c6d761)
