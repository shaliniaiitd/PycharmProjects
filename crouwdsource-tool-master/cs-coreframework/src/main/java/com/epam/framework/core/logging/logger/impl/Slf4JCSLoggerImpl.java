package com.epam.framework.core.logging.logger.impl;

import com.epam.framework.core.logging.logger.CSLogger;
import com.epam.framework.core.logging.logger.LogLevel;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class Slf4JCSLoggerImpl implements CSLogger {

    private Logger logger = LoggerFactory.getLogger("SLF4JLogger");

    @Override
    public void log(String message) {
        logger.info(message);
    }

    @Override
    public void log(Object object) {
        String message = object.toString();
        logger.info(message);
    }

    @Override
    public void log(LogLevel level, String message) {
        switch (level) {
            case DEBUG:
                logger.debug(message);
                break;
            case ERROR:
                logger.error(message);
                break;
            case INFO:
                logger.info(message);
                break;
            case WARNING:
                logger.warn(message);
                break;
        }
    }

    @Override
    public void log(LogLevel level, Object object) {
        log(level, object.toString());
    }
}
