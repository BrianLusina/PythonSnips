import re


def extract_hostname(url: str) -> str:
    regex = r'^(?P<scheme>[a-z]+:\/\/)*(?P<www>(www.)*)?(?P<hostname>[a-z\d][a-z\d-]*)?(\.[a-z\d][a-z\d-]*(\/)*[\w]*(\/)*)+?$'
    m = re.match(regex, url)
    return m.group("hostname")
