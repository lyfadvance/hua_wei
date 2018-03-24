import datetime
import random
import copy
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
#load_data()
def add(a,b):
    return [a[i]+b[i] for i in range(min(len(a),len(b)))]
def div(list1,num):
    return [list1[i]/num for i in range(len(list1))]
def single_box_source_used(single_box):
    obj_vector_len=2
    sum_value=[0 for i in range(obj_vector_len)]
    for i in range(len(single_box)):
        sum_value=add(sum_value,single_box[i])
    return sum_value
def total_source_used(box):
    obj_vector_len=2
    sum_value=[0 for i in range(obj_vector_len)]
    for i in range(len(box)):
        sum_value=add(sum_value,single_box_source_used(box[i]))
    return sum_value
def average_source_used(box):
    return div(total_source_used(box),len(box))
def evaluation(box,box_scale):
    obj_vector_len=2
    average=average_source_used(box)
    pingfangcha=0
    vectorcha=0
    #junzhicha=0
    for i in range(len(box)):
        singlebox=box[i]
        single=single_box_source_used(singlebox)
        pingfangcha+=(single[0]-average[0])*(single[0]-average[0])/(box_scale[0]*box_scale[0])+(single[1]-average[1])*(single[1]-average[1])/(box_scale[1]*box_scale[1])
        vectorcha+=((single[0]/box_scale[0])-(single[1]/box_scale[1]))*((single[0]/box_scale[0])-(single[1]/box_scale[1]))
    ##此时得到平方差总和,向量差总和,平方差尽量大,向量差尽量小
    pingfangcha=pingfangcha/len(box)
    vectorcha=vectorcha/len(box)
    gamma=0.0
    return pingfangcha-gamma*vectorcha
        
def is_box_sufficient(box,obj,box_scale):
    sum_value=[0 for i in range(len(obj))]
    for i in range(len(box)):
        sum_value=add(sum_value,box[i])
    sum_value=add(sum_value,obj)
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
    '''
    print("初始解是:")
    for i in range(len(box)):
        print(box[i])
    print("")
    '''
    return box
def move(box,i,j,j_m,box_scale):#将第j个箱子中的j_m个物体移到第i个箱子中
    new_box=copy.deepcopy(box)
    if is_box_sufficient(new_box[i],new_box[j][j_m],box_scale):
        new_box[i].append(new_box[j][j_m])
        new_box[j].pop(j_m)
        return True,new_box
    else:
        return False,[]
def search_neighbor(box,box_scale):
    #当前解的好坏
    current_eval=evaluation(box,box_scale)
    #找到箱子中平均高度最低的箱子
    best_eval=current_eval
    box_length=len(box)
    lowest_box=0
    lowest_average=1
    for i in range(box_length):
        sum_vector=single_box_source_used(box[i])
        average=(sum_vector[0]/box_scale[0]+sum_vector[1]/box_scale[1])/2
        if average!=0 and average<lowest_average:
            lowest_box=i
            lowest_average=average
    #找到了装载率最小的箱子
    #找到局部最好的解
    for i in range(box_length):
        if i!=lowest_box:
            sufficient,temp_box=move(box,i,lowest_box,0,box_scale)
            if sufficient:
                temp_eval=evaluation(temp_box,box_scale)
                if(temp_eval>best_eval):
                    best_eval=temp_eval
                    best_box=temp_box#此处可以直接赋值，不用深拷贝
    if best_eval==current_eval:#说明当前解已经是最好解
        return True,box
    else:
        return False,best_box
def main(obj_sequence,box_scale):
    best_box_sum=10000000
    for i in range (10):
        #产生随机解
        box=random_solution(obj_sequence,box_scale)
        stop,new_box=search_neighbor(box,box_scale)
        while(not stop):
            stop,new_box=search_neighbor(new_box,box_scale)
        box_sum=0
        print("main最终解是:")
        for i in range(len(new_box)):
            if len(new_box[i])!=0:
                #print(new_box[i])
                box_sum+=1
        print("共用",box_sum,"个箱子")
        if box_sum<best_box_sum:
            best_box_sum=box_sum
    print(best_box_sum)
def first_fit(obj_sequence,box_scale):
    box=[[]]
    box_max_index=0
    for i in range(len(obj_sequence)):
        if is_box_sufficient(box[box_max_index],obj_sequence[i],box_scale):
            box[box_max_index].append(obj_sequence[i])
        else:
            box.append([])
            box_max_index+=1
            box[box_max_index].append(obj_sequence[i])
    print("first_fit最终解是:")
    box_sum=0
    for i in range(len(box)):
        if len(box[i])!=0:
            print(box[i])   
            box_sum+=1
    print("共用",box_sum,"个箱子")
def random_first_fit(obj_sequence,box_scale):
    box=[[]]
    box_max_index=0
    length=len(obj_sequence)
    obj_index_list=[ i for i in range(length)]
    random.shuffle(obj_index_list)
    for i in range(len(obj_index_list)):
        temp=obj_index_list[i]
        for j in range(box_max_index):
            if is_box_sufficient(box[j],obj_sequence[temp],box_scale):
                box[j].append(obj_sequence[temp])
                break
        else:
            box.append([])
            box_max_index+=1
            box[box_max_index].append(obj_sequence[temp])
    print("opt_first_fit最终解是:")
    box_sum=0
    for i in range(len(box)):
        if len(box[i])!=0:
            #print(box[i])   
            box_sum+=1
    print("共用",box_sum,"个箱子")   
def opt_first_fit(obj_sequence,box_scale):
    for i in range(20):
        random_first_fit(obj_sequence,box_scale)
#随机生成物体向量集合,和箱子容量
obj_sequence=[[random.randint(0,9),random.randint(0,9)] for i in range(100)]
#obj_sequence=[[4, 9], [0, 4], [2, 3], [4, 9], [5, 9], [6, 5], [0, 8], [0, 7], [6, 5], [7, 2], [0, 8], [6, 9], [3, 2], [8, 1], [0, 4], [2, 8], [6, 3], [6, 8], [8, 2], [0, 1]]
print("物体向量序列",obj_sequence)
print("")
box_scale=[20,20]
#random_solution([[1,2],[3,2],[2,1]],[3,3])
#random_solution(obj_sequence,box_scale)
first_fit(obj_sequence,box_scale)       
print("")
main(obj_sequence,box_scale)
print("")
opt_first_fit(obj_sequence,box_scale)