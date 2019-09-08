import numpy as nm
import matplotlib.pyplot as plt
import math


def c_matrics():
        
        class_sigma_mean_mix=[]
        print ('enter the total number of clas')
        nu_class=int(input('...........>:'))
        
        class_parameter_sigma_mean_mixcofficient=[0]*nu_class

        for i in range(nu_class):

            s=0
            s1=0
        
            u_op=0
            s_op=0
           
            s3=0
            s4=0

            s5=0
            
            s5_1=0
            
            s6=0
            

            u1=[]
            u2=[]
            u3=[]

            sigma_1=[]
            sigma_2=[]
            sigma_3=[]

            mean=[]
            sigma_class=[]
            sigma=[]
            mix=[]

            parameter=[]

        
        
        
            print ('Enter the file to read optimise mean ')
            file=input('........................>:')
            print ('Enter the class name to read optimise sigma ')
            file1=input('..................>:')
            print('enter the file name to read optimize mix')
            file2=input('.............>>:')
        
            fp=open(file+'.txt','r')
            fp1=open(file1+'.txt','r')
            fp2=open(file2+'.txt','r')
        
            s=fp.readlines()
            s1=fp1.readlines()
        
            
            u_op=s[-1]
            s_op=s1[-1]
           
        
            s3=u_op.split()
            s4=s_op.split()
            
        
            print('enter the dimention')
            dim=int(input('..........>:'))
        
            print('enter total no of cluster')
            k_cluster=int(input('.....>:'))
            
            
                  
            for i in range(len(s3)):
                if(0<=i<dim):
                    u1.append(float(s3[i]))
                elif(dim<=i<dim*2):
                    u2.append(float(s3[i]))
                elif(dim*2<=i<dim*3):
                    u3.append(float(s3[i]))

         
                
            mean.append(u1)
            mean.append(u2)
            mean.append(u3)
            print(mean)

            #print(mean)

        

            
            i=0
            k=0
           
        
            for i2 in range(k_cluster):
        
                k=k+1
                if(k==1):
                    for m in range(dim):
                    
                        b=[]
                        for j in range(dim):
                            b.append(float(s4[i]))
                            i=i+1
                        sigma_1.append(b)
        
                elif(k==2):
                    for m in range(dim):
                        b=[]
                        for j in range(dim):
                            b.append(float(s4[i]))
                            i=i+1
                        sigma_2.append(b)
        


                elif(k==3):
                    for m in range(dim):
                        b=[]
                        for j in range(dim):
                            b.append(float(s4[i]))
                            i=i+1
                        sigma_3.append(b)
                if(k>3):
                    break

           
            sigma_class.append(sigma_1)
            sigma_class.append(sigma_2)
            sigma_class.append(sigma_3)

            print(sigma_1)
            print(sigma_2)
            print(sigma_3)
            #print(sigma_class)

           
                 
            s5=fp2.readlines()
            
            s5_1=s5[-1]
            
            s6=s5_1.split()
            for i in range(k_cluster):
                
                mix.append(float(s6[i]))

                

            #print(mix)
            print(mix)

            parameter.append(sigma_class)
            parameter.append(mean)
            parameter.append(mix)

            #print(parameter)
          
            class_sigma_mean_mix.append(parameter)
            
            #print(class_sigma_mean_mix)
            

            
            
            fp.close()
            fp1.close()
            fp2.close()
            
            

        A=[[],[]]
        B=[[],[]]
        C=[[],[]]
        
        #k_cluster=3        
        #dim=2
        y_axis=200
        x_axis=150
        k=0
        k_1=0
        i=0


       
        if(k_1==0):
     

          
            if(k==0):
            
          
        
                '''
                self.confusion_matrics_true_1=[['Actual_Yes','Predicted_Yes','Predicted_No'],[0,0,0]]
                self.confusion_matrics_false_1=[['Actual_No','Predicted_Yes','Predicted_No'],[0,0,0]]

                self.confusion_matrics_true_2=[['Actual_Yes','Predicted_Yes','Predicted_No'],[0,0,0]]
                self.confusion_matrics_false_2=[['Actual_No','Predicted_Yes','Predicted_No'],[0,0,0]]

                self.confusion_matrics_true_3=[['Actual_Yes','Predicted_Yes','Predicted_No'],[0,0,0]]
                self.confusion_matrics_false_3=[['Actual_No','Predicted_Yes','Predicted_No'],[0,0,0]]
                '''

              
                while(1):
                    y_axis=y_axis+5
                    if(y_axis>1500):
                        break
                    x_axis=-5
                    while(1):
                        x_axis=x_axis+5
                        if(x_axis>1200):
                            break
                        a=[0,0]
                        a[0]=x_axis
                        a[1]=y_axis
                       
                        
                        sum1=0
                        for j in range(k_cluster):
                            b=[0]*dim
                            for l in range(dim):
                                b[l]=a[l]-class_sigma_mean_mix[k][1][j][l]
                        
                            d=nm.linalg.det(class_sigma_mean_mix[k][0][j])
                            if(d<0):
                                d=(-1)*d
                            inv=nm.linalg.inv(class_sigma_mean_mix[k][0][j])

                            c0=(-1/2)*nm.dot(b,nm.dot(inv,b))
                            
                            p1=(class_sigma_mean_mix[k][2][j] )* (math.log(1/(2*3.14* nm.sqrt(d)))+c0)
                            sum1=sum1+p1
                        #print('sum1:',sum1)


                        
                        sum2=0
                        for j in range(k_cluster):
                            b=[0]*dim
                            for l in range(dim):
                                b[l]=a[l]- class_sigma_mean_mix[k+1][1][j][l]
                            
                            d=nm.linalg.det( class_sigma_mean_mix[k+1][0][j])
                            if(d<0):
                                d=(-1)*d
                            inv=nm.linalg.inv(class_sigma_mean_mix[k+1][0][j])
                            
                            c1=(-1/2)*nm.dot(b,nm.dot(inv,b))
                            
                            p2= (class_sigma_mean_mix[k+1][2][j]) * (math.log(1/(2*3.14* nm.sqrt(d)))+c1)
                            sum2=sum2+p2
                        #print('sum2:',sum2)

                        sum3=0
                        for j in range(k_cluster):
                            b=[0]*dim
                            for l in range(dim):
                                b[l]=a[l]-class_sigma_mean_mix[k+2][1][j][l]
                            
                            d=nm.linalg.det(class_sigma_mean_mix[k+2][0][j])
                            if(d<0):
                                d=(-1)*d
                            inv=nm.linalg.inv(class_sigma_mean_mix[k+2][0][j])
                            
                            c2=(-1/2)*nm.dot(b,nm.dot(inv,b))
                            
                            p3=(class_sigma_mean_mix[k+2][2][j]) * ( math.log(1/(2*3.14* nm.sqrt(d)))+ c2)
                            
                            sum3=sum3+p3
                        #print('sum3:',sum3)

                        if(sum1>sum2 and sum1>sum3):
                            A[0].append(a[0])
                            A[1].append(a[1])
                            #plt.scatter(a[0],a[1],s=100,color='blue')

                        elif(sum2>sum1 and sum2>sum3):
                            B[0].append(a[0])
                            B[1].append(a[1])
                            #plt.scatter(a[0],a[1],s=100,color='red')
                        elif(sum3>sum2 and sum3>sum1):
                            C[0].append(a[0])
                            C[1].append(a[1])
                            #plt.scatter(a[0],a[1],s=100,color='green')

                        #print(i)
                        #i=i+1
                    

        plt.scatter(A[0],A[1],s=0.01,color='orange')
        plt.scatter(B[0],B[1],s=0.01,color='purple')
        plt.scatter(C[0],C[1],s=0.01,color='pink')
      
            





            
        

        
