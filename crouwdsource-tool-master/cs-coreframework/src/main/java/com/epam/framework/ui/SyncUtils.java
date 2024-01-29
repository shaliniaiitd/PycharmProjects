package com.epam.framework.ui;

import com.epam.framework.core.TestContext;
import com.epam.framework.core.constants.WaitConstants;
import com.epam.framework.core.logging.logger.LogLevel;
import com.google.common.collect.ImmutableMap;
import org.openqa.selenium.*;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.remote.Command;
import org.openqa.selenium.remote.CommandExecutor;
import org.openqa.selenium.remote.RemoteWebDriver;
import org.openqa.selenium.remote.Response;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.io.IOException;
import java.time.Duration;
import java.util.HashMap;
import java.util.Map;

public class SyncUtils {

    private SyncUtils() {
    }

    public static void waitUntilPageIsFullyLoaded(WebDriver driver, long timeOutInSeconds) {
        long startTime = System.currentTimeMillis();
        try {
            WebDriverWait wait = new WebDriverWait(driver, timeOutInSeconds);
            wait.until(
                    driver1 -> ((RemoteWebDriver) driver1).executeScript("return document.readyState")
                                    .toString().equals("complete"));
            wait.until((
                    driver1 -> (Boolean) ((JavascriptExecutor) driver1)
                            .executeScript("return (window.jQuery != null) && (jQuery.active === 0);")));
            TestContext.getLogger().log(LogLevel.INFO,
                    String.format("Actual wait: %s milliseconds, Expected was %s",
                            (System.currentTimeMillis() - startTime), timeOutInSeconds * 1000));
        } catch (Exception ex) {
            TestContext.getLogger().log(LogLevel.INFO,"Timeout during waitForPageLoad");
        }
    }

    public static void waitUntilClickable(WebDriver driver, WebElement element) {
        waitUntilClickable(driver, element, WaitConstants.DEFAULT);
    }

    public static void waitUntilClickable(WebDriver driver, WebElement element, long waitInSeconds) {
        try {
            WebDriverWait wait = new WebDriverWait(driver, waitInSeconds);

            wait.ignoring(NoSuchElementException.class)
                    .until(ExpectedConditions.elementToBeClickable(element));
        } catch (Exception e) {
            TestContext.getLogger().log(LogLevel.INFO,"Timeout during waitForClickable");
        }
    }

    public static void waitForElementVisibility(WebDriver driver, WebElement element) {
        waitForElementVisibility(driver, element, WaitConstants.DEFAULT);
    }

    public static void waitForElementVisibility(WebDriver driver, WebElement element, long waitInSeconds) {
        WebDriverWait wait = new WebDriverWait(driver, waitInSeconds);
        wait.ignoring(NoSuchElementException.class)
                .until(ExpectedConditions.visibilityOf(element));
    }

    public static void waitForElementInVisibility(WebDriver driver, WebElement element) {
        waitForElementInVisibility(driver, element, WaitConstants.DEFAULT);
    }

    public static void waitForElementInVisibility(WebDriver driver, WebElement element, long waitInSeconds) {
        WebDriverWait wait = new WebDriverWait(driver, waitInSeconds);
        wait.until(ExpectedConditions.invisibilityOf(element));
    }

    public static void waitPresenceOfElement(WebDriver driver, By element) {
        waitPresenceOfElement(driver, element, WaitConstants.DEFAULT);
    }

    public static void waitPresenceOfElement(WebDriver driver, By element, long waitInSeconds) {
        WebDriverWait wait = new WebDriverWait(driver, waitInSeconds);
        wait.until(ExpectedConditions.presenceOfElementLocated(element));
    }

    public static void sleep(int timeInMilli) {
        try {
            Thread.sleep(timeInMilli);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            TestContext.getLogger().log(LogLevel.WARNING,String.format("Exception: %s", e));
        }
    }

    public static void enableNetworkThrottling(WebDriver driver) {
        Map<String,Object> map = new HashMap<>();
        map.put("offline", false);
        map.put("latency", 4);
        map.put("download_throughput", 2000);
        map.put("upload_throughput", 2000);


        CommandExecutor executor = ((ChromeDriver) driver).getCommandExecutor();
        Response response = null;
        try {
            response = executor.execute(
                    new Command(((ChromeDriver) driver).getSessionId(), "setNetworkConditions", ImmutableMap.of("network_conditions", ImmutableMap.copyOf(map)))
            );
        } catch (IOException e) {
            TestContext.getLogger().log(LogLevel.INFO, String.format("Error while throttling browser speed : %s", e));
        }
        TestContext.getLogger().log(LogLevel.WARNING,  String.format("Throttling response %s", response));
    }
}
