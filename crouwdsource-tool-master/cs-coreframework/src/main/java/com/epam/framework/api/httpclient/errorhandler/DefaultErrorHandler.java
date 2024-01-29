package com.epam.framework.api.httpclient.errorhandler;

import com.epam.framework.api.httpclient.RestAPIResponse;
import com.epam.framework.core.TestContext;
import com.epam.framework.core.exceptions.EnvironmentException;
import com.epam.framework.core.exceptions.HttpRequestException;
import com.epam.framework.core.logging.logger.LogLevel;
import org.apache.http.HttpResponse;
import org.apache.http.client.methods.HttpUriRequest;

import java.text.MessageFormat;

import static java.lang.String.format;

public class DefaultErrorHandler implements IHttpErrorHandler {

    @Override
    public void checkResponseCodeAndThrowsException(final HttpUriRequest requestBase, final HttpResponse responseWrapper,
                                                    final int expectedResponseCode, final String requestLog, final String responseLog) {
        int statusCode = RestAPIResponse.getResponse().getStatusLine().getStatusCode();
        if (statusCode > 499 && statusCode < 512) {
            TestContext.getLogger().log(LogLevel.ERROR,"Request {"+requestBase.getURI()+"} failed because status code is in range 500-511");
            throw new EnvironmentException(format("Request %s failed because status code is in range 500-511", requestBase.getURI()));
        }

        if (expectedResponseCode != -1 && statusCode != expectedResponseCode) {
            throw new HttpRequestException(MessageFormat.format("Expected code {0} but actual is {1}\n" +
                        "EXCEPTION DETAILS:\n{2}\n{3}", expectedResponseCode, statusCode, requestLog, responseLog));
        }
    }

}
