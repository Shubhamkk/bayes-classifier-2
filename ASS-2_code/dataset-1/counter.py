import numpy as nm
import matplotlib.pyplot as plt
import math
from matplotlib import cm
import boundary_region
class inv():
    
    def Matrix_inv(self,C0_Matrix):

        det_matrics=(C0_Matrix[0][0])*(C0_Matrix[1][1]) - (C0_Matrix[0][1])*(C0_Matrix[1][0])
        
        A00=C0_Matrix[0][0]
        A01=C0_Matrix[0][1]
        A10=C0_Matrix[1][0]
        A11=C0_Matrix[1][1]

        C0_Matrix[0][0]=A11/det_matrics
        
        C0_Matrix[1][1]=A00/det_matrics
        
        C0_Matrix[0][1]=(-1)*A01/det_matrics
        
        C0_Matrix[1][0]=(-1)*A10/det_matrics

        return C0_Matrix
    

class Contour(inv):
    def __init__(self):
        pass
    def counter_represent(self):
        print('enter total number of class')
        t=int(input('.............>:'))
        t1=0
        plt.figure(4)
        boundary_region.c_matrics()
        while(1):
            if(t1==t):
                break
            
            
            print('enter the name of class  for counter plot')
            file=input('.......>:')
            fp=open(file+'.txt','r')
            x=[]
            y=[]
            while(1):
                d=fp.readline()
                if(d==''):
                    break
                d1=d.split()
                x.append(float(d1[0]))
                y.append(float(d1[1]))

            
            plt.xlim(-5,5)
            plt.ylim(-2,2)
        
            plt.title('DATASET_1')
            if(t1==0):
                cl='black'
                lb='Class1'
            elif(t1==1):
                cl='yellow'
                lb='Class2'
            elif(t1==2):
                cl='brown'
                lb='Class3'
            plt.scatter(x,y,color=cl ,marker='*',s=10,label=lb)
        
            print ('Enter the file to read optimise mean ')
            file=input('........................>:')
            print ('Enter the class name to read optimise sigma ')
            file1=input('..................>:')
        
            fp=open(file+'.txt','r')
            fp1=open(file1+'.txt','r')
        
            s=fp.readlines()
            s1=fp1.readlines()
        
            fp.close()
            fp1.close()
        
            u_op=s[-1]
            s_op=s1[-1]
            print(u_op,'\n',s_op)
        
            s3=u_op.split()
            s4=s_op.split()
            print(s3,'\n',s4)
        
            print('enter the dimention')
            dim=int(input('..........>:'))
        
            print('enter total no of cluster')
            k_cluster=int(input('.....>:'))
            u1=[]
            u2=[]
            u3=[]
        
            
            self.mean=[]        
            for i in range(len(s3)):
                if(0<=i<dim):
                    u1.append(float(s3[i]))
                elif(dim<=i<dim*2):
                    u2.append(float(s3[i]))
                elif(dim*2<=i<dim*3):
                    u3.append(float(s3[i]))
                
            self.mean.append(u1)
            self.mean.append(u2)
            self.mean.append(u3)
        
            plt.scatter(self.mean[0][0],self.mean[0][1],color='green',s=5)
            plt.scatter(self.mean[1][0],self.mean[1][1],color='red',s=5)
            plt.scatter(self.mean[2][0],self.mean[2][1],color='blue',s=5)
        
 

            sigma_1=[]
            sigma_2=[]
            sigma_3=[]
            i=0
            k=0
            self.sigma=[]
            
            for i2 in range(k_cluster):
        
                k=k+1
                if(k==1):
                    for m in range(dim):
                    
                        b=[]
                        for j in range(dim):
                            b.append( float(s4[i]))
                            i=i+1
                        sigma_1.append(b)
        
                elif(k==2):
                    for m in range(dim):
                        b=[]
                        for j in range(dim):
                            b.append( float(s4[i]))
                            i=i+1
                        sigma_2.append(b)
        


                elif(k==3):
                    for m in range(dim):
                        b=[]
                        for j in range(dim):
                            b.append( float(s4[i]))
                            i=i+1
                        sigma_3.append(b)
                if(k>3):
                    break
                

        
        
        
        

            
            self.sigma.append(nm.linalg.inv(sigma_1))
            self.sigma.append(nm.linalg.inv(sigma_2))
            self.sigma.append(nm.linalg.inv(sigma_3))
        
            plt.xlabel('X-axis')
            plt.ylabel('Y-label')

            #plt.figure(2)
            
            for k in range(3):
                if(k==0):
                    clr='green'
                    lb='class_1_cluster_1'
                elif(k==1):
                    clr='red'
                    lb='class_1_cluster_2'
                elif(k==2):
                    clr='blue'
                    lb='class_1_cluster_3'

                #print(self.sigma[k])

                '''
            
                for i in range(dim):
                    for j in range(dim):
                        m=self.sigma[k][i][j]
                        self.sigma[k][i][j]=float('%.2f' % m )
                '''

                    
                #print(self.sigma[k])

                b=(self.sigma[k][0][1]+ self.sigma[k][1][0])
                #b=float('%.2f'%b)
                    
                a=self.sigma[k][0][0]
                #a=float('%.2f'%a)
                
                c=self.sigma[k][1][1]
                #c=float('%.2f'%c)
                
                u_0=self.mean[k][0]
                
                u_1=self.mean[k][1]

                
                #print('ssssssssss',b,a,c)

                a1=nm.arange((u_0-.5),(u_0 +.5),0.01)
                a2=nm.arange((u_1-.5),(u_1 +.5),0.01)
                x,y= nm.meshgrid(a1,a2)


            
                
                  
                #aa=(1/(2*3.14*nm.sqrt(nm.linalg.det(self.sigma[k])))) 
                    
                z=  nm.exp(  (-1/2)*(a*x*x +a*u_0*u_0 -a*2*x*u_0 + b*x*y -b*x*u_1 - b*u_0*y + b*u_0*u_1 + c*y*y +c*u_1*u_1 - c*2*y*u_1))

                #for i in z:
                    #print (i)
                #if(k==2):
                plt.contour(x,y,z,6,colors=clr,label=lb,linnestyles='solid')
                                                                                            
                                                                      
            
            
   

        
            
            
            
            t1=t1+1
        
        plt.legend()
        plt.show()
                
if(__name__=='__main__'):
    ob=Contour()
    ob.counter_represent()
            
            



        


            
            
        
                
        
            
                

            
                    
            
            
        
        
