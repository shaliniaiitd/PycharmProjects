package com.epam.framework.api.httpclient;


import com.epam.framework.core.TestContext;
import com.epam.framework.core.constants.MessageConstants;
import com.epam.framework.core.logging.logger.LogLevel;
import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.jayway.jsonpath.DocumentContext;
import com.jayway.jsonpath.JsonPath;
import com.jayway.jsonpath.PathNotFoundException;
import org.apache.http.util.EntityUtils;
import org.assertj.core.api.Assertions;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.util.*;

public class RestAPIResponseValidator {

    RestAPIRequest restAPIRequest;
    RestAPIResponse restApIResponse;

    public static boolean validateURI(String uri){
        String url = RestAPIRequest.getHttpUriRequest().getURI().toString();
        if (url.equals(uri))
            return true;
        else {
            TestContext.getLogger().log(LogLevel.ERROR, String.format(MessageConstants.API_VALIDATION_ERROR_MESSAGE,url,uri));
            return false;
        }
    }


    public static boolean validateProtocolVersion(String protocol) {
        String responseProtocol = RestAPIResponse.getResponse().getStatusLine().getProtocolVersion().toString();
        if (responseProtocol.equals(protocol))
            return true;
        else {
            TestContext.getLogger().log(LogLevel.ERROR, String.format(MessageConstants.API_VALIDATION_ERROR_MESSAGE,protocol,responseProtocol));
            return false;
        }
    }

    public static boolean validateStatusLine(String responseLine) {
        String responseProtocol = RestAPIResponse.getResponse().getStatusLine().toString();
        if (responseProtocol.equals(responseLine))
            return true;
        else {
            TestContext.getLogger().log(LogLevel.ERROR, String.format(MessageConstants.API_VALIDATION_ERROR_MESSAGE,responseLine,responseProtocol));
            return false;
        }
    }

    public static boolean validateStatusCode(int expectedStatusCode) {
        int actualStatusCode = RestAPIResponse.getResponse().getStatusLine().getStatusCode();
        if (actualStatusCode == expectedStatusCode)
            return true;
        else {
            TestContext.getLogger().log(LogLevel.ERROR, String.format(MessageConstants.API_VALIDATION_ERROR_MESSAGE,expectedStatusCode,actualStatusCode));
            return false;
        }
    }

    public static boolean validateReasonPhrase(String ok) {
        String responseProtocol = RestAPIResponse.getResponse().getStatusLine().toString().substring(13, 15);
        if (responseProtocol.equals(ok))
            return true;
        else {
            TestContext.getLogger().log(LogLevel.ERROR, String.format(MessageConstants.API_VALIDATION_ERROR_MESSAGE,ok,responseProtocol));
            return false;
        }
    }

    public <T> void validateNodeInResponseBody(String node, T expectedValue) throws IOException {
        String responseBody = EntityUtils.toString(RestAPIResponse.getResponse().getEntity(), StandardCharsets.UTF_8);
        Map<String, Object> object = JsonPath.read(responseBody, "$");
        Assertions.assertThat(object.get(node)).withFailMessage(() -> "Response doesn't contain node '" + node + "'")
                .isNotNull();
        Assertions.assertThat(object.get(node)).withFailMessage(() -> "Expected value for node '" + node + "' is not matching with actual value")
                .isEqualTo(expectedValue);
    }

    public void validateIfNodeDoesNotExist(String node) throws IOException {
        String responseBody = EntityUtils.toString(RestAPIResponse.getResponse().getEntity(), StandardCharsets.UTF_8);
        Map<String, Object> object = JsonPath.read(responseBody, "$");
        Assertions.assertThat(object.get(node))
                .withFailMessage(() -> "Node '" + node + "' should not exist in the response")
                .isNull();
    }

    public void validateNodeWithJsonpathInResponseBody(String jsonPath, String expectedValue) throws IOException {
        String responseBody = EntityUtils.toString(RestAPIResponse.getResponse().getEntity(), StandardCharsets.UTF_8);
        jsonPath = jsonPath.startsWith("$") ? jsonPath : "$" + jsonPath;
        String retrievedValue = JsonPath.read(responseBody, jsonPath);
        Assertions.assertThat(retrievedValue).withFailMessage(() -> "Node is null for the given jsonpath")
                .isNotNull();
        Assertions.assertThat(retrievedValue)
                .withFailMessage(() -> "The expected value" + expectedValue + " is not matching with actual value" + retrievedValue)
                .isEqualTo(expectedValue);
    }

    public <T> void validateNodeListsWithJsonpathInResponseBody(String jsonPath, T expectedValue) throws IOException {
        String responseBody = EntityUtils.toString(RestAPIResponse.getResponse().getEntity(), StandardCharsets.UTF_8);
        jsonPath = jsonPath.startsWith("$") ? jsonPath : "$" + jsonPath;
        List<T> retrievedValues = new ArrayList<>();
        retrievedValues.addAll(JsonPath.read(responseBody, jsonPath));
        retrievedValues.forEach(value -> {
            Assertions.assertThat(value).withFailMessage(() -> "Node is null for the given jsonpath")
                    .isNotNull();
            Assertions.assertThat(String.valueOf(value))
                    .withFailMessage(() -> "The expected value" + expectedValue + " is not matching with actual value" + value)
                    .isEqualTo(expectedValue);
        });
    }

    public Map<String, Object> mapJsonObject() throws IOException {
        String responseBody = EntityUtils.toString(RestAPIResponse.getResponse().getEntity(), StandardCharsets.UTF_8);
        ObjectMapper mapper = new ObjectMapper();
        return mapper.readValue(responseBody, new TypeReference<Map<String, Object>>() {
        });
    }

    public Map<String, String> getObjectMapFromListOfMaps(List<Object> childList, String nodeObjectValue) {
        Map<String, String> innerMap = new HashMap<>();
        for (Object value : childList) {
            if (value instanceof Map) {
                for (Map.Entry<String, String> me : ((Map<String, String>) value).entrySet()) {
                    if (me.getValue().equalsIgnoreCase(nodeObjectValue)) {
                        innerMap = (Map<String, String>) value;
                    }
                }
            }
        }
        return innerMap;
    }

    public List<Object> getChildNodesFromParentNode(String node) throws IOException {
        List<Object> childNodes = new ArrayList<>();
        Map<String, Object> map = mapJsonObject();
        for (Map.Entry<String, Object> entry : map.entrySet()) {
            if (String.valueOf(entry.getKey()).equalsIgnoreCase(node) && entry.getValue() instanceof Map) {
                childNodes = Collections.singletonList(getChildNodesForObjects((Map<String, Object>) entry.getValue()));
            } else if (String.valueOf(entry.getKey()).equalsIgnoreCase(node) && entry.getValue() instanceof List) {
                List<Object> nodeValues = new ArrayList<>();
                nodeValues.addAll((Collection<?>) entry.getValue());
                childNodes = nodeValues;
            }
        }
        return childNodes;
    }

    public static List<String> getChildNodesForObjects(Map<String, Object> map) {
        List<String> childNodes = new ArrayList<>();
        for (Map.Entry<String, Object> mapEntry : map.entrySet()) {
            childNodes.add(mapEntry.getKey());
        }
        return childNodes;
    }

    public void verifyBodyNodeValue(String jsonPath, String expValue, String errMsg) {
        try {
            String responseBody = EntityUtils.toString(RestAPIResponse.getResponse().getEntity(), StandardCharsets.UTF_8);
            DocumentContext jsonContext = JsonPath.parse(responseBody);
            String actValue = jsonContext.read(jsonPath);
            Assertions.assertThat(actValue).withFailMessage(() -> errMsg).isEqualTo(expValue);
        } catch (PathNotFoundException e) {
            Assertions.fail("Path not found");
        } catch (Exception e) {
            Assertions.fail("Exception while reading the value:" + e);
        }
    }

    public void verifyBodyNodePresence(String jsonPath, String errMsg) {
        try {
            String responseBody = EntityUtils.toString(RestAPIResponse.getResponse().getEntity(), StandardCharsets.UTF_8);
            DocumentContext jsonContext = JsonPath.parse(responseBody);
            String actValue = jsonContext.read(jsonPath);
            Assertions.assertThat(actValue).isNotEmpty().withFailMessage(() -> errMsg);
        } catch (PathNotFoundException e) {
            Assertions.fail("Path not found");
        } catch (Exception e) {
            Assertions.fail("Exception while reading the value:" + e);
        }
    }

    public static void verifyJSONs(String actualJson, String expectedJson, String errMsg) throws IOException {
        ObjectMapper mapper = new ObjectMapper();
        Assertions.assertThat(mapper.readTree(actualJson))
                .withFailMessage(() -> errMsg)
                .isEqualTo(mapper.readTree(expectedJson));
    }
}

