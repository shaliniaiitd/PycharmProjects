package com.epam.framework.ui.driver;

import java.util.Map;

/**
 * This class is responsible for providing the DriverLauncher as per the specification provided.
 *
 *
 */
public class DriverLauncherFactory {

    private DriverLauncherFactory() {
    }

    public static DriverLauncher getDriverLauncher(String browser,
                                                   String version,
                                                   String platform,
                                                   String environment,
                                                   Map<String, Object> addCapabilities) {
        switch (browser.toLowerCase()) {
            case "firefox":
                return new FirefoxLauncher(browser, version, platform, environment, addCapabilities);
            case "safari":
                return new SafariLauncher(browser, version, platform, environment, addCapabilities);
            case "edge":
                return new EdgeLauncher(browser, version, platform, environment, addCapabilities);
            case "ie":
                return new IELauncher(browser, version, platform, environment, addCapabilities);
            case "chrome":
            default:
                return new ChromeLauncher(browser, version, platform, environment, addCapabilities);
        }
    }

}