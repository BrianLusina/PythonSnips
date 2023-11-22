from typing import List


def restore_ip_addresses(s: str) -> List[str]:
    def backtrack(candidate: str, current: List[str], start: int, ips: List[str]):
        if len(current) == 4:
            if start == len(candidate):
                ips.append(".".join(current))
            return
        for i in range(start, min(start + 3, len(candidate))):
            if candidate[start] == '0' and i > start:
                continue
            if 0 <= int(candidate[start:i + 1]) <= 255:
                backtrack(candidate, current + [candidate[start:i + 1]], i + 1, ips)

    ip_addresses = []
    backtrack(s, [], 0, ip_addresses)
    return ip_addresses
