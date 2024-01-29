package com.epam.framework.core.exceptions;


public class DBUtilityException extends TAFRuntimeException {
    public DBUtilityException(String message) {
        super(message);
    }

    public DBUtilityException(Throwable throwable) {
        super(throwable);
    }

    public DBUtilityException(String message, Exception innerException) {
        super(message, innerException);
    }
}
