package com.epam.framework.core.reporting.extent;

import com.aventstack.extentreports.ExtentReports;
import com.aventstack.extentreports.ExtentTest;
import com.aventstack.extentreports.MediaEntityBuilder;
import com.aventstack.extentreports.reporter.ExtentSparkReporter;
import com.epam.framework.core.logging.logger.LogLevel;
import com.epam.framework.core.reporting.HTMLReportObserver;
import com.epam.framework.core.utils.PropertyReader;
import org.apache.commons.io.FileUtils;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import javax.imageio.ImageIO;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.nio.charset.Charset;
import java.text.SimpleDateFormat;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Date;
import java.util.Map;

public class ExtentHTMLReportObserver implements HTMLReportObserver {

    private static final Logger logger = LoggerFactory.getLogger(ExtentHTMLReportObserver.class);
    private static final String REPORT_OUT_PROPERTY = "html.report.out.directory";
    private static final String REPORT_OUT_DEFAULT_VALUE = "target/html-report/";
    private static final String SCREENSHOTS_FOLDER = "/screenshots/";

    PropertyReader propertyReader = new PropertyReader("src\\test\\resources\\system.properties");

    private static ExtentReports extentReports = new ExtentReports();
    private static ThreadLocal<ExtentTest> extentTestThreadLocal = new ThreadLocal<>();

    @Override
    public synchronized void setUp() {
        String currentDateTime = LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy_MM_dd HH_mm"));
        ExtentSparkReporter htmlReporter = new ExtentSparkReporter(new File(propertyReader.getProperty(REPORT_OUT_PROPERTY, REPORT_OUT_DEFAULT_VALUE) + currentDateTime+File.separator+ propertyReader.getProperty("html.report.name", "report.html")));
        configureExtentReportFromXml(htmlReporter);
        extentReports.attachReporter(htmlReporter);
    }

    @Override
    public void setUp(String reportName) {
        String currentDateTime = LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy_MM_dd HH_mm"));
        ExtentSparkReporter htmlReporter = new ExtentSparkReporter(propertyReader.getProperty(REPORT_OUT_PROPERTY, REPORT_OUT_DEFAULT_VALUE) + reportName + currentDateTime+File.separator + propertyReader.getProperty("html.report.name", "report.html"));
        configureExtentReportFromXml(htmlReporter);
        extentReports.attachReporter(htmlReporter);
    }

    @Override
    public synchronized void tearDown() {
        extentReports.flush();
        extentTestThreadLocal.remove();
    }

    @Override
    public synchronized void createTest(String testName) {
        ExtentTest methodTest = extentReports.createTest(testName);
        extentTestThreadLocal.set(methodTest);
    }

    @Override
    public void createTest(String testName, Map<String, Object> additionalParams) {
        ExtentTest methodTest = extentReports.createTest(testName);
        extentTestThreadLocal.set(methodTest);
    }

    @Override
    public synchronized void log(LogLevel messageType, String message) {
        switch (messageType) {
            case WARNING:
                warning(message);
                break;
            case ERROR:
                error(message);
                break;
            case DEBUG:
                error("DEBUG: " + message);
                break;
            case INFO:
            default:
                info(message);
                break;
        }

    }

    @Override
    public void log(LogLevel messageType, String message, Throwable throwable) {
        switch (messageType) {
            case WARNING:
                warning(message, throwable);
                break;
            case ERROR:
                error(message, throwable);
                break;
            case DEBUG:
                error("DEBUG: " + message, throwable);
                break;
            case INFO:
            default:
                info(message, throwable);
                break;
        }
    }

    @Override
    public synchronized void info(String message) {
        getTest().info(message);
    }

    @Override
    public synchronized void info(String message, Throwable throwable) {
        getTest().info(message);
        getTest().info(throwable);
    }

    @Override
    public synchronized void pass(String message) {
        getTest().pass(message);
    }

    @Override
    public synchronized void fail(String message) {
        getTest().fail(message);
    }

    @Override
    public synchronized void fail(String message, Throwable throwable) {
        getTest().fail(message);
        getTest().fail(throwable);
    }

    @Override
    public synchronized void skip(String message) {
        getTest().skip(message);
    }

    @Override
    public synchronized void skip(String message, Throwable throwable) {
        getTest().skip(message);
        getTest().skip(throwable);
    }

    @Override
    public synchronized void warning(String message) {
        getTest().warning(message);
    }

    @Override
    public synchronized void warning(String message, Throwable throwable) {
        getTest().warning(message);
        getTest().warning(throwable);
    }

    @Override
    public synchronized void error(String message) {
        getTest().error(message);
    }

    @Override
    public synchronized void error(String message, Throwable throwable) {
        getTest().error(message);
        getTest().error(throwable);
    }

    @Override
    public synchronized void addScreenshot(String screenshotName, String description) {

        String newFileName = screenshotName + new SimpleDateFormat("yyyyMMddHHmmss").format(new Date());

        File destFilePath = new File(propertyReader.getProperty(REPORT_OUT_PROPERTY, REPORT_OUT_DEFAULT_VALUE) + SCREENSHOTS_FOLDER);
        if(!destFilePath.exists()){
            destFilePath.mkdirs();
        }
        File destFile = new File(propertyReader.getProperty(REPORT_OUT_PROPERTY, REPORT_OUT_DEFAULT_VALUE) + SCREENSHOTS_FOLDER + newFileName + ".png");
        try {
            Robot r = new Robot();
            Rectangle capture =
                    new Rectangle(Toolkit.getDefaultToolkit().getScreenSize());
            BufferedImage image = r.createScreenCapture(capture);
            ImageIO.write(image, "png", destFile);
            getTest().info(description, MediaEntityBuilder.createScreenCaptureFromPath(destFile.getAbsolutePath()).build());
        } catch (Exception e) {
            logger.info("Getting exception While taking the Screenshots", e);
        }
    }

    @Override
    public synchronized void addFile(String fileName, String description,String fileData){
        String newFileName = fileName + new SimpleDateFormat("yyyyMMddHHmmss").format(new Date());
        try {
            File destFile = new File(propertyReader.getProperty(REPORT_OUT_PROPERTY, REPORT_OUT_DEFAULT_VALUE) + SCREENSHOTS_FOLDER + newFileName);
            FileUtils.writeStringToFile(destFile,fileData, Charset.defaultCharset());
            getTest().info("<a href='" + destFile.getAbsolutePath() + "'>click to view text</a>");
        }
        catch (Exception e){
            logger.info("Getting exception While taking the Screenshots", e);
        }
    }

    private synchronized ExtentTest getTest() {
        return extentTestThreadLocal.get();
    }

    private synchronized void configureExtentReportFromXml(ExtentSparkReporter htmlReporter) {

        try {
            String configXmlFile = System.getProperty("user.dir")
                    +File.separator
                    +"src\\test\\resources\\"+propertyReader.getProperty("html.report.xmlconfig.name", "extent-config.xml");;
            logger.info("Loading Extent Report configuration parameters from XML File{}", configXmlFile);
            htmlReporter.loadXMLConfig(configXmlFile);
        } catch (Exception ex) {
            logger.info("Got the exception while reading Extent report parameters from xml file. " +
                    "So setting Dark Mode and keeping rest as default");

        }

    }
}