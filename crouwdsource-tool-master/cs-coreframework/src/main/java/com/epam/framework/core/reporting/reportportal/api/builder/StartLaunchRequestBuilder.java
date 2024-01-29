package com.epam.framework.core.reporting.reportportal.api.builder;

import com.epam.framework.core.reporting.reportportal.api.requests.StartLaunchRequest;

import java.util.List;

public class StartLaunchRequestBuilder {

	private StartLaunchRequest startLaunchRequest = new StartLaunchRequest();

	public StartLaunchRequestBuilder withAttributes(List<Object> attributes) {
		startLaunchRequest.setAttributes(attributes);
		return this;
	}

	public StartLaunchRequestBuilder withDescription(String description) {
		startLaunchRequest.setDescription(description);
		return this;
	}

	public StartLaunchRequestBuilder withMode(String mode) {
		startLaunchRequest.setMode(mode);
		return this;
	}

	public StartLaunchRequestBuilder withName(String name) {
		startLaunchRequest.setName(name);
		return this;
	}

	public StartLaunchRequestBuilder withRerun(Boolean rerun) {
		startLaunchRequest.setRerun(rerun);
		return this;
	}

	public StartLaunchRequestBuilder withRerunOf(String rerunOf) {
		startLaunchRequest.setRerunOf(rerunOf);
		return this;
	}

	public StartLaunchRequestBuilder withStartTime(String startTime) {
		startLaunchRequest.setStartTime(startTime);
		return this;
	}
	
	public StartLaunchRequest build() {
		return startLaunchRequest;
	}

}