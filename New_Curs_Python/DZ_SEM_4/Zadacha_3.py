# Возьмите задачу о банкомате из семинара.

# Разбейте её на отдельные операции — функции.

# Дополнительно сохраняйте все операции поступления и снятия средств в список.


# Напишите программу банкомат.

# Начальная сумма равна нулю

# Допустимые действия: пополнить, снять, выйти

# Сумма пополнения и снятия кратны 50 у.е.

# Процент за снятие - 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.

# После каждой третей операции пополнения или снятия начисляются проценты - 3%

# Нельзя снять больше, чем на счёте

# При превышении суммы в 5 млн,

# вычитать налог на богатство 10% перед каждой операцией, даже ошибочной

# Любое действие выводит сумму денег


def replenishment(frindering):

    global balance, count, transactions

    withdrow = int(input('введите сумму: '))

    if withdrow % frindering == 0:

        balance += withdrow

        count += 1

        transactions.append(("пополнение", withdrow))

    return balance, count, transactions


def withdrawal(FREENDERING, MINLIMIT, MAXLIMIT):

    global balance, count

    withdrow = int(input('введите сумму снятия : '))

    if withdrow % FREENDERING == 0:

        comission = withdrow * COMMISSIONOUTDROW

    if comission < MINLIMIT:

        comission = MINLIMIT

    elif comission > MAXLIMIT:

        comission = MAXLIMIT

    if (comission + withdrow) < balance:

        balance -= (withdrow + comission)

        count += 1

        transactions.append(("снятие", (withdrow + comission)))

    return balance, count, transactions


balance = 10000

count = 0

RICHLIMIT = 5_000_000

RICHTAX = 0.9

THREEOPERATIONS = 3

BONUSTHREE = 1.03

COMMISSIONOUTDROW = 0.015

FREENDERING = 50

MINLIMIT = 30

MAXLIMIT = 600

transactions = []

while True:

    action = input('Введите операцию: пополнение - 1, снятие - 2, выход - 3: ')

    if balance >= RICHLIMIT:

        balance *= RICHTAX

    if count % THREEOPERATIONS == 0 and count != 0:

        balance *= BONUSTHREE
        count = 0

    if action == '1':

        replenishment(FREENDERING)

    elif action == '2':

        withdrawal(FREENDERING, MINLIMIT, MAXLIMIT)

    else:

        break

    print("Текущий баланс:", balance)
    print(f'Транзакции по счету : {transactions}')
