# person={}
# person['name'] ='ivan'
# person['age']=30
# print(person)
# person1={'name': 'mary', 'age':22}
# print(person1)
#
# person2=dict(name='alex', age=45)
# print(person2)
#
# person3=dict((('peter',30),('olga',25)))
# print(person3)

# person={'name':'ivan','age':30}
# age=person.get('age')
# print(age)
##########################################################################
# mytuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
#      #     0, 1, 2, 3, 4, 5, 6, 7, 8
# print(mytuple[3])
# print(mytuple[2:6])
# newtuple= mytuple+('a','b','c')
# print(newtuple)
# print(5 in mytuple)
# print(11 in newtuple)
# print(len(newtuple))
# my_operator='mts'
# call_operator='beeline'
# tarif_dict={('mts','beeline'):50}
# time = 10
# call_cost=tarif_dict[(my_operator, call_operator)]*time
# print(call_cost)
    #######################################################################

words=('pitin','java','c++','script','ruby')
print('кол-во элем кортежа(длина) - ',len(words))
serf_word=input('введите ЯП для поиска: ')
if serf_word in words:
    print(f'{serf_word},есть в корт')
else:
    print(f'{serf_word},нет в корт')
print(f'первый эл,{words[0]}')
print(f'последний,{words[-1]}')



