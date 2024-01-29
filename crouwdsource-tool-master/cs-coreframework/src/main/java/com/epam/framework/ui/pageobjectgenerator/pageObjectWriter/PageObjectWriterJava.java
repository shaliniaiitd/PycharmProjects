package com.epam.framework.ui.pageobjectgenerator.pageObjectWriter;

import com.epam.framework.ui.pageobjectgenerator.exceptions.ActionMethodCreationException;
import com.epam.framework.ui.pageobjectgenerator.exceptions.VerificationMethodCreationException;
import com.epam.framework.ui.pageobjectgenerator.pageObjectTemplate.PageObjectsTemplate;
import com.epam.framework.ui.pageobjectgenerator.pojo.Locators;
import com.epam.framework.ui.pageobjectgenerator.pojo.PageObject;
import com.epam.framework.ui.pageobjectgenerator.verificationTemplate.PageVerificationTemplate;
import org.apache.log4j.Logger;

import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;


public class PageObjectWriterJava implements PageObjectWriter {

    PageObject pageObject;
    PageObjectsTemplate pageObjectsTemplate;
    PageVerificationTemplate pageVerificationTemplate;
    private FileWriter myWriter;

    private static final Logger logger = Logger.getLogger(PageObjectWriterJava.class);

    public PageObjectWriterJava(PageObject pageObject, PageObjectsTemplate pageObjectsTemplate,
                                PageVerificationTemplate pageVerificationTemplate) {
        this.pageObject = pageObject;
        this.pageObjectsTemplate = pageObjectsTemplate;
        this.pageVerificationTemplate = pageVerificationTemplate;
    }


    @Override
    public void writeClass(String pageObjectsPath, String packageName) {
        Path path = Paths.get(pageObjectsPath);
        try {
            if (!Files.exists(path)) {
                Files.createDirectories(path);
            }
            logger.info("Starting PageObject Writing For Class "+pageObject.getPageName());
            myWriter = new FileWriter(pageObjectsPath+"\\"+pageObject.getPageName()+".java");
            writeParentAndChild(packageName, myWriter);
            writeElementTemplate(myWriter);
            myWriter.write(pageObjectsTemplate.getClassConstructor(pageObject.getPageName()));
            writeGettersForLocators(myWriter);
            writeLocatorMethods(myWriter);
            myWriter.write(pageObjectsTemplate.getClosureBracket());
            logger.info("Finished Writing PageObject Class "+pageObject.getPageName());
            myWriter.close();
        } catch (IOException e) {
            logger.error(e.getStackTrace());
        }
    }

    @Override
    public void writeVerifications(String verificationPath, String packageName) {
        Path path = Paths.get(verificationPath);
        try {
            if (!Files.exists(path)) {
                logger.info("Invalid Path "+path.toString()+", Creating Directory");
                Files.createDirectories(path);
            }
            logger.info("Starting PageObjectVerification Writing For Class "+pageObject.getPageName());
            myWriter = new FileWriter(verificationPath+"\\"+pageObject.getPageName()+"Verification.java");
            writePackageAndParent(packageName, myWriter);
            writeVerificationConstructor(myWriter);
            writeVerificationMethods(myWriter);
            myWriter.write(pageVerificationTemplate.getClosureBracket());
            logger.info("Finished Writing PageObjectVerification Class "+pageObject.getPageName());
            myWriter.close();
        } catch (IOException e) {
            logger.error(e.getStackTrace());
        }
    }

    private void writeVerificationMethods(FileWriter myWriter) throws IOException {
        for (Locators locator : pageObject.getLocators()) {
            if(!locator.getElementVerificationMethods().equalsIgnoreCase("")){
            for (String verification : locator.getElementVerificationMethods().split(",")) {
                boolean methodFound = false;
                switch (verification.trim().toLowerCase()) {
                    case "verifyelementstate":
                        myWriter.write(pageVerificationTemplate.getVerifyElementStateMethod(locator.getElementName()));
                        methodFound = true;
                        break;
                    case "verifyelementvalue":
                        myWriter.write(pageVerificationTemplate.getVerifyElementValue(locator.getElementName()));
                        methodFound = true;
                        break;
                    case "verifyelementattribute":
                        myWriter.write(pageVerificationTemplate.getVerifyElementAttribute(locator.getElementName()));
                        methodFound = true;
                        break;
                    case "verifyiselementpresent":
                        myWriter.write(pageVerificationTemplate.getVerifyElementPresence(locator.getElementName()));
                        methodFound = true;
                        break;
                    case "verifyelementdisplayed":
                        myWriter.write(pageVerificationTemplate.getVerifyElementDisplay(locator.getElementName()));
                        methodFound = true;
                        break;
                    case "verifydropdownvalues":
                        myWriter.write(pageVerificationTemplate.getVerifyDropdownValues(locator.getElementName()));
                        methodFound = true;
                        break;
                    case "verifyelementtext":
                        myWriter.write(pageVerificationTemplate.getVerifyElementText(locator.getElementName()));
                        methodFound = true;
                        break;
                    case "verifyelementchecked":
                        myWriter.write(pageVerificationTemplate.getVerifyElementIsChecked(locator.getElementName()));
                        methodFound = true;
                        break;
                    case "verifyelementselected":
                        myWriter.write(pageVerificationTemplate.getVerifyElementIsSelected(locator.getElementName()));
                        methodFound = true;
                        break;
                    default:
                        break;
                }

                if (!methodFound) {
                    throw new VerificationMethodCreationException("Verification method " + verification + " not found");
                }


            }
        }
    }
        logger.info("Finished Writing Verification Class For "+pageObject.getPageName());
    }

    private void writeVerificationConstructor(FileWriter myWriter) throws IOException {
        myWriter.write(pageVerificationTemplate.getClassConstructor(pageObject.getPageName()));
    }

    private void writePackageAndParent(String packageName, FileWriter myWriter) throws IOException {
        myWriter.write(pageVerificationTemplate.getClassTemplateWithParent(packageName, pageObject.getPageName()));
        logger.info("Finished Writing Verification Class "+pageObject.getPageName()+
                "Verification With Parent Class " + pageObject.getPageName());
    }

    void writeLocatorActions(Locators locator,String[] locatorActionsList) throws IOException{
        for (String action : locatorActionsList) {
            boolean methodFound = false;
            switch (locator.getElementType().trim().toLowerCase()) {
                case "textbox":
                case "textarea":
                    methodFound = writeTextActions(myWriter, locator.getElementName(), action);
                    break;
                case "link":
                case "button":
                case "image":
                    methodFound = writeButtonImageLinkActions(myWriter, locator.getElementName(), action);
                    break;
                case "checkbox":
                    methodFound = writeCheckBoxActions(myWriter, locator.getElementName(), action);
                    break;
                case "label":
                    methodFound = writeLabelActions(myWriter, locator.getElementName(), action);
                    break;
                case "iframe":
                    methodFound = writeIframeActions(myWriter, locator, action);
                    break;
                case "select":
                    methodFound = writeSelectActions(myWriter, locator.getElementName(), action);
                    break;
                case "combobox":
                    methodFound = writeComboBoxActions(myWriter, locator.getElementName(), action);
                    break;
                default:

            }

            if (!methodFound) {
                methodFound = writeUnifiedActions(myWriter, locator.getElementName(), action);
            }
            if (!methodFound) {
                throw new ActionMethodCreationException("Mentioned " + action + " not eligible on the element");
            }
        }
    }

    void writeLocatorMethods(FileWriter myWriter) throws IOException {
        for (Locators locator : pageObject.getLocators()) {
            if(!locator.getElementActionMethods().equalsIgnoreCase("")){
            String[] locatorActionsList = locator.getElementActionMethods().split(",");
            writeLocatorActions(locator,locatorActionsList);
        }
    }
        logger.info("Finished Writing Action Methods For Locators");
    }

    private boolean writeLabelActions(FileWriter myWriter, String locatorName, String locatorAction) throws IOException {
        boolean methodFound = false;
        if (locatorAction.equalsIgnoreCase("getText")) {
            myWriter.write(pageObjectsTemplate.getTextMethod(locatorName, getCamelCaseString(locatorName)));
            methodFound = true;
        }
        return methodFound;
    }

    private boolean writeSelectActions(FileWriter myWriter, String locatorName, String locatorAction) throws IOException {
        boolean methodFound = false;
        if (locatorAction.equalsIgnoreCase("selectByIndex")) {
            myWriter.write(pageObjectsTemplate.getSelectByIndexMethod(locatorName, getCamelCaseString(locatorName)));
            methodFound = true;
        }
        if (locatorAction.equalsIgnoreCase("selectByValue")) {
            myWriter.write(pageObjectsTemplate.getSelectByValueMethod(locatorName, getCamelCaseString(locatorName)));
            methodFound = true;
        }
        if (locatorAction.equalsIgnoreCase("selectByVisibleText")) {
            myWriter.write(pageObjectsTemplate.getSelectByVisibleTextMethod(locatorName, getCamelCaseString(locatorName)));
            methodFound = true;
        }
        if (locatorAction.equalsIgnoreCase("deselectByIndex")) {
            myWriter.write(pageObjectsTemplate.getDeselectByIndexMethod(locatorName, getCamelCaseString(locatorName)));
            methodFound = true;
        }
        if (locatorAction.equalsIgnoreCase("deselectByValue")) {
            myWriter.write(pageObjectsTemplate.getDeselectByValueMethod(locatorName, getCamelCaseString(locatorName)));
            methodFound = true;
        }
        if (locatorAction.equalsIgnoreCase("deselectByVisibleText")) {
            myWriter.write(pageObjectsTemplate.getDeselectByVisibleTextMethod(locatorName, getCamelCaseString(locatorName)));
            methodFound = true;
        }
        if (locatorAction.equalsIgnoreCase("deselectAll")) {
            myWriter.write(pageObjectsTemplate.getDeselectAllMethod(locatorName, getCamelCaseString(locatorName)));
            methodFound = true;
        }
        if (locatorAction.equalsIgnoreCase("isMultiple")) {
            myWriter.write(pageObjectsTemplate.getSelectIsMultipleMethod(locatorName, getCamelCaseString(locatorName)));
            methodFound = true;
        }

        return methodFound;
    }

    private boolean writeComboBoxActions(FileWriter myWriter, String locatorName, String locatorAction) throws IOException{
        boolean methodFound = false;
        if (locatorAction.equalsIgnoreCase("enterTextInComboBox")) {
            myWriter.write(pageObjectsTemplate.getEnterTextInComboBoxMethod(locatorName, getCamelCaseString(locatorName)));
            methodFound = true;
        }
        if (locatorAction.equalsIgnoreCase("getComboBoxValue")) {
            myWriter.write(pageObjectsTemplate.getComboBoxValueMethod(locatorName, getCamelCaseString(locatorName)));
            methodFound = true;
        }
        if (locatorAction.equalsIgnoreCase("validateComboBoxList")) {
            myWriter.write(pageObjectsTemplate.getValidateComboBoxListMethod(locatorName, getCamelCaseString(locatorName)));
            methodFound = true;
        }
        return methodFound;
    }

    private boolean writeCheckBoxActions(FileWriter myWriter, String locatorName, String locatorAction)
            throws IOException {
        boolean methodFound = false;
        if (locatorAction.equalsIgnoreCase("check")) {
            myWriter.write(pageObjectsTemplate.getCheckBoxCheckMethod(locatorName, getCamelCaseString(locatorName)));
            methodFound = true;
        }
        return methodFound;
    }

    private boolean writeButtonImageLinkActions(FileWriter myWriter, String locatorName, String locatorAction)
            throws IOException {
        boolean methodFound = false;
        if (locatorAction.equalsIgnoreCase("click")){
            myWriter.write(pageObjectsTemplate.getClickMethod(locatorName, getCamelCaseString(locatorName)));
            methodFound = true;}
        if (locatorAction.equalsIgnoreCase("doubleClick")){
            myWriter.write(pageObjectsTemplate.getDoubleClickMethod(locatorName, getCamelCaseString(locatorName)));
            methodFound = true;}
        if (locatorAction.equalsIgnoreCase("getText")){
            myWriter.write(pageObjectsTemplate.getTextMethod(locatorName, getCamelCaseString(locatorName)));
            methodFound = true;}
        return methodFound;
    }

    private boolean writeIframeActions(FileWriter myWriter, Locators locator, String locatorAction)
            throws IOException {
        boolean methodFound = false;
        if (locatorAction.equalsIgnoreCase("switchTo")) {
            myWriter.write(pageObjectsTemplate.getSwitchToIframeMethod(locator.getElementType(),
                    locator.getLocatorIdentifierType(), getCamelCaseString(locator.getElementName())));
            methodFound = true;
        }
        return methodFound;
    }

    private boolean writeTextActions(FileWriter myWriter, String locatorName, String locatorAction)
            throws IOException {
        boolean methodFound = false;
        if (locatorAction.equalsIgnoreCase("setText")){
            myWriter.write(pageObjectsTemplate.getSetterInputMethod(locatorName, getCamelCaseString(locatorName)));
            methodFound = true;}
        if (locatorAction.equalsIgnoreCase("getValue")){
            myWriter.write(pageObjectsTemplate.getGetterInputMethod(locatorName, getCamelCaseString(locatorName)));
            methodFound = true;}
        if (locatorAction.equalsIgnoreCase("clearText")){
            myWriter.write(pageObjectsTemplate.getClearInputMethod(locatorName,  getCamelCaseString(locatorName)));
            methodFound = true;}
        return methodFound;
    }

    private boolean writeUnifiedActions(FileWriter myWriter, String locatorName, String locatorAction)
            throws IOException {
        boolean methodFound = false;
        if (locatorAction.equalsIgnoreCase("getAttribute")){
            myWriter.write(pageObjectsTemplate.getAttributeMethod(locatorName, getCamelCaseString(locatorName)));
            methodFound = true;}
        if (locatorAction.equalsIgnoreCase("getCssValue")){
            myWriter.write(pageObjectsTemplate.getCssValueMethod(locatorName, getCamelCaseString(locatorName)));
            methodFound = true;}
        if (locatorAction.equalsIgnoreCase("getTagName")){
            myWriter.write(pageObjectsTemplate.getTagNameMethod(locatorName, getCamelCaseString(locatorName)));
            methodFound = true;}
        return methodFound;
    }

    private void writeGettersForLocators(FileWriter myWriter) throws IOException {
        for (Locators locator : pageObject.getLocators()) {
            myWriter.write(pageObjectsTemplate.getGetterForLocators(locator.getElementName(),
                    getCamelCaseString(locator.getElementName()), locator.getElementType(), locator.getLocatorIdentifierType()));
        }
        logger.info("Finished Writing Getters For Locators");
    }


    void writeElementTemplate(FileWriter myWriter) throws IOException {
        for (Locators locator : pageObject.getLocators()) {
            myWriter.write(pageObjectsTemplate.getElementTemplate(locator.getLocatorIdentifierType(),
                    locator.getLocatorIdentifierValue(),
                    getCamelCaseString(locator.getElementName()), locator.getElementType()));
        }
        logger.info("Finished Writing FindBy Templates");
    }

    void writeParentAndChild(String packageName, FileWriter myWriter) throws IOException {
        if(pageObject.getParentClassName().equalsIgnoreCase("NA")) {
            myWriter.write(pageObjectsTemplate.getClassConstructionTemplateWithParent(packageName,
                    pageObject.getPageName(), "PageWrapper"));
            logger.info("Finished Writing Parent Class " + pageObject.getPageName());
        }
        else {
            myWriter.write(pageObjectsTemplate.getClassConstructionTemplateWithParent(packageName,
                    pageObject.getPageName(), pageObject.getParentClassName()));
            logger.info("Finished Writing Parent Class " + pageObject.getPageName());
        }
        for (String child : pageObject.getChildClassName().split(",")) {
            if (!child.equalsIgnoreCase("NA")) {
                myWriter.write(pageObjectsTemplate.getInstanceVariablesTemplateForHasARelationShip(child,
                        getCamelCaseString(child)));
                logger.info("Finished Writing Child Class " + pageObject.getChildClassName());
            }
        }
    }

    private String getCamelCaseString(String string){
        return string.substring(0, 1).toLowerCase() + string.substring(1);
    }
}
