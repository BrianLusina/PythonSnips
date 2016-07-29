"""func to find median in a list"""
def median(lst):
    sortList = sorted(lst)
    med = 0
    if len(sortList) == 1:
        med = sortList[0]
    elif len(sortList)%2 == 0:
        fMidIndex = len(sortList)/2
        sMidIndex = fMidIndex - 1
        med = (sortList[fMidIndex] + sortList[sMidIndex]) / 2.0
    elif len(sortList)%2 != 0:
        fMidIndex = (len(sortList)/2)
        med = sortList[fMidIndex]
    return med