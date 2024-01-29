package com.epam.framework.runners.cucumber.testng;

import com.epam.framework.core.Context;
import com.epam.framework.core.TestContext;
import com.epam.framework.core.logging.logger.LogLevel;
import com.epam.framework.core.reporting.Reporter;
import io.cucumber.java.Before;
import io.cucumber.testng.AbstractTestNGCucumberTests;
import io.cucumber.testng.CucumberOptions;
import io.cucumber.testng.TestNGCucumberRunner;
import org.testng.annotations.AfterClass;
import org.testng.annotations.DataProvider;
import org.testng.annotations.Listeners;

@Listeners(CucumberTestNGListener.class)
@CucumberOptions(
        strict = false,
        features = {"src/test/resources/features"},
        glue = {"com.epam.stepdefinitions","com.epam.framework.runners.cucumber"}
)
public class CucumberRunner extends AbstractTestNGCucumberTests {
    private TestNGCucumberRunner testNGCucumberRunner;

    @Before (order = 1)
    public void setUp() {
        testNGCucumberRunner = new TestNGCucumberRunner(this.getClass());
        TestContext.getLogger().log(LogLevel.INFO,"<=============================On Before Class======================================>");
        Context scenarioContext = new Context();
        TestContext.registerContext(scenarioContext);
        Reporter.register(TestContext.getReporter());
        Reporter.setUp();
    }

    @DataProvider
    public Object[][] features() {
        return testNGCucumberRunner.provideScenarios();
    }

    @AfterClass
    public void tearDownClass() {
        testNGCucumberRunner.finish();
    }
    
}
