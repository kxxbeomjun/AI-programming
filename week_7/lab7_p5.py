#lab7_p5.py

#getting input & split by '-'
n1, n2, n3, n4, n5 = map(int, input('Enter an ISBN: ').split('-'))

#print구문들
print(format(n1, '.<20')+'GS1 prefix')
print(format(n2, '.<20')+'Group identifier')
print(format(n3, '.<20')+'Publisher code')
print(format(n4, '.<20')+'Item number')
print(format(n5, '.<20')+'Check digit')