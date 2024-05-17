scores = []
weights = []
num_scores = int(input("Enter the number of test scores: "))

for i in range(num_scores):
    score = float(input(f"Enter score for test {i + 1}: "))
    weight = float(input(f"Enter weight (percentage) for test {i + 1}: "))
    scores.append(score)
    weights.append(weight / 100)

if len(scores) != len(weights):
    raise ValueError("Number of scores and weights must be equal.")

total_weighted_score = 0
total_weights = sum(weights)

score_grade_pairs = zip(scores, weights)
for score, weight in score_grade_pairs:
    total_weighted_score += score * weight

avg = total_weighted_score / total_weights

grade = ""
if avg >= 90:
    grade = "A"
elif avg >= 80:
    grade = "B"
elif avg >= 70:
    grade = "C"
elif avg >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Weighted Average: {avg:.1f}, Grade: {grade}")
