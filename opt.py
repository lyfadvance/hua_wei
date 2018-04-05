from mynumpy import matrix
from mynumpy import array
def min_opt_rmse(func,para,args,bounds=None,maxiter=10000,step=0.0001,approx_grad = True):
    para_num=para.shape
    grad_array=array(para_num)
    iter=0
    for iter in range(maxiter):
        grad_array=grad(func,para,args)
        if iter==0:
            print(grad_array)
        if bounds==None:
            para=para-grad_array*step
        else:
            for i in range(grad_array.shape):
                temp=para[i]-grad_array[i]*step
                if temp>bounds[i][1]:
                    para[i]=bounds[i][1]
                elif temp<bounds[i][0]:
                    para[i]=bounds[i][0]
                else:
                    para[i]=temp
                    
    return para        
def grad(func,para,args):
    epi=0.000001
    para_num=para.shape
    grad_array=array(para_num)
    grad_array[0]=0.44
    #grad_array.show()
    for i in range(para.shape):
    #x0.show()
        #print(i)
        para_for=array(para)
        para_for[i]=para[i]+epi
        para_back=array(para)
        para_back[i]=para[i]-epi
        fx1=func(para_for,*args)
        fx2=func(para_back,*args)
        '''
        fx1.show()
        fx2.show()
        fx3=fx1-fx2
        fx3.show()
        fx4=fx3/(2*epi)
        fx4.show()
        '''
        grad_array[i]=(fx1-fx2)/(2*epi)
    return grad_array
def square(para,*args):
    #x0.show()
    pingfang=(para-2)*(para-2)
    #print((pingfang*args[0]).sum()+4)
    return (pingfang*args[0]).sum()+4
if __name__=='__main__':
    #(grad(square,array([2]),args=(1))).show()
    #(grad(square,array([5]),args=(1))).show()
    para=min_opt_rmse(square,array([1]),(1,2),bounds=[(0,1.5)])
    print(para)