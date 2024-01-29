package com.epam.framework.core.reporting.reportportal.api.requests;

import java.util.List;

public class StartSuiteRequest {

	private List<Object> attributes = null;
	private String codeRef;
	private String description;
	private Boolean hasStats;
	private String launchUuid;
	private String name;
	private List<Object> parameters = null;
	private Boolean retry;
	private String retryOf;
	private String startTime;
	private String testCaseId;
	private String type;
	private String uniqueId;

	public List<Object> getAttributes() {
		return attributes;
	}

	public void setAttributes(List<Object> attributes) {
		this.attributes = attributes;
	}

	public String getCodeRef() {
		return codeRef;
	}

	public void setCodeRef(String codeRef) {
		this.codeRef = codeRef;
	}

	public String getDescription() {
		return description;
	}

	public void setDescription(String description) {
		this.description = description;
	}

	public Boolean getHasStats() {
		return hasStats;
	}

	public void setHasStats(Boolean hasStats) {
		this.hasStats = hasStats;
	}

	public String getLaunchUuid() {
		return launchUuid;
	}

	public void setLaunchUuid(String launchUuid) {
		this.launchUuid = launchUuid;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public List<Object> getParameters() {
		return parameters;
	}

	public void setParameters(List<Object> parameters) {
		this.parameters = parameters;
	}

	public Boolean getRetry() {
		return retry;
	}

	public void setRetry(Boolean retry) {
		this.retry = retry;
	}

	public String getRetryOf() {
		return retryOf;
	}

	public void setRetryOf(String retryOf) {
		this.retryOf = retryOf;
	}

	public String getStartTime() {
		return startTime;
	}

	public void setStartTime(String startTime) {
		this.startTime = startTime;
	}

	public String getTestCaseId() {
		return testCaseId;
	}

	public void setTestCaseId(String testCaseId) {
		this.testCaseId = testCaseId;
	}

	public String getType() {
		return type;
	}

	public void setType(Enum<TestItem> type) {
		this.type = type.name();
	}

	public String getUniqueId() {
		return uniqueId;
	}

	public void setUniqueId(String uniqueId) {
		this.uniqueId = uniqueId;
	}
	
	public enum TestItem{
		SUITE,
		STORY,
		TEST,
		SCENARIO,
		STEP,
		BEFORE_CLASS,
		BEFORE_GROUPS,
		BEFORE_METHOD,
		BEFORE_SUITE,
		BEFORE_TEST,
		AFTER_CLASS,
		AFTER_GROUPS,
		AFTER_METHODS,
		AFTER_SUITE,
		AFETR_TEST
	}

}