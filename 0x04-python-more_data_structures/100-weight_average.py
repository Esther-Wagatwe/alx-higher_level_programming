#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        total_score = 0
        total_weight = 0
        for score, weight in my_list:
            total_score += weight * score
            total_weight += weight
        return total_score / total_weight
    else:
        return (0)
