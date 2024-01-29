package com.epam.framework.core.utils.fileutils.fileoperationimpl;

import com.epam.framework.core.exceptions.TABaseException;
import com.epam.framework.core.utils.fileutils.fileoperations.FileUtil;

import java.io.FileInputStream;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.Properties;

public class PropertyFileUtil extends FileUtil {

    public PropertyFileUtil(String fileName) {
        super(fileName);
    }

    public void setFileName(String fileName) {
        this.fileName = fileName;
    }

    public Map<String, String> loadContentsToMap() {
        try (FileInputStream input = new FileInputStream(getFullFilePath())) {

            Properties p = new Properties();
            p.load(input);
            Map<String, String> m = new HashMap<>();
            p.forEach((key, value) -> m.put((String) key, (String) value));
            return m;
        } catch (IOException e) {
            throw new TABaseException(e.getMessage(), e.getCause());
        }
    }

    @Override
    public Boolean checkIfNodeOrKeyExist(String key) {
        try (FileInputStream input = new FileInputStream(getFullFilePath())) {
            Properties p = new Properties();
            p.load(input);
            if ((p.get(key) != null) || (p.getProperty(key) != null)) {
                return Boolean.TRUE;
            }

        } catch (IOException e) {
            throw new TABaseException("Specified key doesnt exist", e.getCause());
        }
        return Boolean.FALSE;
    }

}
