import datetime
import random
def load_data():
    file=open("traindata.txt")
    initial_date=datetime.datetime(2015,1,1)
    final_date=datetime.datetime(2015,5,31)
    total_date=(final_date-initial_date).days+1
    print("2015年总共有",total_date,"日")
    num1=[0 for i in range(total_date)]
    #print(num1)
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
    #print(num1)
load_data()
def is_box_sufficient(box,obj,box_scale):
    sum_value=[0 for i in range(len(obj))]
    for i in range(len(box)):
        sum_value=sum_value+box[i]
    sum_value=sum_value+obj
    for i in range(len(obj)):
        if sum_value[i]>box_scale[i]:
            return False
    return True
def random_solution(obj_sequence,box_scale):
    box=[[]]
    ##产生一个随机物体
    length=len(obj_sequence)
    obj_index_list=[ i for i in range(length)]
    random.shuffle(obj_index_list)
    for i in range(len(obj_index_list)):
        temp=obj_index_list[i]
        #print(temp)
        if random.randint(0,3)!=0:##产生一个新箱子
            box.append([])
            box[-1].append(obj_sequence[temp])
        else:
            rand_box_index=random.randint(0,len(box)-1)
            if is_box_sufficient(box[rand_box_index],obj_sequence[temp],box_scale):##如果选取的物体放的下随机选取的box,则放置
                box[rand_box_index].append(obj_sequence[temp])
            else:
                new_box=False
                itery=100
                while not is_box_sufficient(box[rand_box_index],obj_sequence[temp],box_scale):
                    if random.randint(0,itery)==0:
                        box.append([])
                        box[-1].append(obj_sequence[temp])
                        new_box=True
                        break
                    else:
                        rand_box_index=random.randint(0,len(box)-1)
                        itery=itery-1
                if not new_box:
                    box[rand_box_index].append(obj_sequence[temp])
    for i in range(len(box)):
        print(box[i])


#随机生成物体向量集合,和箱子容量
obj_sequence=[[random.randint(0,9),random.randint(0,9)] for i in range(20)]
box_scale=[20,20]
#random_solution([[1,2],[3,2],[2,1]],[3,3])
random_solution(obj_sequence,box_scale)
        
