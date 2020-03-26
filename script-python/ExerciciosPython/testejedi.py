import emoji
nome = str(input('Qual é o seu nome? ')).strip().upper().split()[0]
if nome == 'LUCAS':
    print('Você é um jovem Padawan!\nVá estudar vagabundo!')
if nome == 'HUGO':
    print('Você é um mestre Jedi!\nMuito obrigado mestre!')
elif nome != 'LUCAS' and 'HUGO':
    print('Você não é um detentor da força...')
print('May the force be with you... Bye!',
      emoji.emojize(':thumbsup:', use_aliases=True))
