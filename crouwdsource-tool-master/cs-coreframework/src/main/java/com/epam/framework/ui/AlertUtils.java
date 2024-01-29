package com.epam.framework.ui;

import com.epam.framework.core.TestContext;
import com.epam.framework.core.logging.logger.LogLevel;
import org.openqa.selenium.Alert;
import org.openqa.selenium.WebDriver;

public class AlertUtils {
    private WebDriver webDriver;
    private TestContext testContext;

    public AlertUtils(WebDriver webDriver) {
        this.webDriver = webDriver;
    }

    private Alert switchToAlert(){
        TestContext.getLogger().log(LogLevel.INFO, "Switched to Alert pop-up");
        return webDriver.switchTo().alert();
    }

    public void cancelAlert(){
        switchToAlert().dismiss();
        TestContext.getLogger().log(LogLevel.INFO, "The Alert is Cancelled");
    }

    public void acceptAlert(){
        switchToAlert().accept();
        TestContext.getLogger().log(LogLevel.INFO, "The Alert is Accepted");
    }

    public String getTextFromAlert(){
        TestContext.getLogger().log(LogLevel.INFO, "Retrieving text from Alert");
        return switchToAlert().getText();
    }

    public void sendTextToAlert(String input){
        switchToAlert().sendKeys(input);
        TestContext.getLogger().log(LogLevel.INFO, "Text is inputted to the Alert");
    }
}
