package com.epam.framework.core.logging.logger.facory;

import com.epam.framework.core.logging.logger.CSLogger;
import com.epam.framework.core.logging.logger.LoggerType;
import com.epam.framework.core.logging.logger.exceptions.ArgumentNotSupportedException;
import com.epam.framework.core.logging.logger.impl.Log4JCSLoggerImpl;
import com.epam.framework.core.logging.logger.impl.Slf4JCSLoggerImpl;

public class LoggerFactory {

    private static CSLogger logger = null;

    private LoggerFactory(){
    }

    public static CSLogger getLogger(LoggerType loggerType) {
        if (logger == null) {
            createLogger(loggerType);
        }
        return logger;
    }

    private static void createLogger(LoggerType loggerType) {
        switch (loggerType) {
            case LOG4J:
                logger = new Log4JCSLoggerImpl();
                break;
            case SL4J:
                logger = new Slf4JCSLoggerImpl();
                break;
            default:
                throw new ArgumentNotSupportedException("Currently Supported Loggers - log4j and slf4j");
        }
    }
}
