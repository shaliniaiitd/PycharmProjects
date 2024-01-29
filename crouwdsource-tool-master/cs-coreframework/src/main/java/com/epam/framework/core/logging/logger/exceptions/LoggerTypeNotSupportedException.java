package com.epam.framework.core.logging.logger.exceptions;

import com.epam.framework.core.exceptions.CollabFrameworkException;

public class LoggerTypeNotSupportedException extends CollabFrameworkException {
    public LoggerTypeNotSupportedException(String message) {
        super(message);
    }

}
