import re


def get_users_ids(phrase):
    uid, res = r"uid|\W", []
    return re.sub(uid, "", phrase, 1)

uid, res = r"uid|\W", []
s = "uid12345uid"
if s.startswith("uid"):
    print(s.replace("uid", "", 1))
print(re.sub(uid, "", s, 1))
