def int32_to_ip(int32: int) -> str:
    return f"{int32 >> 24}.{(int32 >> 16) & 0xff}.{(int32 >> 8) & 0xff}.{int32 & 0xff}"
