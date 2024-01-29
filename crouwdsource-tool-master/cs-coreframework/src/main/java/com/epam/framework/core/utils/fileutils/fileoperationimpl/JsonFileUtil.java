package com.epam.framework.core.utils.fileutils.fileoperationimpl;

import com.epam.framework.core.exceptions.TABaseException;
import com.epam.framework.core.utils.fileutils.fileoperations.FileUtil;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.Map;

public class JsonFileUtil extends FileUtil {

    public JsonFileUtil(String fileName) {
        super(fileName);
    }

    public void setFileName(String fileName) {
        this.fileName = fileName;
    }

    @Override
    public Map<String, String> loadContentsToMap() {
        Map<String, String> map;
        ObjectMapper mapper = new ObjectMapper();
        Object obj;
        JSONParser parser = new JSONParser();
        try {
            obj = parser.parse(new FileReader(getFullFilePath()));
            map = mapper.readValue(obj.toString(), Map.class);
        } catch (IOException | ParseException e) {
            throw new TABaseException(e.getMessage(), e.getCause());
        }
        return map;
    }

    @Override
    public Boolean checkIfNodeOrKeyExist(String key) {
        ObjectMapper mapper = new ObjectMapper();
        JsonNode rootNode;
        try {
            rootNode = mapper.readTree(new File(getFullFilePath()));

            if (!rootNode.findPath(key).isMissingNode()) {
                return Boolean.TRUE;
            }
        } catch (IOException e) {
            throw new TABaseException(e.getMessage(), e.getCause());
        }
        return Boolean.FALSE;
    }
}