package com.epam.framework.api.core.parsers;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.json.JsonMapper;
import org.apache.http.HttpResponse;

public class JsonParser implements IParser {
    @Override
    public <T> T deserialize(String payload, Class<T> classDetails) throws Exception {
        ObjectMapper mapper = new JsonMapper();
        return mapper.readValue(payload.getBytes(), classDetails);
    }

    @Override
    public <T> String serialize(T payload) throws Exception {
        ObjectMapper mapper = new JsonMapper();
        return mapper.writeValueAsString(payload);
    }

    public static <T> String parseJSONPayload(T payload) throws Exception {
        IParser parser = ParserFactory.createParser(ContentType.APPLICATION_JSON);
        return parser.serialize(payload);
    }

    public static <T> T getDeserializedResponseForJSON(HttpResponse response, Class<T> classObject) throws Exception {
        if (response == null)
            throw new IllegalStateException("No response found");
        IParser parser = ParserFactory.createParser(ContentType.APPLICATION_JSON);
        return parser.deserialize(response.toString(), classObject);
    }
}

