package com.epam.framework.core.exceptions;

public class ReportingException extends TAFRuntimeException{
    public ReportingException(String message) {
        super(message);
    }
    public ReportingException(String message, Exception innerException) {
        super(message, innerException);
    }
}
