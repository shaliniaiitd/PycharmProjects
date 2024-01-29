package com.epam.framework.core.exceptions;

public class TABaseException extends RuntimeException {

    public TABaseException() {
    }

    public TABaseException(String message) {
        super(message);
    }

    public TABaseException(String message, Throwable cause) {
        super(message, cause);
    }

    public TABaseException(Throwable cause) {
        super(cause);
    }

    public TABaseException(String message, Throwable cause, boolean enableSuppression, boolean writableStackTrace) {
        super(message, cause, enableSuppression, writableStackTrace);
    }
}
