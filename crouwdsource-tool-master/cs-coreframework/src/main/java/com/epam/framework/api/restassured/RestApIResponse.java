package com.epam.framework.api.restassured;

import com.epam.framework.core.TestContext;
import com.epam.framework.core.logging.logger.LogLevel;
import io.restassured.RestAssured;
import io.restassured.response.Response;


public class RestApIResponse {

    private static Response response;
    static RestAPIRequest restAPIRequest;


    private RestApIResponse() {

    }

    public static Response getResponse() {
        return response;
    }



    public static Response sendRequest(HttpMethod requestType) {
        if (RestAPIRequest.getRequestSpecification() == null) {
            TestContext.getLogger().log(LogLevel.ERROR, "Please create a valid request by RestAPIRequest.createRequest()");
            return response;
        }

        switch (requestType) {
            case GET:
                TestContext.getLogger().log(LogLevel.INFO, "Creating a get request for : " + RestAPIRequest.getQueryableRequestSpecification().getBaseUri());
                response = RestAssured.given().when().spec(RestAPIRequest.getRequestSpecification()).get();
                break;
            case POST:
                response = RestAssured.given().when().spec(RestAPIRequest.getRequestSpecification()).post();
                break;
            case DELETE:
                response = RestAssured.given().when().spec(RestAPIRequest.getRequestSpecification()).delete();
                break;
            case PUT:
                response = RestAssured.given().when().spec(RestAPIRequest.getRequestSpecification()).put();
                break;
            case PATCH:
                response = RestAssured.given().when().spec(RestAPIRequest.getRequestSpecification()).patch();
                break;
            case OPTIONS:
                response = RestAssured.given().when().spec(RestAPIRequest.getRequestSpecification()).options();
                break;
            default:
                TestContext.getLogger().log(LogLevel.INFO, "Please give the correct action like GET,PUT,POST :");
                break;
        }
        return response;
    }


}
