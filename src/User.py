"""======================================================================"""

""" ====== IMPORTS ====== """

from lib.imports import *
from lib.Data import *
from lib.Driver import *
from lib.Driver import initialize_and_navigate
from lib.page import random_click_elements




"""====================================================================="""

""" ====== Main Code ====== """

def main():
    
    """================================================================="""
    """ ====== Start Driver====== """
    
    driver = initialize_and_navigate(url)
    actions = ActionChains(driver)
    
    """================================================================="""
    """ ====== Make CSV ====== """
    
    csvv = HomePage(driver)
    
    csvv.make_csv('BSWA User Report.csv', 'Create New User Report\n\n')
    # csvv.make_csv('BSWA Report.csv', f'Test Case,Scenario,Results\n\n', new=False)

    """================================================================="""
    
    """ ====== LOGIN PAGE ====== """
    
    Login_Pagee = HomePage(driver)
    Login_Pagee.wait(Login.login_page)
    
    # Enter Username.
    time.sleep(0.5)
    Username = HomePage(driver)
    Username.click_btn(Login.USERNAME)
    time.sleep(0.5)
    Username = HomePage(driver)
    Username.enter_name_delay(Login.USERNAME, USER_Name)
    
    # Enter Password.
    time.sleep(0.5)
    Password = HomePage(driver)
    Password.click_btn(Login.PASSWORD)
    time.sleep(0.5)
    Password = HomePage(driver)
    Password.enter_name_delay(Login.PASSWORD, PASS_Word)
   
   # Enter Password.
    time.sleep(0.5)
    Login_btn = HomePage(driver)
    Login_btn.click_btn(Login.LOGIN_BTN)
    
    """================================================================="""
    
    """==================Create_User==================="""
    
    # main page 
    mainpage = HomePage(driver)
    mainpage.wait(MainPage.Main_Page)
    
    if mainpage:
        print("Successfull")
    else:
        print("UnSuccessfull")
    
    # Click on Userbutton.
    time.sleep(0.5)
    User_btn = HomePage(driver)
    User_btn.click_btn(User.User_btn)
    
    # main page 
    User_Page = HomePage(driver)
    User_Page.wait(User.User_Page)
    
    # Click on Users.
    time.sleep(0.5)
    Create_User_btn = HomePage(driver)
    Create_User_btn.click_btn(User.Create_User_btn)
    
    # main page 
    User_Modal = HomePage(driver)
    User_Modal.wait(User.User_Modal)
    
    if User_Modal:
        print("Successfull")
    else:
        print("UnSuccessfull")

    # Enter Username.
    time.sleep(0.5)
    Username = HomePage(driver)
    Username.click_btn(User.User_Input)
    time.sleep(0.5)
    Usernamee = HomePage(driver)
    Usernamee.enter_name_delay(User.User_Input, USERName)
    
    # Select Role.
    time.sleep(0.5)
    User_Role = HomePage(driver)
    User_Role.click_btn(User.User_Role)
    
    time.sleep(0.5)
    User_Rolee = HomePage(driver)
    User_Rolee.click_btn(User.User_Rolee)

    # Enter Email.
    time.sleep(0.5)
    User_Email = HomePage(driver)
    User_Email.click_btn(User.User_Email)
    time.sleep(0.5)
    User_Email = HomePage(driver)
    User_Email.enter_name_delay(User.User_Email, Email)
    
    # Enter Password.
    time.sleep(0.5)
    Password = HomePage(driver)
    Password.click_btn(User.User_Password)
    time.sleep(0.5)
    Password = HomePage(driver)
    Password.enter_name_delay(User.User_Password, PASSWord)
    
    # Enter Confrim Password.
    time.sleep(0.5)
    CPassword = HomePage(driver)
    CPassword.click_btn(User.User_Password)
    time.sleep(0.5)
    CPassword = HomePage(driver)
    CPassword.enter_name_delay(User.C_User_Password, PASSWord)
    
    # Create User.
    time.sleep(0.5)
    Create_User = HomePage(driver)
    Create_User.click_btn(User.Create_User_button)
    
    # Check for Pop_Up
    try:
        pop_up = HomePage(driver)
        pop_up.waitt(User.User_Pop_up)
    
        if pop_up:
            print("Successfull")
        else:
            print("UnSuccessfull")
        pop_up = driver.find_element(By.XPATH, User.User_Pop_up)
        csvv.make_csv('BSWA User Report.csv', f'Create User,{pop_up.text}\n', new=False)
    except:
        pass
    
    # Check for Created User
    time.sleep(0.5)
    User_Search = HomePage(driver)
    User_Search.click_btn(User.User_Search)
     
    time.sleep(0.5)
    User_Search = HomePage(driver)
    User_Search.enter_name_delay(User.User_Search, USERName)
    
    pop_up = HomePage(driver)
    pop_up.waitt(User.User)

    if pop_up:
        print("Successfull")
    else:
        print("UnSuccessfull")
    
    user = driver.find_element(By.XPATH, User.User)
    csvv.make_csv('BSWA User Report.csv', f'Create User,{user.text}\n', new=False)
    
    
    # Logout Current User drop down
    time.sleep(5)
    User_Logoutt = HomePage(driver)
    User_Logoutt.click_btn(User.User_Logoutt)
    
    # Logout Current User
    time.sleep(1)
    User_Logout = HomePage(driver)
    User_Logout.click_btn(User.User_Logout)
    
    """================================================================="""
    
    """ ====== LOGIN PAGE For Confrim User====== """
    
    Login_Pagee = HomePage(driver)
    Login_Pagee.wait(Login.login_page)
    
    # Enter Username.
    time.sleep(0.5)
    Username = HomePage(driver)
    Username.click_btn(Login.USERNAME)
    time.sleep(0.5)
    Username = HomePage(driver)
    Username.enter_name_delay(Login.USERNAME, USERName)
    
    # Enter Password.
    time.sleep(0.5)
    Password = HomePage(driver)
    Password.click_btn(Login.PASSWORD)
    time.sleep(0.5)
    Password = HomePage(driver)
    Password.enter_name_delay(Login.PASSWORD, PASSWord)
   
   # Enter Password.
    time.sleep(0.5)
    Login_btn = HomePage(driver)
    Login_btn.click_btn(Login.LOGIN_BTN)
    
    """================================================================="""
    
    """==================Confirm User==================="""
    
    # main page 
    mainpage = HomePage(driver)
    mainpage.wait(MainPage.Main_Page)
    
    if mainpage:
        print("Successfull")
    else:
        print("UnSuccessfull")
        
    # Click on Userbutton.
    time.sleep(0.5)
    User_btn = HomePage(driver)
    User_btn.click_btn(User.User_Logoutt)
    
    try:
        userr_c = driver.find_element(By.XPATH ,User.C_User)
        csvv.make_csv('BSWA User Report.csv', f'Confirm User,{userr_c.text}\n', new=False)
    except:
        pass
    
    """================================================================="""
    """==================Create Campaign By this User============="""
    
    if i == 1:
        # Enter Password.
        time.sleep(0.5)
        Campaign_btn = HomePage(driver)
        Campaign_btn.click_btn(Campaigns.Campaign_btn_M)
        
        # main page 
        mainpage = HomePage(driver)
        mainpage.wait(MainPage.Main_Page)
        
        if mainpage:
            print("Successfull")
        else:
            print("UnSuccessfull")
        
        # Enter Password.
        time.sleep(0.5)
        Campaign_btn = HomePage(driver)
        Campaign_btn.click_btn(Campaigns.Campaign_btn)
        
        # main page 
        Campage = HomePage(driver)
        Campage.wait(Campaigns.Campaign_page)
        
        if Campage:
            print("Successfull")
        else:
            print("UnSuccessfull")
        
        """Fill campaign data"""
        
        time.sleep(0.5)
        Campaign = HomePage(driver)
        Campaign.select_Client(Campaigns.dropdown_xpath)
        
        # Enter Password.
        time.sleep(0.5)
        Campaign_Input = HomePage(driver)
        Campaign_Input.click_btn(Campaigns.Campaign_Input)        
        time.sleep(0.5)
        Campaign_Input = HomePage(driver)
        Campaign_Input.enter_name_delay(Campaigns.Campaign_Input, Campaign_Name)

        # Enter Password.
        time.sleep(0.5)
        GMC_CID_input = HomePage(driver)
        GMC_CID_input.click_btn(Campaigns.GMC_CID_input)        
        time.sleep(0.5)
        GMC_CID_input = HomePage(driver)
        GMC_CID_input.enter_name_delay(Campaigns.GMC_CID_input, GMC_Cid)
        
        # Enter Password.
        time.sleep(1)
        GMC_CID_btn = HomePage(driver)
        GMC_CID_btn.click_btn(Campaigns.GMC_CID_btn) 
        print("Successfull")
        
        # main page 
        try:    
            Keyword_con = HomePage(driver)
            Keyword_con.waittt(Campaigns.Keyword_con)
        except:
            pass
        
        if Keyword_con:
            print("Successfull")
        else:
            print("UnSuccessfull")
            
        try:
            in_c_gmb = driver.find_element(By.XPATH , Campaigns.in_c_gmb)
            csvv.make_csv('BSWA Quick Analysis Report.csv', f'Check GMB_CID,{in_c_gmb.text}, Please try again\n', new=False)
            print("======================================")
            print("-----------Incorrect GMB Cid----------")
            print("======================================")
            driver.quit()  # Close the browser
        except:
            print("======================================")
            print("-----------keyword Found----------")
            print("======================================")
            
            """Fill campaign data"""
        
        time.sleep(1)
        actions.send_keys(Keys.PAGE_DOWN).perform()
        print("Successfull")
        Keyword_list = HomePage(driver)
        time.sleep(2)
        Keyword_list = HomePage.get_key_words(driver)
        
        # Enter Password.
        time.sleep(0.5)
        Submit_btn = HomePage(driver)
        Submit_btn.click_btn(Campaigns.Submit_btn) 
        
        # Check for Pop_Up
        try:
            pop_up = HomePage(driver)
            pop_up.waitt(Campaigns.Cam_Pop_up)
            pop_up = driver.find_element(By.XPATH, Campaigns.Cam_Pop_up)
            csvv.make_csv('BSWA User Report.csv', f'Create User,{pop_up.text}\n', new=False)
        except:
            pass

        # Refresh page
        time.sleep(0.5)
        driver.refresh()
        time.sleep(1)

        # Enter Password.
        time.sleep(0.5)
        Noti_btn = HomePage(driver)
        Noti_btn.click_btn(Campaigns.Noti_btn) 
        
    time.sleep(15)
if __name__ == "__main__":
    main()