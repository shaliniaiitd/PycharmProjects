package com.epam.framework.runners.cucumber.junit;

import io.cucumber.junit.Cucumber;
import io.cucumber.junit.CucumberOptions;
import org.junit.runner.RunWith;

@RunWith(Cucumber.class)
@CucumberOptions(
        glue = {"com.epam.stepdefinitions","com.epam.framework.runners.cucumber"},
        features = "src/test/resources/features"
)

public class CucumberJunitRunner {

}
