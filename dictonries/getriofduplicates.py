students = [
{'id': 1, 'name': 'Sowmya', 'class': '10A', 'subject': 'Math'},
{'id': 2, 'name': 'Ravi', 'class': '10A', 'subject': 'Science'},
{'id': 3, 'name': 'Sowmya', 'class': '10A', 'subject': 'Math'},
{'id': 4, 'name': 'Pinky', 'class': '10B', 'subject': 'English'},
{'id': 5, 'name': 'Ravi', 'class': '10A', 'subject': 'Science'}
]
unique_students = []
seen = set()
for s in students:
 record = tuple(s.items())
 if record not in seen:
  seen.add(record)
  unique_students.append(s)
print("Unique student records:")
for u in unique_students:
 print(u)