package com.epam.framework.core.constants;


import com.epam.framework.core.utils.PropertyReader;

public class WaitConstants {

    private static PropertyReader prop = new PropertyReader("src\\test\\resources\\system.properties");

    private WaitConstants(){

    }
    public static final long LONG = Long. parseLong(getPropertyAsPerThePriority("test.wait.long",""));
    public static final long DEFAULT = Long. parseLong(getPropertyAsPerThePriority("test.wait.default",""));
    public static final long SHORT = Long. parseLong(getPropertyAsPerThePriority("test.wait.short",""));
    public static final long TIMEOUT = Long. parseLong(getPropertyAsPerThePriority("test.wait.timeout",""));

    public static String getPropertyAsPerThePriority(String property, String defaultValue) {
        if (prop != null) {
            return System.getProperty(property, prop.getProperty(property,defaultValue));
        }
        return System.getProperty(property, defaultValue);
    }

}
