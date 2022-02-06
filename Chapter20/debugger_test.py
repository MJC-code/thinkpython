
known = {}
def binomial_coeff_memoized(n, k):
    """Uses recursion to compute the binomial coefficient "n choose k", sped up by memoization
    n: number of trials
    k: number of successes
    returns: int
    """
    breakpoint()
    if k == 0:
        return 1
    if n == 0:
        return 0
    if (n, k) in known:
        return known[n, k]
    result = binomial_coeff_memoized(n-1, k) + binomial_coeff_memoized(n-1, k-1)
    known[(n, k)] = result
    return result


n = 150
k = 4

t = binomial_coeff_memoized(n, k)
print(t)
