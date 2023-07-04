# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 13:40:41 2023

@author: anatl
"""

#################################
# STEP 1
#################################

PATH = "C:/Users/Student/"
fname = PATH + "personal_details.txt"

# fh = open(fname)
# lst = list() 
# for line in fh:
#     lineWords = line.rstrip().split(',')
#     # print(lineWords)
#     person_details_dict = {}
#     person_details_dict["name"] = lineWords[0]
#     person_details_dict["year_born"] = lineWords[1]
#     person_details_dict["address"] = lineWords[2]
#     person_details_dict["city"] = lineWords[3]
#     lst.append(person_details_dict)
    

# print(lst)


#################################
# STEP 2
#################################

def get_person_details(line):
    lineWords = line.rstrip().split(',')
    person_details_dict = {}
    #Approach 1: building the dictionary using a loop
    keys = ["name", "year_born", "address","city"]
    for i in range(len(keys)):
        person_details_dict[keys[i]]=lineWords[i]
    
    # Approach 2: building the dictionary directly
    # person_details_dict["name"] = lineWords[0]
    # person_details_dict["year_born"] = lineWords[1]
    # person_details_dict["address"] = lineWords[2]
    # person_details_dict["city"] = lineWords[3]

    return person_details_dict

# fh = open(fname)
# lst = list()
# for line in fh:
#     lst.append(get_person_details(line))
# print(lst)



#################################
# STEP 3
#################################

def get_person_list(fname):
    fh = open(fname)
    lst = list()
    for line in fh:
        lst.append(get_person_details(line))
    return (lst)

print(get_person_list(fname))


print("**************************************************")

#################################
# STEP 4: יצירת מילון לפי שם 
#################################

def get_person_dictionary(fname):
    
    fh = open(fname)
    d = {}
    for line in fh:
        details = get_person_details(line)
        d[details.get("name") ]= details
    return (d)

print(get_person_dictionary(fname))

print("**************************************************")

#################################
# STEP 5: יצירת רשימה ממוינת לפי גיל 
#################################

def sort_by_age(person_list):
    new_list = []
    for p in person_list:
        cur_year = int(p["year_born"])
        
        flag = False
        if len(new_list)==0:
            new_list.append(p)
        else:
            for ind, e in enumerate(new_list):
                print("e: ", e["year_born"])
                if int(e["year_born"])>cur_year:
                    new_list.insert(ind, p)
                    flag = True
                    break
            if not flag:
                new_list.append(p)
                
    return new_list

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
# print(sort_by_age(get_person_list(fname)))


########################################################
# another approach - using dataframe
########################################################
# import pandas as pd
# lst = get_person_list(fname)
# df = pd.DataFrame(lst)
# print(df)
# df.sort_values(by=['year_born'],inplace=True,ascending=False) #
# print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
# print(df)

lst = get_person_list(fname)
# print(lst)

for i,e in enumerate(lst):
    print(type(i))
