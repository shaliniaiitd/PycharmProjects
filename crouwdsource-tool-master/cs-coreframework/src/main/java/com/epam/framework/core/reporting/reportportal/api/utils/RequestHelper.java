package com.epam.framework.core.reporting.reportportal.api.utils;


import com.epam.framework.core.exceptions.HttpRequestException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.SerializationFeature;

import java.io.IOException;

public class RequestHelper {
	
	private RequestHelper(){}

	@SuppressWarnings("deprecation")
	public static String getJsonString(Object o) {
        ObjectMapper objectMapper = new ObjectMapper();
        objectMapper.getSerializationConfig().without(SerializationFeature.WRITE_NULL_MAP_VALUES);

        try {
            return objectMapper.writeValueAsString(o);
        } catch (IOException e) {
            throw new HttpRequestException(e.getMessage());
        }

    }

}
