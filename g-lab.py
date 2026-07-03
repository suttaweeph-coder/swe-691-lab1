def calculate_grade(scores):
    # 1. เช็คกรณีลิสต์ว่าง เพื่อป้องกัน ZeroDivisionError
    if not scores:
        return "No Grade", 0  # หรือ return None, 0 ตามความเหมาะสม

    # 2. ใช้ฟังก์ชัน sum() เพื่อความรวดเร็วและลดโอกาสเขียนผิด (Pythonic Way)
    total = sum(scores)
    average = total / len(scores)
    
    # 3. การเช็คเกรด (ตรรกะเดิมถูกต้องแล้ว แต่เขียนให้กระชับได้)
    if average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"
        
    return grade, average

# ทดสอบกรณีมีคะแนน
scores = [85, 92, 78, 88, 95]
grade, avg = calculate_grade(scores)
print(f"Average: {avg}, Grade: {grade}")

# ทดสอบกรณีลิสต์ว่าง (ป้องกัน Bug)
empty_scores = []
print(f"Empty case: {calculate_grade(empty_scores)}")
