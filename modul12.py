money = int(input("Введите сумму:"))
print(money)

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []
bank_deposit = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}


accumulated_funds_TKB = money / 100 * per_cent['ТКБ']
accumulated_funds_SKB = money / 100 * per_cent['СКБ']
accumulated_funds_VTB = money / 100 * per_cent['ВТБ']
accumulated_funds_SBER = money / 100 * per_cent['СБЕР']

deposit.append(int(accumulated_funds_TKB))
deposit.append(int(accumulated_funds_SKB))
deposit.append(int(accumulated_funds_VTB))
deposit.append(int(accumulated_funds_SBER))

bank_deposit['ТКБ'] = accumulated_funds_TKB
bank_deposit['СКБ'] = accumulated_funds_SKB
bank_deposit['ВТБ'] = accumulated_funds_VTB
bank_deposit['СБЕР'] = accumulated_funds_SBER

max_bank_deposit = max(bank_deposit, key=bank_deposit.get)

print('Депозит -', deposit)

print('Максимальная сумма, которую вы можете заработать —', str(max(deposit)),"|", 'В банке -', str(max_bank_deposit),)