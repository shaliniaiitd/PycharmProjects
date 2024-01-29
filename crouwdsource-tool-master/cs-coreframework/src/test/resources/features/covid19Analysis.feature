Feature: Covid 19 India Web UI Testing

  Scenario: Validate that top 3 states with highest test positivity ratio have correct data mapped with API response
    Given user navigates to the covid19 india application url
    When user calls get request API for covid19 data successfully
    Then user validates the top state data from UI to API



  Scenario: Validate that district details of state with highest positivity ratio have correct data mapped with API response of district details call
    Given user navigates to the covid19 india application url
    And user clicks on first state displayed in table
    When user clicks on See More option
    And user calls get request API for covid19 district data successfully
    Then correct data from districts API is mapped with districts data in UI