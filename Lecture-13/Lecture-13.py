##class clg:
##    clg_name='Hansa International School'
##    def info(self,name,age,percent):
##        print(f'School name is {self.clg_name} \n Name: {name} \n Age: {age} \n pecentage is {percent}')
##
##s1=clg()
##s2=clg()
##s3=clg()
##
##s1.info('Vinod',23,34)
##s2.info('Sachin',36,24)
##s3.info('Sahil',54,234)

class clg:
    def info(self,name,age,percent,clg_name):
        print(f'School name is {clg_name} \n Name: {name} \n Age: {age} \n pecentage is {percent}')

s1=clg()
s2=clg()
s3=clg()

s1.info('Vinod',23,34,'Hansa International School')
s2.info('Sachin',36,24,'Hansa International School')
s3.info('Sahil',54,234,'Hansa International School')















