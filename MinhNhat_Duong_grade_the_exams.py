# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#filename = input("Enter a filename: ")
#if filename == "class1":
        # open class1.txt
        #file = open(filename+".txt","r")
        #content=file.readlines()
        #print(content)
#elif filename == "class2":
        # open class2.txt
        #file = open(filename+".txt","r")
        #content=file.readlines()
        #print(content)
#else:
        #print ("Sorry, I can't find this filename")
        
import pandas as pd
import numpy as np

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            print(f"\nSuccessfully opened {file_path}")
            print('\n**** ANALYZING ****\n')
            return file.readlines()
    except FileNotFoundError:
        print("\nFile cannot be found.")
        return None
def analyze_data(lines):
    dong_hop_le = []
    dong_khong_hop_le = 0
    error_lines = []
    has_errors = False

    for line in lines:
        data = line.strip().split(',')
        invalid_reason = None

        if len(data) != 26:
            invalid_reason = "does not contain exactly 26 values"
        elif not data[0].startswith('N'):
            invalid_reason = f"N# is invalid"
        elif len(data[0][1:]) != 8 or not data[0][1:].isdigit():
            invalid_reason = f"N# is invalid"
 
            
        if invalid_reason:
            dong_khong_hop_le += 1
            error_lines.append(f"Invalid line of data: {invalid_reason}:\n{line.strip()}\n")
            print(f"Invalid line of data in file: {invalid_reason}:\n{line.strip()}\n")
            has_errors = True
        else:
            dong_hop_le.append(data) 

    if not has_errors:
        print("No errors found!\n")
    print("**** REPORT ****\n")
    print(f"Total valid lines of data: {len(dong_hop_le)}\n")
    print(f"Total invalid lines of data: {dong_khong_hop_le}\n")
    return dong_hop_le, error_lines
answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D".split(',')
class_name = input("Enter a class name to grade (i.e. class1 for class1.txt): ")
file_path = f"D:\\DAP304\\ASM1\\{class_name}.txt"

lines = read_file(file_path)
print(lines)


def grading(valid_student_list):
 #Biến đổi answer key thành một list cho dễ thao tác
    answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D" 
    answer_list = answer_key.split(",")
 #Khai báo các biến sử dụng trong hàm
    grades = []
    high_score_student = 0
    skip_question = []
    incorrect_question = []

#Vòng lặp qua từng dòng dữ liệu để tính toán điểm cho từng học sinh 
    for i in range(len(valid_student_list)):
        grade = 0
        for j in range(1,len(valid_student_list[i])):
            if valid_student_list[i][j] == answer_list [j-1]:
               grade += 4
            elif valid_student_list[i][j] == "":
               grade += 0
               skip_question.append(j)
            else:
               grade -= 1
               incorrect_question.append(j)
        if grade > 80:
            high_score_student += 1
            grades.append(grade)
#Trả về danh sách điểm học sinh, số học sinh điểm cao, các câu được skip và các câu trả lời sai 
    return grades, high_score_student, skip_question, incorrect_question

def generate_grade_file(class_name, diem_tung_sv):
    df = pd.DataFrame(diem_tung_sv, columns=['STT', 'Diem'])
    df.to_csv(f"{class_name}_grades.csv", index=False) 

def grade_student(dong_hop_le, answer_key):
    diem_tung_sv = []
    cau_hoi_bo_qua = [0] * 25
    cau_tra_loi_sai = [0] * 25
    diem_cao = 0

    for data in dong_hop_le:
        diem = 0
        for index, answer in enumerate(data[1:]):
            if answer == "":
                cau_hoi_bo_qua[index] += 1
            elif answer == answer_key[index]:
                diem += 4
            elif answer != answer_key[index]:
                diem -= 1
                cau_tra_loi_sai[index] += 1

        diem_tung_sv.append((data[0], diem))
        if diem > 80:
            diem_cao += 1

    diem_cao_nhat = max(diem_tung_sv, key=lambda x: x[1])[1]
    diem_thap_nhat = min(diem_tung_sv, key=lambda x: x[1])[1]
    khoang_cach = diem_cao_nhat - diem_thap_nhat
    diem_trung_binh = round(np.mean([diem[1] for diem in diem_tung_sv]), 3)
    trung_vi = round(np.median([diem[1] for diem in diem_tung_sv]), 3)

    return (diem_tung_sv, (diem_cao, diem_trung_binh, diem_cao_nhat, diem_thap_nhat, khoang_cach, trung_vi), cau_hoi_bo_qua, cau_tra_loi_sai)
    
def calculate_skipped_and_incorrect(dong_hop_le, answer_key):
    num_students = len(dong_hop_le)
    cau_hoi_bo_qua = [0] * 25
    cau_tra_loi_sai = [0] * 25

    for data in dong_hop_le:
        for index, answer in enumerate(data[1:]):
            correct_answer = answer_key[index]
            if answer == "":
                cau_hoi_bo_qua[index] += 1
            elif answer != correct_answer:
                cau_tra_loi_sai[index] += 1

    ty_le_bo_qua = [skip/num_students for skip in cau_hoi_bo_qua]
    ty_le_cau_sai = [incorrect/num_students for incorrect in cau_tra_loi_sai]

    bo_qua_nhieu_nhat = max(cau_hoi_bo_qua)
    sai_nhieu_nhat = max(cau_tra_loi_sai)

    most_skipped = [(index + 1, skipped, round(rate, 2)) for index, (skipped, rate) in enumerate(zip(cau_hoi_bo_qua, ty_le_bo_qua)) if skipped == bo_qua_nhieu_nhat]
    most_incorrect = [(index + 1, incorrect, round(rate, 2)) for index, (incorrect, rate) in enumerate(zip(cau_tra_loi_sai, ty_le_cau_sai)) if incorrect == sai_nhieu_nhat]

    return most_skipped, most_incorrect

def save_student_details(class_name, diem_tung_sv, directory):
    output_file_path = f"{directory}\\{class_name}_grades.txt"

    with open(output_file_path, "w") as f:
        for data in diem_tung_sv:
            f.write(f"{data[0]}, {data[1]}\n")


lines = read_file(file_path)
print(lines)
if lines:
    dong_hop_le, error_lines = analyze_data(lines)
    if dong_hop_le:
        (diem_tung_sv, stats, cau_hoi_bo_qua, cau_tra_loi_sai) = grade_student(dong_hop_le, answer_key)

        print(f"Total students of high scores: {stats[0]}\n")
        print(f"Mean (average) score: {stats[1]}\n")
        print(f"Highest score: {stats[2]}\n")
        print(f"Lowest score: {stats[3]}\n")
        print(f"Range of scores: {stats[4]}\n")
        print(f"Median score: {stats[5]}\n")

        generate_grade_file(class_name, diem_tung_sv)
        save_student_details(class_name, diem_tung_sv, "D:\\DAP304\\ASM1")

        most_skipped, most_incorrect = calculate_skipped_and_incorrect(dong_hop_le, answer_key)
        print("Question that most people skip:", ', '.join([f"{q[0]} - {q[1]} - {q[2]}" for q in most_skipped]))
        print()
        print("Question that most people answer incorrectly:", ', '.join([f"{q[0]} - {q[1]} - {q[2]}" for q in most_incorrect]))


 


    