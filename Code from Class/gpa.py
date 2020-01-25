'''
    CS5001
    Spring 2020
    Source code from class - the GPA function
'''

def calculate_gpa(current_gpa, num_class, current_grade):
    ''' Function: current_gpa
        Parameters: current_gpa (float), num_class (int),
                    and current_grade (float)
        Returns: uupdated_gpa (float)
    '''
    updated_gpa = current_gpa * num_class + current_grade
    updated_gpa = updated_gpa / (num_class + 1)
    return updated_gpa
