package com.epam.framework.core.exceptions;

public class TAFRuntimeException extends RuntimeException {

    public TAFRuntimeException(String message) {
        super(message);
    }

    public TAFRuntimeException(Throwable exception) {
        super(exception);
    }

    public TAFRuntimeException(String message, Throwable exception) {
        super(message, exception);
    }

    public void throwIf(final boolean conditionResult) {
        if (conditionResult) {
            throw this;
        }
    }

}
