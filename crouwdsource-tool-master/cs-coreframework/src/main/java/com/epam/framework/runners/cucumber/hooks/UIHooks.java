package com.epam.framework.runners.cucumber.hooks;

import com.epam.framework.core.TestContext;
import com.epam.framework.core.logging.logger.LogLevel;
import com.epam.framework.core.reporting.Reporter;
import com.epam.framework.core.utils.SauceUtils;
import com.epam.framework.ui.UiConstants;
import com.epam.framework.ui.driver.DriverManager;
import io.cucumber.java.After;
import io.cucumber.java.Before;
import io.cucumber.java.Scenario;

import java.util.HashMap;
import java.util.Map;

public class UIHooks {

    @Before (order = 2)
    public void beforeBaseMethod(Scenario scenario){
        String testCaseName = scenario.getName();
        TestContext.getLogger().log(LogLevel.INFO,"TestCase '{"+testCaseName+"}' is started...!!!");
        Map<String, Object> additionalCapabilities = new HashMap<>();
        additionalCapabilities.put("testCaseName", testCaseName);
        DriverManager.initializeDriver(UiConstants.BROWSER, UiConstants.BROWSER_VERSION, UiConstants.PLATFORM, UiConstants.EXEC_ENV, additionalCapabilities);
    }
    @After
    public void afterBaseMethod(Scenario scenario) {
        if(UiConstants.EXEC_ENV.equalsIgnoreCase("sauce")) {
            SauceUtils.updateResults(scenario.isFailed(), DriverManager.getSessionIds());
        }
        DriverManager.quitDriver();
        Reporter.tearDown();
    }
}
