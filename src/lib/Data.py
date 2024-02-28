
""" ====== Credentials and data for all scripts ====== """

# ======================================================================

""" ====== Credentials For Login with Role ID 2 ====== """

USER_Name ="API_Security_test"
PASS_Word = "Usman@112"  

""" ====== Data to Create New User  ====== """

Role = "2,admin"               #Add role with Role Id like (2,admin), (3,manager), (4,user), (5,reporting_user).
USERName ="MianUsman_0026_sqaEN"   #Add new Username.
PASSWord = "Usman@112"           #Add password also used for confirm password. 
Email = f"{USERName}@gmail.com"  #Add new Email. (Automatically created with your user name)

""" ====== Create Campaign Data DATA ====== """
i = 1  #make it 1 if you want that user create campaign.

Campaign_Name = "UsmanAutotest"
GMC_Cid = "10469100432931003566"
Keyword_Count = 3


"""===========Quick Analysis data============="""

Q_GMC_Cid = "10469100432931003566"
Q_Business_name = "Sqa house"
Campaign_namee = "Sqa houseee"



# print("++++++++++++++++++++++++++++++++++++++++")
    # pop_name4 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"popUpMessage",)))
    # print("++++++++++++ee++++++++++++++++++++++++++++")
    # pop_name5 =driver.find_element(By.ID,"popUpMessage",)
    # print("++++++++++++++++++++++++++++++++++++++++")
    # csvv.make_csv('BSWA Quick Analysis Report.csv', f'Create Quick Analysis Campaign,{pop_name5.text}\n', new=False)