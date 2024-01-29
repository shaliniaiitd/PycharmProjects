package com.epam.framework.core.logging.logger.exceptions;

import com.epam.framework.core.exceptions.CollabFrameworkException;

public class ArgumentNotSupportedException extends CollabFrameworkException {
    public ArgumentNotSupportedException(String message) {
        super(message);
    }

}
