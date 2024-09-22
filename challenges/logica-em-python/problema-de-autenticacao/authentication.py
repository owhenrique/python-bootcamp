import json

with open('users.json', 'r') as file:
  data = json.load(file)

def authentication(username: str, password: str) -> bool:
  for user in data['users']:
    if user.get('username') == username and user.get('password') == password:
      return True
  return False

if authentication(input("Digite seu usuário: "), input("Digite sua senha: ")):
  print("Usuário autenticado")
else:
  print("Credenciais inválidas")

file.close()