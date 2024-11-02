
# Считываем входные данные
import sys

def main():
    import sys

    # Считываем первую строку
    line = sys.stdin.readline().strip()
    if not line:
        return

    N, M, S = map(int, line.strip().split())
    N = int(N)
    M = int(M)
    S = int(S)

    lots = []

    while True:
        line = sys.stdin.readline()
        if not line or line.strip() == '':
            break
        parts = line.strip().split()
        day = int(parts[0])
        name = parts[1]
        price_percent = float(parts[2])
        quantity = int(parts[3])
        # Вычисляем стоимость и прибыль для лота
        price_per_bond = price_percent * 10  # Так как номинал 1000 единиц
        cost_lot = int(round(quantity * price_per_bond))
        purchase_day = day
        coupon_income_per_bond = N + 30 - purchase_day
        redemption_profit_per_bond = 1000 - price_per_bond
        profit_per_bond = coupon_income_per_bond + redemption_profit_per_bond
        profit_lot = int(round(quantity * profit_per_bond))
        lot = {
            'day': day,
            'name': name,
            'price_percent': price_percent,
            'quantity': quantity,
            'cost': cost_lot,
            'profit': profit_lot,
            'index': len(lots),
            'line': line.strip()
        }
        lots.append(lot)

    dp = {0: (0, set())}  # прибыль: (стоимость, набор индексов лотов)

    for lot in lots:
        profit_lot = lot['profit']
        cost_lot = lot['cost']
        new_dp = dp.copy()
        for p in dp:
            c = dp[p][0]
            lots_used = dp[p][1]
            p_new = p + profit_lot
            c_new = c + cost_lot
            if c_new > S:
                continue
            if p_new not in new_dp or new_dp[p_new][0] > c_new:
                new_dp[p_new] = (c_new, lots_used | {lot['index']})
        dp = new_dp

    # Находим максимальную прибыль в рамках бюджета S
    max_profit = max([p for p in dp if dp[p][0] <= S])
    min_cost, lots_used = dp[max_profit]

    # Выводим результаты
    print(max_profit)
    for idx in sorted(lots_used, key=lambda i: (lots[i]['day'], i)):
        print(lots[idx]['line'])
    print('')

if __name__ == '__main__':
    main()
