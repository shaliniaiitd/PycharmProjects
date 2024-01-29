package com.epam.framework.core.exceptions;

public class CollabFrameworkException extends RuntimeException{
    public CollabFrameworkException(){}
    public CollabFrameworkException(String message) {
        super(message);
    }
    public CollabFrameworkException(String message,Throwable cause) {
        super(message,cause);
    }
}
