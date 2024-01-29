package com.epam.framework.ui.pageobjectgenerator.pageObjectTemplate;

/**
 * Page Object Template Interface. Contains the methods
 * to produce the required Page Object Model (POM).
 *
 */

public interface PageObjectsTemplate {

    // Constructor Template
    String getClassConstructionTemplate(String className);
    String getClassConstructionTemplate(String packagePath, String className);
    String getClassConstructionTemplateWithParent(String packagePath, String className, String parentClassName);
    String getClassConstructor(String className);

    // Locator Template
    String getLocatorsLabelTemplate();
    String getGetterForLocators(String methodName, String elementName, String elementType, String locatorType);

    public String getElementTemplate(String locatorType, String locatorValue, String elementName, String elementType);

    String getInstanceVariablesTemplate();
    String getInstanceVariablesTemplateForHasARelationShip(String child, String instanceVariableName);

    // Text Element Template
    String getClearInputMethod(String methodName, String camelCaseString);
    String getSetterInputMethod(String methodName,String elementName);
    String getSetterInputMethod(String methodName);
    String getGetterInputMethod(String methodName, String elementName);
    String getGetterInputMethod(String methodName);

    // Button, Image And Link Template
    String getClickMethod(String methodName, String elementName);
    String getDoubleClickMethod(String methodName, String elementName);

    // Checkbox Templates
    String getCheckBoxCheckMethod(String methodName, String elementName);

    // Label Template
    String getTextMethod(String methodName, String elementName);

    String getClosureBracket();
    String getSingleTab();
    String getLocator(String methodName, String elementName);

    String getAttributeMethod(String methodName, String locatorName);
    String getCssValueMethod(String methodName, String elementName);
    String getTagNameMethod(String methodName, String elementName);

    String getSwitchToIframeMethod(String elementType, String locatorIdentifierType, String methodName);

    //select
    String getSelectByIndexMethod(String methodName, String elementName);
    String getSelectByValueMethod(String methodName, String elementName);
    String getSelectByVisibleTextMethod(String methodName, String elementName);
    String getDeselectByIndexMethod(String methodName, String elementName);
    String getDeselectByValueMethod(String methodName, String elementName);
    String getDeselectByVisibleTextMethod(String methodName, String elementName);
    String getDeselectAllMethod(String methodName, String elementName);
    String getSelectIsMultipleMethod(String methodName, String elementName);

    //combo box
    String getValidateComboBoxListMethod(String methodName, String elementName);
    String getComboBoxValueMethod(String methodName, String elementName);
    String getEnterTextInComboBoxMethod(String methodName, String elementName);

}
