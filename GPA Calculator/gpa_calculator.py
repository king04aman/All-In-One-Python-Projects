class GPACalculator:
    def __init__(self, number_of_courses):
        self.is_valid_grade = True
        self.course_grades = []
        self.number_of_courses = number_of_courses
        self.if_invalid_grade = ""
    
    def grade_validator(self):
        for i in range(self.number_of_courses):
            x, y = input(f"Course {i+1} grade: "), int(input(f"Credits for course {i+1}: "))
            self.course_grades.append((x.upper(), y))
            print()
        for x in self.course_grades:
            if x[0].upper() not in GRADE_TO_GP:
                self.if_invalid_grade = f"{x[0].upper()} is not a valid grade!"
                self.is_valid_grade = False
                return self.is_valid_grade
        return self.is_valid_grade

    def overall_gpa_using_previous(self):
        if self.grade_validator():
            current_gpa = float(input("Current overall GPA: "))
            print()
            credits_completed_till_now = int(input("Total credits completed till now: "))
            print()
            current_sem_product = 0
            total_credits = 0
            for grade, credits in self.course_grades:
                current_sem_product += credits*GRADE_TO_GP[grade]
                total_credits += credits
            return f"Expected Overall GPA after the current semester: {round((current_sem_product + (current_gpa * credits_completed_till_now))/(total_credits + credits_completed_till_now), 2)}"
        else: return self.if_invalid_grade

    def overall_gpa(self):
        if self.grade_validator():
            product = 0
            total_credits = 0
            for i, j in self.course_grades:
                product += j*GRADE_TO_GP[i]
                total_credits += j
            return f"Expected Overall GPA: {round(product/total_credits, 2)}"
        else: return self.if_invalid_grade

if __name__ == "__main__":
    GRADE_TO_GP = {
    "A" : 4,
    "A-" : 3.67,
    "B+" : 3.33,
    "B" : 3,
    "B-" : 2.67,
    "C+" : 2.33,
    "C" : 2,
    "F" : 0
}

    while True:
        choice = input("\n*** GPA Calculator ***\n\n1. Calcualte expected GPA after the current semester\n2. Calculate the GPA using each course's grade\n3. Press 'q' to quit\n\nYour choice number: ")
        print()
        try:
            if choice == "1":
                number_of_courses = int(input("Number of courses taken in the current semester: "))
                new_gpa = GPACalculator(number_of_courses)
                print(new_gpa.overall_gpa_using_previous())
            elif choice == "2":
                number_of_courses = int(input("Number of courses taken: "))
                new_gpa = GPACalculator(number_of_courses)
                print(new_gpa.overall_gpa())
            elif choice.lower() == "q" or choice == "3":
                print("Goodbye!")
                x = input("Press enter to exit...\n")
                break
            else:
                print("Enter a valid choice number!")
                continue
        except Exception as e:
            print("\nInvalid input!")