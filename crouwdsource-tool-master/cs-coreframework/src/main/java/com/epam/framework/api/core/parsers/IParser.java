package com.epam.framework.api.core.parsers;

public interface IParser {
    public <T> T deserialize(String payload, Class<T> classDetails) throws Exception;
    public <T> String serialize(T payload) throws Exception;
}
