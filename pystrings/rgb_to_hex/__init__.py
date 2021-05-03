def rgb_to_hex(r: int, g: int, b: int) -> str:
    rounder = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(rounder(r), rounder(g), rounder(b))
