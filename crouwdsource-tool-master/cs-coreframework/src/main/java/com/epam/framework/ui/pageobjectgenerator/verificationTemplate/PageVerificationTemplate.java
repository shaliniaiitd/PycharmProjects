package com.epam.framework.ui.pageobjectgenerator.verificationTemplate;

/**
 * Page Object Verification Template Interface.
 * Contains the methods to produce the required
 * Page Object Model (POM) Verification template.
 *
 */

public interface    PageVerificationTemplate {

    String getClassTemplateWithParent(String packagePath, String parentClassName);
    String getClassConstructor(String className);

    // Verification Methods
    String getVerifyElementStateMethod(String elementName);
    String getVerifyElementValue(String elementName);
    String getVerifyElementAttribute(String elementName);
    String getVerifyElementPresence(String elementName);
    String getVerifyElementDisplay(String elementName);
    String getVerifyDropdownValues(String elementName);
    String getVerifyElementText(String elementName);
    String getVerifyElementIsChecked(String elementName);
    String getVerifyElementIsSelected(String elementName);
    String getClosureBracket();

}
