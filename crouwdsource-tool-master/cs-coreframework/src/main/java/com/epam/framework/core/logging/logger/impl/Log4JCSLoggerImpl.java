package com.epam.framework.core.logging.logger.impl;

import com.epam.framework.core.logging.logger.CSLogger;
import com.epam.framework.core.logging.logger.LogLevel;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

public class Log4JCSLoggerImpl implements CSLogger {

    private Logger logger = LogManager.getLogger("Log4JLogger");

    @Override
    public void log(String message) {
        logger.debug(message);
    }

    @Override
    public void log(Object object) {
        logger.info(object.toString());
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
