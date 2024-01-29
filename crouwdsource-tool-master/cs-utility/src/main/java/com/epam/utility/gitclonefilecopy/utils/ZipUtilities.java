package com.epam.utility.gitclonefilecopy.utils;

import net.lingala.zip4j.ZipFile;
import net.lingala.zip4j.exception.ZipException;
import org.apache.log4j.Logger;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import java.io.File;

@Component
public class ZipUtilities {

    private static final Logger logger = Logger.getLogger(ZipUtilities.class);

    @Autowired
    private FileUtilities fileUtilities;

    public void createZipFile(String downloadFolderPath) {
        ZipFile zipFile = new ZipFile(new File(fileUtilities.getDownloadFileName()));
        try {
            logger.info("Started zipping the files");
            zipFile.addFolder(new File(downloadFolderPath));
        } catch (ZipException e) {
            logger.error("Unable to zip the files: {}", e);
        }
    }
}
