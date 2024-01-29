package com.epam.framework.api.httpclient.tests;

import com.epam.framework.api.httpclient.RestAPIResponseValidator;
import com.epam.framework.api.httpclient.RestAPIRequest;
import com.epam.framework.api.httpclient.RestAPIResponse;
import org.apache.hc.core5.http.HttpException;
import org.apache.http.HttpHeaders;
import org.apache.http.HttpResponse;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpUriRequest;
import org.apache.http.client.methods.RequestBuilder;
import org.apache.http.entity.ContentType;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.HttpClients;
import org.junit.Test;
import org.testng.Assert;

import java.io.IOException;
import java.net.URISyntaxException;

import static com.epam.framework.api.httpclient.HttpMethod.GET;
import static com.epam.framework.api.httpclient.HttpMethod.POST;

public class Sample_Test {

    private static String requestBody = "{\"email\":\"eve.holt@reqres.in\",\"password\":\"cityslicka\"}";

    @Test
    public void
    getRequestTest() throws HttpException, URISyntaxException, IOException, org.apache.http.HttpException {
        RestAPIRequest.createRequest("https://dog.ceo/api/breeds/image/random", GET);   //.basePath("breeds/image/random");
        RestAPIRequest.sendRequest();
        // Write Asset here as people may want to choose different Assert like testng/junit/AssertJ/Hamcrest
        Assert.assertEquals(RestAPIResponseValidator.validateURI("https://dog.ceo/api/breeds/image/random"), true);
        Assert.assertEquals(RestAPIResponseValidator.validateProtocolVersion("HTTP/1.1"), true);
        Assert.assertEquals(RestAPIResponseValidator.validateStatusLine("HTTP/1.1 200 OK"), true);
        Assert.assertEquals(RestAPIResponseValidator.validateReasonPhrase("OK"), true);
    }

    @Test
    public void postTest() throws IOException {
        RestAPIRequest.createRequest("https://reqres.in/api/login", POST);
        RestAPIRequest.addBody(requestBody);
        RestAPIRequest.sendRequest();
        Assert.assertEquals(200, RestAPIResponse.getResponse().getStatusLine().getStatusCode());
    }

    @Test
    public void postTestUsingRequestBuilder() throws IOException {
        RestAPIRequest.createRequest("https://reqres.in/api/login", POST).setEntity(new StringEntity(requestBody, ContentType.APPLICATION_JSON));
        RestAPIRequest.sendRequest();
        Assert.assertEquals(200, RestAPIResponse.getResponse().getStatusLine().getStatusCode());
    }

    @Test
    public void nativeMethodTest() throws IOException {
        HttpClient client = HttpClients.custom().build();
        HttpUriRequest request = RequestBuilder.get()
                .setUri("https://dog.ceo/api/breeds/image/random")
                .setHeader(HttpHeaders.CONTENT_TYPE, "application/json")
                .build();
        HttpResponse response = client.execute(request);
    }

}

