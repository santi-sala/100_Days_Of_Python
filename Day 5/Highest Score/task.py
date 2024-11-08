student_scores = [150, 142, 185, 120, 171,
                  184, 149, 24, 59, 68,
                  199, 78, 65, 89, 86,
                  55, 91, 64, 89]
print(range(1, 10))

print(str(len(student_scores)))
print(str(sum(student_scores)))

biggest_score= 0
for score in student_scores:
    if score > biggest_score:
        biggest_score = score

print(f"Biggest score is: {biggest_score}.")
print(f"Max is: {max(student_scores)}")