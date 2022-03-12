import sys
import numpy as np
import matplotlib.pyplot as plt
import pwst_util as util 
from sample_user_rank import Sample_User
import application_data

alpha_plot_lines = []
error_plot_lines = []

def pareto_weighted_sum_tuning(all_tuples, alpha_vector, tolerance_vector, batch_size, iteration_limit):
    """
    Runs Pareto-Weighted-Sum-Tuning on a simulated sample user/decision-maker
    Returns criteria weights
    """
    f = open("svm_rank/user_queries_train.dat", "w")
    f.close()
    #create random user
    user_profile = Sample_User(alpha_vector, tolerance_vector)

    all_alphaes_leaned = []
    #the result
    result_mean_alpha = [] 

    #get batch of all_tuples.batch size=batch_size=setting
    #return all_tuples as list and one_batch=one batch
    data_subset = util.get_data_subset(all_tuples, batch_size)
    #one batch
    one_batch = data_subset[1]

    iteration_number = 0
    ##til 15 itration.while there is stocks:
    while iteration_number < iteration_limit and len(all_tuples) != 0:
        iteration_number += 1
        #leran vecor of constraint.the "user" rank each tuple
        #svm ranking
        one_alpha_learned = util.user_feedback(one_batch, user_profile, iteration_number)
        #the rest of objective_value_pairs that isnt in the batch
        objective_value_pairs = [x for x in all_tuples if x not in one_batch]
        #get a new batch(without the pair in the last batch)
        data_subset = util.get_data_subset(objective_value_pairs, batch_size)
        one_batch = data_subset[1]
        
        all_alphaes_leaned.append(one_alpha_learned)

        mean_alpha_learned = util.average_vectors(all_alphaes_leaned)


        result_mean_alpha.append(mean_alpha_learned)
        # create a new user after learning user preference
        user_1 = Sample_User(mean_alpha_learned, [0 for i in range(len(mean_alpha_learned))])
        #the user rank again another batch,based on the alpha lreand
        for example in one_batch:
            user_1.user_decision(example) 

        del user_1
        user_profile.clear_user_history()
    
    alpha_plot_lines.append(result_mean_alpha)


    return result_mean_alpha[-1]