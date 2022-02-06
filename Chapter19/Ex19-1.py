
known = {}
def binomial_coeff_memoized(n, k):
    """Uses recursion to compute the binomial coefficient "n choose k", sped up by memoization
    n: number of trials
    k: number of successes
    returns: int
    """    
    if k == 0:
        return 1
    if n == 0:
        return 0
    if (n, k) in known:
        return known[n, k]
    result = binomial_coeff_memoized(n-1, k) + binomial_coeff_memoized(n-1, k-1)
    known[(n, k)] = result
    return result

def binomial_coeff_nested_conditionals(n, k):
    """Original rewritten using nested conditional expressions.
    """
    return 1 if k==0 else 0 if n == 0 else (binomial_coeff_nested_conditionals(n-1, k) + binomial_coeff_nested_conditionals(n-1, k-1))


def binomial_coeff_recursive(n, k): #This is the author's original version
    """Uses recursion to compute the binomial coefficient "n choose k"
    n: number of trials
    k: number of successes
    returns: int
    """
    if k == 0:
        return 1
    if n == 0:
        return 0
    res = binomial_coeff_recursive(n-1, k) + binomial_coeff_recursive(n-1, k-1)
    return res


n = 150
k = 4
t = binomial_coeff_nested_conditionals(n, k)
print(t)
t = binomial_coeff_recursive(n, k)
print(t)
t = binomial_coeff_memoized(n, k)
print(t)
