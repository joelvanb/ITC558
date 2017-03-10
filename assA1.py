
# coding: utf-8

# In[1]:

# ==========================================================================
# Write a program in Python that will ask a lecturer to enter a student's
# marks for Assignment 1, Assignment 2 and the Final Exam, one by one.
# The Weights of each are as follows:
#                                     Assignment 1: 20%
#                                     Assignment 2: 30%
#                                     Final Exam  : 50%
#The program is to display the:
#                              weighted mark of each individual assignment
#                              total weighted mark of the assignment
#                              weighted mark for the Final Exam
#                              total weighted mark of the subject
# ===========================================================================

print("---------------------------------------------------------")
print("The Innovation University of Australia (IUA) Grade System")
print("---------------------------------------------------------")
print("")
print("Please enter all makrs out of 100")
assignment_1 = float(input('Please enter the marks for Assignment 1: ')) # Presents a input box for user to enter A1 Marks
assignment_2 = float(input('Please enter the marks for Assignment 2: ')) # Presents a input box for user to enter A2 Marks
final_exam = float(input('Please enter the marks for Final Exam: '))   # Presents a input box for user to enter Exam marks

weighted_assignment_1 = assignment_1 * 0.2 # Converts the mark to a weighted score based on 20%
weighted_assignment_2 = assignment_2 * 0.3 # Converts the mark to a weighted score based on 30%
weighted_final_exam = final_exam * 0.5     # Converts the mark to a weighted score based on 50%
total_assignments = weighted_assignment_1 + weighted_assignment_2   # Adds assignment 1 & 2's weighted score together

#===================================================================================================
#Displays and calculates  values for the following:
                                                    # weighted mark of each individual assignment
                                                    # total weighted mark of the assignment
                                                    # weighted mark for the Final Exam
                                                    # total weighted mark of the subject
#===================================================================================================

print("")
print("Thank You!")
print("")
print("Weighted mark for Assignment 1:         ", format(weighted_assignment_1, '.0f'))
print("Weighted mark for Assignment 2:         ", format(weighted_assignment_2, '.0f'))
print("Total weighted mark of the assignments: ", format(total_assignments, '.0f'))
print("")
print("Weighed mark for the Final Exam is:        ", format(weighted_final_exam, '.0f'))
print("Total weighted mark for the subject:       ", format(weighted_assignment_1+weighted_assignment_2+                                                             weighted_final_exam, '.0f'))
print("")
print("Goodbye")




# In[ ]:




