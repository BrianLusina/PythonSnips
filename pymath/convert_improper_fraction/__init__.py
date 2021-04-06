def convert_to_mixed_numeral(parm):
    numerator, denominator = parm.split('/')
    num, dem = int(numerator), int(denominator)
    divide, mod = int(num / dem) or '', int(abs(num) % dem) or 0

    if bool(divide) and bool(mod):
        return "%s %s/%s" % (divide, mod, denominator)
    else:
        return "%s/%s" % (int(mod) if num > 0 else int(-mod), int(denominator)) if bool(mod) else str(divide)
