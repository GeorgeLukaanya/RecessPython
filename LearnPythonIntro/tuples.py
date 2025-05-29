def class_statistics(*scores):
    minimum = min(scores)
    maximum = max(scores)
    average = sum(scores) / len(scores)
    return minimum, maximum, average

min_score, max_score, avg_score = class_statistics(87, 73, 91, 65, 80)

print("Minimum:", min_score)
print("Maximum:", max_score)
print("Average:", avg_score)
