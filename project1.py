# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 17:49:28 2022

@author: AAGAM
"""

# project 1: school administration programme
import csv

def write_into_csv(info_list):
    with open('student_info.csv','a',newline='') as csv_file:
        writer = csv.writer(csv_file)


        if csv_file.tell() == 0:     #header line is only one time writen when file is empty otherwise its written in every line
            writer.writerow(["Name", "Div", "Roll_no", "Mail_id"])
            
        writer.writerow(info_list)
if __name__ == '__main__':
    Condition = True
    student_num = 1

    while(Condition):
        student_info = input("enter some student information for student #{} in following format (Name Div Roll_no Mail_id): ".format(student_num))

        #split
        student_info_list = student_info.split(' ')


        print("\nenterd information is:\nName: {}\nDiv: {}\nRoll_no: {}\nMail_id: {}"
              .format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
        
        choice_check=input("is the enterd information is right or not please press(yes/no): ")
        
        if choice_check == "yes":
            write_into_csv(student_info_list)
            condition_check = input("enter (yes/no) if you want to enter informarion for another student: ")
            if condition_check == "yes":
                Condition = True
                student_num = student_num + 1
            elif condition_check == "no":
                Condition = False
        elif choice_check =="no":
            print("\nplease re-enter the value")






