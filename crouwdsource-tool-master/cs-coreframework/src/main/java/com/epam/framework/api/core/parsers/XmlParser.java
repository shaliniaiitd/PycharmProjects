package com.epam.framework.api.core.parsers;

import com.fasterxml.jackson.core.JsonParseException;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonMappingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.dataformat.xml.XmlMapper;
import org.apache.http.HttpResponse;

import java.io.IOException;

public class XmlParser implements IParser {
    @Override
    public <T> T deserialize(String payload, Class<T> classDetails)
            throws JsonParseException, JsonMappingException, IOException {
        ObjectMapper mapper = new XmlMapper();
        return mapper.readValue(payload.getBytes(), classDetails);
    }

    @Override
    public <T> String serialize(T payload) throws JsonProcessingException {
        ObjectMapper mapper = new XmlMapper();
        return mapper.writeValueAsString(payload);
    }

    public static <T> String parseXmlPayload(T payload) throws Exception {
        IParser parser = ParserFactory.createParser(ContentType.APPLICATION_XML);
        return parser.serialize(payload);
    }

    public static <T> T getDeserializedResponseForXML(HttpResponse response, Class<T> classObject) throws Exception {
        if (response == null)
            throw new IllegalStateException("No response found");
        IParser parser = ParserFactory.createParser(ContentType.APPLICATION_XML);
        return parser.deserialize(response.toString(), classObject);
    }

}
