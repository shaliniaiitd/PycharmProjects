package com.epam.framework.core.reporting.reportportal.api.requests;

import java.util.Collections;
import java.util.List;

public class StartLaunchRequest {

	private List<Object> attributes = Collections.emptyList();
	private String description;
	private String mode;
	private String name;
	private Boolean rerun;
	private String rerunOf;
	private String startTime;

	public List<Object> getAttributes() {
		return attributes;
	}

	public void setAttributes(List<Object> attributes) {
		this.attributes = attributes;
	}

	public String getDescription() {
		return description;
	}

	public void setDescription(String description) {
		this.description = description;
	}

	public String getMode() {
		return mode;
	}

	public void setMode(String mode) {
		this.mode = mode;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public Boolean getRerun() {
		return rerun;
	}

	public void setRerun(Boolean rerun) {
		this.rerun = rerun;
	}

	public String getRerunOf() {
		return rerunOf;
	}

	public void setRerunOf(String rerunOf) {
		this.rerunOf = rerunOf;
	}

	public String getStartTime() {
		return startTime;
	}

	public void setStartTime(String startTime) {
		this.startTime = startTime;
	}

}