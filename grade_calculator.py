subject = input("Which subject?")
if subject in ["Math", "Chinese", "Chemistry", "Physics", "Biology"]:
    mark1 = input("Enter your Term 1 score:")
    parts = mark1.split("/")
    obtained = float(parts[0])
    total = float(parts[1])
    percentage1 = obtained / total * 100
    mark2 = input("Enter your Term 2 score:")
    parts = mark2.split("/")
    obtained = float(parts[0])
    total = float(parts[1])
    percentage2 = obtained / total * 100
    mark3 = input("Enter your Term 3 score:")
    parts = mark3.split("/")
    obtained = float(parts[0])
    total = float(parts[1])
    percentage3 = obtained / total * 100
    mark4 = input("Enter your EOY score:")
    parts = mark4.split("/")
    obtained = float(parts[0])
    total = float(parts[1])
    percentage4 = obtained / total * 100
    overall = (percentage1 * 0.15) + (percentage2 * 0.15) + \
        (percentage3 * 0.15) + (percentage4 * 0.55)
    print(f"Your overall is {overall}%")
elif subject == "Literature":
    mark1 = input("Enter your Term 1 score:")
    parts = mark1.split("/")
    obtained = float(parts[0])
    total = float(parts[1])
    percentage1 = obtained / total * 100
    mark2 = input("Enter your Term 2 score:")
    parts = mark2.split("/")
    obtained = float(parts[0])
    total = float(parts[1])
    percentage2 = obtained / total * 100
    mark3 = input("Enter your Term 3 score:")
    parts = mark3.split("/")
    obtained = float(parts[0])
    total = float(parts[1])
    percentage3 = obtained / total * 100
    mark4 = input("Enter your EOY score:")
    parts = mark4.split("/")
    obtained = float(parts[0])
    total = float(parts[1])
    percentage4 = obtained / total * 100
    overall = (percentage1 * 0.15) + (percentage2 * 0.10) + \
        (percentage3 * 0.15) + (percentage4 * 0.60)
    print(f"Your overall is {overall}%")
elif subject == "ELCT":
    mark1 = input("Enter your Term 1 score:")
    parts = mark1.split("/")
    obtained = float(parts[0])
    total = float(parts[1])
    percentage1 = obtained / total * 100
    mark2 = input("Enter your Term 2 score:")
    parts = mark2.split("/")
    obtained = float(parts[0])
    total = float(parts[1])
    percentage2 = obtained / total * 100
    mark3 = input("Enter your Term 3 score:")
    parts = mark3.split("/")
    obtained = float(parts[0])
    total = float(parts[1])
    percentage3 = obtained / total * 100
    mark4 = input("Enter your RE score:")
    parts = mark4.split("/")
    obtained = float(parts[0])
    total = float(parts[1])
    percentage4 = obtained / total * 100
    mark5 = input("Enter your EOY score:")
    parts = mark5.split("/")
    obtained = float(parts[0])
    total = float(parts[1])
    percentage5 = obtained / total * 100
    overall = (percentage1 * 0.15) + (percentage2 * 0.15) + \
        (percentage3 * 0.15) + (percentage4 * 0.25) + (percentage5 * 0.30)
    print(f"Your overall is {overall}%")


def calculate_percentage(score):
    parts = score.split("/")
    obtained = float(parts[0])
    total = float(parts[1])
    return obtained / total * 100


if year == "Year 1":
    year1_weights = {
        "Chinese": [
            ("Term 1", 0.10),
            ("Term 2", 0.15),
            ("Term 3", 0.15),
            ("EOY Paper 1", 0.30),
            ("EOY Paper 2", 0.30)
        ],
        "History + Geography": [
            ("Geography 1", 0.10),
            ("Geography 2", 0.10),
            ("Geography EOY", 0.30),
            ("History 1", 0.10),
            ("History 2", 0.10),
            ("History EOY", 0.30)
        ]
    }
