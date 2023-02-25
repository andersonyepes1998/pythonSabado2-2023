#Represa hidruituango

#Entradas

levelWrote = float(input('Digite el nivel del agua: '))

#proceso

if levelWrote >=0 and levelWrote<=250:
    print('El sensor marca ',levelWrote, 'muy bajo..')
elif levelWrote >250 and levelWrote<=400:
    print('El sensor marca ',evelWrote,'y esta operando normalmente..')
else:
    print('El sensor marca ',levelWrote, 'PELIGRO..')
