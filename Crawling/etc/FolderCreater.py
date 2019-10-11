import os
import time
import datetime

def get_today() :
    now = time.localtime()
    s = "%04d-%02d-%02d" % (now.tm_year,now.tm_mon,now.tm_mday)
    return s

def get_time() :
    now = time.localtime()
    now_time = time.localtime()
    t = "%02d%02d" %(now.tm_hour,now.tm_min)
    return t

def make_folder(folder_name) :
    if not os.path.isdir(folder_name) :
        os.mkdir(folder_name)


root_dir="C:/Users/student/Documents/jinahan/Crawling/etc"
today = get_today()
work_dir = root_dir + "/" + today

make_folder(work_dir)        

root_dir_2 = work_dir
time = get_time()
work_dir_2 = root_dir_2+"/"+time

make_folder(work_dir_2)

# def get_today() :
#     now = time.localtime()
#     s = "%04d-%02d-%02d" % (now.tm_year,now.tm_mon,now.tm_mday)
#     return s

# def make_folder(folder_name) :
#     if not os.path.isdir(folder_name) :
#         os.mkdir(folder_name)


# root_dir="C:/Users/student/Documents/jinahan/Crawling/etc"
# today = get_today()
# work_dir = root_dir + "/" + today

# make_folder(work_dir)

# now = time.localtime()
# s = "%04d-%02d-%02d" % (now.tm_year,now.tm_mon,now.tm_mday)
# print(s)

# try:
#     test_date = datetime.datetime.now()
#     convert_date =str(test_date)
#     #print(convert_date)
#     #now = datetime.datetime.now().text
#     if os.path.isdir('C:/Users/student/Documents/jinahan/Crawling/etc'+convert_date):
#         #os.makedirs('C:/Users/student/Documents/jinahan/Crawling/etc'+convert_date)
#         #except OSError:
#         print('Error: Creating directory')


# #print(test_date)
# #convert_date = datetime.datetime.strptime(test_date,"%Y%m%d").date