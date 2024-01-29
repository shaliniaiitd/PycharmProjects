from framework.ui.base.base_page import BasePage


class HomePage(BasePage):
    link_welcome_username = "xpath|//a[@title='Edit your details']"
    btn_nav_daily_status_entry = "xpath|//td[@class='wpn_menu']//a[text()='Daily Status Entry']"
    btn_nav_my_profile = "xpath|//td[@class='wpn_menu']//a[text()='My Profile']"
    tb_daily_date_box = "xpath|//input[@name='date']"
    btn_daily_hours_spent = "xpath|//input[@value='Hours Spent']"
    tb_daily_nth_row_hours_spent_dynamic = "xpath|//form/..//tr[@class='dailyheader'][2]/following-sibling::tr[{}]/td[@class='project_name']/label"
    tb_daily_nth_row_comments_dynamic = "xpath|//form/..//tr[@class='dailyheader'][2]/following-sibling::tr[{}]/td[3]/textarea"
    ddn_daily_nth_row_start_hour_dynamic = "xpath|//form/..//tr[@class='dailyheader'][2]/following-sibling::tr[{}]/td[@class='npj_start_time']/select[@name='nonpro_start_hour[]']"
    ddn_daily_nth_row_start_min_dynamic = "xpath|//form/..//tr[@class='dailyheader'][2]/following-sibling::tr[{}]/td[@class='npj_start_time']/select[@name='nonpro_start_min[]']"
    ddn_daily_nth_row_start_ampm_dynamic = "xpath|//form/..//tr[@class='dailyheader'][2]/following-sibling::tr[{}]/td[@class='npj_start_time']/select[@name='nonpro_start_am[]']"
    ddn_daily_nth_row_end_hour_dynamic = "xpath|//form/..//tr[@class='dailyheader'][2]/following-sibling::tr[{}]/td[@class='npj_end_time']/select[@name='nonpro_end_hour[]']"
    ddn_daily_nth_row_end_min_dynamic = "xpath|//form/..//tr[@class='dailyheader'][2]/following-sibling::tr[{}]/td[@class='npj_end_time']/select[@name='nonpro_end_min[]']"
    ddn_daily_nth_row_end_ampm_dynamic = "xpath|//form/..//tr[@class='dailyheader'][2]/following-sibling::tr[{}]/td[@class='npj_end_time']/select[@name='nonpro_end_am[]']"
    btn_daily_save = "xpath|//input[@value='Save Time Status']"
    btn_daily_clear = "xpath|//input[@value='Clear']"
    btn_daily_back = "xpath|//input[@value='Back']"
    lb_daily_success = "xpath|//td[@align='center'][text()='Time Sheet Status Saved Successfully']"
    btn_weekly_previous = "xpath|//input[@name='previous']"
    btn_weekly_current = "xpath|//input[@name='current']"
    btn_weekly_next = "xpath|//input[@name='next']"
    lb_weekly_nth_day_dynamic = "xpath|//tr[@class='headerStyle']/td[{}]"
    tb_weekly_mon_nth_project_hours_dynamic = "xpath|//tr[@class='projectsums'][{}]/td[2]/input[@id='projectsum']"
    tb_weekly_tue_nth_project_hours_dynamic = "xpath|//tr[@class='projectsums'][{}]/td[3]/input[@id='projectsum']"
    tb_weekly_wed_nth_project_hours_dynamic = "xpath|//tr[@class='projectsums'][{}]/td[4]/input[@id='projectsum']"
    tb_weekly_thu_nth_project_hours_dynamic = "xpath|//tr[@class='projectsums'][{}]/td[5]/input[@id='projectsum']"
    tb_weekly_fri_nth_project_hours_dynamic = "xpath|//tr[@class='projectsums'][{}]/td[6]/input[@id='projectsum']"
    tb_weekly_sat_nth_project_hours_dynamic = "xpath|//tr[@class='projectsums'][{}]/td[7]/input[@id='projectsum']"
    tb_weekly_sun_nth_project_hours_dynamic = "xpath|//tr[@class='projectsums'][{}]/td[8]/input[@id='projectsum']"
    tb_weekly_sum_nth_project_hours_dynamic = "xpath|//tr[@class='projectsums'][{}]/td[@class='footerstyle']"
    btn_weekly_save = "xpath|//input[@value='Save Time Status']"
    btn_weekly_submit = "xpath|//input[@value='Submit Time status']"
    btn_weekly_clear = "xpath|//input[@value='Clear']"
    lb_weekly_save_success = "xpath|//td[@align='center'][text()='Time Sheet Status Saved Successfully with status as pending. Your timesheet status will not be displayed on report page until you hit the Submit Time Status button.']"
    lb_weekly_submit_success = "xpath|//td[@align='center'][text()='Time Sheet Status Saved Successfully. You could not reenter timesheet status again.']"
    tb_profile_first_name = "xpath|//input[@name='first_name']"
    tb_profile_last_name = "xpath|//input[@name='last_name']"
    tb_profile_doj = "xpath|//input[@name='date_of_join']"

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)

    def get_text_link_welcome_username(self):
        # This is the function to perform getText on web element link_welcome_username
        return self.do.get_text(self.link_welcome_username)

    def click_btn_nav_daily_status_entry(self):
        # This is the function to perform click on web element btn_nav_daily_status_entry
        self.do.click(self.btn_nav_daily_status_entry)
        return self

    def click_btn_nav_my_profile(self):
        # This is the function to perform click on web element btn_nav_my_profile
        self.do.click(self.btn_nav_my_profile)
        return self

    def input_text_tb_daily_date_box(self, text):
        # This is the function to perform setText on web element tb_daily_date_box
        self.do.input_text(self.tb_daily_date_box, text)
        return self

    def click_btn_daily_hours_spent(self):
        # This is the function to perform click on web element btn_daily_hours_spent
        self.do.click(self.btn_daily_hours_spent)
        return self

    def get_value_tb_daily_nth_row_hours_spent_dynamic(self, dynamic_text):
        # This is the function to perform getValue on web element tb_daily_nth_row_hours_spent_dynamic
        return self.do.get_value(self.tb_daily_nth_row_hours_spent_dynamic.format(dynamic_text))

    def clear_value_tb_daily_nth_row_hours_spent_dynamic(self, dynamic_text):
        # This is the function to perform clearText on web element tb_daily_nth_row_hours_spent_dynamic
        self.do.clear_value(self.tb_daily_nth_row_hours_spent_dynamic.format(dynamic_text))
        return self

    def input_text_tb_daily_nth_row_hours_spent_dynamic(self, text, dynamic_text):
        # This is the function to perform setText on web element tb_daily_nth_row_hours_spent_dynamic
        self.do.input_text(self.tb_daily_nth_row_hours_spent_dynamic.format(dynamic_text), text)
        return self

    def get_attribute_tb_daily_nth_row_hours_spent_dynamic(self, attribute, dynamic_text):
        # This is the function to perform getAttribute on web element tb_daily_nth_row_hours_spent_dynamic
        return self.do.get_attribute(self.tb_daily_nth_row_hours_spent_dynamic.format(dynamic_text), attribute)

    def get_value_tb_daily_nth_row_comments_dynamic(self, dynamic_text):
        # This is the function to perform getValue on web element tb_daily_nth_row_comments_dynamic
        return self.do.get_value(self.tb_daily_nth_row_comments_dynamic.format(dynamic_text))

    def clear_value_tb_daily_nth_row_comments_dynamic(self, dynamic_text):
        # This is the function to perform clearText on web element tb_daily_nth_row_comments_dynamic
        self.do.clear_value(self.tb_daily_nth_row_comments_dynamic.format(dynamic_text))
        return self

    def input_text_tb_daily_nth_row_comments_dynamic(self, text, dynamic_text):
        # This is the function to perform setText on web element tb_daily_nth_row_comments_dynamic
        self.do.input_text(self.tb_daily_nth_row_comments_dynamic.format(dynamic_text), text)
        return self

    def get_attribute_tb_daily_nth_row_comments_dynamic(self, attribute, dynamic_text):
        # This is the function to perform getAttribute on web element tb_daily_nth_row_comments_dynamic
        return self.do.get_attribute(self.tb_daily_nth_row_comments_dynamic.format(dynamic_text), attribute)

    def drop_down_select_item_by_index_ddn_daily_nth_row_start_hour_dynamic(self, index, dynamic_text):
        # This is the function to perform selectByIndex on web element ddn_daily_nth_row_start_hour_dynamic
        self.do.drop_down_select_item_by_index(self.ddn_daily_nth_row_start_hour_dynamic.format(dynamic_text), index)
        return self

    def drop_down_select_item_by_value_ddn_daily_nth_row_start_hour_dynamic(self, value, dynamic_text):
        # This is the function to perform selectByValue on web element ddn_daily_nth_row_start_hour_dynamic
        self.do.drop_down_select_item_by_value(self.ddn_daily_nth_row_start_hour_dynamic.format(dynamic_text), value)
        return self

    def drop_down_select_item_by_text_ddn_daily_nth_row_start_hour_dynamic(self, text, dynamic_text):
        # This is the function to perform selectByText on web element ddn_daily_nth_row_start_hour_dynamic
        self.do.drop_down_select_item_by_text(self.ddn_daily_nth_row_start_hour_dynamic.format(dynamic_text), text)
        return self

    def drop_down_get_selected_value_ddn_daily_nth_row_start_hour_dynamic(self, dynamic_text):
        # This is the function to perform getSelectedValue on web element ddn_daily_nth_row_start_hour_dynamic
        return self.do.drop_down_get_selected_value(self.ddn_daily_nth_row_start_hour_dynamic.format(dynamic_text))

    def drop_down_get_selected_text_ddn_daily_nth_row_start_hour_dynamic(self, dynamic_text):
        # This is the function to perform getSelectedText on web element ddn_daily_nth_row_start_hour_dynamic
        return self.do.drop_down_get_selected_text(self.ddn_daily_nth_row_start_hour_dynamic.format(dynamic_text))

    def drop_down_select_item_by_index_ddn_daily_nth_row_start_min_dynamic(self, index, dynamic_text):
        # This is the function to perform selectByIndex on web element ddn_daily_nth_row_start_min_dynamic
        self.do.drop_down_select_item_by_index(self.ddn_daily_nth_row_start_min_dynamic.format(dynamic_text), index)
        return self

    def drop_down_select_item_by_value_ddn_daily_nth_row_start_min_dynamic(self, value, dynamic_text):
        # This is the function to perform selectByValue on web element ddn_daily_nth_row_start_min_dynamic
        self.do.drop_down_select_item_by_value(self.ddn_daily_nth_row_start_min_dynamic.format(dynamic_text), value)
        return self

    def drop_down_select_item_by_text_ddn_daily_nth_row_start_min_dynamic(self, text, dynamic_text):
        # This is the function to perform selectByText on web element ddn_daily_nth_row_start_min_dynamic
        self.do.drop_down_select_item_by_text(self.ddn_daily_nth_row_start_min_dynamic.format(dynamic_text), text)
        return self

    def drop_down_get_selected_value_ddn_daily_nth_row_start_min_dynamic(self, dynamic_text):
        # This is the function to perform getSelectedValue on web element ddn_daily_nth_row_start_min_dynamic
        return self.do.drop_down_get_selected_value(self.ddn_daily_nth_row_start_min_dynamic.format(dynamic_text))

    def drop_down_get_selected_text_ddn_daily_nth_row_start_min_dynamic(self, dynamic_text):
        # This is the function to perform getSelectedText on web element ddn_daily_nth_row_start_min_dynamic
        return self.do.drop_down_get_selected_text(self.ddn_daily_nth_row_start_min_dynamic.format(dynamic_text))

    def drop_down_select_item_by_index_ddn_daily_nth_row_start_ampm_dynamic(self, index, dynamic_text):
        # This is the function to perform selectByIndex on web element ddn_daily_nth_row_start_ampm_dynamic
        self.do.drop_down_select_item_by_index(self.ddn_daily_nth_row_start_ampm_dynamic.format(dynamic_text), index)
        return self

    def drop_down_select_item_by_value_ddn_daily_nth_row_start_ampm_dynamic(self, value, dynamic_text):
        # This is the function to perform selectByValue on web element ddn_daily_nth_row_start_ampm_dynamic
        self.do.drop_down_select_item_by_value(self.ddn_daily_nth_row_start_ampm_dynamic.format(dynamic_text), value)
        return self

    def drop_down_select_item_by_text_ddn_daily_nth_row_start_ampm_dynamic(self, text, dynamic_text):
        # This is the function to perform selectByText on web element ddn_daily_nth_row_start_ampm_dynamic
        self.do.drop_down_select_item_by_text(self.ddn_daily_nth_row_start_ampm_dynamic.format(dynamic_text), text)
        return self

    def drop_down_get_selected_value_ddn_daily_nth_row_start_ampm_dynamic(self, dynamic_text):
        # This is the function to perform getSelectedValue on web element ddn_daily_nth_row_start_ampm_dynamic
        return self.do.drop_down_get_selected_value(self.ddn_daily_nth_row_start_ampm_dynamic.format(dynamic_text))

    def drop_down_get_selected_text_ddn_daily_nth_row_start_ampm_dynamic(self, dynamic_text):
        # This is the function to perform getSelectedText on web element ddn_daily_nth_row_start_ampm_dynamic
        return self.do.drop_down_get_selected_text(self.ddn_daily_nth_row_start_ampm_dynamic.format(dynamic_text))

    def drop_down_select_item_by_index_ddn_daily_nth_row_end_hour_dynamic(self, index, dynamic_text):
        # This is the function to perform selectByIndex on web element ddn_daily_nth_row_end_hour_dynamic
        self.do.drop_down_select_item_by_index(self.ddn_daily_nth_row_end_hour_dynamic.format(dynamic_text), index)
        return self

    def drop_down_select_item_by_value_ddn_daily_nth_row_end_hour_dynamic(self, value, dynamic_text):
        # This is the function to perform selectByValue on web element ddn_daily_nth_row_end_hour_dynamic
        self.do.drop_down_select_item_by_value(self.ddn_daily_nth_row_end_hour_dynamic.format(dynamic_text), value)
        return self

    def drop_down_select_item_by_text_ddn_daily_nth_row_end_hour_dynamic(self, text, dynamic_text):
        # This is the function to perform selectByText on web element ddn_daily_nth_row_end_hour_dynamic
        self.do.drop_down_select_item_by_text(self.ddn_daily_nth_row_end_hour_dynamic.format(dynamic_text), text)
        return self

    def drop_down_get_selected_value_ddn_daily_nth_row_end_hour_dynamic(self, dynamic_text):
        # This is the function to perform getSelectedValue on web element ddn_daily_nth_row_end_hour_dynamic
        return self.do.drop_down_get_selected_value(self.ddn_daily_nth_row_end_hour_dynamic.format(dynamic_text))

    def drop_down_get_selected_text_ddn_daily_nth_row_end_hour_dynamic(self, dynamic_text):
        # This is the function to perform getSelectedText on web element ddn_daily_nth_row_end_hour_dynamic
        return self.do.drop_down_get_selected_text(self.ddn_daily_nth_row_end_hour_dynamic.format(dynamic_text))

    def drop_down_select_item_by_index_ddn_daily_nth_row_end_min_dynamic(self, index, dynamic_text):
        # This is the function to perform selectByIndex on web element ddn_daily_nth_row_end_min_dynamic
        self.do.drop_down_select_item_by_index(self.ddn_daily_nth_row_end_min_dynamic.format(dynamic_text), index)
        return self

    def drop_down_select_item_by_value_ddn_daily_nth_row_end_min_dynamic(self, value, dynamic_text):
        # This is the function to perform selectByValue on web element ddn_daily_nth_row_end_min_dynamic
        self.do.drop_down_select_item_by_value(self.ddn_daily_nth_row_end_min_dynamic.format(dynamic_text), value)
        return self

    def drop_down_select_item_by_text_ddn_daily_nth_row_end_min_dynamic(self, text, dynamic_text):
        # This is the function to perform selectByText on web element ddn_daily_nth_row_end_min_dynamic
        self.do.drop_down_select_item_by_text(self.ddn_daily_nth_row_end_min_dynamic.format(dynamic_text), text)
        return self

    def drop_down_get_selected_value_ddn_daily_nth_row_end_min_dynamic(self, dynamic_text):
        # This is the function to perform getSelectedValue on web element ddn_daily_nth_row_end_min_dynamic
        return self.do.drop_down_get_selected_value(self.ddn_daily_nth_row_end_min_dynamic.format(dynamic_text))

    def drop_down_get_selected_text_ddn_daily_nth_row_end_min_dynamic(self, dynamic_text):
        # This is the function to perform getSelectedText on web element ddn_daily_nth_row_end_min_dynamic
        return self.do.drop_down_get_selected_text(self.ddn_daily_nth_row_end_min_dynamic.format(dynamic_text))

    def drop_down_select_item_by_index_ddn_daily_nth_row_end_ampm_dynamic(self, index, dynamic_text):
        # This is the function to perform selectByIndex on web element ddn_daily_nth_row_end_ampm_dynamic
        self.do.drop_down_select_item_by_index(self.ddn_daily_nth_row_end_ampm_dynamic.format(dynamic_text), index)
        return self

    def drop_down_select_item_by_value_ddn_daily_nth_row_end_ampm_dynamic(self, value, dynamic_text):
        # This is the function to perform selectByValue on web element ddn_daily_nth_row_end_ampm_dynamic
        self.do.drop_down_select_item_by_value(self.ddn_daily_nth_row_end_ampm_dynamic.format(dynamic_text), value)
        return self

    def drop_down_select_item_by_text_ddn_daily_nth_row_end_ampm_dynamic(self, text, dynamic_text):
        # This is the function to perform selectByText on web element ddn_daily_nth_row_end_ampm_dynamic
        self.do.drop_down_select_item_by_text(self.ddn_daily_nth_row_end_ampm_dynamic.format(dynamic_text), text)
        return self

    def drop_down_get_selected_value_ddn_daily_nth_row_end_ampm_dynamic(self, dynamic_text):
        # This is the function to perform getSelectedValue on web element ddn_daily_nth_row_end_ampm_dynamic
        return self.do.drop_down_get_selected_value(self.ddn_daily_nth_row_end_ampm_dynamic.format(dynamic_text))

    def drop_down_get_selected_text_ddn_daily_nth_row_end_ampm_dynamic(self, dynamic_text):
        # This is the function to perform getSelectedText on web element ddn_daily_nth_row_end_ampm_dynamic
        return self.do.drop_down_get_selected_text(self.ddn_daily_nth_row_end_ampm_dynamic.format(dynamic_text))

    def click_btn_daily_save(self):
        # This is the function to perform click on web element btn_daily_save
        self.do.click(self.btn_daily_save)
        return self

    def click_btn_daily_clear(self):
        # This is the function to perform click on web element btn_daily_clear
        self.do.click(self.btn_daily_clear)
        return self

    def click_btn_daily_back(self):
        # This is the function to perform click on web element btn_daily_back
        self.do.click(self.btn_daily_back)
        return self

    def get_text_lb_daily_success(self):
        # This is the function to perform getText on web element lb_daily_success
        return self.do.get_text(self.lb_daily_success)

    def click_btn_weekly_previous(self):
        # This is the function to perform click on web element btn_weekly_previous
        self.do.click(self.btn_weekly_previous)
        return self

    def click_btn_weekly_current(self):
        # This is the function to perform click on web element btn_weekly_current
        self.do.click(self.btn_weekly_current)
        return self

    def click_btn_weekly_next(self):
        # This is the function to perform click on web element btn_weekly_next
        self.do.click(self.btn_weekly_next)
        return self

    def get_text_lb_weekly_nth_day_dynamic(self, dynamic_text):
        # This is the function to perform getText on web element lb_weekly_nth_day_dynamic
        return self.do.get_text(self.lb_weekly_nth_day_dynamic.format(dynamic_text))

    def get_value_tb_weekly_mon_nth_project_hours_dynamic(self, dynamic_text):
        # This is the function to perform getValue on web element tb_weekly_mon_nth_project_hours_dynamic
        return self.do.get_value(self.tb_weekly_mon_nth_project_hours_dynamic.format(dynamic_text))

    def clear_value_tb_weekly_mon_nth_project_hours_dynamic(self, dynamic_text):
        # This is the function to perform clearText on web element tb_weekly_mon_nth_project_hours_dynamic
        self.do.clear_value(self.tb_weekly_mon_nth_project_hours_dynamic.format(dynamic_text))
        return self

    def input_text_tb_weekly_mon_nth_project_hours_dynamic(self, text, dynamic_text):
        # This is the function to perform setText on web element tb_weekly_mon_nth_project_hours_dynamic
        self.do.input_text(self.tb_weekly_mon_nth_project_hours_dynamic.format(dynamic_text), text)
        return self

    def get_attribute_tb_weekly_mon_nth_project_hours_dynamic(self, attribute, dynamic_text):
        # This is the function to perform getAttribute on web element tb_weekly_mon_nth_project_hours_dynamic
        return self.do.get_attribute(self.tb_weekly_mon_nth_project_hours_dynamic.format(dynamic_text), attribute)

    def get_value_tb_weekly_tue_nth_project_hours_dynamic(self, dynamic_text):
        # This is the function to perform getValue on web element tb_weekly_tue_nth_project_hours_dynamic
        return self.do.get_value(self.tb_weekly_tue_nth_project_hours_dynamic.format(dynamic_text))

    def clear_value_tb_weekly_tue_nth_project_hours_dynamic(self, dynamic_text):
        # This is the function to perform clearText on web element tb_weekly_tue_nth_project_hours_dynamic
        self.do.clear_value(self.tb_weekly_tue_nth_project_hours_dynamic.format(dynamic_text))
        return self

    def input_text_tb_weekly_tue_nth_project_hours_dynamic(self, text, dynamic_text):
        # This is the function to perform setText on web element tb_weekly_tue_nth_project_hours_dynamic
        self.do.input_text(self.tb_weekly_tue_nth_project_hours_dynamic.format(dynamic_text), text)
        return self

    def get_attribute_tb_weekly_tue_nth_project_hours_dynamic(self, attribute, dynamic_text):
        # This is the function to perform getAttribute on web element tb_weekly_tue_nth_project_hours_dynamic
        return self.do.get_attribute(self.tb_weekly_tue_nth_project_hours_dynamic.format(dynamic_text), attribute)

    def get_value_tb_weekly_wed_nth_project_hours_dynamic(self, dynamic_text):
        # This is the function to perform getValue on web element tb_weekly_wed_nth_project_hours_dynamic
        return self.do.get_value(self.tb_weekly_wed_nth_project_hours_dynamic.format(dynamic_text))

    def clear_value_tb_weekly_wed_nth_project_hours_dynamic(self, dynamic_text):
        # This is the function to perform clearText on web element tb_weekly_wed_nth_project_hours_dynamic
        self.do.clear_value(self.tb_weekly_wed_nth_project_hours_dynamic.format(dynamic_text))
        return self

    def input_text_tb_weekly_wed_nth_project_hours_dynamic(self, text, dynamic_text):
        # This is the function to perform setText on web element tb_weekly_wed_nth_project_hours_dynamic
        self.do.input_text(self.tb_weekly_wed_nth_project_hours_dynamic.format(dynamic_text), text)
        return self

    def get_attribute_tb_weekly_wed_nth_project_hours_dynamic(self, attribute, dynamic_text):
        # This is the function to perform getAttribute on web element tb_weekly_wed_nth_project_hours_dynamic
        return self.do.get_attribute(self.tb_weekly_wed_nth_project_hours_dynamic.format(dynamic_text), attribute)

    def get_value_tb_weekly_thu_nth_project_hours_dynamic(self, dynamic_text):
        # This is the function to perform getValue on web element tb_weekly_thu_nth_project_hours_dynamic
        return self.do.get_value(self.tb_weekly_thu_nth_project_hours_dynamic.format(dynamic_text))

    def clear_value_tb_weekly_thu_nth_project_hours_dynamic(self, dynamic_text):
        # This is the function to perform clearText on web element tb_weekly_thu_nth_project_hours_dynamic
        self.do.clear_value(self.tb_weekly_thu_nth_project_hours_dynamic.format(dynamic_text))
        return self

    def input_text_tb_weekly_thu_nth_project_hours_dynamic(self, text, dynamic_text):
        # This is the function to perform setText on web element tb_weekly_thu_nth_project_hours_dynamic
        self.do.input_text(self.tb_weekly_thu_nth_project_hours_dynamic.format(dynamic_text), text)
        return self

    def get_attribute_tb_weekly_thu_nth_project_hours_dynamic(self, attribute, dynamic_text):
        # This is the function to perform getAttribute on web element tb_weekly_thu_nth_project_hours_dynamic
        return self.do.get_attribute(self.tb_weekly_thu_nth_project_hours_dynamic.format(dynamic_text), attribute)

    def get_value_tb_weekly_fri_nth_project_hours_dynamic(self, dynamic_text):
        # This is the function to perform getValue on web element tb_weekly_fri_nth_project_hours_dynamic
        return self.do.get_value(self.tb_weekly_fri_nth_project_hours_dynamic.format(dynamic_text))

    def clear_value_tb_weekly_fri_nth_project_hours_dynamic(self, dynamic_text):
        # This is the function to perform clearText on web element tb_weekly_fri_nth_project_hours_dynamic
        self.do.clear_value(self.tb_weekly_fri_nth_project_hours_dynamic.format(dynamic_text))
        return self

    def input_text_tb_weekly_fri_nth_project_hours_dynamic(self, text, dynamic_text):
        # This is the function to perform setText on web element tb_weekly_fri_nth_project_hours_dynamic
        self.do.input_text(self.tb_weekly_fri_nth_project_hours_dynamic.format(dynamic_text), text)
        return self

    def get_attribute_tb_weekly_fri_nth_project_hours_dynamic(self, attribute, dynamic_text):
        # This is the function to perform getAttribute on web element tb_weekly_fri_nth_project_hours_dynamic
        return self.do.get_attribute(self.tb_weekly_fri_nth_project_hours_dynamic.format(dynamic_text), attribute)

    def get_value_tb_weekly_sat_nth_project_hours_dynamic(self, dynamic_text):
        # This is the function to perform getValue on web element tb_weekly_sat_nth_project_hours_dynamic
        return self.do.get_value(self.tb_weekly_sat_nth_project_hours_dynamic.format(dynamic_text))

    def clear_value_tb_weekly_sat_nth_project_hours_dynamic(self, dynamic_text):
        # This is the function to perform clearText on web element tb_weekly_sat_nth_project_hours_dynamic
        self.do.clear_value(self.tb_weekly_sat_nth_project_hours_dynamic.format(dynamic_text))
        return self

    def input_text_tb_weekly_sat_nth_project_hours_dynamic(self, text, dynamic_text):
        # This is the function to perform setText on web element tb_weekly_sat_nth_project_hours_dynamic
        self.do.input_text(self.tb_weekly_sat_nth_project_hours_dynamic.format(dynamic_text), text)
        return self

    def get_attribute_tb_weekly_sat_nth_project_hours_dynamic(self, attribute, dynamic_text):
        # This is the function to perform getAttribute on web element tb_weekly_sat_nth_project_hours_dynamic
        return self.do.get_attribute(self.tb_weekly_sat_nth_project_hours_dynamic.format(dynamic_text), attribute)

    def get_value_tb_weekly_sun_nth_project_hours_dynamic(self, dynamic_text):
        # This is the function to perform getValue on web element tb_weekly_sun_nth_project_hours_dynamic
        return self.do.get_value(self.tb_weekly_sun_nth_project_hours_dynamic.format(dynamic_text))

    def clear_value_tb_weekly_sun_nth_project_hours_dynamic(self, dynamic_text):
        # This is the function to perform clearText on web element tb_weekly_sun_nth_project_hours_dynamic
        self.do.clear_value(self.tb_weekly_sun_nth_project_hours_dynamic.format(dynamic_text))
        return self

    def input_text_tb_weekly_sun_nth_project_hours_dynamic(self, text, dynamic_text):
        # This is the function to perform setText on web element tb_weekly_sun_nth_project_hours_dynamic
        self.do.input_text(self.tb_weekly_sun_nth_project_hours_dynamic.format(dynamic_text), text)
        return self

    def get_attribute_tb_weekly_sun_nth_project_hours_dynamic(self, attribute, dynamic_text):
        # This is the function to perform getAttribute on web element tb_weekly_sun_nth_project_hours_dynamic
        return self.do.get_attribute(self.tb_weekly_sun_nth_project_hours_dynamic.format(dynamic_text), attribute)

    def get_value_tb_weekly_sum_nth_project_hours_dynamic(self, dynamic_text):
        # This is the function to perform getValue on web element tb_weekly_sum_nth_project_hours_dynamic
        return self.do.get_value(self.tb_weekly_sum_nth_project_hours_dynamic.format(dynamic_text))

    def get_attribute_tb_weekly_sum_nth_project_hours_dynamic(self, attribute, dynamic_text):
        # This is the function to perform getAttribute on web element tb_weekly_sum_nth_project_hours_dynamic
        return self.do.get_attribute(self.tb_weekly_sum_nth_project_hours_dynamic.format(dynamic_text), attribute)

    def click_btn_weekly_save(self):
        # This is the function to perform click on web element btn_weekly_save
        self.do.click(self.btn_weekly_save)
        return self

    def click_btn_weekly_submit(self):
        # This is the function to perform click on web element btn_weekly_submit
        self.do.click(self.btn_weekly_submit)
        return self

    def click_btn_weekly_clear(self):
        # This is the function to perform click on web element btn_weekly_clear
        self.do.click(self.btn_weekly_clear)
        return self

    def get_text_lb_weekly_save_success(self):
        # This is the function to perform getText on web element lb_weekly_save_success
        return self.do.get_text(self.lb_weekly_save_success)

    def get_text_lb_weekly_submit_success(self):
        # This is the function to perform getText on web element lb_weekly_submit_success
        return self.do.get_text(self.lb_weekly_submit_success)

    def get_value_tb_profile_first_name(self):
        # This is the function to perform getValue on web element tb_profile_first_name
        return self.do.get_value(self.tb_profile_first_name)

    def clear_value_tb_profile_first_name(self):
        # This is the function to perform clearText on web element tb_profile_first_name
        self.do.clear_value(self.tb_profile_first_name)
        return self

    def input_text_tb_profile_first_name(self, text):
        # This is the function to perform setText on web element tb_profile_first_name
        self.do.input_text(self.tb_profile_first_name, text)
        return self

    def get_attribute_tb_profile_first_name(self, attribute):
        # This is the function to perform getAttribute on web element tb_profile_first_name
        return self.do.get_attribute(self.tb_profile_first_name, attribute)

    def get_value_tb_profile_last_name(self):
        # This is the function to perform getValue on web element tb_profile_last_name
        return self.do.get_value(self.tb_profile_last_name)

    def clear_value_tb_profile_last_name(self):
        # This is the function to perform clearText on web element tb_profile_last_name
        self.do.clear_value(self.tb_profile_last_name)
        return self

    def input_text_tb_profile_last_name(self, text):
        # This is the function to perform setText on web element tb_profile_last_name
        self.do.input_text(self.tb_profile_last_name, text)
        return self

    def get_attribute_tb_profile_last_name(self, attribute):
        # This is the function to perform getAttribute on web element tb_profile_last_name
        return self.do.get_attribute(self.tb_profile_last_name, attribute)

    def get_value_tb_profile_doj(self):
        # This is the function to perform getValue on web element tb_profile_doj
        return self.do.get_value(self.tb_profile_doj)

    def get_attribute_tb_profile_doj(self, attribute):
        # This is the function to perform getAttribute on web element tb_profile_doj
        return self.do.get_attribute(self.tb_profile_doj, attribute)


