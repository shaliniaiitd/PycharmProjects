package com.epam.utility.gitclonefilecopy.structure.impl;

import com.epam.utility.gitclonefilecopy.structure.exceptions.InvalidBatchFileException;
import com.epam.utility.gitclonefilecopy.utils.FileUtilities;
import org.apache.log4j.Logger;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import java.io.*;

import static com.epam.utility.gitclonefilecopy.constant.Constants.*;

@Component
public class ProjectBuilder {

    private static final Logger logger = Logger.getLogger(ProjectBuilder.class);

    @Autowired
    FileUtilities fileUtilities;

    public void compileFramework(String filePath) {
        String fileName;
        logger.info("Framework compilation started!!");
        fileName = (System.getProperty("os.name").contains("Windows"))? "run.bat":"run.sh";
        createExecutableFile(filePath, fileName);
        updateRunnableFile(filePath, fileName);
        readCompiledOutput(runExecutableFile(filePath, fileName));
        deleteTargetFolderAndExecutableFile(filePath,fileName);
        logger.info("Framework compilation completed!!");
    }

    private void createExecutableFile(String filePath, String fileName) {
        File file = new File(filePath + File.separator + fileName);
        boolean newFile;
        try {
            newFile = file.createNewFile();
            checkFileExistence(newFile, fileName);
        } catch (IOException e) {
            throw new InvalidBatchFileException("No batch file created: " + e.getMessage());
        }
    }

    private void checkFileExistence(boolean newFile, String fileName) {
        if (!newFile) {
            logger.warn("Executable " + fileName + " file existed, no new file created!!");
        }
    }

    private void readCompiledOutput(Process process) {
        try {
            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            StringBuilder stringBuilder = new StringBuilder();
            String line;
            while ((line = reader.readLine()) != null) {
                stringBuilder.append(line).append(NEW_LINE);
            }
            logger.info(stringBuilder);
        } catch (IOException e) {
            logger.fatal("Not able to read batch file: " + e.getMessage());
        }
    }

    private Process runExecutableFile(String filePath, String fileName) {
        try {
            return (System.getProperty("os.name").contains("Windows"))? new ProcessBuilder(filePath + File.separator + fileName).start():
                    Runtime.getRuntime().exec("chmod u+x "+filePath + File.separator + fileName);
        } catch (Exception e) {
            throw new InvalidBatchFileException("Not able to run batch file: " + e.getMessage());
        }
    }

    private void updateRunnableFile(String filePath, String fileName) {
        try (FileWriter myWriter = new FileWriter(filePath + File.separator + fileName)) {
            myWriter.write(
                    COMMAND_CHANGE_DIRECTORY + filePath + NEW_LINE + COMMAND_MAVEN_BUILD);
        } catch (IOException e) {
            logger.fatal("Not able to write in batch file: " + e.getMessage());
        }
    }

    private void deleteTargetFolderAndExecutableFile(String filePath,String fileName){
        fileUtilities.deleteDirectory(filePath+File.separator+"target");
        fileUtilities.deleteFile(filePath+File.separator+fileName);
     }
}
