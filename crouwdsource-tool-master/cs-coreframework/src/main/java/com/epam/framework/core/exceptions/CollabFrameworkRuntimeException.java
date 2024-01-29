package com.epam.framework.core.exceptions;

public class CollabFrameworkRuntimeException extends CollabFrameworkException {

    public CollabFrameworkRuntimeException(String message) {
        super(message);
    }

    public CollabFrameworkRuntimeException(String message,Throwable cause) {
        super(message,cause);
    }
}
