package com.epam.framework.api.restassured;

import com.epam.framework.core.TestContext;
import com.epam.framework.core.logging.logger.LogLevel;
import org.apache.http.HttpException;
import java.net.URISyntaxException;

public class ResponseValidator {
    RestAPIRequest restAPIRequest ;
    RestApIResponse restApIResponse ;

    public static boolean validateBaseURI(String baseUri) throws HttpException, URISyntaxException {
        String url =RestAPIRequest.getQueryableRequestSpecification().getBaseUri();
        if(url.equals(baseUri))
            return true;
        else
        {
            TestContext.getLogger().log(LogLevel.ERROR,"Expected :"+url+ "  found :"+ baseUri);
            return false;
        }
    }


    public static boolean validateProtocolVersion(String protocol) {
        String responseProtocol =RestApIResponse.getResponse().getStatusLine().substring(0,8);
        if(responseProtocol.equals(protocol))
            return true;
        else
        {
            TestContext.getLogger().log(LogLevel.ERROR,"Expected :"+protocol+ "  found :"+ responseProtocol);
            return false;
        }
    }

    public static boolean validateStatusLine(String responseLine) {
        String responseProtocol =RestApIResponse.getResponse().getStatusLine();
        if(responseProtocol.equals(responseLine))
            return true;
        else
        {
            TestContext.getLogger().log(LogLevel.ERROR,"Expected :"+responseLine+ "  found :"+ responseProtocol);
            return false;
        }
    }

    public static boolean validateReasonPhrase(String ok) {
        String responseProtocol =RestApIResponse.getResponse().getStatusLine().substring(13,15);
        if(responseProtocol.equals(ok))
            return true;
        else
        {
            TestContext.getLogger().log(LogLevel.ERROR,"Expected :"+ok+ "  found :"+ responseProtocol);
            return false;
        }
    }
}
