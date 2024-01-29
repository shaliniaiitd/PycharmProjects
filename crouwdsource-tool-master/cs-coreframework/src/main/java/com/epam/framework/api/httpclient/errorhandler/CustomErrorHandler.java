package com.epam.framework.api.httpclient.errorhandler;

import com.epam.framework.api.httpclient.RestAPIResponse;
import com.epam.framework.core.exceptions.HttpRequestException;
import org.apache.http.HttpResponse;
import org.apache.http.client.methods.HttpUriRequest;

import java.text.MessageFormat;

public class CustomErrorHandler implements IHttpErrorHandler {

    @Override
    public void checkResponseCodeAndThrowsException(HttpUriRequest requestBase, HttpResponse responseWrapper,
                                                    int expectedResponseCode, String requestLog, String responseLog) {
        int actualCode = RestAPIResponse.getResponse().getStatusLine().getStatusCode();
        if (expectedResponseCode != -1 && actualCode != expectedResponseCode) {
           throw new HttpRequestException(MessageFormat.format("Expected code {0} but actual is {1}\n" +
                        "EXCEPTION DETAILS:\n{2}\n{3}", expectedResponseCode, actualCode, requestLog, responseLog));
        }
    }
}
