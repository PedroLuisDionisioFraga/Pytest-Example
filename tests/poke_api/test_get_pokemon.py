from flask import Flask
import requests

app = Flask(__name__)

@app.route("/pokemon/piplup", methods=["GET"])
def get_piplup():
  response = requests.get("https://pokeapi.co/api/v2/pokemon/piplup")
  return str(response.json()), response.status_code

def test_get_piplup_contains_bubble():
  response, status_code = get_piplup()
  assert status_code == 200
  assert "bubble" in response

def test_get_piplup_contains_piplup():
  response, status_code = get_piplup()
  assert status_code == 200
  assert "piplup" in response

def test_get_piplup_not_contains_charmander():
  response, status_code = get_piplup()
  assert status_code == 200
  assert not "charmander" in response
