package com.epam.framework.core.reporting.reportportal.api.utils;


import com.fasterxml.jackson.databind.DeserializationFeature;
import com.fasterxml.jackson.databind.ObjectMapper;

import java.io.IOException;

public class ResponseHelper {

	@SuppressWarnings("unchecked")
	public static Object getResponseAsObject(String responseString, Class<?> responseClass) throws IOException {
        ObjectMapper mapper = new ObjectMapper();
        mapper.configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, false);
        return mapper.readValue(responseString, responseClass);
    }
}
