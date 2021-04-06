from re import search

receiver = {
    "it": "Roma",
    "design": "Danik",
    "chemistry": "Maxim",
}

letters = {
    "bug": "it",
    "boom": "chemistry",
    "edits": "design"
}


def memesorting(meme):
    full_pattern = r"bug|boom|edits"
    match = search(full_pattern, meme)

    if match:
        group = match.group(0)
        if group == "bug":
            return receiver[letters[group]]
        if group == "boom":
            return receiver[letters[group]]
        if group == "edits":
            return receiver[letters[group]]
    else:
        spelled_word = ""
        words = meme.lower().split(" ")
        for word in words:
            if 'b' in word or 'u' in word or 'g' in word:
                spelled_word += letter

    return receiver.get(letters[spelled_word], "Vlad")


Test.assert_equals(memesorting('This is programmer meme ecause it has bug'), 'Roma')
Test.assert_equals(memesorting('This is also programbur meme gecause it has needed key word'), 'Roma')
Test.assert_equals(memesorting('This is edsigner meme cause it has key word'), 'Danik')
Test.assert_equals(memesorting('This could be chemistry meme but our gey word boom is too late'), 'Roma')
Test.assert_equals(memesorting('This is meme'), 'Vlad')
