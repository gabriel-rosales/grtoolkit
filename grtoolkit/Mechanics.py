import math

def minPulleys(load_weight, pull_weight, Safety_factor, exact=False):
### Pull_weight = load_weight/(2**(n-1)) where load_weight is the heavier load.
    # You can use any base for the exp or log functions. The more used are 2, e and 10.
    # https://www.researchgate.net/post/Why_log_with_base_e_is_frequently_used_as_compared_to_base_10
    if exact:
        return math.log(load_weight/pull_weight)/math.log(2)
    return math.ceil(math.log(load_weight/pull_weight)/math.log(2))

# print(minPulleys(100,10,1, exact=True))
