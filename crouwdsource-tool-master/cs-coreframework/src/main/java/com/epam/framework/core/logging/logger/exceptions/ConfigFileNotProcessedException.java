package com.epam.framework.core.logging.logger.exceptions;

import com.epam.framework.core.exceptions.CollabFrameworkException;

public class ConfigFileNotProcessedException extends CollabFrameworkException {
    public ConfigFileNotProcessedException(String message) {
        super(message);
    }

}
