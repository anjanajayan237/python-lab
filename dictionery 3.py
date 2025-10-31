students={
    "anu":[85,95,100],"gowri":[65,68,89],"vishnu":[95,80,85]
}
for name,marks in students.items():
    total = sum(marks)
    average = total / len(marks)
    print(f"student:{name}")
    print(f"marks:{marks}")
    print(f"total marks:{total}")
    print(f"average marks:{average:.2f}")
    print("." * 20)