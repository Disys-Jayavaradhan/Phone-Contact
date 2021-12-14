class phone_Contacts:                                                                                   #OOPS
    
    def __init__(self,Firstname,Lastname,Phone_number,Email_ID,Groups,DOB):                             #function
        self.firstname=input("First name: ")
        self.lastname=input("Last name: ")
        self.phonenumber=input("Phone number: ")
        self.emailid=input("Email ID: ")
        self.groups=input("Groups: ")
        self.dob=input("DOB: ")


    def view_contact(self):
        print(self.firstname,self.lastname,self.phonenumber,self.emailid,self.groups,self.dob)
        
    def openphone_contacts(self):
        print("Phone Contacts")
    
        
    def firstname_verification(self):
        if type(self.firstname) == str:
            if len(self.firstname) <= 15:                                                                                #LEN FUNCTION
                print("First Name is  Verified")
            else:
                raise ValueError("First Name should contain lesser than or equal to 15 letters")
        else:
            raise TypeError("First Name should contain letters only")
        
    def lastname_verification(self):
        if type(self.lastname) == str:
            if len(self.lastname) <= 15:                                                                                #LEN FUNCTION
                print("Last Name verified")
            else:
                raise ValueError("Last Name should contain lesser than or equal to 15 letters")
        else:
            raise TypeError("Last Name should contain letters only")
        
    def phonenumber_verification(self):
        if len(self.phonenumber)==10:
            if type(int(self.phonenumber)) == int:                                                                            #TYPE VALIDATION
                print("Phone Number verified")
            else:
                raise TypeError("Phone Number should contain only integers ")
        else:
            raise ValueError("Phone Number should not be grater than or lesser than 10")
        
    def emailid_verification(self):
        if type(self.emailid) == str:                                                                               #VALUE VALIDATION
            if len(self.emailid) <= 25:                                                                              
                print("Emailid verified")
            else:
                raise ValueError("Emailid should not contain more than 25 values")
        else:
            raise TypeError("Invalid E-mail ID")    
        

    def groups_verification(self):
        if type(self.groups) == str:
            if len(self.groups) <= 20:                                                                              #LEN FUNCTION
                print("Groups Verified")
            else:
                raise ValueError("Groups should contain lesser than or equal to 10 letters")
        else:
            raise TypeError("Groups should contain letters only")

    def dob_verification(self):
        if isinstance(self.dob,str):                                                                                #ISINSTANCE METHOD
            if len(self.dob) <= 10:                                                                                 #LEN FUNCTION
                print("DOB verified")
            else:
                raise ValueError("DOB should contain lesser than or equal to 10 letters")
        else:
            raise TypeError("DOB should contain numbers and symbols only")   
   


Jaya=phone_Contacts("First Name""Jaya","Lastname""Varadhan","Phone Number""9361486028","Email_ID""jayavaradhan07@gmail.com","Group""Family","DOB""06/04/2007")
Jaya.openphone_contacts()
Jaya.firstname_verification()
Jaya.lastname_verification()
Jaya.phonenumber_verification()
Jaya.emailid_verification()
Jaya.groups_verification()
Jaya.dob_verification()
Jaya.view_contact()



phone=[{"First Name":"Abi","Last Name":"Rithinyaa","Phone Number":9854268725,"Email_id":"abi@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                  #DICTIONARY INSIDE LIST
           {"Firstname":"Anu","Lastname":"priyaa","Phno":9987968725,"Email_id":"anu@gmail.com","Groups":"Friends","DOB":"03/05/2001"},]


for i in phone:                                                                                                             #LOOPING
    for j,k in i.items():                                                                                                     #KEY VALUES LOOPING
        print(f"{j}:{k}")


