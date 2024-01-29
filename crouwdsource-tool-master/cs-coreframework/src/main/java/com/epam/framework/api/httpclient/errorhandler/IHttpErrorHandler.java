package com.epam.framework.api.httpclient.errorhandler;

import org.apache.http.HttpResponse;
import org.apache.http.client.methods.HttpUriRequest;

public interface IHttpErrorHandler {

    void checkResponseCodeAndThrowsException(final HttpUriRequest requestBase, final HttpResponse response,
                                             final int expectedResponseCode, final String requestLog, final String responseLog);

}
