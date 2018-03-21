import datetime
import random
def load_data():
    file=open("traindata.txt")
    initial_date=datetime.datetime(2015,1,1)
    final_date=datetime.datetime(2015,5,31)
    total_date=(final_date-initial_date).days+1
    print("2015年总共有",total_date,"日")
    num1=[0 for i in range(total_date)]
    print(num1)
    for line in file.readlines():
        line=line.strip()
        #print(line)
        line=line.split('\t')
        virtualName=line[1]
        time=line[2]
        date=time.split(' ')[0].split('-')
        #print(date)
        #print(int(virtualName[6:]))
        if int(virtualName[6:])<=15:
            d2=datetime.datetime(int(date[0]),int(date[1]),int(date[2]))
            num1[(d2-initial_date).days]+=1
        #print(virtualName,date)
    print(num1)
load_data()
def random_solution(obj_sequence,box_scale):
    box=[]
    ##产生一个随机物体
    length=len(obj_sequence)
    obj_index_list=[ i for i in range(length)]
    random.shuffle(obj_index_list)
    for i in range(len(obj_index_list)):
        temp=obj_index_list[i]
        print(temp)
        if random.randint(0,1)==0:##产生一个新箱子
            box.append([])
            box.[-1].append(obj_sequence[temp])
        else:
            



random_solution([i for i in range(10)],[1,2,3])
        
