student_heights = ["156", "178", "165", "171", "187", "199"]
combined_heights = 0

for n in range(0, len(student_heights)):
  combined_heights += int(student_heights[n])

print(f"Average height is {int(combined_heights/len(student_heights))}")