package com.epam.framework.core.exceptions;

public class EnvironmentOrDataException extends CollabFrameworkException{

    public EnvironmentOrDataException(String message) {
        super(message);
    }
    public EnvironmentOrDataException(String message,Throwable cause) {
        super(message,cause);
    }
}
