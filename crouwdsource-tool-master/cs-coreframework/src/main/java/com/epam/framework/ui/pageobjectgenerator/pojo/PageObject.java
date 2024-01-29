package com.epam.framework.ui.pageobjectgenerator.pojo;

public class PageObject {

    private String pageName;
    private String operation;
    private String parentClassName;
    private String childClassNames;
    private Locators[] locators;

    public PageObject() {}

    public PageObject(String pageName, String operation, String parentClassName,
                      String childClassNames, Locators[] locators) {
        this.pageName = pageName;
        this.operation = operation;
        this.parentClassName = parentClassName;
        this.childClassNames = childClassNames;
        this.locators = locators;
    }

    public String getPageName() {
        return pageName;
    }

    public void setPageName(String pageName) {
        this.pageName = pageName;
    }

    public String getOperation() {
        return operation;
    }

    public void setOperation(String operation) {
        this.operation = operation;
    }

    public String getParentClassName() {
        return parentClassName;
    }

    public void setParentClassName(String parentClassName) {
        this.parentClassName = parentClassName;
    }

    public String getChildClassName() {
        return childClassNames;
    }

    public void setChildClassName(String childClassNames) {
        this.childClassNames = childClassNames;
    }

    public Locators[] getLocators() {
        return locators;
    }

    public void setLocators(Locators[] locators) {
        this.locators = locators;
    }
}
