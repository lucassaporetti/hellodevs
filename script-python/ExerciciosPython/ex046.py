from time import sleep
import emoji
for c in range(10, -1, -1):
    print(c), sleep(0.5)
print('FELIZ ANO NOVO!!!', emoji.emojize(':boom:', use_aliases=True))
