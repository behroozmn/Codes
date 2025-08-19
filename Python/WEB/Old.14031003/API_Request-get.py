import requests

res1 = requests.get("https://barnamenevisan.info/api/courses/getactivecourses")
res2 = requests.get("https://jsonplaceholder.typicode.com/comments", params={'postId': 2})

# 1)
print(f"[res1.status_code]: {res1.status_code}\n\n")

# 2)
print(f"[res1.text]:{res1.text}\n\n")  # string

# 3)
for course in res1.json():
    print(f"Curse:{course['title']} Teacher: {course['teacher']}")

# 4)
print(f"[res2.json()]: {res2.json()}")
