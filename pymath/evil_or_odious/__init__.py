def evil(n):
    return "It's Evil!" if "{0:b}".format(n).count("1") % 2 == 0 else "It's Odious!"
    # return "It's %s!" % ["Evil","Odious"][bin(n).count("1")%2]
