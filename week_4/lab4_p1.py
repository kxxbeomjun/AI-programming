#lab4_p1.py

#getting input
income = int(input('Enter the taxable income in USD: '))

#구간별로 tax 비율 나누기
if income < 751:
    tax = 0.02 * income
elif income < 2251:
    tax = 7.50 + 0.03*(income-750)
elif income < 3751:
    tax = 37.50 + 0.06*(income-2250)
elif income < 5251:
    tax = 82.50 + 0.09 * (income-3750)
elif income < 7001:
    tax = 0.03*income + 0.1*(income-5250)
else:
    tax = 0.04*income + 0.12*(income-7000)

#세금 제외한 income 계산
final_income = income - tax

#print 구문 소수둘째자리 까지 표현 위해 format함수 사용
print('Tax due:', format(tax, '.2f'), 'USD')
print('Final income:', format(final_income, '.2f'), 'USD')
