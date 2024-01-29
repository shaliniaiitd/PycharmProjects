package com.epam.framework.api.httpclient.errorhandler;

public class ObjectParseException extends RuntimeException{
    private final String message;

    public ObjectParseException(String message) {
        super(message);
        this.message = message;
    }

    @Override
    public String getMessage() {
        return message;
    }
}