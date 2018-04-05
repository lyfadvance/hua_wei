import copy
class array:
    def __init__(self,para,fill=0.0):#只支持一维数组
        self.shape=[]
        self._array=[]
        if isinstance(para,int):
            self.shape=para
            self._array=[fill for i in range(para)]
        elif isinstance(para,list):
            self.shape=len(para)
            self._array=para
        elif isinstance(para,array):
            self.shape=para.shape
            for i in range(para.shape):
                self._array.append(para[i])
    def __getitem__(self,index):
        return self._array[index]
    def __setitem__(self,index,value):
        self._array[index]=value
    def __add__(self,N):
        if isinstance(N,int)or isinstance(N,float):
            M=array(self.shape)
            for i in range(self.shape):
                M[i]=self[i]+N
            return M
        elif isinstance(N,array):
            M=array(self.shape)
            for i in range(self.shape):
                M[i]=self[i]+N[i]
            return M
    def __sub__(self,N):
        if isinstance(N,int)or isinstance(N,float):
            M=array(self.shape)
            for i in range(self.shape):
                M[i]=self[i]-N
            return M
        elif isinstance(N,array):
            M=array(self.shape)
            for i in range(self.shape):
                M[i]=self[i]-N[i]
            return M
    def __mul__(self,N):
        if isinstance(N,int)or isinstance(N,float):
            M=array(self.shape)
            for i in range(self.shape):
                M[i]=self[i]*N
            return M
        elif isinstance(N,array):
            M=array(self.shape)
            for i in range(self.shape):
                M[i]=self[i]*N[i]
            return M    
    def __truediv__(self,N):
        if isinstance(N,int)or isinstance(N,float):
            M=array(self.shape)
            for i in range(self.shape):
                M[i]=self[i]/N
            return M
        elif isinstance(N,array):
            M=array(self.shape)
            for i in range(self.shape):
                M[i]=self[i]/N[i]
            return M
    def sum(self):
        total=0
        for i in range(self.shape):
            total+=self[i]
        return total
    def show(self):
        print("[",end='')
        for c in range(self.shape):
            print(self[c],end='  ')
        print("]",end='  ')
        print()
        print()
    def __repr__(self):
        string=''
        string=string+'['
        #print("[",end='')
        for c in range(self.shape):
            string=string+str(self[c])+' '
        string=string+']'
        return string
    def __len__(self):
        return self.shape
class matrix:
    def __init__(self,para,fill=0.0):
        
        self.column=0
        self.row=0
        self.shape=(0,0)
        self._matrix=[]
        if isinstance(para,tuple):
            row,column=para
            self.shape=(row,column)
            self.row=row
            self.column=column
            self._matrix=[[fill]*column for i in range(row)]
        elif isinstance(para,list):
            self.shape[0]=len(list)
            self.shape[1]=len(list[0])
            self.row=list.shape[0]
            slef.column=list.shape[1]
            self._matrix=copy.deepcopy(list)
    def __getitem__(self,index):
        if isinstance(index,int):
            return self._matrix[index-1]
        elif isinstance(index,tuple):
            return self._matrix[index[0]-1][index[1]-1]
    def __setitem__(self,index,value):
        if isinstance(index,int):
            self._matrix[index-1]=copy.deepcopy(value)
        elif isinstance(index,tuple):
            self._matrix[index[0]-1][index[1]-1]=value
    def __eq__(self,N):
        #assert isinstance(N,matrix)
        return N.shape==self.shape
    def __add__(self,N):
        #assert N.shape==self.shape
        M=matrix((self.row,self.column))
        for r in range(self.row):
            for c in range(self.column):
                R[r+1,c+1]=self[r+1,c+1]+N[r+1,c+1]
        return M
    def __sub__(self,N):
        assert N.shape==self.shape,"维度不匹配,不能相减"
        M=matrix((self.row,self.column))
        for r in range(self.row):
            for c in range(self.column):
                M[r+1,c+1]=self[r+1,c+1]-N[r+1,c+1]
        return M
    def __mul__(self,N):
        if isinstance(N,int) or isinstance(N,float):
            M=matrix((self.row,self.column))
            for r in range(self.row):
                for c in range(self.column):
                    M[r+1,c+1]=self[r+1,c+1]*N
        else:
            assert N.row==self.column,"维度不匹配，不能相乘"
            M=matrix((self.row,N.column))
            for r in range(self.row):
                for c in range(N.column):
                    sum=0
                    #print(r,c)
                    for k in range(self.column):
                        #print(r,c,k)
                        sum += self[r+1,k+1]*N[k+1,c+1]
                        M[r+1,c+1]=sum
        return M
    def __truediv__(self,N):
        pass
    def __pow__(self,k):
        assert self.row==self.column,"不是方阵，不能乘方"
        M=copy.deepcopy(self)
        for i in range(k):
            M=M*self
        return M
    def rank(self):
        pass
    def trace(self):
        pass
    def adjoint(self):
        pass
    def invert(self):
        pass
    def jieti(self):
        pass
    def transpose(self):
        M=matrix((sel.column,self.row))
        for r in range(self.column):
            for c in range(self.row):
                M[r+1,c+1]=self[c+1,r+1]
        return M*self
    def cofactor(self,row,column):
        pass
    def show(self):
        for r in range(self.row):
            for c in range(self.column):
                print(self[r+1,c+1],end='  ')
            print()
        print()
if __name__=='__main__':
    m=matrix((3,3),fill=2.0)
    m.show()
    n=matrix((3,3),fill=3.5)
    m[1]=[1,2,3]
    m[2]=[1,2,1]
    m[3]=[2,1,1]
    print(m[1,1])
    print(m[3,3])
    p=m*n
    q=m*2
    
    n.show()
    
    p.show()
    q.show()
    
    x=array([1,3,4])
    x.show()
    x0=x[0]
    print(x0)
    y=x+4
    y.show()
    y0=y[0]
    print(y0)
    m=array(y)
    m.show()
    n=m/2
    n.show()
    n[2]=4
    n.show()
    print(n)
    print(len(n))
    a,b,c=n
    print(a,b,c)