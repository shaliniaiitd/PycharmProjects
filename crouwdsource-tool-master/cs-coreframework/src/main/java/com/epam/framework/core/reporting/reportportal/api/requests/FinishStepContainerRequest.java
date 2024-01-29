package com.epam.framework.core.reporting.reportportal.api.requests;

public class FinishStepContainerRequest {

	private String endTime;
	private String launchUuid;

	public String getEndTime() {
		return endTime;
	}

	public void setEndTime(String endTime) {
		this.endTime = endTime;
	}

	public String getLaunchUuid() {
		return launchUuid;
	}

	public void setLaunchUuid(String launchUuid) {
		this.launchUuid = launchUuid;
	}

}