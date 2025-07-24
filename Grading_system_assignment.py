def get_grade_and_remark(score):
    if score >= 70:
        return 'A', 'Excellent'
    elif score >= 60:
        return 'B', 'Very Good'
    elif score >= 50:
        return 'C', 'Good'
    elif score >= 45:
        return 'D', 'Fair'
    elif score >= 40:
        return 'E', 'Pass'
    else:
        return 'F', 'Fail'

def main():
    print("=== Natural Grading System ===\n")

    name = input("Enter student name: ")
    try:
        score = float(input("Enter student score: "))
        grade, remark = get_grade_and_remark(score)

        print("\n--- Result ---")
        print(f"Name   : {name}")
        print(f"Score  : {score}")
        print(f"Grade  : {grade}")
        print(f"Remark : {remark}")
    except ValueError:
        print("❌ Invalid input! Please enter a number for the score.")

    print("\n===============================")
    print("  © 2025 OBI STEPHANIE NMACHUKWU")
    print("===============================")

if __name__ == "__main__":
    main()