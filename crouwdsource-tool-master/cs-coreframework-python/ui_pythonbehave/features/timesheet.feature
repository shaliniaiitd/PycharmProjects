@web
Feature: Timesheet basic login
  As an employee,
  I want to login to timesheets,
  So I can log time tracking for work done.

  # The "@" annotations are tags
  # One feature can have multiple scenarios
  # The lines immediately after the feature title are just comments

#  @fixture.basiclogin
  Scenario: Basic login
    Given the Timesheet home page is displayed
    When the user enter username as "clbuser1" and password as "password" and clicks login
    Then user should be navigated to welcome page
