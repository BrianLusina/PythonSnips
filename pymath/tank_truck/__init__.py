from math import sqrt, pi, acos, floor


def tankvol(h, d, vt):
    radius = d / 2
    cylinder_height = vt / (pi * (radius ** 2))
    triangle_height = radius - h
    theta = acos(triangle_height / radius)

    # or base = radius * sin(theta)
    base = sqrt((radius ** 2) - (triangle_height ** 2))

    triangle_area = (base * triangle_height) / 2
    sector_area = (radius * radius * theta) / 2

    remainder_area = (sector_area - triangle_area) * 2
    return floor(cylinder_height * remainder_area)
