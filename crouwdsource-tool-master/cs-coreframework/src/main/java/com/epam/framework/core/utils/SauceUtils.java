package com.epam.framework.core.utils;

import com.epam.framework.core.exceptions.CollabFrameworkRuntimeException;
import com.saucelabs.saucerest.DataCenter;
import com.saucelabs.saucerest.SauceREST;

import java.util.HashMap;
import java.util.Map;

public class SauceUtils {
    /**
     * Login singleton instance of the Sauce REST client
     */
    private static SauceREST sauceClient;
    private static PropertyReader prop = new PropertyReader("src\\test\\resources\\system.properties");
    //SauceLab Constants
    public static final String USER_NAME = getUserName();
    public static final String ACCESS_KEY = getAccessKey();
    public static final String SAUCE_HUB_URL = getSauceHubUrl();
    public static final DataCenter SAUCE_DATA_CENTER = getSauceDataCenter();
    public static final String BUILD_NAME = getBuildName();

    private SauceUtils() {
    }

    private static SauceREST getSauceRestClient() {
        if (sauceClient == null) {
            sauceClient = new SauceREST(USER_NAME, ACCESS_KEY, SAUCE_DATA_CENTER);
        }
        return sauceClient;
    }

    public static synchronized void updateResults(boolean testResults, String sessionId) {
        Map<String, Object> updates = new HashMap<>();
        updates.put("passed", testResults);
        try {
            getSauceRestClient().updateJobInfo(sessionId, updates);
        } catch (Exception ex) {
            throw new CollabFrameworkRuntimeException("Getting exception while updating the test result status...!!!", ex);
        }
    }

    private static String getUserName() {
        return getPropertyAsPerThePriority("userName", "defaultUser");
    }

    private static String getAccessKey() {
        return getPropertyAsPerThePriority("accessKey", "defaultAccessKey");
    }

    private static String getSauceHubUrl() {
        return getPropertyAsPerThePriority("sauceHubUrl", "https://ondemand.saucelabs.com/wd/hub");
    }

    private static DataCenter getSauceDataCenter() {
        String sauceHUbUrl = getSauceHubUrl();
        if (sauceHUbUrl.contains(".eu-central-1")) {
            return DataCenter.EU;
        } else if (sauceHUbUrl.contains(".us-east-1")) {
            return DataCenter.US_EAST;
        } else
            return DataCenter.US;
    }

    private static String getBuildName() {
        return getPropertyAsPerThePriority("buildName", "DentsplySironaTest");
    }
    public static String getPropertyAsPerThePriority(String property, String defaultValue) {
        if (prop != null) {
            return System.getProperty(property, prop.getProperty(property,defaultValue));
        }
        return System.getProperty(property, defaultValue);
    }
}
