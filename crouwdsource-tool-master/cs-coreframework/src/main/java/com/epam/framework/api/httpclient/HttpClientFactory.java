package com.epam.framework.api.httpclient;

import org.apache.http.client.HttpClient;

interface HttpClientFactory {

    /** Main instance for testing */
    static HttpClient getDefaultSecureClient() {
        return SecureClientInitializer.getDefaultSecureHttpClient().getSecureClient();
    }

}

