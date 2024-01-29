package com.epam.framework.core.dbutils;

public class DBProperties {

    private String dbURL;
    private String dbUserName;
    private String dbPassword;
    private String dbDriver;

    public DBProperties() {
        dbDriver = DBPropertiesReader.getDbDriverType();
        dbURL = DBPropertiesReader.getDbUrl();
        dbUserName = DBPropertiesReader.getDbUsername();
        dbPassword = DBPropertiesReader.getDbPassword();
    }

    public String getDbURL() {
        return dbURL;
    }

    public String getDbUserName() {
        return dbUserName;
    }

    public String getDbPassword() {
        return dbPassword;
    }

    public String getDbDriver() {
        return dbDriver;
    }
}
