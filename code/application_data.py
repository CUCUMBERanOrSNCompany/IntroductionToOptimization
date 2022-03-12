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
    np.random.seed(101)
    factor_change = 1.3
    price = 30
    objective_value_tuples = []

    for i in range(10):
        for j in range(20):
            # the current stock prices
            stock_prices = binomial_model(1, price, factor_change, 0.25, 8)

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
