package com.epam.framework.ui.pageobjectgenerator.verificationTemplate;

import com.epam.framework.ui.pageobjectgenerator.constant.TemplateConstants;
import org.apache.log4j.Logger;

/**
 * Page Object Verification Template for Java. Contains
 * the methods to produce the required templates for the
 * Page Object Model (POM) Verification.
 *
 * implements: PageVerificationTemplate.java
 *
 */

public class PageVerificationTemplateJava implements PageVerificationTemplate {
    private static final Logger logger = Logger.getLogger(PageVerificationTemplateJava.class);

    @Override
    public String getClassTemplateWithParent(String packagePath, String parentClassName) {
        logger.info("Creating Class "+parentClassName+"Verification");
        return String.format("package %s.verifications;"
                + TemplateConstants.DOUBLE_NEWLINE+ "import %s"+".actions"+".%s;"
                + TemplateConstants.SINGLE_NEWLINE+ "import org.openqa.selenium.WebDriver;"
                + TemplateConstants.DOUBLE_NEWLINE+ "public class %sVerification extends %s {"
                + TemplateConstants.SINGLE_NEWLINE,
                packagePath, packagePath, parentClassName, parentClassName, parentClassName);
    }

    @Override
    public String getClassConstructor(String parentClassName) {
        logger.info("Creating Constructor For Class "+parentClassName+"Verification");
        return String.format(TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.SINGLE_TAB+ "public %sVerification (WebDriver webDriver) {"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.DOUBLE_TAB+"super(webDriver);"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.SINGLE_TAB+"}"+ TemplateConstants.DOUBLE_NEWLINE, parentClassName);
    }
//what is element state?
    @Override
    public String getVerifyElementStateMethod(String locatorName) {
        logger.info("Writing Verify Element Status Method For Element "+locatorName);
        return String.format(TemplateConstants.SINGLE_TAB+"public void verify%sState() {"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.DOUBLE_TAB+"verifyElementState(get%s());"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.SINGLE_TAB+"}"
                + TemplateConstants.DOUBLE_NEWLINE, locatorName, locatorName);
    }

    @Override
    public String getVerifyElementValue(String locatorName) {
        logger.info("Writing Verify Element Value Method For Element "+locatorName);
        return String.format(TemplateConstants.SINGLE_TAB
                + "public void verify%sValue(String errMsg, String expValue, String ... formatArgs) {"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.DOUBLE_TAB+"verifyElementValue(errMsg, get%s(formatArgs),expValue);"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.SINGLE_TAB+"}"
                + TemplateConstants.DOUBLE_NEWLINE, locatorName, locatorName);
    }

    @Override
    public String getVerifyElementAttribute(String locatorName) {
        logger.info("Writing Verify Element Attribute Method For Element "+locatorName);
        return String.format(TemplateConstants.SINGLE_TAB
                + "public void verify%sAttribute(String errMsg, String attributeName, String expValue, String ... formatArgs) {"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.DOUBLE_TAB+"verifyElementAttribute(errMsg, get%s(formatArgs), attributeName,expValue);"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.SINGLE_TAB+"}"
                + TemplateConstants.DOUBLE_NEWLINE, locatorName, locatorName);
    }


    @Override
    public String getVerifyElementPresence(String locatorName) {
        logger.info("Writing Verify Element Presence Method For Element "+locatorName);
        return String.format(TemplateConstants.SINGLE_TAB
                + "public void verify%sPresence(String errMsg, boolean isPresent, String ... formatArgs) {"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.DOUBLE_TAB+"verifyIsElementPresent(errMsg, isPresent, get%s(formatArgs), \"%s\");"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.SINGLE_TAB+"}"
                + TemplateConstants.DOUBLE_NEWLINE, locatorName, locatorName,locatorName);
    }

    @Override
    public String getVerifyElementDisplay(String locatorName) {
        logger.info("Writing Verify Element Display Method For Element "+locatorName);
        return String.format(TemplateConstants.SINGLE_TAB
                + "public void verify%sDisplay(String errMsg, boolean, isDisplayed, String ... formatArgs) {"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.DOUBLE_TAB+"verifyIsElementDisplayed(errMsg, get%s(formatArgs), isDisplayed );"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.SINGLE_TAB+"}"
                + TemplateConstants.DOUBLE_NEWLINE, locatorName, locatorName);
    }

    @Override
    public String getVerifyDropdownValues(String locatorName) {
        logger.info("Writing Verify Dropdown Values Method For Element "+locatorName);
        return String.format(TemplateConstants.SINGLE_TAB
                + "public void verify%sDropdownValues(String errMsg, List<String>expValues, String... formatArgs) {"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.DOUBLE_TAB+"verifyDropdownValues(errMsg,get%s(formatArgs), expValues);"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.SINGLE_TAB+"}"
                + TemplateConstants.DOUBLE_NEWLINE, locatorName, locatorName);
    }

    @Override
    public String getVerifyElementText(String locatorName) {
        logger.info("Writing Verify Element Text Method For Element "+locatorName);
        return String.format(TemplateConstants.SINGLE_TAB
                + "public void verify%sText(String errMsg, String expectedValue, String... formatArgs) {"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.DOUBLE_TAB+"verifyElementText(errMsg, get%s(formatArgs), expectedValue);"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.SINGLE_TAB+"}"
                + TemplateConstants.DOUBLE_NEWLINE, locatorName, locatorName);
    }

    @Override
    public String getVerifyElementIsChecked(String locatorName) {
        logger.info("Writing Verify Element is checked Method For Element "+locatorName);
        return String.format(TemplateConstants.SINGLE_TAB
                + "public void verify%sText(String errMsg, String isChecked, String... formatArgs) {"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.DOUBLE_TAB+"getVerifyElementIsChecked(errMsg, get%s(formatArgs), isChecked);"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.SINGLE_TAB+"}"
                + TemplateConstants.DOUBLE_NEWLINE, locatorName, locatorName);
    }

    @Override
    public String getVerifyElementIsSelected(String locatorName) {
        logger.info("Writing Verify Element is selected Method For Element "+locatorName);
        return String.format(TemplateConstants.SINGLE_TAB
                + "public void verify%sText(String errMsg, String isSelected, String... formatArgs) {"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.DOUBLE_TAB+"getVerifyElementIsSelected(errMsg, get%s(formatArgs), isSelected);"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.SINGLE_TAB+"}"
                + TemplateConstants.DOUBLE_NEWLINE, locatorName, locatorName);
    }

    @Override
    public String getClosureBracket() {
        logger.info("Writing Closure Bracket");
        return "}";
    }
}
