package com.epam.framework.api.httpclient;

import org.apache.http.HttpResponse;


public class RestAPIResponse {

    private static int statusCode;
    private static String body;
    private static String bodyEncoded;
    private HttpResponse rawResponse;
    private static byte[] fileEntity;
    private static HttpResponse response;

    private RestAPIResponse() {

    }

    public static HttpResponse getResponse() {
        return response;
    }

    public static byte[] getFileEntity() {
        return fileEntity;
    }

    public static String getBody() {
        return body;
    }

    public static String getBodyEncoded() {
        return bodyEncoded;
    }

    public static int getStatusCode() {
        return statusCode;
    }

    public static void setResponse(HttpResponse response){
        RestAPIResponse.response = response;
    }

    public static void setFileEntity(byte[] fileEntity){
        RestAPIResponse.fileEntity = fileEntity;
    }

    public static void setBodyEncoded(String bodyEncoded){
        RestAPIResponse.bodyEncoded = bodyEncoded;
    }

    public static void setBody(String body){
        RestAPIResponse.body = body;
    }

    HttpResponse getRawResponse() {
        return rawResponse;
    }
}

