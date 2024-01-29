package com.epam.framework.core.reporting.reportportal.api.response;

import com.fasterxml.jackson.annotation.JsonProperty;

public class TokenResponse {
	@JsonProperty("access_token")
	private String accessToken;
	@JsonProperty("token_type")
	private String tokenType;
	private String scope;

	public String getAccessToken() {
		return accessToken;
	}

	public void setAccessToken(String access_token) {
		this.accessToken = access_token;
	}

	public String getTokenType() {
		return tokenType;
	}

	public void setTokenType(String token_type) {
		this.tokenType = token_type;
	}

	public String getScope() {
		return scope;
	}

	public void setScope(String scope) {
		this.scope = scope;
	}

}