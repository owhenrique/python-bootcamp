def obter_notas() -> list:
  notas = []
  while True:
    entrada = input("Digite uma nota (ou 'x' para finalizar): ")
    if entrada.lower() == 'x':
      break
    try:
      nota = float(entrada)
      notas.append(nota)
    except ValueError:
      print("Digite um valor de nota válido!")
  
  return notas

def calcula_media(lista) -> None or float:
  if not lista:
    return None
  
  media = sum(lista) / len(lista)
  return round(media, 1)

print(calcula_media([85, 90, 78]))
print(calcula_media([83, 45, 27]))
print(calcula_media([23, 49, 51]))

notas = obter_notas()

print(calcula_media(notas))



