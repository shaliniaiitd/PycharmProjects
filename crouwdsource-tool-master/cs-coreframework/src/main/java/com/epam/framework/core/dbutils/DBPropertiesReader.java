package com.epam.framework.core.dbutils;

import com.epam.framework.core.utils.PropertyReader;

public class DBPropertiesReader {

    private static final String STRING_DB_URL = "db.url";
    private static final String STRING_DB_PASSWORD = "db.password";
    private static final String STRING_DB_USERNAME = "db.username";
    private static final String STRING_DB_TYPE = "db.type";
    private static final String STRING_DEFAULT_USER = "defaultUser";
    private static final String STRING_DEFAULT_PASSWORD = "defaultPassword";
    private static final String STRING_DEFAULT_DB_URL = "jdbc:mysql://[host][,failoverhost...][:port]/[database]";
    private static final String STRING_DEFAULT_DB_TYPE = "oracle";

    private static PropertyReader prop = new PropertyReader("src\\test\\resources\\system.properties");

    private DBPropertiesReader() {
    }

    public static String getDbPassword() {
        return getProperty(STRING_DB_PASSWORD, STRING_DEFAULT_PASSWORD);
    }

    public static String getDbUsername() {
        return getProperty(STRING_DB_USERNAME, STRING_DEFAULT_USER);
    }

    public static String getDbUrl() {
        return getProperty(STRING_DB_URL, STRING_DEFAULT_DB_URL);
    }

    private static String getProperty(String property, String defaultValue) {
        if (prop != null) {
            return System.getProperty(property, prop.getProperty(property, defaultValue));
        }
        return System.getProperty(property, defaultValue);
    }

    public static String getDbDriverType() {
        return DBDriverMap.get(getProperty(STRING_DB_TYPE, STRING_DEFAULT_DB_TYPE));
    }
}
