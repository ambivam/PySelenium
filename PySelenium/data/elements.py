#*********************Login-Page*****************************
UserNameEle = "xpath_//input[@type='text']"
PasswordEle = "xpath_//input[@type='password']"
SignInEle = "xpath_//button[@type='submit']"
ShowingEle = "xpath_//*[@id='page-content-wrapper']//select[@ng-model='selectedObj.val']"
LoginEle = "xpath_//*[text()='Login']"
#*******************Admin landing page***********************
AdminLogoutAvatar = "xpath_//*[@id='wrapper']//img[@alt='Avatar']"
AdminCreateSolution = "xpath_//*[@id='wrapper']//button[@class='btn btn-custom']"
AdminLogout = "xpath_//*[@id='wrapper']//a[@ng-click='logout()']"
AdminWelcomeText = "xpath_//*[@id='page-content-wrapper']//p[text()='Welcome to User Management Page']"

#*********************Configuration-Source*****************************
SourceEle = "xpath_//*[@id='demo']//a/span[text()='Source']"
#IngestFileBrowseEle = "xpath_//*[@id='page-content-wrapper']//input[@type='file']"
IngestFileBrowseEle = "xpath_//input[@name='file']"
ConfigurationEle = "xpath_//*[@id='menu']//a/span[text()='Configuration ']"
IngestFileUploadEle = "xpath_//*[@id='page-content-wrapper']//button[text()='Upload']"
#********************Dashboard*****************************************
SearchTextFieldEle = "xpath_//*[@id='page-content-wrapper']//input[@ng-model='searchValue']"
SearchButtonEle = "xpath_//*[@id='page-content-wrapper']//button[@type='button']"
DashboardLinkEle = "xpath_//*[@id='menu']//a/span[text()='Dashboard']"