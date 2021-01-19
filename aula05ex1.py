#contador = 1
#while(contador <= 10):
#    print(contador)
#    contador = contador + 1

#for contador in range(1, 11):
#    print(contador)

num_tabuada = int(input('Digite o número você deseja a tabuada: '))

for multiplicador in range(1,11):
    calc = num_tabuada*multiplicador
    print('{}x{}={}'.format(num_tabuada,multiplicador,calc))