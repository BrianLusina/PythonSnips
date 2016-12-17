greek_alphabet = (
'alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu', 'nu', 'xi',
'omicron', 'pi', 'rho', 'sigma', 'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega')
import itertools


def greek_comparator(lhs, rhs):
    m = list(sorted(greek_alphabet))  # m.index(lhs) - m.index(rhs)
    product = list(itertools.product(m))
    return product


print greek_comparator('alpha', 'beta')  # < 0, "result should be negative"
print greek_comparator('chi', 'chi')
print greek_comparator('upsilon', 'rho')

m = list(sorted(greek_alphabet))
for element in itertools.product(m):
    print element
