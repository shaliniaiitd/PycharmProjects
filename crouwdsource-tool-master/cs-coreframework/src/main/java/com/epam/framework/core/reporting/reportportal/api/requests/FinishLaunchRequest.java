
package com.epam.framework.core.reporting.reportportal.api.requests;

public class FinishLaunchRequest {

	private String endTime;
	private String status;

	public String getEndTime() {
		return endTime;
	}

	public void setEndTime(String endTime) {
		this.endTime = endTime;
	}

	public String getStatus() {
		return status;
	}

	public void setStatus(Enum<statusEnum> status) {
		this.status = status.name();
	}
	
	public enum statusEnum{
		PASSED,
		FAILED,
		STOPPED,
		SKIPPED,
		INTERUPTTED,
		CANCELLED
	}

}