'''
a = input('Digite algo: ')
  print(f'O tipo primitivo desse valor é {type(a)} \n'
      f'Só tem espaços? {a.isspace()} \n'
      f'É alfabético? {a.isalpha()} \n'
      f'É alfanumérico? {a.isalnum()} \n'
      f'Está em maiúsculas?, "sim" if{a.isupper()} \n'
      f'Está em minúsculas? {a.islower()} \n'
      f'Está capitalizado? {a.istitle()}') 

a = input('Digite algo: ')

print('O tipo primitivo desse valor é:', type(a))
print('Só tem espaços?:', 'Sim.' if a.isspace() else 'Não.' ,"\n")
print('É um numero?:', 'Sim.' if a.isnumeric() else 'Não.')
print('É um alfabético?:', 'Sim.' if a.isalpha() else 'Não.')
print('É um alfanumérico?:', 'Sim.' if a.isalnum() else 'Não.')
print('Está em maiúsculo?:', 'Sim.' if a.isupper() else 'Não.')
print('Está em minúsculo?: ', 'Sim.' if a.islower() else 'Não.')
print('Está capitalizada?:', 'Sim.' if a.istitle() else 'Não.')

'''

ent = input('Digite algo: ')
print('O tipo primitivo desse valor é: ', type(ent), '\n'
     'Só tem espaços? ', "Sim" if ent.isspace() else "Não", '\n'
     'È um número? ', "Sim" if ent.isnumeric() else "Não", '\n'
     'È alfabeto? ', "Sim" if ent.isalpha() else "Não", '\n'
     'È alfanumerico? ', 'Sim' if ent.isalnum() else "Não", '\n'
     'Está em maiúscula? ', 'Sim' if ent.isupper() else "Não", '\n'
      'Está em minuscula? ', "Sim" if ent.islower() else "Não", '\n'
      )
