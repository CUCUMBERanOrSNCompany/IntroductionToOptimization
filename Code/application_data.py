"""
Courtesy of:
Harry Wang
Name: Pareto-Weighted-Sum-Tuning
Git: https://github.com/harryw1248/Pareto-Weighted-Sum-Tuning
Presented at: The 2020 International Conference on Machine Learning,
Computational Optimization, and Data Science (LOD)
(https://lod2020.icas.xyz/program/).
"""

"""
Used for generating stock model data-set
"""

import numpy as np
import matplotlib.pyplot as plt
import random

# create info on the stock
def binomial_model(N, S0, u, r, K):
    """
    N = number of binomial iterations
    S0 = initial stock price
    u = factor change of upstate
    r = risk free interest rate per annum
    K = strike price
    """
    d = 1 / u

    # make stock price tree
    stock = np.zeros([N + 1, N + 1])
    for i in range(N + 1):
        for j in range(i + 1):
            stock[j, i] = S0 * (u ** (i - j)) * (d ** j)

    return stock

# create data on all the stocks


def generate_stock_objective_values():
    """
    Runs Binomial Pricing Tree Model Several Times to create application data-set
    """
    '''
        Our Stocks Prices:
        AAPL 148.1788976
        AMAZON 3,314.99
        TSLA 807.4015748
        F 15.85
        WYNN 102.5719685
        MGM 42.32
        C 68.92
        JPM 157.1856
        KO 56.14
        MCD 242.26 
        
        LIST COMPILED BY Or SN and accurate to March 12th, 2022.
    '''
    np.random.seed(101)
    factor_change = 1.3
    price = 30
    objective_value_tuples = []
    our_stocks_prices = [148.1788976, 3, 314.99, 807.4015748, 15.85, 102.5719685, 42.32, 68.92, 157.1856, 56.14, 242.26]
    for i in range(10):
        for j in range(20):
            # the current stock prices
            stock_prices = binomial_model(1,our_stocks_prices[i], factor_change, 0.25, 8)

            random_factor = np.random.uniform(0.90, 1.1)
            # the best gain of money for the first col
            best_gain_0 = (stock_prices[0][1] - price) * random_factor
            # the worst loss of money for the first col
            worst_loss_0 = (stock_prices[1][1] - price) * random_factor

            random_factor = np.random.uniform(0.90, 1.1)
            # the best gain of money
            best_gain_1 = (stock_prices[0][1] - price) * random_factor
            random_factor = np.random.uniform(0.90, 1.1)
            # the worst loss of money
            worst_loss_1 = (stock_prices[1][1] - price) * random_factor

            random_factor = np.random.uniform(0.90, 1.1)
            best_gain_2 = (stock_prices[0][1] - price) * random_factor
            random_factor = np.random.uniform(0.90, 1.1)
            worst_loss_2 = (stock_prices[1][1] - price) * random_factor

        # add all of it the the objective_value_tuples
            objective_value_tuples.append(
                (best_gain_0, worst_loss_0))
            objective_value_tuples.append(
                (best_gain_1, worst_loss_1))
            objective_value_tuples.append(
                (best_gain_2, worst_loss_2))

            factor_change += 0.01
        price += 0.05

    return objective_value_tuples
