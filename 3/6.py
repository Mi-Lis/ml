m,d = input().split()
md = {
    '1':"spades",
    '2':"clubs",
    '3':"diamonds",
    '4':"hearts"
}

dd = {
    '6':"six",
    '7':"seven",
    '8':"eight",
    '9':"nine",
    '10':"ten",
    '11':"jack",
    '12':"queen",
    '13':"king",
    '14':"ace"
}

print("the "+ dd[d]+" of "+md[m])