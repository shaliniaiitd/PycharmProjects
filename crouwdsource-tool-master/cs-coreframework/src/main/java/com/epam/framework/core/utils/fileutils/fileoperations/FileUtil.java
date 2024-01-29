package com.epam.framework.core.utils.fileutils.fileoperations;

import com.epam.framework.core.exceptions.TABaseException;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Map;

public abstract class FileUtil {

    protected String fileName = null;

    protected FileUtil(String fileName) {
        this.setFileName(fileName);
    }

    public abstract <T> Map<T, T> loadContentsToMap();

    public abstract Boolean checkIfNodeOrKeyExist(String key);

    public abstract void setFileName(String fileName);

    public String readFileToString() {
        try {
            return new String(Files.readAllBytes(Paths.get(getFullFilePath())));
        } catch (IOException e) {
            throw new TABaseException(e.getMessage(), e.getCause());
        }
    }

    protected String getFullFilePath() {
        return getUserDiretory() + "\\" + fileName;
    }

    protected String getUserDiretory() {
        return System.getProperty("user.dir");
    }


}

