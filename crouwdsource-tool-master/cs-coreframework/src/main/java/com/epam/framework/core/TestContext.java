package com.epam.framework.core;

import com.epam.framework.core.constants.LoggerConstants;
import com.epam.framework.core.exceptions.CollabFrameworkRuntimeException;
import com.epam.framework.core.logging.logger.CSLogger;
import com.epam.framework.core.logging.logger.LoggerType;
import com.epam.framework.core.logging.logger.exceptions.ArgumentNotSupportedException;
import com.epam.framework.core.logging.logger.exceptions.LoggerTypeNotSupportedException;
import com.epam.framework.core.logging.logger.facory.LoggerFactory;
import com.epam.framework.core.reporting.HTMLReportObserver;
import com.epam.framework.core.reporting.factory.ReporterFactory;
import com.epam.framework.core.reporting.factory.ReporterType;

public class TestContext {

    private static ThreadLocal<Context> scenarioContext = new ThreadLocal<>();
    private static CSLogger logger = LoggerFactory.getLogger(getLoggerType());
    private static HTMLReportObserver reporter = ReporterFactory.getReporter(getReporterType());

    private TestContext() {
    }

    public static synchronized <T> T get(String key) {
        if (scenarioContext.get() != null) {
            return scenarioContext.get().get(key);
        } else {
            throw new CollabFrameworkRuntimeException("Test Context is not initialized..!!");
        }
    }

    public static synchronized void put(String key, Object value) {
        scenarioContext.get().put(key, value);
    }

    public static void registerContext(Context context) {

        scenarioContext.set(context);
        if(logger==null) {
            logger = LoggerFactory.getLogger(getLoggerType());
        }
        if(reporter==null) {
            reporter = ReporterFactory.getReporter(getReporterType());
        }
    }

    public static void removeContext() {
        scenarioContext.remove();
    }

    private static LoggerType getLoggerType() {
        return getLoggerType(LoggerConstants.getPropertyAsPerThePriority("tool.logger","log4j"));
    }

    private static LoggerType getLoggerType(String loggerType){
        switch (loggerType){
            case "log4j":
                return LoggerType.LOG4J;
            case "slf4j":
                return LoggerType.SL4J;
            default:
                throw new LoggerTypeNotSupportedException("Logger Type '" + loggerType + "' not defined.");
        }
    }

    public static CSLogger getLogger() {
        return logger;
    }

    private static ReporterType getReporterType() {
        return getReporter(LoggerConstants.getPropertyAsPerThePriority("tool.reporter", "ExtentReport"));
    }

    private static ReporterType getReporter(String reporterType){
        switch (reporterType){
            case "ExtentReport":
                return ReporterType.EXTENTREPORT;
            case "ReportPortal":
                return ReporterType.REPORTPORTAL;
            default:
                throw new ArgumentNotSupportedException("Reporter Type '" + reporterType + "' not defined.");
        }
    }

    public static HTMLReportObserver getReporter() {
        return reporter;
    }
}
