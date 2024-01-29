package com.epam.utility.gitclonefilecopy.utils;

import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import org.apache.commons.io.FileUtils;
import org.apache.log4j.Logger;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.UUID;

@Component
public class FileUtilities {

    private static final Logger logger = Logger.getLogger(FileUtilities.class);

    private String sourcePath = null;
    private JsonObject languageObject;

    @Value("${collab.download.file.name}")
    private String downloadFileName;

    public void readFolderConfigFile(String language) {
        JsonParser jsonParser;
        Object parserObject;
        JsonObject folderConfigObject;
        try (FileReader jsonReader = new FileReader(getFolderConfigFilePath())) {
            logger.info("Started reading folder configuration json file!!");
            jsonParser = new JsonParser();
            parserObject = jsonParser.parse(jsonReader);
            folderConfigObject = (JsonObject) parserObject;
            languageObject = (JsonObject) folderConfigObject.get(language);
            logger.info("Folder configuration read successfully!!");
        } catch (Exception e) {
            logger.fatal("Error while reading Folder Setup configuration file: " + e.getMessage());
        }
    }

    public JsonObject getLanguageObject() {
        return languageObject;
    }

    public void copyRequiredFiles(String sourcePath, String projectDirectoryPath) {
        try {
            logger.info("Copying required files");
            org.apache.commons.io.FileUtils.copyDirectory(new File(sourcePath), new File(projectDirectoryPath));
            logger.info("Finished copying files");
        } catch (IOException e) {
            logger.error(e.getMessage());
        }
    }

    public void deleteDirectory(String directoryPath) {
        try {
            Path path = Paths.get(directoryPath);
            logger.info("Checking if directory exists : " + directoryPath);
            if (Files.exists(path)) {
                logger.info("Directory exists. Cleaning : " + directoryPath);
                FileUtils.cleanDirectory(new File(directoryPath));
                logger.info("Successfully cleaned directory : " + directoryPath);
                logger.info("Deleting : " + directoryPath);
                FileUtils.deleteDirectory(new File(directoryPath));
                logger.info("Successfully deleted directory : " + directoryPath);
            }
        } catch (IOException e) {
            logger.error(e.getMessage());
        }
    }

    public void deleteFile(String filePath) {
        try {
            Path path = Paths.get(filePath);
            logger.info("Checking if file exists : " + filePath);
            if (Files.exists(path)) {
                logger.info("File exists. Deleting : " + filePath);
                Files.delete(path);
                logger.info("Successfully deleted file : " + filePath);
            }
        } catch (IOException e) {
            logger.error(e.getMessage());
        }
    }

    public void setupDirectories(String directoryPath) {
        try {
            Path path = Paths.get(directoryPath);
            logger.info("Checking if directory exists : " + directoryPath);
            if (Files.exists(path)) {
                logger.info("Directory exists. Cleaning : " + directoryPath);
                FileUtils.cleanDirectory(new File(directoryPath));
                logger.info("Successfully cleaned directory : " + directoryPath);
            } else {
                logger.info("Directory does not exists. Creating : " + directoryPath);
                Files.createDirectory(path);
                logger.info("Successfully created directory : " + directoryPath);
            }
        } catch (IOException e) {
            logger.error(e.getMessage());
        }
    }

    public void updateSourcePathBasedOnLanguage(String language) {
        String tempDirectoryPath = this.getTempDirectoryPath();
        if (language.equalsIgnoreCase("Java")) {
            sourcePath = tempDirectoryPath + File.separator + "cs-coreframework" + File.separator;
        } else {
            sourcePath = tempDirectoryPath + File.separator + "cs-coreframework-python" + File.separator;
        }
    }

    public String getSourcePath() {
        return this.sourcePath;
    }

    public String getDownloadFolderPath() {
        Path path = Paths.get("src", "main", "resources", "download");
        return path.toString();
    }

    public String getFolderConfigFilePath() {
        Path path = getResourcePath();
        return path.toString() + File.separator + "FolderConfig.json";
    }

    public String getDependencyConfigFilePath() {
        Path path = getResourcePath();
        return path.toString() + File.separator + "DependencyConfig.json";
    }

    private Path getResourcePath() {
        return Paths.get("src", "main", "resources");
    }


    public String getTempDirectoryPath() {
        return this.getDownloadFolderPath() + File.separator + "temp";
    }

    public File getRandomFileName() {
        return new File("download-" + UUID.randomUUID() + ".zip");
    }

    public String getDownloadFileName() {
        return Paths.get(downloadFileName).toFile().getName();
    }

    public void removeDirectories() {
        this.deleteDirectory(this.getDownloadFolderPath());
    }

    public void removeTempDirectory() {
        this.deleteDirectory(this.getTempDirectoryPath());
    }

}
