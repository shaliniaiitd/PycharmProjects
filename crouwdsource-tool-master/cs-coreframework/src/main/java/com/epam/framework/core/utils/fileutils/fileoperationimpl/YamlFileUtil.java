package com.epam.framework.core.utils.fileutils.fileoperationimpl;

import com.epam.framework.core.exceptions.TABaseException;
import com.epam.framework.core.utils.fileutils.fileoperations.FileUtil;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.dataformat.yaml.YAMLFactory;

import java.io.FileInputStream;
import java.io.IOException;
import java.util.Map;

public class YamlFileUtil extends FileUtil {

    public YamlFileUtil(String fileName) {
        super(fileName);
    }

    public void setFileName(String fileName) {
        this.fileName = fileName;
    }

    @Override
    public Map<String, String> loadContentsToMap() {

        Map<String, String> readValue;
        ObjectMapper mapper = new ObjectMapper(new YAMLFactory());
        try (FileInputStream input = new FileInputStream(getFullFilePath())) {
            readValue = mapper.readValue(input, Map.class);
        } catch (IOException e1) {
            throw new TABaseException();
        }
        return readValue;
    }

    @Override
    public Boolean checkIfNodeOrKeyExist(String key) {

        Map<String, String> readValue = null;
        ObjectMapper mapper = new ObjectMapper(new YAMLFactory());
        try (FileInputStream input = new FileInputStream(getFullFilePath())) {
            readValue = mapper.readValue(input, Map.class);
            if (readValue.containsKey(key)) {
                return Boolean.TRUE;
            }
        } catch (IOException e1) {
            throw new TABaseException();
        }
        return Boolean.FALSE;
    }
}