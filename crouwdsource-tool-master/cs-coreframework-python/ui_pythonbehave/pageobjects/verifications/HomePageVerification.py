from ui_pythonbehave.pageobjects.actions.HomePage import HomePage


class HomePageVerification(HomePage):
    def __init__(self, driver):
        super(HomePageVerification, self).__init__(driver)

    def is_present_link_welcome_username(self):
        # This is the function to perform verifyIsElementPresent on web element link_welcome_username
        return self.verify.is_present(self.link_welcome_username)

    def is_text_link_welcome_username(self, text):
        # This is the function to perform verifyElementText on web element link_welcome_username
        return self.verify.is_text(self.link_welcome_username, text)

    def is_present_btn_nav_daily_status_entry(self):
        # This is the function to perform verifyIsElementPresent on web element btn_nav_daily_status_entry
        return self.verify.is_present(self.btn_nav_daily_status_entry)

    def is_present_btn_nav_my_profile(self):
        # This is the function to perform verifyIsElementPresent on web element btn_nav_my_profile
        return self.verify.is_present(self.btn_nav_my_profile)

    def is_present_tb_daily_date_box(self):
        # This is the function to perform verifyIsElementPresent on web element tb_daily_date_box
        return self.verify.is_present(self.tb_daily_date_box)

    def is_present_btn_daily_hours_spent(self):
        # This is the function to perform verifyIsElementPresent on web element btn_daily_hours_spent
        return self.verify.is_present(self.btn_daily_hours_spent)

    def is_present_tb_daily_nth_row_hours_spent_dynamic(self, dynamic_text):
        # This is the function to perform verifyIsElementPresent on web element tb_daily_nth_row_hours_spent_dynamic
        return self.verify.is_present(self.tb_daily_nth_row_hours_spent_dynamic, dynamic_text)

    def is_present_tb_daily_nth_row_comments_dynamic(self, dynamic_text):
        # This is the function to perform verifyIsElementPresent on web element tb_daily_nth_row_comments_dynamic
        return self.verify.is_present(self.tb_daily_nth_row_comments_dynamic, dynamic_text)

    def is_present_ddn_daily_nth_row_start_hour_dynamic(self, dynamic_text):
        # This is the function to perform verifyIsElementPresent on web element ddn_daily_nth_row_start_hour_dynamic
        return self.verify.is_present(self.ddn_daily_nth_row_start_hour_dynamic, dynamic_text)

    def is_present_ddn_daily_nth_row_start_min_dynamic(self, dynamic_text):
        # This is the function to perform verifyIsElementPresent on web element ddn_daily_nth_row_start_min_dynamic
        return self.verify.is_present(self.ddn_daily_nth_row_start_min_dynamic, dynamic_text)

    def is_present_ddn_daily_nth_row_start_ampm_dynamic(self, dynamic_text):
        # This is the function to perform verifyIsElementPresent on web element ddn_daily_nth_row_start_ampm_dynamic
        return self.verify.is_present(self.ddn_daily_nth_row_start_ampm_dynamic, dynamic_text)

    def is_present_ddn_daily_nth_row_end_hour_dynamic(self, dynamic_text):
        # This is the function to perform verifyIsElementPresent on web element ddn_daily_nth_row_end_hour_dynamic
        return self.verify.is_present(self.ddn_daily_nth_row_end_hour_dynamic, dynamic_text)

    def is_present_ddn_daily_nth_row_end_min_dynamic(self, dynamic_text):
        # This is the function to perform verifyIsElementPresent on web element ddn_daily_nth_row_end_min_dynamic
        return self.verify.is_present(self.ddn_daily_nth_row_end_min_dynamic, dynamic_text)

    def is_present_ddn_daily_nth_row_end_ampm_dynamic(self, dynamic_text):
        # This is the function to perform verifyIsElementPresent on web element ddn_daily_nth_row_end_ampm_dynamic
        return self.verify.is_present(self.ddn_daily_nth_row_end_ampm_dynamic, dynamic_text)

    def is_present_btn_daily_save(self):
        # This is the function to perform verifyIsElementPresent on web element btn_daily_save
        return self.verify.is_present(self.btn_daily_save)

    def is_present_btn_daily_clear(self):
        # This is the function to perform verifyIsElementPresent on web element btn_daily_clear
        return self.verify.is_present(self.btn_daily_clear)

    def is_present_btn_daily_back(self):
        # This is the function to perform verifyIsElementPresent on web element btn_daily_back
        return self.verify.is_present(self.btn_daily_back)

    def is_present_lb_daily_success(self):
        # This is the function to perform verifyIsElementPresent on web element lb_daily_success
        return self.verify.is_present(self.lb_daily_success)

    def is_present_btn_weekly_previous(self):
        # This is the function to perform verifyIsElementPresent on web element btn_weekly_previous
        return self.verify.is_present(self.btn_weekly_previous)

    def is_present_btn_weekly_current(self):
        # This is the function to perform verifyIsElementPresent on web element btn_weekly_current
        return self.verify.is_present(self.btn_weekly_current)

    def is_present_btn_weekly_next(self):
        # This is the function to perform verifyIsElementPresent on web element btn_weekly_next
        return self.verify.is_present(self.btn_weekly_next)

    def is_present_lb_weekly_nth_day_dynamic(self, dynamic_text):
        # This is the function to perform verifyIsElementPresent on web element lb_weekly_nth_day_dynamic
        return self.verify.is_present(self.lb_weekly_nth_day_dynamic, dynamic_text)

    def is_present_tb_weekly_mon_nth_project_hours_dynamic(self, dynamic_text):
        # This is the function to perform verifyIsElementPresent on web element tb_weekly_mon_nth_project_hours_dynamic
        return self.verify.is_present(self.tb_weekly_mon_nth_project_hours_dynamic, dynamic_text)

    def is_present_tb_weekly_tue_nth_project_hours_dynamic(self, dynamic_text):
        # This is the function to perform verifyIsElementPresent on web element tb_weekly_tue_nth_project_hours_dynamic
        return self.verify.is_present(self.tb_weekly_tue_nth_project_hours_dynamic, dynamic_text)

    def is_present_tb_weekly_wed_nth_project_hours_dynamic(self, dynamic_text):
        # This is the function to perform verifyIsElementPresent on web element tb_weekly_wed_nth_project_hours_dynamic
        return self.verify.is_present(self.tb_weekly_wed_nth_project_hours_dynamic, dynamic_text)

    def is_present_tb_weekly_thu_nth_project_hours_dynamic(self, dynamic_text):
        # This is the function to perform verifyIsElementPresent on web element tb_weekly_thu_nth_project_hours_dynamic
        return self.verify.is_present(self.tb_weekly_thu_nth_project_hours_dynamic, dynamic_text)

    def is_present_tb_weekly_fri_nth_project_hours_dynamic(self, dynamic_text):
        # This is the function to perform verifyIsElementPresent on web element tb_weekly_fri_nth_project_hours_dynamic
        return self.verify.is_present(self.tb_weekly_fri_nth_project_hours_dynamic, dynamic_text)

    def is_present_tb_weekly_sat_nth_project_hours_dynamic(self, dynamic_text):
        # This is the function to perform verifyIsElementPresent on web element tb_weekly_sat_nth_project_hours_dynamic
        return self.verify.is_present(self.tb_weekly_sat_nth_project_hours_dynamic, dynamic_text)

    def is_present_tb_weekly_sun_nth_project_hours_dynamic(self, dynamic_text):
        # This is the function to perform verifyIsElementPresent on web element tb_weekly_sun_nth_project_hours_dynamic
        return self.verify.is_present(self.tb_weekly_sun_nth_project_hours_dynamic, dynamic_text)

    def is_present_tb_weekly_sum_nth_project_hours_dynamic(self, dynamic_text):
        # This is the function to perform verifyIsElementPresent on web element tb_weekly_sum_nth_project_hours_dynamic
        return self.verify.is_present(self.tb_weekly_sum_nth_project_hours_dynamic, dynamic_text)

    def is_present_btn_weekly_save(self):
        # This is the function to perform verifyIsElementPresent on web element btn_weekly_save
        return self.verify.is_present(self.btn_weekly_save)

    def is_present_btn_weekly_submit(self):
        # This is the function to perform verifyIsElementPresent on web element btn_weekly_submit
        return self.verify.is_present(self.btn_weekly_submit)

    def is_present_btn_weekly_clear(self):
        # This is the function to perform verifyIsElementPresent on web element btn_weekly_clear
        return self.verify.is_present(self.btn_weekly_clear)

    def is_present_lb_weekly_save_success(self):
        # This is the function to perform verifyIsElementPresent on web element lb_weekly_save_success
        return self.verify.is_present(self.lb_weekly_save_success)

    def is_present_lb_weekly_submit_success(self):
        # This is the function to perform verifyIsElementPresent on web element lb_weekly_submit_success
        return self.verify.is_present(self.lb_weekly_submit_success)

    def is_present_tb_profile_first_name(self):
        # This is the function to perform verifyIsElementPresent on web element tb_profile_first_name
        return self.verify.is_present(self.tb_profile_first_name)

    def is_present_tb_profile_last_name(self):
        # This is the function to perform verifyIsElementPresent on web element tb_profile_last_name
        return self.verify.is_present(self.tb_profile_last_name)

    def is_value_tb_profile_last_name(self, value):
        # This is the function to perform verifyElementValue on web element tb_profile_last_name
        return self.verify.is_value(self.tb_profile_last_name, value)

    def is_present_tb_profile_doj(self):
        # This is the function to perform verifyIsElementPresent on web element tb_profile_doj
        return self.verify.is_present(self.tb_profile_doj)

    def is_value_tb_profile_doj(self, value):
        # This is the function to perform verifyElementValue on web element tb_profile_doj
        return self.verify.is_value(self.tb_profile_doj, value)


