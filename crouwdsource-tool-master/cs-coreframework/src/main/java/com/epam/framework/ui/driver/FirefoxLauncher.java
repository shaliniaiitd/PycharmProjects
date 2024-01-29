package com.epam.framework.ui.driver;

import com.epam.framework.core.utils.SauceUtils;
import com.epam.framework.ui.UiConstants;

import io.github.bonigarcia.wdm.WebDriverManager;

import org.openqa.selenium.MutableCapabilities;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.firefox.FirefoxOptions;
import org.openqa.selenium.remote.CapabilityType;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.remote.RemoteWebDriver;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.net.MalformedURLException;
import java.net.URL;
import java.util.Map;

public class FirefoxLauncher implements DriverLauncher {

    private String browser;
    private String version;
    private String platform;
    private String environment;
    private Map<String, Object> additionalCapabilities;
    private Logger logger = LoggerFactory.getLogger(FirefoxLauncher.class);

    public FirefoxLauncher(String browser, String version, String platform, String environment, Map<String, Object> additionalCapabilities) {
        this.browser = browser;
        this.version = version;
        this.platform = platform;
        this.environment = environment;
        this.additionalCapabilities = additionalCapabilities;
    }

    @Override
    public DriverDTO launch() {
        logger.info("launching the '{}' browser with version '{}' on platform {}", browser, version, platform);
        switch (environment.toLowerCase()) {
            case "sauce":
                return initializeTheFirefoxDriverForSauceLab();
            case "local":
            default:
                return initializeTheFirefoxLocalDriver();
        }
    }

    private DriverDTO initializeTheFirefoxLocalDriver() {
    	WebDriverManager.firefoxdriver().setup();
        FirefoxOptions ffOptions = new FirefoxOptions();
        if ("true".equalsIgnoreCase(UiConstants.HEADLESS)) {
            ffOptions.setHeadless(true);
        }
        ffOptions.addArguments(CapabilityType.SUPPORTS_JAVASCRIPT);
        WebDriver webDriver = new FirefoxDriver();
        return new DriverDTO(webDriver);
    }

    private DriverDTO initializeTheFirefoxDriverForSauceLab() {
        MutableCapabilities firefoxCapabilities = getFirefoxCapabilities();
        WebDriver driver = null;
        try {
            driver = new RemoteWebDriver(new URL(SauceUtils.SAUCE_HUB_URL), firefoxCapabilities);
        } catch (MalformedURLException e) {
            logger.error("Error while browser initialization ", e);
        }
        return new DriverDTO(driver);
    }

    private MutableCapabilities getFirefoxCapabilities() {
        DesiredCapabilities firefoxCapabilities = DesiredCapabilities.firefox();
        firefoxCapabilities.setBrowserName(browser);
        firefoxCapabilities.setJavascriptEnabled(true);
        firefoxCapabilities.setVersion(version);
        firefoxCapabilities.setCapability("platformName", UiConstants.PLATFORM);
        String scenarioName = (String) additionalCapabilities.get("name");
        firefoxCapabilities.setCapability("sauce:options", getSauceCapabilities(scenarioName));
        return firefoxCapabilities;
    }

    private MutableCapabilities getSauceCapabilities(String scenarioName) {
        MutableCapabilities sauceCapabilities = new MutableCapabilities();
        sauceCapabilities.setCapability("username", SauceUtils.USER_NAME);
        sauceCapabilities.setCapability("accessKey", SauceUtils.ACCESS_KEY);
        sauceCapabilities.setCapability("seleniumVersion", "3.141.59");
        sauceCapabilities.setCapability("name", scenarioName);
        sauceCapabilities.setCapability("build", SauceUtils.BUILD_NAME);
        return sauceCapabilities;
    }
}
