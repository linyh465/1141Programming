class Course:
    def __init__(self, course_id, day, time, capacity):
        self.course_id = course_id
        self.schedule = (day, time)  # Tuple for time conflict checking
        self.capacity = capacity
        self.students = set()  # Set of student names
    
    def is_full(self):
        """判斷課程是否額滿"""
        return len(self.students) >= self.capacity

class Student:
    def __init__(self, name):
        self.name = name
        self.my_courses = []  # List of Course Objects
    
    def has_time_conflict(self, course):
        """判斷是否與已選課程衝突"""
        for enrolled_course in self.my_courses:
            if enrolled_course.schedule == course.schedule:
                return True
        return False

def register(student_name, course_id):
    """註冊課程"""
    # 創建學生（如果不存在）
    if student_name not in students:
        students[student_name] = Student(student_name)
    
    student = students[student_name]
    course = courses[course_id]
    
    # 1. 檢查課程是否額滿
    if course.is_full():
        return "Full"
    
    # 2. 檢查學生是否有時間衝突
    if student.has_time_conflict(course):
        return "Time Conflict"
    
    # 3. 成功則雙向更新
    student.my_courses.append(course)
    course.students.add(student_name)
    return "Success"

courses = {}
students = {}

n = int(input())
for _ in range(n):
    command = input().split()
    
    if command[0] == "add_course":
        course_id = command[1]
        day = command[2]
        time = int(command[3])
        capacity = int(command[4])
        courses[course_id] = Course(course_id, day, time, capacity)
    
    elif command[0] == "register":
        student_name = command[1]
        course_id = command[2]
        print(register(student_name, course_id))
