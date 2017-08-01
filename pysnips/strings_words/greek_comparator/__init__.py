greek_alphabet = ('alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta', 'theta', 'iota', 'kappa', 'lambda',
                  'mu', 'nu', 'xi', 'omicron', 'pi', 'rho', 'sigma', 'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega'
                  )


def greek_comparator(lhs, rhs):
    GREEK_ALPHABET = {alpha: indx for indx, alpha in enumerate(greek_alphabet)}

    return GREEK_ALPHABET[lhs] - GREEK_ALPHABET[rhs]
