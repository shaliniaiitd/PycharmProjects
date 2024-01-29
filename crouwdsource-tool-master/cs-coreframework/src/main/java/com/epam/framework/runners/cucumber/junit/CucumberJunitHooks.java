package com.epam.framework.runners.cucumber.junit;

import com.epam.framework.core.Context;
import com.epam.framework.core.TestContext;
import com.epam.framework.core.logging.logger.LogLevel;
import com.epam.framework.core.reporting.Reporter;
import io.cucumber.java.After;
import io.cucumber.java.Before;
import io.cucumber.java.Scenario;

import java.util.HashMap;
import java.util.Map;

public class CucumberJunitHooks {

    private boolean reportStart = false;

    @Before(order = 1)
    public void onStart(){
        if(!reportStart){
            TestContext.getLogger().log(LogLevel.INFO,"<=============================On Before Class======================================>");
            Context scenarioContext = new Context();
            TestContext.registerContext(scenarioContext);
            Reporter.register(TestContext.getReporter());
            Reporter.setUp();
            reportStart = true;
        }
    }

    @Before (order = 2)
    public synchronized void onTestStart(Scenario scenario) {
        String methodName = scenario.getName();
        Map<String, Object> additionalParams = new HashMap<>();
        additionalParams.put("ITestResult", scenario);
        additionalParams.put("desc", scenario.getStatus());
        Reporter.createTest(methodName, additionalParams);
        Reporter.info("TEST EXECUTION STARTED - "+methodName);

    }

    @After (order = 1)
    public synchronized void onTestFinished(Scenario scenario) {
        String methodName = scenario.getName();
        if (scenario.isFailed()){
            Reporter.fail("FAILED - " + methodName);
            Reporter.addScreenshot(methodName + "-Failed", "Screenshot After Test Failure..!!!");
        } else if (String.valueOf(scenario.getStatus()).equals("PASSED")){
            Reporter.pass("PASSED - " + methodName);
        } else {
            Reporter.info("INFO - " + methodName);
        }

    }
    @After (order = 2)
    public void onFinish(){
        Reporter.tearDown();
    }
}
