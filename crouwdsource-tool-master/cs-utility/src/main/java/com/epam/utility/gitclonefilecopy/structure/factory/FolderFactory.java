package com.epam.utility.gitclonefilecopy.structure.factory;

import com.epam.utility.gitclonefilecopy.structure.Folder;
import com.epam.utility.gitclonefilecopy.structure.exceptions.NoLanguageSelectedException;
import com.epam.utility.gitclonefilecopy.structure.impl.FolderOptimizer;
import com.epam.utility.gitclonefilecopy.structure.impl.ProjectBuilder;
import com.epam.utility.gitclonefilecopy.models.ToolConfigBean;
import com.epam.utility.gitclonefilecopy.utils.FileUtilities;
import org.apache.log4j.Logger;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import static com.epam.utility.gitclonefilecopy.constant.Constants.*;

@Component
public class FolderFactory {

    @Autowired
    private FileUtilities fileUtilities;

    @Autowired
    private DependencyFactory dependencyFactory;

    @Autowired
    private ProjectBuilder projectBuilder;

    @Autowired
    private FolderOptimizer folder;

    private static final Logger logger = Logger.getLogger(FolderFactory.class);

    public void moveRequiredFiles(ToolConfigBean toolConfig) {
        logger.info("Framework structure creation is in progress!!");
        String language = toolConfig.getLanguage().toLowerCase();
        validateIfUserSelectedAnyLanguage(language);
        fileUtilities.readFolderConfigFile(language);
        buildProject(folder, toolConfig);
        logger.info("Framework structure creation step completed!!");
    }

    private void buildProject(Folder folder, ToolConfigBean toolConfig) {
        if (toolConfig.getLanguage().equalsIgnoreCase(LANGUAGE_JAVA)) {
            buildJavaProject(folder, toolConfig);
        } else if (toolConfig.getLanguage().equalsIgnoreCase(LANGUAGE_PYTHON)) {
            buildPythonProject(folder, toolConfig);
        } else if (toolConfig.getLanguage().equalsIgnoreCase(LANGUAGE_DOTNET)) {
            logger.warn("No dotnet project available as of now!!");
        } else {
            logger.error("Please provide correct language!!");
        }
    }

    private void buildJavaProject(Folder folder, ToolConfigBean toolConfig) {
        dependencyFactory.createUpdatedPOMFile(toolConfig);
        folder.moveFilesAndDirectories(fileUtilities, toolConfig);
        String downloadFolderPath = fileUtilities.getDownloadFolderPath();
        projectBuilder.compileFramework(downloadFolderPath);
    }

    private void buildPythonProject(Folder folder, ToolConfigBean toolConfig) {
        folder.moveFilesAndDirectories(fileUtilities, toolConfig);
    }

    private void validateIfUserSelectedAnyLanguage(String language) {
        if (language.isEmpty()) {
            throw new NoLanguageSelectedException("Please provide Language type!!");
        }
    }

}
