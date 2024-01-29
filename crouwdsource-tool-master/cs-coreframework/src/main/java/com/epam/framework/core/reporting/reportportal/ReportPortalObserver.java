package com.epam.framework.core.reporting.reportportal;

import com.epam.framework.api.httpclient.RestAPIRequest;
import com.epam.framework.api.httpclient.RestAPIResponse;
import com.epam.framework.core.Context;
import com.epam.framework.core.TestContext;
import com.epam.framework.core.exceptions.ReportingException;
import com.epam.framework.core.logging.logger.LogLevel;
import com.epam.framework.core.reporting.HTMLReportObserver;
import com.epam.framework.core.reporting.reportportal.api.builder.StartLaunchRequestBuilder;
import com.epam.framework.core.reporting.reportportal.api.requests.*;
import com.epam.framework.core.reporting.reportportal.api.requests.FinishLaunchRequest.statusEnum;
import com.epam.framework.core.reporting.reportportal.api.requests.Issue.issueType;
import com.epam.framework.core.reporting.reportportal.api.requests.StartSuiteRequest.TestItem;
import com.epam.framework.core.reporting.reportportal.api.response.StartLaunchResponse;
import com.epam.framework.core.reporting.reportportal.api.response.StartStepContainerResponse;
import com.epam.framework.core.reporting.reportportal.api.response.StartStepResponse;
import com.epam.framework.core.reporting.reportportal.api.response.StartSuiteResponse;
import com.epam.framework.core.reporting.reportportal.api.utils.RequestHelper;
import com.epam.framework.core.reporting.reportportal.api.utils.ResponseHelper;
import com.epam.framework.core.utils.PropertyReader;
import org.apache.commons.io.FileUtils;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import javax.imageio.ImageIO;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.time.ZoneOffset;
import java.time.ZonedDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Date;
import java.util.Map;

import static com.epam.framework.api.httpclient.HttpMethod.POST;
import static com.epam.framework.api.httpclient.HttpMethod.PUT;

public class ReportPortalObserver implements HTMLReportObserver {


	private static final String STEP_ID = "stepId";
	private static final String CONTAINER_ID = "containerId";
	private static final String LAUNCH_ID = "launchId";
	private static final String TEST_NAME = "testName";
	private static final Logger logger = LoggerFactory.getLogger("ReportPortalLogger");
	public static final PropertyReader prop = new PropertyReader("src\\test\\resources\\reportportal.properties");

	private static final String BASE_URI = "https://reportportal.epam.com/api/v1/";
	private static final String PROJECT_NAME = prop.getProperty("rp.project");
	private static final String START_LAUNCH_URI = BASE_URI + PROJECT_NAME + "/launch";
	private static final String START_SUITE_URI = BASE_URI + PROJECT_NAME + "/item";
	private static final String START_STEP_URI = BASE_URI + PROJECT_NAME + "/item/";
	private static final String FINISH_STEP_URI = BASE_URI + PROJECT_NAME + "/item/";
	private static final String FINISH_LAUNCH_URI = BASE_URI + PROJECT_NAME + "/launch/";

	private static final String INTERRUPTED = "interrupted";
	private static final String ROOT_ID = "rootId";
	private static final String CONTEXT_TYPE = "application/json";
	private static final String UUID = "rp.uuid";
	private static final String TOKEN = "token";
	private static final String SCREENSHOTS_FOLDER = "/screenshots/";

	private static final String OUTPUT_DIRECTORY = prop.getProperty("html.report.out.directory", "target/html-report/");
	private static final String FAILED_MESSAGE = "failed";

	@Override
	public void setUp() {
		TestContext.registerContext(new Context());
		TestContext.put(TOKEN, prop.getProperty(UUID));
	}


	@Override
	public void setUp(String reportName) {
	/*
	This method can be used in case of setting up the report with a report name
	 */
	}

	@Override
	public void tearDown() {
	/*
	This method can be used in case of flushing the reports like extent report
	 */
	}


	@Override
	public void createTest(String testName) {
		/*
	This method is used only in case of Extent report
	 */
	}

	@Override
	public void createTest(String testName, Map<String, Object> additionalParams) {
		createLaunch(testName, additionalParams);
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
	public void info(String message) {
		logger.info(message);
	}

	@Override
	public void info(String message, Throwable throwable) {
		logger.info(message, throwable);
	}

	@Override
	public void pass(String message) {
		logger.info("[PASS] {}", message);
		addScreenshot("Pass", message);
		triggerReportPortalRequests(message,"passed");
	}



	@Override
	public void fail(String message) {
		logger.error(message);
		addScreenshot("Failure", message);
		triggerReportPortalRequests(message,FAILED_MESSAGE);
	}

	@Override
	public void fail(String message, Throwable throwable) {
		logger.error(message, throwable);
		addScreenshot("Failure", message);
		triggerReportPortalRequests(message+"/n"+throwable.getMessage(),FAILED_MESSAGE);
	}

	@Override
	public void skip(String message) {
		logger.info("[SKIP] {}", message);
		triggerReportPortalRequests(message,"skipped");
	}

	@Override
	public void skip(String message, Throwable throwable) {
		logger.info(message, throwable);
		triggerReportPortalRequests(message+"/n"+throwable.getMessage(),"skipped");
	}

	@Override
	public void warning(String message) {
		logger.warn(message);
		triggerReportPortalRequests(message,INTERRUPTED);
	}

	@Override
	public void warning(String message, Throwable throwable) {
		logger.warn(message, throwable);
		triggerReportPortalRequests(message+"/n"+throwable.getMessage(),INTERRUPTED);
	}

	@Override
	public void error(String message) {
		logger.error(message);
		triggerReportPortalRequests(message,INTERRUPTED);
	}

	@Override
	public void error(String message, Throwable throwable) {
		logger.error(message, throwable);
		triggerReportPortalRequests(message+"/n"+throwable.getMessage(),INTERRUPTED);
	}

	private void triggerReportPortalRequests(String message,String status) {
		startSuiteRequest(message);
		startStepContainer(message);
		startStepRequest(message);
		finishStepRequest(message, status);
		finishStepContainer();
		finishSuiteRequest();
		finishLaunch(status);
	}

	private void finishStepRequest(String message, String status) {
		FinishStepRequest finishStepRequest = new FinishStepRequest();
		Issue issue = new Issue();
		finishStepRequest.setEndTime(getISOTime());
		if(status.equals(FAILED_MESSAGE)) {
			setIssue(message, finishStepRequest, issue);
		}else if(status.equals(INTERRUPTED)) {
			setIssue(message, finishStepRequest, issue);
		}else {
			finishStepRequest.setStatus(status);
		}
		finishStepRequest.setLaunchUuid(TestContext.get(LAUNCH_ID));
		RestAPIRequest.createRequest(FINISH_STEP_URI+TestContext.get(STEP_ID),PUT);
		RestAPIRequest.addBearerTokenAuth(TestContext.get(TOKEN));
		RestAPIRequest.addBody(RequestHelper.getJsonString(finishStepRequest));
		RestAPIRequest.addContentType(CONTEXT_TYPE);
		try {
			RestAPIRequest.sendRequest();
		} catch (IOException e) {
			throw new ReportingException(e.getMessage(),e);
		}
	}

	private void setIssue(String message, FinishStepRequest finishStepRequest, Issue issue) {
		issue.setIssueType(issueType.PB001);
		issue.setComment(message);
		finishStepRequest.setIssue(issue);
	}

	private void startStepRequest(String message) {
		StartStepRequest startStepRequest = new StartStepRequest();
		startStepRequest.setDescription(message);
		startStepRequest.setName(TestContext.get(TEST_NAME));
		startStepRequest.setLaunchUuid(TestContext.get(LAUNCH_ID));
		startStepRequest.setStartTime(getISOTime());
		startStepRequest.setType("test");

		RestAPIRequest.createRequest(START_STEP_URI+TestContext.get(CONTAINER_ID),POST);
		RestAPIRequest.addBearerTokenAuth(TestContext.get(TOKEN));
		RestAPIRequest.addBody(RequestHelper.getJsonString(startStepRequest));
		RestAPIRequest.addContentType(CONTEXT_TYPE);
		try {
			RestAPIRequest.sendRequest();
			StartStepResponse response = (StartStepResponse) ResponseHelper
					.getResponseAsObject(RestAPIResponse.getBody(), StartStepResponse.class);
			TestContext.put(STEP_ID, response.getId());
		} catch (IOException e) {
			throw new ReportingException(e.getMessage(),e);
		}
	}


	@Override
	public void addScreenshot(String screenshotName, String description) {

		String newFileName = screenshotName + new SimpleDateFormat("yyyyMMddHHmmss").format(new Date());

		File destFilePath = new File(OUTPUT_DIRECTORY + SCREENSHOTS_FOLDER);
		if (!destFilePath.exists()) {
			destFilePath.mkdirs();
		}
		File destFile = new File(OUTPUT_DIRECTORY + SCREENSHOTS_FOLDER + newFileName + ".png");
		try {
			Robot r = new Robot();
			Rectangle capture = new Rectangle(Toolkit.getDefaultToolkit().getScreenSize());
			BufferedImage Image = r.createScreenCapture(capture);
			ImageIO.write(Image, "jpg", destFile);

			logger.info("RP_MESSAGE#FILE#{}#{}", destFile.getAbsolutePath(), description);

		} catch (Exception e) {
			logger.info("Getting exception While taking the Screenshots", e);
		}
	}

	@Override
	public synchronized void addFile(String FileName, String description, String FileData) {
		String newFileName = FileName + new SimpleDateFormat("yyyyMMddHHmmss").format(new Date());
		try {
			File destFile = new File(OUTPUT_DIRECTORY + SCREENSHOTS_FOLDER + newFileName);
			FileUtils.writeStringToFile(destFile, FileData);
			logger.info("RP_MESSAGE#FILE#{}#{}", destFile.getAbsolutePath(), description);
		} catch (Exception e) {
			logger.info("Getting exception While taking the Screenshots", e);
		}
	}

	private void createLaunch(String testName, Map<String, Object> testParams) {
		StartLaunchRequest startLaunchRequest = buildLaunchRequest(testName, testParams);

		RestAPIRequest.createRequest(START_LAUNCH_URI,POST);
		RestAPIRequest.addBearerTokenAuth(TestContext.get(TOKEN));
		RestAPIRequest.addBody(RequestHelper.getJsonString(startLaunchRequest));
		RestAPIRequest.addContentType(CONTEXT_TYPE);

		TestContext.put(TEST_NAME, testName);
		try {
			RestAPIRequest.sendRequest();
			StartLaunchResponse startLaunchResponse = (StartLaunchResponse) ResponseHelper
					.getResponseAsObject(RestAPIResponse.getBody(), StartLaunchResponse.class);
			TestContext.put(LAUNCH_ID, startLaunchResponse.getId());

		} catch (IOException e) {
			throw new ReportingException(e.getMessage(),e);
		}
	}

	private StartLaunchRequest buildLaunchRequest(String testName, Map<String, Object> testParams) {
		return new StartLaunchRequestBuilder().withName(testName).withRerun(false)
				.withStartTime(getISOTime())
				.withMode("DEFAULT").withDescription((String) testParams.get("desc")).build();
	}

	private String getISOTime() {
		return ZonedDateTime.now(ZoneOffset.UTC).format(DateTimeFormatter.ISO_INSTANT);
	}

	private void startSuiteRequest(String message) {
		StartSuiteRequest startSuiteRequest = new StartSuiteRequest();
		startSuiteRequest.setHasStats(true);
		startSuiteRequest.setLaunchUuid(TestContext.get(LAUNCH_ID));
		startSuiteRequest.setName(message);
		startSuiteRequest.setRetry(false);
		startSuiteRequest.setStartTime(getISOTime());
		startSuiteRequest.setType(TestItem.TEST);
		startSuiteRequest.setDescription(message);
		RestAPIRequest.createRequest(START_SUITE_URI,POST);
		RestAPIRequest.addBearerTokenAuth(TestContext.get(TOKEN));
		RestAPIRequest.addBody(RequestHelper.getJsonString(startSuiteRequest));
		RestAPIRequest.addContentType(CONTEXT_TYPE);


		try {
			RestAPIRequest.sendRequest();
			StartSuiteResponse response = (StartSuiteResponse) ResponseHelper
					.getResponseAsObject(RestAPIResponse.getBody(), StartSuiteResponse.class);
			TestContext.put(ROOT_ID, response.getId());
		} catch (IOException e) {
			throw new ReportingException(e.getMessage(),e);
		}
	}

	private void finishLaunch(String status) {
		FinishLaunchRequest finishLaunchRequest = new FinishLaunchRequest();
		finishLaunchRequest.setEndTime(getISOTime());
		finishLaunchRequest.setStatus(statusEnum.valueOf(status));
		RestAPIRequest.createRequest(FINISH_LAUNCH_URI+TestContext.get(LAUNCH_ID),PUT);
		RestAPIRequest.addBearerTokenAuth(TestContext.get(TOKEN));
		RestAPIRequest.addBody(RequestHelper.getJsonString(finishLaunchRequest));
		RestAPIRequest.addContentType(CONTEXT_TYPE);

		try {
			RestAPIRequest.sendRequest();
		} catch (IOException e) {
			throw new ReportingException(e.getMessage(),e);
		}
	}

	private void finishSuiteRequest() {
		FinishSuiteRequest finishSuiteRequest = new FinishSuiteRequest();
		finishSuiteRequest.setEndTime(getISOTime());
		finishSuiteRequest.setLaunchUuid(TestContext.get(LAUNCH_ID));
		RestAPIRequest.createRequest(FINISH_STEP_URI+TestContext.get(ROOT_ID),PUT);
		RestAPIRequest.addBearerTokenAuth(TestContext.get(TOKEN));
		RestAPIRequest.addBody(RequestHelper.getJsonString(finishSuiteRequest));
		RestAPIRequest.addContentType(CONTEXT_TYPE);

		try {
			RestAPIRequest.sendRequest();
		} catch (IOException e) {
			throw new ReportingException(e.getMessage(),e);
		}
	}

	private void finishStepContainer() {
		FinishStepContainerRequest finishStepContainerRequest = new FinishStepContainerRequest();
		finishStepContainerRequest.setEndTime(getISOTime());
		finishStepContainerRequest.setLaunchUuid(TestContext.get(LAUNCH_ID));
		RestAPIRequest.createRequest(FINISH_STEP_URI+TestContext.get(ROOT_ID),PUT);
		RestAPIRequest.addBearerTokenAuth(TestContext.get(TOKEN));
		RestAPIRequest.addBody(RequestHelper.getJsonString(finishStepContainerRequest));
		RestAPIRequest.addContentType(CONTEXT_TYPE);

		try {
			RestAPIRequest.sendRequest();
		} catch (IOException e) {
			throw new ReportingException(e.getMessage(),e);
		}
	}

	private void startStepContainer(String message) {
		StartStepContainerRequest containerRequest = new StartStepContainerRequest();
		containerRequest.setDescription(message);
		containerRequest.setName(TestContext.get(TEST_NAME));
		containerRequest.setLaunchUuid(TestContext.get(LAUNCH_ID));
		containerRequest.setStartTime(getISOTime());
		containerRequest.setType("test");
		RestAPIRequest.createRequest(START_STEP_URI+TestContext.get(ROOT_ID),POST);
		RestAPIRequest.addBearerTokenAuth(TestContext.get(TOKEN));
		RestAPIRequest.addBody(RequestHelper.getJsonString(containerRequest));
		RestAPIRequest.addContentType(CONTEXT_TYPE);

		try {
			RestAPIRequest.sendRequest();
			StartStepContainerResponse response = (StartStepContainerResponse) ResponseHelper
					.getResponseAsObject(RestAPIResponse.getBody(), StartStepContainerResponse.class);
			TestContext.put(CONTAINER_ID, response.getId());
		} catch (IOException e) {
			throw new ReportingException(e.getMessage(),e);
		}
	}

}