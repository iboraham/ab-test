from statsmodels.stats.proportion import proportions_ztest
from scipy.stats import ttest_ind


def two_sided_z_test(count, nobs):
    """
    - Null Hypothesis(H0): means are different from two groups — two sided
    - Null Hypothesis(H0): u0 > u1 or u0 < u2 — one sided
    - Use case: Ran a fair AB test, control group got 486 clicks out of 5000 impression vs experiment
    group got 527 clicks out of 5000 impression. Could we say experiment group won the test?
    Given statistical significance as 0.95
    """
    return proportions_ztest(count, nobs, alternative="two-sided")


def two_sided_t_test(control, experiment):
    return ttest_ind(control, experiment)
