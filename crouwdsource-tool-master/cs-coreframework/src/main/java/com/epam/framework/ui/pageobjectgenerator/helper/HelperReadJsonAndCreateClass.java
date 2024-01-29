package com.epam.framework.ui.pageobjectgenerator.helper;

import com.epam.framework.core.utils.PropertyReader;
import com.epam.framework.ui.pageobjectgenerator.constant.PageObjectOperationConstants;
import com.epam.framework.ui.pageobjectgenerator.pageObjectWriter.PageObjectWriterJava;
import com.epam.framework.ui.pageobjectgenerator.exceptions.InvalidOperationException;
import com.epam.framework.ui.pageobjectgenerator.pageObjectTemplate.PageObjectsTemplate;
import com.epam.framework.ui.pageobjectgenerator.pageObjectTemplate.PageObjectsTemplateJava;
import com.epam.framework.ui.pageobjectgenerator.pageObjectWriter.PageObjectWriter;
import com.epam.framework.ui.pageobjectgenerator.pojo.PageObject;
import com.epam.framework.ui.pageobjectgenerator.pojo.Records;
import com.epam.framework.ui.pageobjectgenerator.verificationTemplate.PageVerificationTemplate;
import com.epam.framework.ui.pageobjectgenerator.verificationTemplate.PageVerificationTemplateJava;
import com.google.gson.Gson;
import fun.mike.dmp.Diff;
import fun.mike.dmp.DiffMatchPatch;
import fun.mike.dmp.Operation;
import org.apache.commons.io.FileUtils;
import org.apache.log4j.Logger;

import java.io.*;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.*;

/**
 * The helper class reads data from input file here it is JSON. JSON file is converted to POJO to be used.
 * Reading the Json array objects one by one, the class creates pageObjects based on PageObjectsTemplate class.
 *
 */

public class HelperReadJsonAndCreateClass {

    private static final String FILE_SEPARATOR = System.getProperty("file.separator");
    private static final String RECORDS_JSON_FILE = FILE_SEPARATOR+"Records.json";
    private static final String FILE_EXTENSION = ".java";
    private static final String ACTIONS_PATH = "actionsPath";
    private static final String BASE_DIR_PATH = "baseDir";
    private static final String PAGE_OBJECTS_PATH = "pageObjectsPath";

    // Templates
    private PageObjectsTemplate pageObjectsTemplate;
    private PageVerificationTemplate pageVerificationTemplate;
    private static final String POM_CONFIG_FILE_PATH = "src"+FILE_SEPARATOR
            +"main"+FILE_SEPARATOR
            +"resources"+FILE_SEPARATOR
            +"POMconfig.properties";
    private static final PropertyReader prop = new PropertyReader(POM_CONFIG_FILE_PATH);

    // Configurations
    private String filePath;
    private String pageObjectRecordPath;
    private String verificationPath;
    private String packageName;
    private String actionsPath;

    // PageObject Container
    private Set<String> pageObjectSet;
    private HashMap<String, PageObject> pageObjectMap;

    // Logger
    private static final Logger logger = Logger.getLogger(HelperReadJsonAndCreateClass.class);

    public void readJSON() {
        String languageType;
        String pageObjectsPath;

        logger.info("Configuration Properties File Found.");
        String projectDirectory = System.getProperty("user.dir");
        filePath = projectDirectory + prop.getProperty("inputFilePath");
        pageObjectRecordPath = projectDirectory + prop.getProperty("objectRecordPath");
        pageObjectsPath = projectDirectory + prop.getProperty(PAGE_OBJECTS_PATH);
        verificationPath = pageObjectsPath + prop.getProperty("verificationPath");
        packageName = prop.getProperty("packageName");
        actionsPath = pageObjectsPath + prop.getProperty(ACTIONS_PATH);
        try {
            pageObjectsTemplate = new PageObjectsTemplateJava();
            pageVerificationTemplate = new PageVerificationTemplateJava();
            logger.info("Initialized Java Templates");
            readAndRetrievePageObject();
        }
        catch (Exception e) {
            logger.error(e.getStackTrace());
        }
    }

    private void readAndRetrievePageObject(){
        retrievePageObjectRecords();
        readPageObjectsFromJson();
    }

    private void retrievePageObjectRecords() {
        try {
            Path path = Paths.get(pageObjectRecordPath);
            if (!Files.exists(path))
                Files.createDirectories(path);
                File recordFile = new File(pageObjectRecordPath+ RECORDS_JSON_FILE);
            if (recordFile.exists()) {
                try (FileReader jsonReader = new FileReader(recordFile)) {
                    Records pageObjectRecords = parseJsonToObject(jsonReader, Records.class);
                    pageObjectSet = new HashSet<>(Arrays.asList(pageObjectRecords.getPageObjectNames()));
                }
            } else {
                boolean result = recordFile.createNewFile();
                if ((result)) {
                    logger.info("Successfully Created New Record File");
                    pageObjectSet = new HashSet<>();
                }
                else retrievePageObjectRecords();
            }
        } catch (IOException e) {
            logger.error(e.getStackTrace());
        }
    }

    private void readPageObjectsFromJson() {
        pageObjectMap = new HashMap<>();
        if (Files.exists(Paths.get(filePath))) {
            File[] files = new File(filePath).listFiles();
            if (files != null && files.length > 0) {
                Arrays.stream(files).forEach(file -> {
                    try (FileReader jsonReader = new FileReader(file)) {
                        logger.info("Started Reading PageObjects From " + file.getName());
                        PageObject[] pageObjectList = parseJsonToObject(jsonReader,PageObject[].class);
                        setPageObject(pageObjectList);
                        logger.info("Finished Reading PageObjects From " + file.getName());
                    } catch (IOException e) {
                        logger.error(e.getStackTrace());
                    }
                });
            } else {
                logger.error("No JSON File Found At Given Location");
            }
        } else {
            logger.error("File Path To JSON Files Is Invalid");
        }
    }

    private <T> T parseJsonToObject(FileReader jsonReader, Class<T> classObject){
        Gson gson = new Gson();
        return gson.fromJson(jsonReader, classObject);
    }

    private void setPageObject(PageObject[] pageObjects){
        Arrays.stream(pageObjects).forEach(pageObject -> {
            String currentPageObjectOperation = pageObject.getOperation();
            operateOnPageObject(currentPageObjectOperation, pageObject);
        });
    }

    private void operateOnPageObject(String currentPageObjectOperation, PageObject pageObject) {
        try{
            if(pageObjectSet.contains(pageObject.getPageName())){
                validateOperationIfPageExists(currentPageObjectOperation, pageObject);
            } else {
                setAndCreatePageObjectMap(pageObject);
            }
        } catch (Exception e) {
            logger.error(e.getStackTrace());
        }
    }

    private void validateOperationIfPageExists(String currentPageObjectOperation, PageObject pageObject){
        try{
            if(currentPageObjectOperation.equalsIgnoreCase(PageObjectOperationConstants.OPERATION_CREATE)){
                logger.error("PageObject "+pageObject.getPageName()+" already exists!");
            } else if(currentPageObjectOperation.equalsIgnoreCase(PageObjectOperationConstants.OPERATION_MODIFY)){
                modifyPageObject(pageObject);
            } else {
                throw new InvalidOperationException(
                        "Operation "+currentPageObjectOperation+" Not Supported!");
            }
        } catch (InvalidOperationException e){
            logger.error(e.getStackTrace());
        }
    }

    private void modifyPageObject(PageObject pageObject) {
        try{
            if (pageObjectMap.containsKey(pageObject.getPageName())) {
                logger.error("Duplicate Entry For PageObject Class "+pageObject.getPageName());
            } else {
                regeneratePageObject(pageObject);
            }
        } catch (Exception e){
            logger.error(e.getStackTrace());
        }
    }

    private void regeneratePageObject(PageObject pageObject){
        try{
            pageObjectMap.put(pageObject.getPageName(), pageObject);
            String pageOldContent = readPageFile(pageObject.getPageName());
            refreshDirectory(pageObject.getPageName());
            writeToPageClass(pageObject);
            String pageNewContent = readPageFile(pageObject.getPageName());
            writeToNewFile(appendDifference(deriveDifferenceBetweenStrings(pageOldContent, pageNewContent), pageNewContent),
                    prop.getProperty(BASE_DIR_PATH)+prop.getProperty(PAGE_OBJECTS_PATH) +
                            prop.getProperty(ACTIONS_PATH),pageObject.getPageName());
        } catch (IOException e){
            logger.error(e.getStackTrace());
        }
    }

    private static String readPageFile(String pageName) throws IOException {
        StringBuilder resultString = new StringBuilder();
        List<String> allLines = Files.readAllLines(Paths.get(prop.getProperty(BASE_DIR_PATH) +
                prop.getProperty(PAGE_OBJECTS_PATH) + prop.getProperty(ACTIONS_PATH) + "\\" +
                pageName + FILE_EXTENSION));
        for (String line : allLines) {
            resultString.append(line).append("\n");
        }
        return resultString.toString();
    }

    private String deriveDifferenceBetweenStrings(String str1, String str2){
        DiffMatchPatch dmp = new DiffMatchPatch();
        LinkedList<Diff> diffs = dmp.diff_main(str2, str1);
        StringBuilder difference = new StringBuilder();
        for(Diff d : diffs){
            if(d.operation.equals(Operation.INSERT) && (d.text.contains("public")
                    || d.text.contains("private")) || d.text.contains("protected")){
                difference.append(d.text);
            }
        }
        return difference.toString();
    }

    private String appendDifference(String diffStr, String finalString){
        StringBuilder stringBuilder = new StringBuilder(finalString);
        for(int i = finalString.length()-1; i >= 0; i--){
            if(finalString.charAt(i) == '}'){
                stringBuilder.deleteCharAt(i);
                break;
            }
        }
        stringBuilder.insert(finalString.length()-1, diffStr);
        return stringBuilder.toString();
    }

    private void writeToNewFile(String content, String path, String fileName) throws IOException {
        try(BufferedWriter writer = new BufferedWriter(new FileWriter(path + "\\" +
                fileName + FILE_EXTENSION))){
            StringBuilder sb = new StringBuilder(content);
            writer.write(sb.append("\n}\n").toString());
        } catch(IOException e){
            logger.error(e.getStackTrace());
        }
    }

    private void refreshDirectory(String fileName) {
        try{
            FileUtils.deleteDirectory(new File(prop.getProperty(BASE_DIR_PATH) +
                    prop.getProperty(PAGE_OBJECTS_PATH) + fileName + FILE_EXTENSION));
        } catch(IOException e){
            logger.error(e.getStackTrace());
        }
    }

    private void writeToPageClass(PageObject pageObject){
        PageObjectWriter pageObjectWriter;
        logger.info("Initializing Writer For Java");
        pageObjectWriter = new PageObjectWriterJava(pageObject, pageObjectsTemplate, pageVerificationTemplate);
        pageObjectWriter.writeClass(actionsPath, packageName);
        pageObjectWriter.writeVerifications(verificationPath, packageName);
    }

    private void setAndCreatePageObjectMap(PageObject pageObject) {
        try{
            if (pageObjectMap.containsKey(pageObject.getPageName())) {
                logger.error("Duplicate Entry For PageObject Class " + pageObject.getPageName());
            } else {
                pageObjectMap.put(pageObject.getPageName(), pageObject);
                pageObjectSet.add(pageObject.getPageName());
                createPageObjectClass();
                addNewPageObjectRecords();
            }
        } catch(Exception e){
            logger.error(e.getStackTrace());
        }
    }

    private void createPageObjectClass() {
        pageObjectMap.entrySet().parallelStream().forEach(entry ->
        {
            logger.info("Started Writing PageObject Class : "+entry.getKey());
            writeToPageClass(entry.getValue());
            logger.info("Finished Writing PageObject Class : "+entry.getKey());
        });
    }

    private void addNewPageObjectRecords() {
        pageObjectMap.forEach(
                (pageObjectName, pageObject) -> pageObjectSet.add(pageObjectName)
        );
        String[] newRecord = new String[pageObjectSet.size()];
        pageObjectSet.toArray(newRecord);
        Records records = new Records(newRecord);
        try (FileWriter recordWriter = new FileWriter(pageObjectRecordPath + RECORDS_JSON_FILE)) {
            Gson gson = new Gson();
            gson.toJson(records, recordWriter);
        } catch (IOException e) {
            logger.error(e.getStackTrace());
        }
    }

    public void cleanRecordDirectory(){
        try {
            FileUtils.deleteDirectory(new File(System.getProperty("user.dir")+File.separator+prop.getProperty("objectRecordPath")));
            logger.info("Successfully deleted the Records file");
        } catch (IOException e) {
            logger.error(e.getStackTrace());
        }
    }

}
