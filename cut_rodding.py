import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 

def rod_cutting_BF(length, price_list, count):
    if length <= 0:
        return 0, 1
    
    max_revenue = 0
    for i in range(length):
        value, count_aux = rod_cutting_BF(length - i - 1, price_list, 0)
        max_revenue = max(max_revenue, price_list[i] + value)
        count += count_aux + 1
    return max_revenue, count


def rod_cutting_top_down(length, price_list):
    memo = [-1 for i in range(length + 1)]
    
    def rod_cutting_aux(length, count):
        if length <= 0:
            return 0, 1
        if memo[length] != -1:
            return memo[length], 1
        
        max_revenue = 0
        for i in range(length):
            value, count_aux = rod_cutting_aux(length - i - 1, count)
            max_revenue = max(max_revenue, price_list[i] + value)
            count += count_aux + 1

        memo[length] = max_revenue
        return max_revenue, count
    
    return rod_cutting_aux(length, 0)

def rod_cutting_greedy(length, price):
    count = 0
    price = [price[i]/(i + 1) for i in range(length)]
    price_sorted = np.argsort(price)
    price_sorted = price_sorted[::-1]

    total_cuts = 0
    max_price = 0
    while total_cuts < length:
        for i in range(length):
            count += 1
            if total_cuts + price_sorted[i] + 1 <= length:
                max_price += price_list[price_sorted[i]]
                total_cuts += price_sorted[i] + 1
                break
    return max_price, count

if __name__ == "__main__":
    
    length = 100
    counts_bf, counts_dp, counts_greedy = [], [], []
    values_bf, values_dp, values_greedy = [], [], []
    for i in range(1, 20):
        price_list = np.random.choice(range(1000), length, replace=False)
        price_list = np.sort(price_list)
        value, count = rod_cutting_BF(length=i, price_list=price_list, count=0)
        value2, count2 = rod_cutting_greedy(length=i, price=price_list)
        value3, count3 = rod_cutting_top_down(length=i, price_list=price_list)

        values_bf.append(value), values_dp.append(value2), values_greedy.append(value3)
        #counts_dp.append(count3), counts_greedy.append(count2)
    
    x = [i for i in range(1, 20)]
    sns.lineplot(x=x, y=values_bf)
    sns.lineplot(x=x, y=values_dp)
    sns.lineplot(x=x, y=values_greedy)
    plt.plot()
    plt.ylabel("Resultado")
    plt.xlabel("Tamanho da entrada")
    plt.savefig("2.png")    
    