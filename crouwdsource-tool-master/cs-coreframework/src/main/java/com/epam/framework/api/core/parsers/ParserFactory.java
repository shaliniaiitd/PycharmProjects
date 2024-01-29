package com.epam.framework.api.core.parsers;

import com.epam.framework.api.httpclient.errorhandler.ObjectParseException;

public class ParserFactory {
    public static IParser createParser(ContentType contentType) {
        IParser parser;
        switch (contentType) {
            case APPLICATION_JSON:
                parser = new JsonParser();
                break;
            case APPLICATION_XML:
                parser = new XmlParser();
                break;
            default:
                throw new ObjectParseException("Invalid parser type: " + contentType);
        }
        return null;
    }
}
