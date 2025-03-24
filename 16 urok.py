# s = ('самолет прилетает 10.23.2025ю будем рады вас видеть после 10.24.2025')
# reg = r'(\d{2})/(\d{2})/(d{4})'
# print(re.sub(reg, r'\2.\1.\3', s))

#
# def to_str(n, base):
#     convert = '0123456789'
#     if n < base:
#         return convert[n]
#     else:
#         return to_str(n // base, base) + convert[n % base]
#
#
# print(to_str(18, 16))
# ###############################################
# names = ['adam', ['bob', ['chet', 'cat'], 'barb', 'berb'], 'alex', ['bea', 'bill'], 'ann']


###########################################

# f=open('text.txt','r')
#
# print(f.read(3))
# print(f.read())
# f.close()

# f = open('xyz.txt')
# f.write('this is line1.\nthis is line2.\nthis is line3\n')
# f.close()


# f=open('xyz.txt')
# for line in f:
#     print(line)
# f.close()


f=open('test.txt','w')
f.write('hello\nworld\n')
f.close()