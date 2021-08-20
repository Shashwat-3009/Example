#file_obj=open("shashwat.txt","w")
# file_obj.write(" Welcome to my file")
# file_obj.close()

# with open("shashwat.txt","a") as file_obj:
#     file_obj.write("this is the new added line")

# filename=input("Enter File name:")
# if filename.strip().endswith(".txt"):
#     pass
# else :
#     filename=filename+".txt"
#     filename=filename.strip()
# writing_mode=input("Enter Mode of Input:")
# writing_mode=writing_mode.strip()
# writing_mode= writing_mode.lower()
# data=input('Enter Your Data :')
# with open(filename,writing_mode) as file_obj:
#     file_obj.write(data)
# with open("shashwat.txt","r") as file_obj:
#     file_content=file_obj.readlines()
#     print(file_content)
#     file_content_2=[i.strip('\n') for i in file_content]
#     print(file_content_2)
#     # file_content1=file_obj.readline()
#     # print(file_content1)
# with open("shashwat.txt","r") as file_obj:
#     file_content=file_obj.readlines()
#     new_content= [i.strip('\n') for i  in file_content]

#------------------------ Date time format----------------------------
# from datetime import datetime
# current_time=datetime.now()
# time_format='%Y_%m_%d_%H_%M_%S'
# final=datetime.strftime(current_time,time_format)
# print(final)

#------------------------ To put code delay --------------------------
# import time
# time.sleep(2)

#-------------------------- TAsk 1-----------------------------------------
# from datetime import datetime,time
# current_time = datetime.now()
# time_format = '%Y_%m_%d_%H_%M_%S'
# new_format = datetime.strftime(current_time, time_format)
# with open("shashwat.txt","r") as file_object:
#     file_content=file_object.readlines()
#     new_content=[x.strip('\n') for x in file_content]
#     print(new_content)
# for i in new_content:
#     file_name = i.strip() + "_" + new_format + ".txt"
#     time.sleep(2)
#     with open(file_name, "w") as new_file:
#         new_file.write("hello Everyone")

#------------------------------------------ REGULAR EXPRESSIONS --------------------------------------------------------
# import re
# my_data="dhoni is greater than kohli"
# my_output=re.match("dhoni",my_data)
# print(my_output.group())
# print(my_output.span())



# import re
# my_data="dhoni is greater than kohli"
# my_output=re.search("is",my_data)
# print(my_output.group())
# print(my_output.span())


# import re
# my_data="<html><head><body>" # greedy Statement
# my_output=re.match("<.*>",my_data,re.I)
# print(my_output.group())
# print(my_output.span())



# import re
# my_data="<html><head><body>" # Non greedy Statement
# my_output=re.match("<.*?>",my_data,re.I)
# print(my_output.group())
# print(my_output.span())


# import re
# my_data="india is better than australia"
# my_output=re.search("(.*) is (.*?)",my_data)
# print(my_output.group())
# print(my_output.group(1))
# print(my_output.group(2))

# import re
my_data ="!!! India won with 49 balls remaining 454443 against SRILANKA on 2019 with 330 on score"
# my_output=re.findall("\D{1,3}",my_data)
# print(my_output)

# import re
# my_data ="!!! India won with 49 balls remaining 454443 against SRILANKA on 2019 with 330 on score"
# my_output=re.findall("\w",my_data)
# print(my_output)
#
# import re
# my_data ="!!! India won with 49 balls remaining 454443 against SRILANKA on 2019 with 330 on score"
# my_output=re.findall("\w*",my_data)
# print(my_output)
#
# import re
# my_data ="!!! India won with 49 balls remaining 454443 against SRILANKA on 2019 with 330 on score"
# my_output=re.findall("\w+",my_data)
# print(my_output)

# import re
# my_data ="!!! India won with 49 balls remaining 454443 against SRILANKA on 2019 with 330 on score"
# my_output=re.sub("\W","_",my_data)
# print(my_output)

#----------------------------------------------------------GENERATORS---------------------------------
# def fun():
#     var=10
#     yield var
#     var=var+10
#     yield var
#     var=var+10
#     yield var
# f=fun()
# print(next(f))
# print(next(f))
# print(next(f))

#--------------------------------CSV MODULE---------------------------------

# import csv
# filename='dhoni.csv'
# fields=[]
# rows=[]
# with open (filename,'r')  as csvfile:
#     #creating csvreader object
#     csvreader=csv.reader(csvfile)
#
#     #extracting field names thorugh first row
#     fileds=next(csvreader)
#
#     #extracting each data row one by one
#     for row in csvreader:
#         rows.append(row)
#
#     #get total number of rows
#     print("Total Number of rows : %d"%(csvreader.line_num))
#
# #printing the field names
# print('Field Names are :'+",'".join(field for field in fields))
#
# #printing first 5 rows
# print('\nFirst 5 rows are : \n')
# for row in rows[:5]:
#     # parsing each column of a row
#     for col in row:
#         print("%22s"%col)
#         print('\n')

#-----------------------------------------------------
#importing csv module
# import csv
#
# # my data rows a s dictionary objects
# mydict=[{'branch': 'COE','cgpa':'9.0','name':'Nikhil','year':'2'},
#         {'branch': 'COE','cgpa':'9.0','name':'Ravi','year':'2'},
#         {'branch': 'IT','cgpa':'9.0','name':'Sanket','year':'2'},
#         {'branch': 'SE','cgpa':'9.0','name':'mukesh','year':'2'},
#         {'branch': 'MCE','cgpa':'9.0','name':'rupesh','year':'2'}]
# fields=['name','branch','year','cgpa']
#
# filename="university_records.csv"
#
# with open ( filename,'w') as csvfile:
#     writer=csv.DictWriter(csvfile, fieldnames=fields)
#     writer.writeheader()
#     writer.writerows(mydict)