#!/usr/bin/env python3

def return_evens(num_list):
    return [num for num in num_list if num % 2 == 0]


    # for num in num_list:
    #     if num % 2 == 0:
    #         num_list = [num for num in num_list]
    #     else:
    #         num_list = []



def make_exclamation(sentence_list):
    return [sentence + "!" for sentence in sentence_list]