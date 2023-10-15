class Employee:
    def __init__(self,emp_id=None,name=None,salary=None) :  # Constructor Method we Call it
        self.emp_id=emp_id,
        self.name=name
        self.salary=salary      
    # Setter methods  : in Python
    def setEmpId(self,empid):
        self.emp_id=empid
    def setName(self,name):
        self.name=name
    def setSalary(self,salary):
        self.salary=salary
    #getter Methods
    def getEmpid(self):
        return self.emp_id
    def getName(self):
        return  self.name
    def getSalary(self):
        return self.salary


E1=Employee()
E2=Employee(1,"Tejas",10000)
E1.setEmpId(2)
E1.setName("tushar")
E1.setSalary(40000)

print(E1.getEmpid(),E1.getName(),E1.getSalary())
print(E2.getEmpid(),E2.getName(),E2.getSalary())


