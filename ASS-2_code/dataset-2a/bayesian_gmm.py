import numpy as nm
import math
import random


class Gmm:

    def Gmm_Model(self,data):
        
        print(len(data))
            
        self.all_data=data
        
        print('enter the number of cluster')
        k_cluster=int(input('Enter the number of cluster ...>:'))
        
        #declaration of storage
        self.Cluster_Nu_Final=[]
        self.Cluster_Nu_Initial=[]
        
        #storage for initial and final clustering data 
        for xyz in range(k_cluster):
            
            b=[]
            c=[]
            self.Cluster_Nu_Final.append(b)
            self.Cluster_Nu_Initial.append(c)
        

        print('enter the dimention of data atleast...>:2  ') 
        dim=int(input('Enter the dimention...>:'))

        
        #Storage of Mean of obtained from data
        self.Mean=[]
        for i in range(k_cluster):
            self.dim=[]
            for j in range(dim):
                self.dim.append(random.randint(1,10))
                
            self.Mean.append(self.dim)


        #storage for Sigma matrics for k_cluster
        self.cluster_sigma_matrics=[]
        for i in range (k_cluster):
            self.sigma_matrics=[]
            for j in range(dim):
                
                self.row=[]
                for k in range(dim):
                    self.row.append(random.randint(1,10))
                    
                self.sigma_matrics.append(self.row)
                
            self.cluster_sigma_matrics.append(self.sigma_matrics)
        #calculation of sigma_inverse and determinant of sigma matrics
        determinant_sigma=[]
        cluster_sigma_inverse=[]
        for i in range(k_cluster):    
            determinant_sigma.append(nm.linalg.det(self.cluster_sigma_matrics[i]))
            cluster_sigma_inverse.append(nm.linalg.inv(self.cluster_sigma_matrics[i]))
            
    
        
            
        print('enter the total number iteration')
        Total_Number_Iteration=int(input('Number iteration...>:'))
        local_var_itr=0
        
        
        #Distributing initial data into k_cluster to find maxium likelyhood parameter
        length_1=len(data)
        length=length_1//k_cluster
        remainder=(len(data)) - length*k_cluster
        
        #print(length)
        k_length=0
        cluster_append_index=0

        
        





        #initialisation of Mixture cofficient for each cluster
        
        self.Mixture_cofficient=[0]*k_cluster
        self.Mixture_cofficient[0]=0.012
        self.Mixture_cofficient[1]=0.72
        self.Mixture_cofficient[2]=0.268
        
        #for i in range(k_cluster):
            #self.Mixture_cofficient[i]=1/k_cluster

        #Declaration of responsblty term
        self.cluster_responsblity =[]
        for i in range(k_cluster):
            b=[]
            self.cluster_responsblity.append(b)
            
        

        # Entering text file to store maximisation sigma mean and mixture cofficint
        print('Enter file name to stor  mean_value:')
        mean_value=input('............>:')
        
        print('Enter file name to store sigma_value:')
        sigma=input('............>:')
        
        print('Enter file name to store cofficient  mean_value:')
        coff=input('............>:')
        fp=open(mean_value+'.txt','w')
        fp1=open(coff+'.txt','w')
        fp2=open(sigma+'.txt','w')



        #print(self.Mean)
        #print(self.Mixture_cofficient)


        
        avinash=0
        while(1):

            self.cluster_responsblity =[]
            for i in range(k_cluster):
                b=[]
                self.cluster_responsblity.append(b)
            
      
            #calculation of responsblity 
            for i in range(k_cluster):
                #print(i)
                #to find resposiblity term of different cluster
                responsblity_denominator=0
                responsblity_numnator=0
                
                for x_n_vector in self.all_data:
                    #calculation to check probablity of xn occuring in one cluster
                    x_u=[]
                    for j in range(dim):
                        x_u.append(x_n_vector[j]-self.Mean[i][j])
                        
                    exp_1=(-1/2)*(nm.dot(x_u,nm.dot(cluster_sigma_inverse[i],x_u)))
                    
                    #exp_1=nm.exp(exp_1)
                    
                    #print('ssssssss',exp_1)
                  
                    exp_1=nm.exp(exp_1)

                    det_m=nm.linalg.det(self.cluster_sigma_matrics[i])
                    #handeling negative det in function 
                    if(det_m<0):
                        det_m=-1*(det_m)
                    
                    exp_2=math.pow(2*3.143,(dim/2))* math.pow((det_m),.5)
                    
                    #print(nm.exp(exp_1)/exp_2)
                    p_xn_znk=exp_1/exp_2
                    
                    '''
                    p_xn_znk=  - math.log(exp_2)  + exp_1
                    if(p_xn_znk>0):
                            p_xn_znk=-1*p_xn_znk
                    
                    p_xn_znk=1/(1-p_xn_znk)
                    '''


                    
                    responsblity_numnator=self.Mixture_cofficient[i]*p_xn_znk
                    
                    # now calculation of probablty of xn occouring in all cluster
                    
                    for k in range(k_cluster):
                        x_u=[]
                        for j in range(dim):
                            x_u.append(x_n_vector[j]-self.Mean[k][j])
                        
                        exp_1= (-1/2)*(nm.dot(x_u,nm.dot(cluster_sigma_inverse[k],x_u)))
                       
                        
                        #exp_1=nm.exp(exp_1)
                        
                        #print(exp_1)
                        #handeling negative det in function
                        det_m1=nm.linalg.det(self.cluster_sigma_matrics[k])
                        if(det_m1<0):
                            det_m1=-1*(det_m1)
                            
                    
                        exp_2=math.pow(2*(3.143),(dim/2))*(math.pow((det_m1),.5))
                        #print('aaaaaaaaaaaa:',k,exp_1)
                        exp_1=nm.exp(exp_1)
                        
                        
                        '''
                        p_xn_znk = exp_1 - math.log(exp_2)
                        if(p_xn_znk>0):
                            p_xn_znk=-1*p_xn_znk
                        p_xn_znk=1/(1-p_xn_znk)
                        #print(exp_1,exp_2)
                        #print(p_xn_znk)
                        '''
                        p_xn_znk=exp_1/exp_2
                        
                        sum_k=self.Mixture_cofficient[k]*p_xn_znk
                        responsblity_denominator=responsblity_denominator + sum_k
                        
                    responsblity=(responsblity_numnator/responsblity_denominator)
                    #ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss
                    #print(responsblity)
                    
                    self.cluster_responsblity[i].append(responsblity)
                    #re-initialization to calculate for next x_n
                    responsblity_denominator=0
                    responsblity_numnator=0


            #print(self.cluster_responsblity[0])




            #find Mixture cofficient of cluster.....
            self.Mixture_cofficient=[0]*k_cluster
            for i in range(k_cluster):
                sum_2=0
                for j in range(len(self.all_data)):
                    sum_2=sum_2+ self.cluster_responsblity[i][j]
                self.Mixture_cofficient[i]=((sum_2/len(self.all_data)))

            for i in self.Mixture_cofficient:
                fp1.write(str(i)+' ')
            fp1.write('\n')
                
            #print(self.Mixture_cofficient)
            
            #calculation of Mean of all_cluster
            self.Mean=[]
            for i in range(k_cluster):
                sum_3=0
                sum_4=0
                mean=[0]*dim
                for j in range(len(self.all_data)):
                    for k in range(dim):
                        mean[k]=mean[k] + self.cluster_responsblity[i][j]*self.all_data[j][k]
                    sum_3=sum_3 + self.cluster_responsblity[i][j]
                if(sum_3==0):
                    sum_3=1
                for p in range(dim):
                    mean[p]=(mean[p]/sum_3)
                self.Mean.append(mean)

                
            #writting mean to a file
            for mean in self.Mean:
                for comp in mean:
                    fp.write(str(comp*1000) +' ')
                fp.write('\t')
            fp.write('\n')
                

            # now calculation of sigma matrics
            self.cluster_sigma_matrics=[]
            for i in range(k_cluster):
                sum_5=0
                self.sigma_matrics=[]
                for j in range(dim):
                    self.row=[0]*dim
                    self.sigma_matrics.append(self.row)
                for x_n in range(len(self.all_data)):
                    for k in range(dim):
                        for m in range(dim):
                            var=(self.all_data[x_n][k]-self.Mean[i][k])*(self.all_data[x_n][m]-self.Mean[i][m])
                            self.sigma_matrics[k][m]=self.sigma_matrics[k][m] + self.cluster_responsblity[i][x_n]*var
                    sum_5=sum_5 + self.cluster_responsblity[i][x_n]
                for n in range(dim):
                    for p in range(dim):
                        self.sigma_matrics[n][p]= (self.sigma_matrics[n][p]/sum_5)

                #here we are creating the sigma matrics for each cluster
                self.cluster_sigma_matrics.append(self.sigma_matrics)

            for i in  self.cluster_sigma_matrics:
                for j in i:
                    for k in j:
                        fp2.write(str(k)+' ')
                    fp2.write(' ')
                fp2.write('\t')
            fp2.write('\n')
                
            #calculation of sigma_inverse and determinant of sigma matrics
            determinant_sigma=[]
            cluster_sigma_inverse=[]
            for i in range(k_cluster):    
                determinant_sigma.append(nm.linalg.det(self.cluster_sigma_matrics[i]))
                cluster_sigma_inverse.append(nm.linalg.inv(self.cluster_sigma_matrics[i]))
            
    
                
               
                        
                
            
            #avinash=avinash+1
            #print(avinash)



            local_var_itr=local_var_itr +1
            if(local_var_itr==Total_Number_Iteration):
                break
            
        fp.close()    
        return [self.cluster_sigma_matrics,self.Mean,self.Mixture_cofficient]
        







class Bayesian_classifier(Gmm):
    def __init__(self,):
        pass

    def Gmm_model_class(self):
        
        print('Enter the number class to be  prepeared in  Gmm model')
        nu_class=int(input('...........>:'))
        self.class_parameter_sigma_mean_mixcofficient=[]
        for i in range(nu_class):
            b=[]
            self.class_parameter_sigma_mean_mixcofficient.append(b)
            
        for i in range(nu_class):
            self.data=[]
            print('Enter the file name of storage class...>:',i)
            file =input('.........>:')
            fp=open(file +'.txt','r')

            # Testing purpose..........................................................
            test=0
            while(1):
                b=[]
                data_1=fp.readline()
                if(data_1==''):
                    break
                data_2=data_1.split()
                for j in range(len(data_2)):
                    b.append(float(data_2[j]))
                self.data.append(b)
                if(test==1865):
                    break
                test=test+1
                
            fp.close()
            parameter=0
            
            parameter=self.Gmm_Model(self.data)
            self.class_parameter_sigma_mean_mixcofficient[i]=parameter
            
                          


if(__name__=='__main__'):
    ob=Bayesian_classifier()
    ob.Gmm_model_class()
            
            
                            
                            
                                
                            
                    
            
        
            
            
            
                     
        
        
