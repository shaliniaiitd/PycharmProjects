package com.epam.framework.core.dbutils;

import com.epam.framework.core.exceptions.TAFRuntimeException;

public class DBDriverMap {

    private DBDriverMap(){

    }
    public static String get(String driverType) {
        switch (driverType){
            case "oracle":
                return "oracle.jdbc.OracleDriver";
            case "mysql":
                return "com.mysql.jdbc.Driver";
            case "sqlserver":
                return "com.microsoft.sqlserver.jdbc.SQLServerDriver";
            case "postgresql":
                return "org.postgresql.Driver";
            case "sqlite":
                return "org.sqlite.JDBC";
            default:
                throw new TAFRuntimeException("Unsupported DB Driver Type "+driverType);
        }
    }
}
