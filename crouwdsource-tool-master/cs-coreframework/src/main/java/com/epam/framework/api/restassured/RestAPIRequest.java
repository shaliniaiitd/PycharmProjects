package com.epam.framework.api.restassured;

import io.restassured.RestAssured;
import io.restassured.builder.RequestSpecBuilder;
import io.restassured.response.Response;
import io.restassured.specification.QueryableRequestSpecification;
import io.restassured.specification.RequestSpecification;
import io.restassured.specification.SpecificationQuerier;

public class RestAPIRequest {
    private static RequestSpecification requestSpecification = RestAssured.given();
    private static QueryableRequestSpecification queryableRequestSpecification;
    private static Response response;

    private RestAPIRequest() {
    }


    public static RequestSpecification getRequestSpecification() {
        return requestSpecification;
    }
    public static QueryableRequestSpecification getQueryableRequestSpecification() {
        return queryableRequestSpecification;
    }

    public static RequestSpecification createRequest(String baseURL) {
        requestSpecification = new RequestSpecBuilder().setBaseUri(baseURL)
                .build().log().all();
        queryableRequestSpecification = SpecificationQuerier.query(requestSpecification);
        return requestSpecification;
    }


}

