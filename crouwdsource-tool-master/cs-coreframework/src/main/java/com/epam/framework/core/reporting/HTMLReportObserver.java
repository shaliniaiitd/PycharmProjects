package com.epam.framework.core.reporting;

import com.epam.framework.core.logging.logger.LogLevel;

import java.util.Map;

/**
 *
 */
public interface HTMLReportObserver {
    void setUp();

    void setUp(String reportName);

    void tearDown();

    void createTest(String testName);

    void createTest(String testName, Map<String, Object> additionalParams);

    void log(LogLevel messageType, String message);

    void log(LogLevel messageType, String message, Throwable throwable);

    void info(String message);

    void info(String message, Throwable throwable);

    void pass(String message);

    void fail(String message);

    void fail(String message, Throwable throwable);

    void skip(String message);

    void skip(String message, Throwable throwable);

    void warning(String message);

    void warning(String message, Throwable throwable);

    void error(String message);

    void error(String message, Throwable throwable);

    void addScreenshot(String screenshotName, String description);

    void addFile(String fileName, String description,String fileData);
}
