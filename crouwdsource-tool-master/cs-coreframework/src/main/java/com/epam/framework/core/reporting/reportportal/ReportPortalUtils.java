package com.epam.framework.core.reporting.reportportal;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import rp.com.google.common.io.BaseEncoding;

import java.io.File;

public class ReportPortalUtils {

    private static final Logger LOGGER = LoggerFactory.getLogger("binary_data_logger");

    private ReportPortalUtils() {
    }

    public static void log(File file, String message) {
        LOGGER.info("RP_MESSAGE#FILE#{}#{}", file.getAbsolutePath(), message);
    }

    public static void log(byte[] bytes, String message) {
        String binaryDataLog = BaseEncoding.base64().encode(bytes);
        LOGGER.info("RP_MESSAGE#BASE64#{}#{}", binaryDataLog, message);
    }

    public static void logBase64(String base64, String message) {
        LOGGER.info("RP_MESSAGE#BASE64#{}#{}", base64, message);
    }
}
