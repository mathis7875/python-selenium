from selenium.webdriver.common.by import By


class LoginPage:

     usernameById= (By.ID, "username")#id
     passwordById = (By.ID, "password")#id
     submitByName= (By.NAME, "Submit") #name
     logout = (By.PARTIAL_LINK_TEXT,"/logout")
     login_link = (By.ID,"login-link")
 

class HomePage:

#left-menu Account
    accountlinkByText = (By.NAME, "account")

#Left Sub-Menu Account dropdown menu list
    premiummembershipByText = (By.NAME,"Premium Membership")
    accounthistorystatementsByText = (By.NAME,"Account History/Statements")
    ltransactionhistoryByText = (By.NAME,"L$ Transaction History")
    processcreditByText = (By.NAME,"Process Credit")
    processcredithistoryByText = (By.NAME,"Process Credit History")
    changeemailsettingsByText = (By.NAME,"Change Email Settings")
    scriptedagentstatusByText = (By.NAME,"Scripted Agent Status")
    meshuploadstatusByText = (By.NAME,"Mesh Upload Status")
    changenameByText = (By.NAME,"Change Name")
    changepasswordByText = (By.NAME,"Change Password")
    partnersByText = (By.NAME,"Partners")
    billinginformationByText =(By.NAME, "Billing Information")
    deleteaccountByText =(By.NAME, "Delete Account")
    welcomeHeader = (By.LINK_TEXT,"/my/account?lang=en-US")
    accountmenubuttonByLink =(By.LINK_TEXT,"/my/account/?lang=en-US")

    #left-menu Event
    eventslinkByText = (By.NAME,"")
    #Left Sub-Menu Events dropdown menu list

    #left-menu Shop
    shoplinkByText = (By.NAME,"Shop")

    #Left Sub-Menu Shop dropdown menu list
    favoritesByText = (By.NAME,"Favorites")
    shoppinghistoryByText = (By.NAME,"Shopping History")
    ratemypurchaseeByText = (By.NAME,"Rate My Purchases")
    myfundsByText = (By.NAME,"My Funds")

    #left-menu Land Manager
    landmanagerlinkByText = (By.NAME,"Land Manager")

    #Left Sub- Menu Land 
    grouplandByText =(By.NAME, "Group Land")
    landusefeesByText = (By.NAME,"Land Use Fees")
    mymainlandByText = (By.NAME,"My Mainland")
    myregionsByText = (By.NAME,"My Regions")


    #Bottom header footer
    lindenlabheaderByText = (By.NAME,"//*[@id='footerLinks' and contains(text(),'Linden Lab)]")
    tiliaheaderByText = (By.NAME,"//*[@id='footerLinks' and contains(text(),'Tilia')]")
    secondlifeheaderByText= (By.NAME,"//*[@id='footerLinks' and contains(text(),'Second Life')]")
    connectwithusheaderByText = (By.NAME,"//*[@id='footerLinks' and contains(text(),'Connect With Us')]")
    partnerwithusheaderByText = (By.NAME,"//*[@id='footerLinks' and contains(text(),'Partner With Us')]")


class AccountHistoryStatement:


    viewbttnText = (By.NAME,"")
    selectmonthId = (By.NAME,"")
    startdateId = (By.NAME,"startDate")
    enddateId = (By.NAME,"endDate")
    filterontextbttnId =(By.NAME, "")
    clearbttnID = (By.NAME,"")


class ProcessCreditHistory:

    filterprocesscreditByText = (By.NAME,"")
    filterbttnByText = (By.NAME,"")
    clearbttnBytext = (By.NAME,"")

class LindenTransactions: 

    daterangeStartByText = (By.NAME,"startDate")
    daterangeEndByText = (By.NAME,"endDate")
    viewbttnByText = (By.NAME,"")#is Type
    filtrtransactionsByName = (By.NAME,"orm-control search-field input-sm ng-pristine ng-valid")
    filterbttnByXpath = (By.NAME,"")
    clearbttnByXpath = (By.NAME,"")

class ChangeEmailPage:

    newemailaddressById = (By.NAME,"preNewEmail")
    confirmemailById = (By.NAME,"preConfirmEmail")
    saveemailDById = (By.NAME,"SaveEmailButton")
    saveimById = (By.NAME,"SaveIMButton")
    subscribedcheckbxById = (By.NAME,"id_pre_subscription_0")
    unsubscribedcheckbxById = (By.NAME,"id_pre_subscription_1")
    savesubscriptionById = (By.NAME,"SaveSubButton")


class BillingInformationPage:

#your Accounts section
    lbalanceByText = (By.NAME,"Transaction History")
    tilliabalanceByText = (By.NAME,"Account History")
    additionalinfoByText = (By.NAME,"additional information")

    #other payment methods
    addcreditcardByText = (By.NAME,"Add a Credit Card")
    addpaypalyText = (By.NAME,"Add a PayPal account")
    addskrillByText = (By.NAME,"Add a Skrill account")

    #gst - goods and services tax 
    changecountryByText = (By.NAME,"Change")
    addabnByText = (By.NAME,"")

  

class MarketPlace:
    
    #login link
    login_link = (By.ID,"login-link")

    #items tab
    search_in = (By.NAME, "12") #dropdown list
    show_maturity_levels = (By.NAME, "12") 
    item_keywords = (By.ID, "keywords") #search input field
    search = (By.NAME, "12") #button 
    product_search_bttn = (By.ID, "product-search-submit")

    #merchant store tab
    search_merchant_store_Tab = (By.ID, "link-merchant-search")
    search_merchant_by_keyword = (By.ID, "merchant-search-keywords")
    merchant_search_button = (By.ID, "merchant-search-submit")
    slm01_store = (By.XPATH, "//*[@id='store_48246']")
    #items arrangement icons 

    listview = (By.CLASS_NAME, "search-layout list-view marketplace-sprite")
    galleryview = (By.CLASS_NAME, "search-layout gallery-view marketplace-sprite")
    thumbnailview = (By.CLASS_NAME, "search-layout thumbnails-view marketplace-sprite")

    #purchase item page 
    add_to_cart = (By.ID, "add-to-cart-button")
    add_to_cart_gift = (By.ID, "add-as-gift-button") #button 
    cart = (By.CLASS_NAME, "marketplace-sprite") #href link
    buy_now_bttn = (By.ID, "buy-now-button")

    #Shopping cart page 
    check_out = (By.ID, "cart-checkout-button") # button 
    update_quantities = (By.ID, "update-quantities") #button
    return_to_marketplace = (By.CLASS_NAME, "button continue") #href link

    #market place flash notice for free items page
    place_your_order_notice = (By.ID, "flash_notice")
    place_your_order_bttn = (By.CLASS_NAME, "button cart-button")

    #market place menu drop down 
    my_account = (By.LINK_TEXT, " My account")
    create_a_store = (By.LINK_TEXT, "Create a Store")
    my_favorites = (By.LINK_TEXT, "favorites")
    #my_favorites_stores (By.LINK_TEXT, "My favorites stores")
    my_wishlist = (By.LINK_TEXT, "My wishlist")
    merchant_home = (By.LINK_TEXT, "Merchant home")

    #Market place Assert values
    item_search_results = (By.XPATH, "//*[@id='search-results-container']/div[1]/h1")
  

class CashierPage:
    buy_now_bttn = (By.ID, "buy")
    
    #cashier assert values
    payment_successful = (By.ID, "DeliverySuccessAlert")



class MerchantHome:

   #Left merchant home menu Inventory 
    manage_listings = (By.LINK_TEXT, "Manage listings")
    manage_subscriptions = (By.LINK_TEXT, "Manage subscriptions")
    import_failure_log = (By.LINK_TEXT, "Import failure log")
    view_audit_logs = (By.LINK_TEXT, "view audit logs")

    #Left merchant home menu orders
    transaction_history = (By.LINK_TEXT, "Transaction history")

    #Left merchant home reports 
    top_selling_products = (By.LINK_TEXT, "")
    top_searched_products = (By.LINK_TEXT, "")
    listing_enhancement = (By.LINK_TEXT, "")
    revenue_distributions = (By.LINK_TEXT, "")
    orders  = (By.LINK_TEXT, "")

    #Left merchant home store setup 
    edit_store_imformation = (By.LINK_TEXT, "")
    view_my_store = (By.LINK_TEXT, "")
    automatic_notifications = (By.LINK_TEXT, "")

    #Left merchant home menu help resources
    merchant_help = (By.LINK_TEXT, "")
    discussion_forums = (By.LINK_TEXT, "") 
    ll_terms_of_conditions = (By.LINK_TEXT, "")
    fee_and_listings_policies = (By.LINK_TEXT, "")
    managing_your_store = (By.LINK_TEXT, "")



#Examples below ----------------------------