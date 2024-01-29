package com.epam.framework.ui.driver;

import com.epam.framework.core.utils.SauceUtils;
import com.epam.framework.ui.UiConstants;

import io.github.bonigarcia.wdm.WebDriverManager;

import org.openqa.selenium.MutableCapabilities;
import org.openqa.selenium.UnexpectedAlertBehaviour;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.remote.CapabilityType;
import org.openqa.selenium.remote.RemoteWebDriver;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.net.MalformedURLException;
import java.net.URL;
import java.util.Map;

/**
 * this is the chromedriver launcher.
 *
 *
 */
public class ChromeLauncher implements DriverLauncher {
    private String browser;
    private String version;
    private String platform;
    private String environment;
    private Map<String, Object> additionalCapabilities;
    private Logger logger = LoggerFactory.getLogger(ChromeLauncher.class);

    public ChromeLauncher(String browser, String version, String platform, String environment, Map<String, Object> additionalCapabilities) {
        this.browser = browser;
        this.version = version;
        this.platform = platform;
        this.environment = environment;
        this.additionalCapabilities = additionalCapabilities;
    }

    @Override
    public DriverDTO launch() {
        switch (environment.toLowerCase()) {
            case "sauce":
                return initializeTheChromeDriverForSauceLab();
            case "local":
            default:
                return initializeTheChromeLocalDriver();
        }
    }

    private DriverDTO initializeTheChromeLocalDriver() {
        logger.info("launching the '{}' browser", browser);
        WebDriverManager.chromedriver().setup();
        ChromeOptions options = new ChromeOptions();
        if ("true".equalsIgnoreCase(UiConstants.HEADLESS)) {
            options.setHeadless(true);
        }
        options.setUnhandledPromptBehaviour(UnexpectedAlertBehaviour.DISMISS);
        options.addArguments(CapabilityType.SUPPORTS_JAVASCRIPT);
        WebDriver webDriver = new ChromeDriver(options);
        return new DriverDTO(webDriver);
    }

    private DriverDTO initializeTheChromeDriverForSauceLab() {
        logger.info("launching the '{}' browser with version '{}'", browser, version);
        MutableCapabilities chromeCapabilities = getChromeCapabilities();
        WebDriver driver = null;
        try {
            driver = new RemoteWebDriver(new URL(SauceUtils.SAUCE_HUB_URL), chromeCapabilities);
        } catch (MalformedURLException e) {
            logger.error("Error while browser initialization ", e);
        }
        return new DriverDTO(driver);
    }

    private MutableCapabilities getChromeCapabilities() {
        ChromeOptions chromeCapabilities = new ChromeOptions();
        chromeCapabilities.setCapability("browserVersion", version);
        chromeCapabilities.addArguments(CapabilityType.SUPPORTS_JAVASCRIPT);
        chromeCapabilities.setCapability("platformName", platform);
        chromeCapabilities.setExperimentalOption("w3c", true);
        chromeCapabilities.setUnhandledPromptBehaviour(UnexpectedAlertBehaviour.DISMISS);
        String scenarioName = (String) additionalCapabilities.get("name");
        chromeCapabilities.setCapability("sauce:options", getSauceCapabilities(scenarioName));
        return chromeCapabilities;
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
