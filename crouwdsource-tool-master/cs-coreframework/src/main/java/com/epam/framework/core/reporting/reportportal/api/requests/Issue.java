package com.epam.framework.core.reporting.reportportal.api.requests;

public class Issue {

	private String issueType;
	private String comment;

	public String getIssueType() {
		return issueType;
	}

	public void setIssueType(Enum<issueType> issueType) {
		this.issueType = issueType.name();
	}

	public String getComment() {
		return comment;
	}

	public void setComment(String comment) {
		this.comment = comment;
	}
	
	public enum issueType{
		ND001,
		PB001,
		TI001,
		AB001,
		SI001
	}

}