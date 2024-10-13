scores = [77, 69, 88, 91, 85, 77, 80, 74, 83, 93, 69, 77, 80, 85, 77]
S = set(scores)
for score in S:
    count = 0
    for x in scores:
        if score == x:
            count += 1
    print("{}점 : {}명".format(score, count))
