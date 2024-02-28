from lib.Data import *

# # Refresh page
# time.sleep(0.5)
# driver.refresh()
# time.sleep(0.5)
    
class Login:
    login_page = "//*[@class='signin-wrapper-box']"
    USERNAME = "//*[@class='signin-form-box'][contains(normalize-space(), 'Username')]/input"
    PASSWORD = "//*[@class='signin-form-box'][contains(normalize-space(), 'Password')]/input"
    LOGIN_BTN = "//*[@id='signinformsubmit']/button[contains(normalize-space(), 'Login')]" 
    
class MainPage:
    Main_Page = "//*[@class='bg-fafbff']"
    Menu_btn = "//*[@class='app-header']//*[@class='header-content-right']//*[@class='header-element']"

    
class User:
    User_btn = "//*[@class='nav-item']/a[contains(normalize-space(), 'Users')]"
    User_Page = "//*[@class='campaign-listing-inner']/h2[contains(normalize-space(), 'Users')]"
    Create_User_btn = "//*[@class='create-new-campaign-btn mobile-hide']/*[contains(normalize-space(), 'New User')]"
    User_Modal = "//*[@class='modal-header agent-header'][contains(normalize-space(), 'Add New User')]"
    User_Input = "//*[@class='campaign-field-wrapper mb-15']/input[@placeholder='User Name']"
    User_Role = "//*[@name='role_id']"
    User_Rolee = f"//*[@name='role_id']/option[@value='{Role}']"
    User_Email = "//*[@class='campaign-field-wrapper mb-15']/input[@placeholder='Enter Email']"
    User_Password = "//*[@class='campaign-field-wrapper mb-15']/input[@id='password']"
    C_User_Password = "//*[@class='campaign-field-wrapper mb-15']/input[@id='password1']"
    Create_User_button = "//*[@class='modal-footer']/button[contains(normalize-space(), 'Add User')]"
    User_Pop_up = "//*[@role='alert']"
    User_Search = "//*[@class='search-field-outer']/input"
    User = f"//tbody/tr/td/div[@class='d-flex align-items-center']//div[normalize-space() = '{USERName}']"
    C_User = f"//*[@class='dropdown']/div/a[contains(normalize-space(), '{USERName}')]"
    User_Logoutt = "//*[@class='dropdown']"
    User_Logout = "//*[@class='dropdown']/div/a[contains(normalize-space(), 'Logout')]"

class Campaigns:
    Campaign_btn_M = "//*[@class='nav-item']/a[contains(normalize-space(), 'Campaigns')]"
    Campaign_btn = "//*[@class='container']//a[@class='createusercamapignid-1'][contains(normalize-space(), 'Create New Campaign')]"
    Campaign_page = "//*[@class='add-compaign-wrapper']"
    # Keyword_list = "div.potential-keywords:not(.Local-keywords)  ul.potential-keyword-list li"
    Keyword_list = "//*[@class='potential-keywords']/ul/li/a"
    Keyword_con = "//*[@class='potential-keywords']/ul/li"
    Campaign_Input = "//*[@class='campaign-field-wrapper mb-40 camp-name']/input"
    dropdown_xpath = "//select[@name='client']"
    GMC_CID_input = "//*[@class='dd-select-field-outer select-location-field']/input"
    GMC_CID_btn = "//*[@class='campaign-field-wrapper mb-40']//button[contains(normalize-space(), 'Check')]"
    Submit_btn = "//*[@class='keyword-wrapper']//button[contains(normalize-space(), 'Submit for Analysis')]"
    # Cam_Pop_up = "//*[@role='alert']"
    Cam_Pop_up = "//*[@id='popUpMessage']"
    in_c_gmb = "//*[@class='potential-keywords'][contains(normalize-space(), 'Incorrect CID, Please try again')]/ul"
    Noti_btn = "//*[@id='navbarSupportedContent']/ul[@class='admin-panel-list']/li/a"

class Quickanalysis:
    Quick_btn = "//nav//li[contains(normalize-space(), 'Quick Analysis')]/a"
    Quick_page = "//div[@class='add-compaign-wrapper'][contains(normalize-space(), 'Create Quick Campaign')]"
    Enter_CID = "//*[@class='campaign-field-wrapper mb-40']//input[@placeholder='Enter GMB CID']"
    Check_btn = "//button[contains(normalize-space(), 'Check')]"
    Keyword_con = "//*[@class='potential-keywords']/ul/li"
    Keyword_list = "//*[@class='potential-keywords']/ul/li/a"
    submit_btn = "//button[contains(normalize-space(), 'Submit for Analysis')]"
    Cam_Pop_up = "//*[@role='alert']"
    # Notifications = f"//*[@class='card-body'][contains(normalize-space(), 'Your campaign {Q_Business_name} quick analysis completed.')]"
    Notifications = f"//*[@class='card text-white notification-unread-bg mb-3 nf-card  '][contains(normalize-space(), 'few seconds ago')]/*[@class='card-body'][contains(normalize-space(), 'Your campaign {Q_Business_name} quick analysis completed.')]/h6"
    notifications = f"//*[@class='card text-white notification-unread-bg mb-3 nf-card  '][contains(normalize-space(), 'few seconds ago')]/*[@class='card-body'][contains(normalize-space(), 'Your campaign {Campaign_namee} quick analysis completed.')]/h6"
    otifications = f"//*[@class='card text-white notification-unread-bg mb-3 nf-card  '][contains(normalize-space(), '1 minute ago')]/*[@class='card-body'][contains(normalize-space(), 'Your campaign {Campaign_namee} quick analysis completed.')]/h6"
    Notification = "//*[@id='navbarSupportedContent']//ul[@class='admin-panel-list']/li/a"
    Campaign = f"//table[@id='queriesDataQuickCompleted']//td[contains(normalize-space(), '{Q_Business_name}')]"
    CCampaign = f"//tbody/tr/td/div/h6[contains(normalize-space(), '{Campaign_namee}')]"
    Q_Campaign_btn = "//*[@class='campaign-listing-wrapper']//li/button[@id='campaign-tab06']"
    edit_Campaign = f"//table[@id='queriesDataQuickCompleted']//tr[contains(normalize-space(), '{Q_Business_name}')]//td/div[@class='assign-campaign-box']"
    edit_Campaignn = f"//table[@id='queriesDataQuickCompleted']//tr[contains(normalize-space(), '{Q_Business_name}')]//td/div[@class='assign-campaign-box']//li/a[contains(normalize-space(), 'Edit Campaign')]"
    edit_Campaign_pg = "//*[@class='add-compaign-wrapper edit-campaign-wrapper'][contains(normalize-space(), 'Edit Campaign')]"
    edit_Campaign_name = "//*[@class='add-compaign-inner']//*[@class='campaign-field-wrapper mb-3']//input[@placeholder='Campaign Name']"
    edit_Campaign_namee = "//*[@class='add-compaign-inner']//*[@class='campaign-field-wrapper mb-3']//input[@placeholder='Campaign Name']"
    edit_Campaign_submit = "//div/input[@class='submit-analysis']"
    Del_Campaign = "//tbody/tr[contains(normalize-space(), 'Sqa house')]/td/div[@class='assign-campaign-box']//ul/li[contains(normalize-space(), 'Delete')]/a"
    Del_Campaign_pop = "//*[@class='modal-content'][contains(normalize-space(), 'Are you sure you want to delete this campaign')]"
    Del_Campaignn = "//*[@class='modal-content'][contains(normalize-space(), 'Are you sure you want to delete this campaign')]//button[@id='delete-confirm-campaign-yes-button']"
    Campaign_btn_M = "//*[@class='nav-item']/a[contains(normalize-space(), 'Campaigns')]"
    Q_Campaign_btnb = "//*[@id='queriesDataQuickCompleted']/tbody/tr"
    in_c_gmb = "//*[@class='potential-keywords'][contains(normalize-space(), 'Incorrect CID, Please try again')]/ul"
    Q_Campaign = "//*[@id='queriesDataQuickCompleted_filter']//input"
    Q_Campaign_table = f"//table[@id='queriesDataQuickCompleted']//tr[contains(normalize-space(), '{Q_Business_name}')]"