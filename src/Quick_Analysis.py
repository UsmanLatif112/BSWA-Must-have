"""======================================================================"""

""" ====== IMPORTS ====== """

from lib.imports import *
from lib.Data import *
from lib.Driver import *
from lib.Driver import initialize_and_navigate
from lib.page import *

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
    
    # csvv.make_csv('BSWA Report.csv', 'Create New User Report\n\n')
    csvv.make_csv('BSWA Quick Analysis Report.csv', f'Test Case,Scenario,Results\n\n', new=True)

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
    
    """==================Get campaign Page status==================="""
    
    # main page 
    mainpage = HomePage(driver)
    mainpage.wait(MainPage.Main_Page)
    
    if mainpage:
        print("======================================")
        print("--------------Home Page---------------")
        print("======================================")
    else:
        print("======================================")
        print("----------Home age not found----------")
        print("======================================")
    # Click on Userbutton.
    time.sleep(0.5)
    Quick_btn = HomePage(driver)
    Quick_btn.click_btn(Quickanalysis.Quick_btn)
    
    # main page 
    Quick_page = HomePage(driver)
    Quick_page.wait(Quickanalysis.Quick_page)
    
    if Quick_page:
        print("======================================")
        print("---------Quick Analysis page----------")
        print("======================================")
    else:
        print("======================================")
        print("----Quick Analysis page not found-----")
        print("======================================")
    # Click on Users.
    time.sleep(0.5)
    Enter_CID = HomePage(driver)
    Enter_CID.click_btn(Quickanalysis.Enter_CID)
    
    time.sleep(0.5)
    Enter_CID = HomePage(driver)
    Enter_CID.enter_name_delay(Quickanalysis.Enter_CID, Q_GMC_Cid)
    
    time.sleep(0.5)
    Check_btn = HomePage(driver)
    Check_btn.click_btn(Quickanalysis.Check_btn)
    
    # main page 
    try:
        Keyword_con = HomePage(driver)
        Keyword_con.waittt(Quickanalysis.Keyword_con)
    except:
        pass
    
    if Keyword_con:
        print("======================================")
        print("--------Keyword container found-------")
        print("======================================")
    else:
        print("======================================")
        print("------Keyword container not found-----")
        print("======================================")
        
    try:
        in_c_gmb = driver.find_element(By.XPATH, Quickanalysis.in_c_gmb)
        csvv.make_csv('BSWA Quick Analysis Report.csv', f'Check GMB_CID,{in_c_gmb.text}, Please try again\n', new=False)
        print("======================================")
        print("-----------Incorrect GMB Cid----------")
        print("======================================")
        driver.quit()  # Close the browser
    except:
        print("======================================")
        print("-------------Keywords Found-----------")
        print("======================================")

    
    """Fill campaign data"""
    
    time.sleep(1)
    actions.send_keys(Keys.PAGE_DOWN).perform()
    Keyword_list = HomePage(driver)
    time.sleep(2)
    Keyword_list = HomePage.get_key_words(driver)
    
    time.sleep(2)
    submit_btn = HomePage(driver)
    submit_btn.click_btn(Quickanalysis.submit_btn)

    time.sleep(0.5)
    driver.refresh()
    time.sleep(0.5)

    try:
        time.sleep(2)
        Noti = HomePage(driver)
        Noti.click_btn(Quickanalysis.Notification)
        time.sleep(0.5)
        Noti =driver.find_element(By.XPATH, Quickanalysis.Notifications)
        print("==============================")
        print(f"----------{Noti.text}--------")
        print("==============================")
        csvv.make_csv('BSWA Quick Analysis Report.csv', f'Create Quick Analysis Campaign,{Noti.text}\n', new=False)
    except:
        pass
    
    time.sleep(0.5)
    driver.refresh()
    time.sleep(2)
    
    Q_Campaign_btn = HomePage(driver)
    Q_Campaign_btn.click_btn(Quickanalysis.Q_Campaign_btn)
    
    
    # main page 
    Q_Campaign_table = HomePage(driver)
    Q_Campaign_table.waittt(Quickanalysis.Q_Campaign_table)
    
    time.sleep(0.2)
    Q_Campaign = HomePage(driver)
    Q_Campaign.click_btn(Quickanalysis.Q_Campaign)
    
    time.sleep(0.5)
    Q_Campaignn = HomePage(driver)
    Q_Campaignn.enter_name_delay(Quickanalysis.Q_Campaign, Q_Business_name)
    
    # main page 
    Q_Campaign_table = HomePage(driver)
    Q_Campaign_table.waittt(Quickanalysis.Campaign)
    
    try:
        time.sleep(1)
        Campaign1 = driver.find_element(By.XPATH, Quickanalysis.Campaign)
        print("==================================")
        print(f"----------{Campaign1.text}--------")
        print("==================================")
        csvv.make_csv('BSWA Quick Analysis Report.csv', f'Check Quick Analysis Created Campaign,{Campaign1.text}\n', new=False)
    except:
        print(f"-------Campaign not found-------")
        pass
    
    time.sleep(2)
    edit_Campaign = HomePage(driver)
    edit_Campaign.click_btn(Quickanalysis.edit_Campaign)
    
    time.sleep(0.5)
    edit_Campaignn = HomePage(driver)
    edit_Campaignn.click_btn(Quickanalysis.edit_Campaignn)
    
    # main page 
    edit_Campaign_pg = HomePage(driver)
    edit_Campaign_pg.waittt(Quickanalysis.edit_Campaign_pg)
    
    if edit_Campaign_pg:
        print("======================================")
        print("----------Edit Q_Campaign page--------")
        print("======================================")
    else:
        print("======================================")
        print("----Edit Q_Campaign page not found----")
        print("======================================")
    time.sleep(0.5)
    edit_Campaign_name = HomePage(driver)
    edit_Campaign_name.click_btn(Quickanalysis.edit_Campaign_name)
    time.sleep(0.3)
    time.sleep(1)
    actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
    time.sleep(0.2)
    actions.send_keys(Keys.BACK_SPACE).perform()
    
    time.sleep(0.5)
    edit_Campaign_namee = HomePage(driver)
    edit_Campaign_namee.enter_name_delay(Quickanalysis.edit_Campaign_name, Campaign_namee)
    
    time.sleep(0.5)
    actions.send_keys(Keys.PAGE_DOWN).perform()
    
    time.sleep(0.5)
    edit_Campaignn = HomePage(driver)
    edit_Campaignn.click_btn(Quickanalysis.edit_Campaign_submit)
    
    # Enter Password.
    time.sleep(0.5)
    Campaign_btn = HomePage(driver)
    Campaign_btn.click_btn(Quickanalysis.Campaign_btn_M)
        
    # Refresh page
    time.sleep(0.5)
    driver.refresh()
    time.sleep(0.5)

    try:
        print("======================================")
        print("------------Get Notification---------")
        print("======================================")
        time.sleep(2)
        Notii = HomePage(driver)
        Notii.click_btn(Quickanalysis.Notification)
        
        time.sleep(1)
        Notii = driver.find_element(By.XPATH, Quickanalysis.notifications)
        print("==================================")
        print(f"------------{Notii.text}---------")
        print("==================================")
        csvv.make_csv('BSWA Quick Analysis Report.csv', f'Edit Quick Analysis Campaign,{Notii.text}\n', new=False)
    except:
        print("======================================")
        print("---------Notification not found-------")
        print("======================================")
        try:
            print("======================================")
            print("--Get Notification with Other method--")
            print("======================================")
            time.sleep(2)
            Notiii = HomePage(driver)
            Notiii.click_btn(Quickanalysis.Notification)
            time.sleep(1)
            Notiii =driver.find_element(By.XPATH, Quickanalysis.otifications)
            print("============================")
            print(f"-------{Notiii.text}-------")
            print("============================")
            csvv.make_csv('BSWA Quick Analysis Report.csv', f'Edit  Quick Analysis Campaign,{Notiii.text}\n', new=False)
        except:
            print("============================================")
            print("--Notification not found with Other method--")
            print("============================================")
            pass
        
    time.sleep(0.5)
    driver.refresh()
    time.sleep(2)
    print("==================================")
    print("----------Campaign_btn_M----------")
    print("==================================")
    time.sleep(0.5)
    Campaign_btn = HomePage(driver)
    Campaign_btn.click_btn(Quickanalysis.Campaign_btn_M)
    time.sleep(2)
    
    print("====================================")
    print("----------Q_Campaign_btnn1----------")
    print("====================================")
    Q_Campaign_btnn1 = HomePage(driver)
    Q_Campaign_btnn1.click_btn(Quickanalysis.Q_Campaign_btn)
        
    try:
        print("=================================================")
        print("----------Get Edited Campaign Campaignn----------")
        print("=================================================")
        Campaignn = HomePage(driver)
        Campaignn.waittt(Quickanalysis.CCampaign)
        time.sleep(5)
        Campaignn =driver.find_element(By.XPATH, Quickanalysis.CCampaign)
        print("=====================================")
        print(f"----------{Campaignn.text}----------")
        print("=====================================")
        csvv.make_csv('BSWA Quick Analysis Report.csv', f'Check Quick Analysis Edit Campaign {Campaignn.text} Edited successfully\n', new=False)
    except:
        print("=============================================")
        print("---Exeception while getinf edited campaign---")
        print("=============================================")
        pass
    
    time.sleep(1)
    Del_Campaign = HomePage(driver)
    Del_Campaign.click_btn(Quickanalysis.edit_Campaign)
    
    time.sleep(0.5)
    Del_Campaign = HomePage(driver)
    Del_Campaign.click_btn(Quickanalysis.Del_Campaign)
    
    # main page 
    Del_Campaign_pop = HomePage(driver)
    Del_Campaign_pop.waittt(Quickanalysis.Del_Campaign_pop)
    
    if Del_Campaign_pop:
        time.sleep(0.5)
        Del_Campaignn = HomePage(driver)
        Del_Campaignn.click_btn(Quickanalysis.Del_Campaignn)
    
    time.sleep(0.5)
    driver.refresh()
    time.sleep(0.5)
    
    Q_Campaign_btn = HomePage(driver)
    Q_Campaign_btn.click_btn(Quickanalysis.Q_Campaign_btn)
    
    # main page 
    Q_Campaign_btnb = HomePage(driver)
    Q_Campaign_btnb.waittt(Quickanalysis.Q_Campaign_btnb)
    
    try:
        print("=====================================")
        print("---Check Camaign is Deleted or Not---")
        print("=====================================")
        time.sleep(2)
        try:
            Campaignnn =driver.find_element(By.XPATH, Quickanalysis.CCampaign)
            print("============================")
            print(f"-----{Campaignnn.text}-----")
            print("============================")
            csvv.make_csv('BSWA Quick Analysis Report.csv', f'Delete Quick Analysis Campaign {Campaignnn.text} not deleted\n', new=False)
        except:
                print("========================================")
                print("---Check Camaign is Deleted or Not 2 ---")
                print("========================================")
                csvv.make_csv('BSWA Quick Analysis Report.csv', f'Delete Quick Analysis Campaign {Campaign_namee} Deleted Successfully\n', new=False)
    except:
        print("======================================")
        print("---Camaign is Deleted Not Execption---")
        print("======================================")
    
    
    time.sleep(150)
if __name__ == "__main__":
    main()