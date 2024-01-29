package com.epam.utility.gitclonefilecopy.structure.factory;

import com.epam.utility.gitclonefilecopy.structure.DependencyManager;
import com.epam.utility.gitclonefilecopy.structure.exceptions.NoObjectException;
import com.epam.utility.gitclonefilecopy.structure.impl.DependencyOptimizer;
import com.epam.utility.gitclonefilecopy.utils.DependencyUtilities;
import com.epam.utility.gitclonefilecopy.models.ToolConfigBean;
import com.epam.utility.gitclonefilecopy.utils.FileUtilities;
import org.apache.log4j.Logger;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import org.w3c.dom.Document;

import javax.xml.XMLConstants;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Optional;

import static com.epam.utility.gitclonefilecopy.constant.Constants.*;

@Component
public class DependencyFactory {

    private static final Logger logger = Logger.getLogger(DependencyFactory.class);

    @Autowired
    private DependencyOptimizer dependencyOptimizer;

    @Autowired
    private FileUtilities fileUtilities;

    @Autowired
    private DependencyUtilities dependencyUtilities;

    public void createUpdatedPOMFile(ToolConfigBean toolConfigBean) {
        ArrayList<Integer> dependencySequenceList;
        Document document;
        logger.info("POM file update is in progress!!");
        document = getDocumentObject();
        validateDependencyManagerOnNull(dependencyOptimizer);
        dependencySequenceList = getDependencySequence(toolConfigBean, document);
        dependencyOptimizer.removeFutileDependencies(document, dependencySequenceList);
        createNewPomFile(document, dependencyOptimizer);
        logger.info("POM file update step completed!!");
    }

    private Document getDocumentObject() {
        Document document = null;
        DocumentBuilderFactory factory;
        DocumentBuilder builder;
        File existingPOMFile;
        try {
            factory = DocumentBuilderFactory.newInstance();
            factory.setAttribute(XMLConstants.ACCESS_EXTERNAL_DTD, "");
            factory.setAttribute(XMLConstants.ACCESS_EXTERNAL_SCHEMA, "");
            builder = factory.newDocumentBuilder();
            existingPOMFile = new File(fileUtilities.getSourcePath() + POM_FILE);
            document = builder.parse(existingPOMFile);
            document.getDocumentElement().normalize();
        } catch (Exception exception) {
            logger.fatal(exception.getMessage());
        }
        validateDocumentOnNull(document);
        return document;
    }

    private ArrayList<Integer> getDependencySequence(ToolConfigBean toolConfigBean, Document document) {
        dependencyUtilities.readDependencyConfigFile(toolConfigBean.getLanguage());
        ArrayList<Integer> dependencyTagSequenceForRemoval = new ArrayList<>();
        dependencyTagSequenceForRemoval.addAll(dependencyOptimizer.fetchDeletedPlatformChildDependencySequence(toolConfigBean, document));
        dependencyTagSequenceForRemoval.addAll(dependencyOptimizer.fetchDeletedTestModelChildDependencySequence(toolConfigBean, document));
        dependencyTagSequenceForRemoval.addAll(dependencyOptimizer.fetchDeletedEngineChildDependencySequence(toolConfigBean, document));
        //dependencyTagSequenceForRemoval.addAll(dependencyOptimizer.fetchDeletedDbChildDependencySequence(toolConfigBean, document));

        return dependencyTagSequenceForRemoval;
    }

    private void createNewPomFile(Document document, DependencyManager manager) {
        String tempPOMFilePath = fileUtilities.getSourcePath() + TEMP_FOLDER_FOR_POM;
        String newPOMFilePath = fileUtilities.getSourcePath() + NEW_FOLDER_WITH_POM_FILE;
        createTempPOMDirectory(tempPOMFilePath);
        manager.createPomFile(document, newPOMFilePath);
    }

    private void createTempPOMDirectory(String folderPath) {
        try {
            Path path = Paths.get(folderPath);
            logger.info("Creating directory path: " + folderPath);
            createFileNotExist(path);
            logger.info("Successfully created directory path: " + folderPath);
        } catch (IOException e) {
            logger.error(e.getMessage());
        }
    }

    private void createFileNotExist(Path path) throws IOException {
        if (!Files.exists(path)) {
            Files.createDirectory(path);
        } else {
            logger.warn("No new POM file created, File already exist!!");
        }
    }

    private void validateDependencyManagerOnNull(DependencyManager dependencyUpdate) {
        if (!Optional.ofNullable(dependencyUpdate).isPresent()) {
            throw new NoObjectException("No Dependency Manager object created!!");
        }
    }

    private void validateDocumentOnNull(Document document) {
        if (!Optional.ofNullable(document).isPresent()) {
            throw new NoObjectException("No Document object created!!");
        }
    }
}
