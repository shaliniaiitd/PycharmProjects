package com.epam.framework.ui.pageobjectgenerator.pojo;

public class Locators {

    private String elementName;
    private String elementType;
    private String locatorIdentifierType;
    private String locatorIdentifierValue;
    private String elementActionMethods;
    private String elementVerificationMethods;

    public Locators() {}

    public Locators(String elementName, String elementType, String locatorIdentifierType,
                    String locatorIdentifierValue, String elementActionMethods,
                    String elementVerificationMethods) {
        this.elementName = elementName;
        this.elementType = elementType;
        this.locatorIdentifierType = locatorIdentifierType;
        this.locatorIdentifierValue = locatorIdentifierValue;
        this.elementActionMethods = elementActionMethods;
        this.elementVerificationMethods = elementVerificationMethods;
    }

    public String getElementName() {
        return elementName;
    }

    public void setElementName(String elementName) {
        this.elementName = elementName;
    }

    public String getElementType() {
        return elementType;
    }

    public void setElementType(String elementType) {
        this.elementType = elementType;
    }

    public String getLocatorIdentifierType() {
        return locatorIdentifierType;
    }

    public void setLocatorIdentifierType(String locatorIdentifierType) {
        this.locatorIdentifierType = locatorIdentifierType;
    }

    public String getLocatorIdentifierValue() {
        return locatorIdentifierValue;
    }

    public void setLocatorIdentifierValue(String locatorIdentifierValue) {
        this.locatorIdentifierValue = locatorIdentifierValue;
    }

    public String getElementActionMethods() {
        return elementActionMethods;
    }

    public void setElementActionMethods(String elementActionMethods) {
        this.elementActionMethods = elementActionMethods;
    }

    public String getElementVerificationMethods() {
        return elementVerificationMethods;
    }

    public void setElementVerificationMethods(String elementVerificationMethods) {
        this.elementVerificationMethods = elementVerificationMethods;
    }
}
