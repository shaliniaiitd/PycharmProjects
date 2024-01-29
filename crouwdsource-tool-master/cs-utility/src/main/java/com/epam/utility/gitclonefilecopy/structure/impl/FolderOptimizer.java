package com.epam.utility.gitclonefilecopy.structure.impl;

import com.epam.utility.gitclonefilecopy.structure.Folder;
import com.epam.utility.gitclonefilecopy.structure.exceptions.*;
import com.epam.utility.gitclonefilecopy.models.ToolConfigBean;
import com.epam.utility.gitclonefilecopy.utils.FileUtilities;
import com.google.gson.JsonObject;
import org.apache.commons.io.FileUtils;
import org.apache.log4j.Logger;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import java.io.File;
import java.io.IOException;
import java.util.function.Consumer;

import static com.epam.utility.gitclonefilecopy.constant.Constants.*;

@Component
public class FolderOptimizer implements Folder {

    private static final Logger logger = Logger.getLogger(FolderOptimizer.class);

    private String sourcePath;
    private String downloadFolderPath;

    @Autowired
    private FileUtilities fileUtilities;

    @Override
    public void moveFilesAndDirectories(FileUtilities fileUtilities, ToolConfigBean toolConfig) {
        logger.info("File and Directories copy started!!");
        sourcePath = fileUtilities.getSourcePath();
        downloadFolderPath = fileUtilities.getDownloadFolderPath() + File.separator;
        movePOMFile(toolConfig);
        moveFilesForPlatform(toolConfig);
        moveFilesForEngine(toolConfig);
        moveFilesForTestModel(toolConfig);
        moveFilesForLoggers(toolConfig);
        moveFilesForReporters(toolConfig);
        //moveFilesForDb(toolConfig);
        logger.info("File and Directories copy completed!!");
    }

	private void moveFilesForDb(ToolConfigBean toolConfig) {
		if (!toolConfig.getDb().isEmpty()) {
			moveDbRelatedDefaultFiles(TAG_DB_UTILITY);
		}
	}

	private void moveDbRelatedDefaultFiles(String db) {
		if (validate.test(db, TAG_DB_UTILITY)) {
			moveFileAndFolderFromList(
					((JsonObject) fileUtilities.getLanguageObject().get(TAG_DB)).get(TAG_DB_UTILITY).getAsString());
		}
	}

	private void movePOMFile(ToolConfigBean toolConfig) {
        if (toolConfig.getLanguage().equalsIgnoreCase(LANGUAGE_JAVA)){
            moveFileAndFolderFromList(NEW_FOLDER_WITH_POM_FILE);
        }
    }

    private void moveFilesForPlatform(ToolConfigBean toolConfig) {
        validateIfUserSelectedAnyPlatform(toolConfig);
        String[] platformList = toolConfig.getPlatform().split(COMMA_SEPARATOR);
        moveFileAndFolderFromList(fileUtilities.getLanguageObject().get(TAG_DEFAULT_FOLDER).getAsString());
        for (String platform : platformList) {
            moveUIRelatedDefaultFiles(platform);
            moveAPIRelatedDefaultFiles(platform);
            moveMobileRelatedDefaultFiles(platform);
        }
    }

    private void moveFilesForEngine(ToolConfigBean toolConfig) {
        validateIfUserSelectedAnyEngine(toolConfig);
        String[] engineList = toolConfig.getEngine().split(COMMA_SEPARATOR);
        for (String engine : engineList) {
            moveSeleniumRelatedDefaultFiles(engine);
            moveAppiumRelatedDefaultFiles(engine);
            moveHTTPClientRelatedDefaultFiles(engine);
        }
    }

    private void moveFilesForTestModel(ToolConfigBean toolConfig) {
        validateIfUserSelectedAnyTestModel(toolConfig);
        String[] testModelList = toolConfig.getTestModel().split(COMMA_SEPARATOR);
        for (String testModel : testModelList) {
            moveTestNGRelatedDefaultFiles(testModel);
            moveCucumberRelatedDefaultFiles(testModel);
        }
    }

    private void moveFilesForLoggers(ToolConfigBean toolConfig) {
        validateIfUserSelectedAnyLogger(toolConfig);
        moveFileAndFolderFromList(fileUtilities.getLanguageObject().get(TAG_LOGGING).getAsString());
    }

    private void moveFilesForReporters(ToolConfigBean toolConfig) {
        validateIfUserSelectedAnyReporter(toolConfig);
        moveFileAndFolderFromList(fileUtilities.getLanguageObject().get(TAG_REPORTING).getAsString());
    }

    private void moveMobileRelatedDefaultFiles(String platform) {
        if (validate.test(platform, PLATFORM_MOBILE)) {
            moveFileAndFolderFromList(((JsonObject) fileUtilities.getLanguageObject().get(TAG_MOBILE))
                    .get(TAG_MOBILE_DEFAULT_FOLDER).getAsString());
        }
    }

    private void moveAPIRelatedDefaultFiles(String platform) {
        if (validate.test(platform, PLATFORM_API)) {
            moveFileAndFolderFromList(((JsonObject) fileUtilities.getLanguageObject().get(TAG_API))
                    .get(TAG_API_DEFAULT_FOLDER).getAsString());
        }
    }

    private void moveUIRelatedDefaultFiles(String platform) {
        if (validate.test(platform, PLATFORM_UI)) {
            moveFileAndFolderFromList(((JsonObject) fileUtilities.getLanguageObject().get(TAG_UI))
                    .get(TAG_UI_DEFAULT_FOLDER).getAsString());
        }
    }

    private void moveHTTPClientRelatedDefaultFiles(String engine) {
        if (validate.test(engine, ENGINE_HTTPCLIENT)) {
            moveFileAndFolderFromList(((JsonObject) fileUtilities.getLanguageObject().get(TAG_API))
                    .get(TAG_HTTPCLIENT).getAsString());
        }
    }

    private void moveAppiumRelatedDefaultFiles(String engine) {
        if (validate.test(engine, ENGINE_APPIUM)) {
            moveFileAndFolderFromList(((JsonObject) fileUtilities.getLanguageObject().get(TAG_MOBILE))
                    .get(TAG_APPIUM).getAsString());
        }
    }

    private void moveSeleniumRelatedDefaultFiles(String engine) {
        if (validate.test(engine, ENGINE_SELENIUM)) {
            moveFileAndFolderFromList(((JsonObject) fileUtilities.getLanguageObject().get(TAG_UI))
                    .get(TAG_SELENIUM).getAsString());
        }
    }

    private void moveCucumberRelatedDefaultFiles(String testModel) {
        if (validate.test(testModel, TESTMODEL_CUCUMBER)) {
            moveFileAndFolderFromList(
                    ((JsonObject) fileUtilities.getLanguageObject().get(TAG_TEST_MODEL))
                            .get(TAG_CUCUMBER).getAsString());
        }
    }

    private void moveTestNGRelatedDefaultFiles(String testModel) {
        if (validate.test(testModel, TESTMODEL_TESTNG)) {
            moveFileAndFolderFromList(
                    ((JsonObject) fileUtilities.getLanguageObject().get(TAG_TEST_MODEL))
                            .get(TAG_TESTNG).getAsString());
        }
    }

    private void validateIfUserSelectedAnyPlatform(ToolConfigBean toolConfig) {
        if (toolConfig.getPlatform().isEmpty() || toolConfig.getPlatform() == null) {
            throw new NoPlatformSelectedException("Please provide Platform type!!");
        }
    }

    private void validateIfUserSelectedAnyEngine(ToolConfigBean toolConfig) {
        if (toolConfig.getEngine().isEmpty() || toolConfig.getEngine() == null) {
            throw new NoEngineSelectedException("Please provide Engine type!!");
        }
    }

    private void validateIfUserSelectedAnyTestModel(ToolConfigBean toolConfig) {
        if (toolConfig.getTestModel().isEmpty() || toolConfig.getTestModel() == null) {
            throw new NoTestModelSelectedException("Please provide Test Model type!!");
        }
    }

    private void validateIfUserSelectedAnyLogger(ToolConfigBean toolConfig) {
        if (toolConfig.getLogger().isEmpty() || toolConfig.getLogger() == null) {
            throw new NoLoggerSelectedException("Please provide Logger type!!");
        }
    }

    private void validateIfUserSelectedAnyReporter(ToolConfigBean toolConfig) {
        if (toolConfig.getReporter().isEmpty() || toolConfig.getReporter() == null) {
            throw new NoReporterSelectedException("Please provide Reporter type!!");
        }
    }

    private void moveFileAndFolderFromList(String filesPath) {
        String[] filePathList = filesPath.split(COMMA_SEPARATOR);
        for (String path : filePathList) {
            copy.accept(path);
        }
    }

    private final Consumer<String> copy = relativePath -> {
        if (!relativePath.isEmpty()) {
            if (relativePath.contains(DOT_SIGN)) {
                copyFile(relativePath);
            } else {
                copyFolder(relativePath);
            }
        }
    };

    private void copyFile(String relativePath) {
        try {
            File source = new File(sourcePath + relativePath);
            File destination = new File(downloadFolderPath + relativePath);
            File pomDestination = new File(downloadFolderPath + File.separator + POM_FILE);

            logger.info("File copy started from " + sourcePath + relativePath);
            if (relativePath.endsWith(POM_FILE)) {
                FileUtils.copyFile(source, pomDestination);
            } else {
                FileUtils.copyFile(source, destination);
            }
            logger.info("File copy finished in " + downloadFolderPath);

        } catch (IOException e) {
            logger.fatal("Error on performing file copy operation - " + e.getMessage());
        }
    }

    private void copyFolder(String path) {
        try {
            File source = new File(sourcePath + path);
            File destination = new File(downloadFolderPath + path);

            logger.info("Directory copy started from " + sourcePath + path);
            FileUtils.copyDirectory(source, destination);
            logger.info("Directory copy finished in " + downloadFolderPath + path);

        } catch (IOException e) {
            logger.fatal("Error on performing folder copy operation - " + e.getMessage());
        }
    }
}
