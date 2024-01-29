package com.epam.framework.api.core.parsers;

public enum ContentType {

    APPLICATION_XML("application/xml"),
    APPLICATION_JSON("application/json;charset=utf-8"),
    APPLICATION_PDF("application/pdf;charset=UTF-8"),
    APPLICATION_OCTET_STREAM("application/octet-stream"), FORM_DATA("application/x-www-form-urlencoded"),
    FORM_DATA_WITH_CHARSET("application/x-www-form-urlencoded; charset=UTF-8"),
    ANY("*/*"),
    MOBILE_USER_AGENT("Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 "
            + "(KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36 "
            + "(compatible; Googlebot/2.1; +http://www.google.com/bot.html)"),
    PLAIN_TEXT("text/plain;charset=UTF-8"),
    XML("text/xml;charset=UTF-8"),
    TEXT_JAVASCRIPT("text/javascript"),
    PKPASS("application/vnd.apple.pkpass"),
    IMAGE_PNG("image/png"),
    TEXT_HTML("text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8");

    private String value;

    ContentType(final String value) {
        this.value = value;
    }

    @Override
    public String toString() {
        return value;
    }
}

