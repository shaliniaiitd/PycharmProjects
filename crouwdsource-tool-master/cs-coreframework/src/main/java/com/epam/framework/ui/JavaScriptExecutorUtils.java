package com.epam.framework.ui;

import com.epam.framework.core.TestContext;
import com.epam.framework.core.constants.WaitConstants;
import com.epam.framework.core.logging.logger.LogLevel;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

import static java.lang.String.format;

public class JavaScriptExecutorUtils {
    protected JavascriptExecutor javascriptExecutor;

    private WebDriver webDriver;

    public JavaScriptExecutorUtils(WebDriver webDriver) {
        this.webDriver = webDriver;
        javascriptExecutor = (JavascriptExecutor) webDriver;
    }

    public void clickElementUsingJS(WebElement webElement) {
        SyncUtils.waitUntilPageIsFullyLoaded(webDriver, WaitConstants.LONG);
        javascriptExecutor.executeScript("arguments[0].click();", webElement);
        TestContext.getLogger().log(LogLevel.INFO, "Completed Click Operation");
    }

    public void setTextUsingJS(WebElement webElement, String input){
        SyncUtils.waitUntilPageIsFullyLoaded(webDriver,WaitConstants.LONG);
        javascriptExecutor.executeScript(format("arguments[0].value='%s'", input), webElement);
        TestContext.getLogger().log(LogLevel.INFO, "Completed Set text Operation");
    }

    public String getTextUsingJS(WebElement webElement){
        SyncUtils.waitUntilPageIsFullyLoaded(webDriver,WaitConstants.LONG);
        return (String) javascriptExecutor.executeScript("return arguments[0].text;", webElement);
    }

    public void executeScript(String script, Object... args)
    {
        javascriptExecutor.executeScript(script, args);
    }

}
