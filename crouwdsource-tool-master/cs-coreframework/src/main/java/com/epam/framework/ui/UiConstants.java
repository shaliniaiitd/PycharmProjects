package com.epam.framework.ui;

import com.epam.framework.core.utils.PropertyReader;
import com.saucelabs.saucerest.DataCenter;

public class UiConstants {
    private static PropertyReader prop = new PropertyReader("src\\test\\resources\\system.properties");
    public static final String BROWSER = getBrowser();
    public static final String PLATFORM = getPlatform();
    public static final String BROWSER_VERSION = getBrowserVersion();
    public static final String EXEC_ENV = getExecEnv();
    //Configuration Constants
    public static final String HEADLESS = getHeadless();
    public static final int DEFAULT_EXPLICITE_WAIT = getDefaultExplicitWait();
    
	private UiConstants() {
	}

	private static String getBrowser() {
        return getPropertyAsPerThePriority("browser", "chrome");
    }

    private static String getPlatform() {
        return getPropertyAsPerThePriority("platform", "Windows 10");
    }

    private static String getBrowserVersion() {
        return getPropertyAsPerThePriority("browserVersion", "latest");
    }

    private static String getExecEnv() {
        return getPropertyAsPerThePriority("exec_env", "local");
    }


    private static int getDefaultExplicitWait() {
        String defaultWait = getPropertyAsPerThePriority("default.explicit.wait.seconds", "5");
        return Integer.parseInt(defaultWait.trim());
    }

    private static String getHeadless() {
        return getPropertyAsPerThePriority("headless", "false");
    }

    public static String getPropertyAsPerThePriority(String property, String defaultValue) {
        if (prop != null) {
            return System.getProperty(property, prop.getProperty(property,defaultValue));
        }
        return System.getProperty(property, defaultValue);
    }
}