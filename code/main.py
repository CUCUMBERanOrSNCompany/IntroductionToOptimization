#%%

import pareto_weighted_sum_tuning as pwst
import matplotlib.pyplot as plt
import application_data

def main():
    #
    #getnare x tuples(array).each tuple contain 2 elmemts:the best profit,the worst loss.
    #each tuple is one stock
    objective_value_tuples = application_data.generate_stock_objective_values()
    #the wieght of every constraint
    alpha = [0.3]
    tolerance = [0.05]

    #batch size
    batch_sizes = [11, 13, 15, 17]
    #epochs
    max_epochs = 15
    
    #for diffrenct batch size:
    for batch in batch_sizes:
        pwst.pareto_weighted_sum_tuning(objective_value_tuples, alpha, tolerance, batch, max_epochs)
    
    #the wieght of every constraint process
    title = "Alpha Progress"
    plt.title(title)
    plt.xlabel("Iteration Number") 
    plt.ylabel("Alpha Value")

    for i in range(len(batch_sizes)):
        alpha_plot_name = "Batch size "+ str(batch_sizes[i])
        plt.plot([i for i in range(max_epochs)], pwst.alpha_plot_lines[i], label=alpha_plot_name)

    plt.legend()
    plt.show()
    plt.clf()
    plt.cla()
    plt.close()

    return pwst.error_plot_lines

if __name__ == "__main__":
    main()
# %%
