def fuel_injection_perfection(n: str) -> int:
    steps = 0
    pellets = int(n)

    while pellets > 1:
        if pellets & 1 == 0:
            pellets >>= 1

        else:
            add = (pellets + 1) & ~(pellets + 1 - 1)
            subtract = (pellets - 1) & ~(pellets - 1 - 1)

            if subtract > add or subtract == pellets - 1:
                pellets -= 1
            else:
                pellets += 1
        steps += 1

    return steps
