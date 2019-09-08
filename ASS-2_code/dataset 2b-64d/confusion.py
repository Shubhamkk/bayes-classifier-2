import numpy as nm
import random
class  confusion_matrics():
    def __init__(self):
        pass




    def c_matrics(self):
        
        self.class_sigma_mean_mix=[]
        print ('enter the total number of clas')
        nu_class=int(input('...........>:'))
        
        self.class_parameter_sigma_mean_mixcofficient=[0]*nu_class

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

            self.mean=[]
            self.sigma_class=[]
            self.sigma=[]
            self.mix=[]

            self.parameter=[]

        
        
        
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
                    u1.append(float('%.2f'%float(s3[i])))
                elif(dim<=i<dim*2):
                    u2.append(float('%.2f'%float(s3[i])))
                elif(dim*2<=i<dim*3):
                    u3.append(float('%.2f'%float(s3[i])))

         
                
            self.mean.append(u1)
            self.mean.append(u2)
            self.mean.append(u3)

            #print(self.mean)

        

            
            i=0
            k=0
           
        
            for i2 in range(k_cluster):
        
                k=k+1
                if(k==1):
                    for m in range(dim):
                    
                        b=[]
                        for j in range(dim):
                            b.append(float('%.2f'%float(s4[i])))
                            i=i+1
                        sigma_1.append(b)
        
                elif(k==2):
                    for m in range(dim):
                        b=[]
                        for j in range(dim):
                            b.append(float('%.2f'%float(s4[i])))
                            i=i+1
                        sigma_2.append(b)
        


                elif(k==3):
                    for m in range(dim):
                        b=[]
                        for j in range(dim):
                            b.append(float('%.2f'%float(s4[i])))
                            i=i+1
                        sigma_3.append(b)
                if(k>3):
                    break

           
            self.sigma_class.append(sigma_1)
            self.sigma_class.append(sigma_2)
            self.sigma_class.append(sigma_3)
            #print(self.sigma_class)

           

            
            s5=fp2.readlines()
            
            s5_1=s5[-1]
            
            s6=s5_1.split()
            for i in range(k_cluster):
                
                self.mix.append(float('%.2f'%float(s6[i])))

            #print(self.mix)

            self.parameter.append(self.sigma_class)
            self.parameter.append(self.mean)
            self.parameter.append(self.mix)

            #print(self.parameter)
          
            self.class_sigma_mean_mix.append(self.parameter)
            
            #print(self.class_sigma_mean_mix)

            
            #gdddddddddd
            '''
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

            self.mean=[]
            self.sigma_class=[]
            self.sigma=[]
            self.mix=[]
            self.parameter=[]


            print(self.class_sigma_mean_mix)
            '''
            

            
            
            
            fp.close()
            fp1.close()
            fp2.close()
            


        #print ('Enter 1 for  Positive class1  2 For Positive clas2 Confusion matrics

        

        #k_cluster=3        
        #dim=2
        for k in range (1):

            

            if(k==0):
                
                self.confusion_matrics_true_1=[['Actual_Yes','Predicted_Yes','Predicted_No'],[0,0,0]]
                self.confusion_matrics_false_1=[['Actual_No','Predicted_Yes','Predicted_No'],[0,0,0]]

                self.confusion_matrics_true_2=[['Actual_Yes','Predicted_Yes','Predicted_No'],[0,0,0]]
                self.confusion_matrics_false_2=[['Actual_No','Predicted_Yes','Predicted_No'],[0,0,0]]

                self.confusion_matrics_true_3=[['Actual_Yes','Predicted_Yes','Predicted_No'],[0,0,0]]
                self.confusion_matrics_false_3=[['Actual_No','Predicted_Yes','Predicted_No'],[0,0,0]]
                
                for test in range(nu_class):
                    print('Enter Class test data')
                    f1=input('...............>>')
                    fp1=open(f1+'.txt','r')
                    print('Enter 1 for Class_1 test data ::2 for Class_2 data test data:: 3 for class Class_3 data::')
                    Tr=int(input('...............>>:') )   
                    while(1):
                        c1=fp1.readline()
                        if(c1==''):
                            break
                        c2=c1.split()
                        a=[]
                        for i in range(dim):
                            a.append(float(c2[i]))
                        #print(a)
                    

                        
                        sum1=0
                        for j in range(k_cluster):
                            b=[0]*dim
                            for l in range(dim):
                                b[l]=a[l]-self.class_sigma_mean_mix[k][1][j][l]
                                
                            #operation to reduce singulal matrics
                            if(nm.linalg.det(self.class_sigma_mean_mix[k][0][j])==0):
                                for dim1 in range(dim):
                                    for dim2 in range(dim):
                                        if(self.class_sigma_mean_mix[k][0][j][dim1][dim2]==0):
                                            self.class_sigma_mean_mix[k][0][j][dim1][dim2]=random.randint(1,5)
                        
                            d=nm.linalg.det(self.class_sigma_mean_mix[k][0][j])
                            if(d<0):
                                d=(-1)*d
                               
                            inv=list(nm.linalg.inv(self.class_sigma_mean_mix[k][0][j]))
                            
                            p1=self.class_sigma_mean_mix[k][2][j] * (1/(2*3.14* nm.sqrt(d)))*nm.exp((-1/2)*nm.dot(b,nm.dot(inv,b)))
                                
                            sum1=sum1+p1


                        
                        sum2=0
                        for j in range(k_cluster):
                            b=[0]*dim
                            for l in range(dim):
                                b[l]=a[l]-self.class_sigma_mean_mix[k+1][1][j][l]
                                
                            # reduce singular matrics 
                            if(nm.linalg.det(self.class_sigma_mean_mix[k+1][0][j])==0):
                                for dim1 in range(dim):
                                    for dim2 in range(dim):
                                        if(self.class_sigma_mean_mix[k+1][0][j][dim1][dim2]==0):
                                            self.class_sigma_mean_mix[k+1][0][j][dim1][dim2]=random.randint(1,5)
                            
                            d=nm.linalg.det(self.class_sigma_mean_mix[k+1][0][j])
                            if(d<0):
                                d=(-1)*d
                            inv=list(nm.linalg.inv(self.class_sigma_mean_mix[k+1][0][j]))
                            p2=self.class_sigma_mean_mix[k+1][2][j] * (1/(2*3.14* nm.sqrt(d)))*nm.exp((-1/2)*nm.dot(b,nm.dot(inv,b)))
                                
                            sum2=sum2+p2

                        sum3=0
                        for j in range(k_cluster):
                            b=[0]*dim
                            for l in range(dim):
                                b[l]=a[l]-self.class_sigma_mean_mix[k+2][1][j][l]
                            #reduce singular matrics to non singular
                            if(nm.linalg.det(self.class_sigma_mean_mix[k+2][0][j])==0):
                                for dim1 in range(dim):
                                    for dim2 in range(dim):
                                        if(self.class_sigma_mean_mix[k+2][0][j][dim1][dim2]==0):
                                            self.class_sigma_mean_mix[k+2][0][j][dim1][dim2]=random.randint(1,5)
                            
                            d=nm.linalg.det(self.class_sigma_mean_mix[k+2][0][j])
                            if(d<0):
                                d=(-1)*d
                                
                            inv=list(nm.linalg.inv(self.class_sigma_mean_mix[k+2][0][j]))
                            
                            p3=self.class_sigma_mean_mix[k+2][2][j] * (1/(2*3.14* nm.sqrt(d)))*nm.exp((-1/2)*nm.dot(b,nm.dot(inv,b)))
                                
                            sum3=sum3+p3

                        if(Tr==1):
                            p_2=sum2
                            if(sum2<sum3):
                                p_2=sum3
                            if(p_2<sum1):
                                self.confusion_matrics_true_1[1][0]=self.confusion_matrics_true_1[1][0] +1    
                                self.confusion_matrics_true_1[1][1]=self.confusion_matrics_true_1[1][1] +1

                                self.confusion_matrics_false_2[1][0]=self.confusion_matrics_false_2[1][0] +1    
                                self.confusion_matrics_false_2[1][2]=self.confusion_matrics_false_2[1][2] +1

                                self.confusion_matrics_false_3[1][0]=self.confusion_matrics_false_3[1][0] +1    
                                self.confusion_matrics_false_3[1][2]=self.confusion_matrics_false_3[1][2] +1
                                
                            else:

                                
                                self.confusion_matrics_true_1[1][0]=self.confusion_matrics_true_1[1][0] +1    
                                self.confusion_matrics_true_1[1][2]=self.confusion_matrics_true_1[1][2] +1
                                
                                if(sum2>sum3):
                                    self.confusion_matrics_false_2[1][0]=self.confusion_matrics_false_2[1][0] +1    
                                    self.confusion_matrics_false_2[1][1]=self.confusion_matrics_false_2[1][1] +1
                                    
                                    self.confusion_matrics_false_3[1][0]=self.confusion_matrics_false_3[1][0] +1    
                                    self.confusion_matrics_false_3[1][2]=self.confusion_matrics_false_3[1][2] +1
                                else:
                                    self.confusion_matrics_false_2[1][0]=self.confusion_matrics_false_2[1][0] +1    
                                    self.confusion_matrics_false_2[1][2]=self.confusion_matrics_false_2[1][2] +1
                                    
                                    self.confusion_matrics_false_3[1][0]=self.confusion_matrics_false_3[1][0] +1    
                                    self.confusion_matrics_false_3[1][1]=self.confusion_matrics_false_3[1][1] +1
                            
                        elif(Tr==2):
                            p_2=sum1
                            if(sum1<sum3):
                                p_2=sum3
                                
                            if(p_2<sum2):
                                
                                self.confusion_matrics_true_2[1][0]=self.confusion_matrics_true_2[1][0] +1    
                                self.confusion_matrics_true_2[1][1]=self.confusion_matrics_true_2[1][1] +1

                                self.confusion_matrics_false_1[1][0]=self.confusion_matrics_false_1[1][0] +1    
                                self.confusion_matrics_false_1[1][2]=self.confusion_matrics_false_1[1][2] +1

                                self.confusion_matrics_false_3[1][0]=self.confusion_matrics_false_3[1][0] +1    
                                self.confusion_matrics_false_3[1][2]=self.confusion_matrics_false_3[1][2] +1

                                
                            else:
                                self.confusion_matrics_true_2[1][0]=self.confusion_matrics_true_2[1][0] +1    
                                self.confusion_matrics_true_2[1][2]=self.confusion_matrics_true_2[1][2] +1
                                
                                if(sum1>sum3):
                                    self.confusion_matrics_false_1[1][0]=self.confusion_matrics_false_1[1][0] +1    
                                    self.confusion_matrics_false_1[1][1]=self.confusion_matrics_false_1[1][1] +1
                                    
                                    self.confusion_matrics_false_3[1][0]=self.confusion_matrics_false_3[1][0] +1    
                                    self.confusion_matrics_false_3[1][2]=self.confusion_matrics_false_3[1][2] +1
                                else:
                                    self.confusion_matrics_false_1[1][0]=self.confusion_matrics_false_1[1][0] +1    
                                    self.confusion_matrics_false_1[1][2]=self.confusion_matrics_false_1[1][2] +1
                                    
                                    self.confusion_matrics_false_3[1][0]=self.confusion_matrics_false_3[1][0] +1    
                                    self.confusion_matrics_false_3[1][1]=self.confusion_matrics_false_3[1][1] +1
                        
                        elif(Tr==3):
                            p_2=sum2
                            if(sum2<sum1):
                                p_2=sum1
                            if(p_2<sum3):
                                self.confusion_matrics_true_3[1][0]=self.confusion_matrics_true_3[1][0] +1    
                                self.confusion_matrics_true_3[1][1]=self.confusion_matrics_true_3[1][1] +1

                                self.confusion_matrics_false_2[1][0]=self.confusion_matrics_false_2[1][0] +1    
                                self.confusion_matrics_false_2[1][2]=self.confusion_matrics_false_2[1][2] +1

                                self.confusion_matrics_false_1[1][0]=self.confusion_matrics_false_1[1][0] +1    
                                self.confusion_matrics_false_1[1][2]=self.confusion_matrics_false_1[1][2] +1
                                
                            else:

                                
                                self.confusion_matrics_true_3[1][0]=self.confusion_matrics_true_3[1][0] +1    
                                self.confusion_matrics_true_3[1][2]=self.confusion_matrics_true_3[1][2] +1
                                
                                if(sum2>sum1):
                                    self.confusion_matrics_false_2[1][0]=self.confusion_matrics_false_2[1][0] +1    
                                    self.confusion_matrics_false_2[1][1]=self.confusion_matrics_false_2[1][1] +1
                                    
                                    self.confusion_matrics_false_1[1][0]=self.confusion_matrics_false_1[1][0] +1    
                                    self.confusion_matrics_false_1[1][2]=self.confusion_matrics_false_1[1][2] +1
                                else:
                                    self.confusion_matrics_false_2[1][0]=self.confusion_matrics_false_2[1][0] +1    
                                    self.confusion_matrics_false_2[1][2]=self.confusion_matrics_false_2[1][2] +1
                                    
                                    self.confusion_matrics_false_1[1][0]=self.confusion_matrics_false_1[1][0] +1    
                                    self.confusion_matrics_false_1[1][1]=self.confusion_matrics_false_1[1][1] +1
                            
                                    
                                
                    fp1.close()
                #representation of class 1   
                fp1=open('Class_1_teast_result.txt','w')
                for term in self.confusion_matrics_true_1:
                    for term1 in term:
                        fp1.write(str(term1)+'  ' )
                    fp1.write('\n\n')
                    
                for term in self.confusion_matrics_false_1:
                    for term1 in term:
                        fp1.write(str(term1)+'  ' )
                    fp1.write('\n\n')

                    
                # representation of class 2
                fp2=open('Class_2_teast_result.txt','w')
                for term in self.confusion_matrics_true_2:
                    for term1 in term:
                        fp2.write(str(term1)+'  ' )
                    fp2.write('\n\n')
                    
                for term in self.confusion_matrics_false_2:
                    for term1 in term:
                        fp2.write(str(term1)+'  ' )
                    fp2.write('\n\n')


                #representation of class 2
                fp3=open('Class_3_teast_result.txt','w')
                for term in self.confusion_matrics_true_3:
                    for term1 in term:
                        fp3.write(str(term1)+'  ' )
                    fp3.write('\n\n')
                    
                for term in self.confusion_matrics_false_3:
                    for term1 in term:
                        fp3.write(str(term1)+'  ' )
                    fp3.write('\n\n')



                    
            





            
        
  
        
if(__name__=='__main__'):
    ob=confusion_matrics()
    ob.c_matrics()
        

        
