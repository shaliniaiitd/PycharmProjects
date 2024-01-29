package com.epam.framework.ui.pageobjectgenerator.pageObjectTemplate;

import com.epam.framework.core.TestContext;
import com.epam.framework.core.logging.logger.LogLevel;
import com.epam.framework.ui.pageobjectgenerator.constant.TemplateConstants;
import org.apache.log4j.Logger;


public class PageObjectsTemplateJava implements PageObjectsTemplate {

    private static final Logger logger = Logger.getLogger(PageObjectsTemplateJava.class);

    @Override
    public String getClassConstructionTemplate(String className) {
        return "";
    }

    @Override
    public String getClassConstructionTemplate(String packagePath, String className){
        TestContext.getLogger().log(LogLevel.INFO,"Creating Class "+className);
        return String.format("package %s;"+ TemplateConstants.DOUBLE_NEWLINE+
                "import com.epam.framework.ui.PageWrapper;"+ TemplateConstants.SINGLE_NEWLINE+
                "import org.openqa.selenium.WebDriver;"+ TemplateConstants.SINGLE_NEWLINE+
                "import org.openqa.selenium.WebElement;"+ TemplateConstants.SINGLE_NEWLINE+
                "public class %s {"+ TemplateConstants.SINGLE_NEWLINE,packagePath, className);
    }

    @Override
    public String getClassConstructionTemplateWithParent(String packagePath, String className, String parentClassName){
        TestContext.getLogger().log(LogLevel.INFO,"Creating Class "+className+" With Parent Class "+parentClassName);
        return String.format("package %s"+".actions;"+ TemplateConstants.DOUBLE_NEWLINE+
                "import com.epam.framework.ui.PageWrapper;"+ TemplateConstants.SINGLE_NEWLINE+
                "import org.openqa.selenium.WebDriver;"+ TemplateConstants.SINGLE_NEWLINE+
                "import org.openqa.selenium.WebElement;"+ TemplateConstants.SINGLE_NEWLINE+
                "public class %s extends %s {"+ TemplateConstants.SINGLE_NEWLINE, packagePath, className, parentClassName);
    }

    @Override
    public String getClassConstructor(String className){
        TestContext.getLogger().log(LogLevel.INFO,"Writing Class Constructor For Class "+className);
        return String.format(TemplateConstants.DOUBLE_NEWLINE
                + TemplateConstants.SINGLE_TAB + "public %s(WebDriver webDriver) {"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.DOUBLE_TAB+"super(webDriver);"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.SINGLE_TAB+"}"+ TemplateConstants.DOUBLE_NEWLINE,className);
    }

    @Override
    public String getLocatorsLabelTemplate(){
        return "";
    }

    @Override
    public String getGetterForLocators(String methodName, String elementName, String elementType, String locatorType) {
        TestContext.getLogger().log(LogLevel.INFO,"Writing Getter Method For Element "+elementName);
        String getterForLocator ="";
        if(isNotIframeByIndex(elementType, locatorType) && isNotWindowIndex(elementType))
        {
            getterForLocator= String.format(TemplateConstants.SINGLE_TAB
                    + "public String get%s(String ... formatArgs) {"
                    + TemplateConstants.SINGLE_NEWLINE
                    + TemplateConstants.DOUBLE_TAB + "return formatLocator("+elementName+", formatArgs);"
                    + TemplateConstants.SINGLE_NEWLINE
                    + TemplateConstants.SINGLE_TAB + "}" + TemplateConstants.DOUBLE_NEWLINE, methodName, elementName);
        }

        return getterForLocator;
    }

    public String getElementTemplate(String locatorType, String locatorValue, String elementName, String elementType){
        TestContext.getLogger().log(LogLevel.INFO,"Writing Element Template For Element s"+elementName);
        String elementTemplate;
        if(isDynamicLocator(locatorValue))
        {
            elementTemplate = String.format(TemplateConstants.SINGLE_NEWLINE
                            + TemplateConstants.SINGLE_TAB+ "private String %s = \"%s -> %s\";"
                    , elementName, locatorType, locatorValue);
        }
        else if(isIframeByIndex(elementType, locatorType))
        {
            elementTemplate = String.format(TemplateConstants.SINGLE_NEWLINE
                            + TemplateConstants.SINGLE_TAB+  "private static final int %s = %s;"
                    , elementName, locatorValue);
        }
        else {
            elementTemplate = String.format(TemplateConstants.SINGLE_NEWLINE
                            + TemplateConstants.SINGLE_TAB + "private static final String %s = \"%s -> %s\";"
                    , elementName, locatorType, locatorValue);
        }

        return elementTemplate;
    }

    private boolean isIframeByIndex(String elementType, String locatorType) {
        return (elementType.equalsIgnoreCase("iframe") && locatorType.equalsIgnoreCase("Index"));
    }

    private boolean isNotIframeByIndex(String elementType, String locatorType) {
        return !(elementType.equalsIgnoreCase("iframe") && locatorType.equalsIgnoreCase("Index"));
    }

    private boolean isNotWindowIndex(String elementType) {
        return !elementType.equalsIgnoreCase("Window");
    }

    @Override
    public String getInstanceVariablesTemplate(){
        TestContext.getLogger().log(LogLevel.INFO,"Writing WebDriver Instance Variable");
        return TemplateConstants.SINGLE_TAB+"private WebDriver driver;"+ TemplateConstants.DOUBLE_NEWLINE;
    }

    @Override
    public String getInstanceVariablesTemplateForHasARelationShip(String child, String instanceVariableName){
        TestContext.getLogger().log(LogLevel.INFO,"Writing Child "+child+" Class Instance Variable");
        return String.format(TemplateConstants.SINGLE_TAB
                + "private %s %s;"
                + TemplateConstants.DOUBLE_NEWLINE, child, instanceVariableName);
    }

    // Text Element Template Methods
    @Override
    public String getClearInputMethod(String methodName, String variableName) {
        TestContext.getLogger().log(LogLevel.INFO,"Writing Clear Method For Element "+methodName);
        return String.format(TemplateConstants.SINGLE_TAB
                + "public void clear%s(String... formatArgs) {"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.DOUBLE_TAB+"clearField(%s,\"%s\", formatArgs);"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.SINGLE_TAB+"}"+ TemplateConstants.DOUBLE_NEWLINE,methodName, variableName,variableName);
    }

    // Text Element Template Methods
    @Override
    public String getSetterInputMethod(String methodName, String variableName){
        TestContext.getLogger().log(LogLevel.INFO,"Writing Set Method For Element "+methodName);
        return String.format(TemplateConstants.SINGLE_TAB
                + "public void set%s(String value, String ... formatArgs) {"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.DOUBLE_TAB+ "setText(value, %s,\"%s\", formatArgs);"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.SINGLE_TAB+"}"+ TemplateConstants.DOUBLE_NEWLINE,methodName, variableName,methodName);
    }

    @Override
    public String getSetterInputMethod(String methodName) {
        return "";
    }

    // Text Element Template Methods
    @Override
    public String getGetterInputMethod(String methodName, String elementName){
        TestContext.getLogger().log(LogLevel.INFO,"Writing Get Method For Element "+methodName);
        return String.format(TemplateConstants.SINGLE_TAB
                + "public String get%sText(String ... formatArgs){"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.DOUBLE_TAB+"return getText(%s,\"%s\", formatArgs);"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.SINGLE_TAB+"}"+ TemplateConstants.DOUBLE_NEWLINE,methodName, methodName,methodName);
    }

    @Override
    public String getGetterInputMethod(String methodName) {
        return "";
    }

    //iFrame switchTo

    @Override
    public String getSwitchToIframeMethod(String elementType, String locatorIdentifierType, String methodName)
    {
        TestContext.getLogger().log(LogLevel.INFO,"Writing SwitchTo Method For Element "+methodName);

        if(isIframeByIndex(elementType, locatorIdentifierType))
        {
            return String.format(TemplateConstants.SINGLE_TAB
                    +"public void getSwitchTo%s(){"
                    + TemplateConstants.SINGLE_NEWLINE
                    + TemplateConstants.DOUBLE_TAB +"this.switchToIframeByIndex(%s);"
                    + TemplateConstants.SINGLE_NEWLINE
                    + TemplateConstants.SINGLE_TAB+"}"+ TemplateConstants.DOUBLE_NEWLINE,methodName, methodName);
        }
        else {

            return String.format(TemplateConstants.SINGLE_TAB
                    + "public void getSwitchTo%s(String ... formatArgs){"
                    + TemplateConstants.SINGLE_NEWLINE
                    + TemplateConstants.DOUBLE_TAB + "this.switchToIframeByElement(%s, formatArgs);"
                    + TemplateConstants.SINGLE_NEWLINE
                    + TemplateConstants.SINGLE_TAB + "}" + TemplateConstants.DOUBLE_NEWLINE, methodName, methodName);
        }
    }

    // Button, Image And Link Template Method
    @Override
    public String getClickMethod(String methodName, String elementName){
        TestContext.getLogger().log(LogLevel.INFO,"Writing Click Method For Element "+methodName);
        return String.format(TemplateConstants.SINGLE_TAB
                +"public void click%s(String... formatArgs){"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.DOUBLE_TAB+"click(%s, \"%s\",formatArgs);"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.SINGLE_TAB+"}"+ TemplateConstants.DOUBLE_NEWLINE,methodName, elementName,elementName);
    }

    // Button, Image And Link Template Method
    @Override
    public String getDoubleClickMethod(String methodName, String elementName) {
        TestContext.getLogger().log(LogLevel.INFO,"Writing Double Click Method For Element "+methodName);

        return String.format(TemplateConstants.SINGLE_TAB
                +"public void doubleClick%s(String... formatArgs){"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.DOUBLE_TAB+"doubleClick(%s, \"%s\",formatArgs);"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.SINGLE_TAB+"}"+ TemplateConstants.DOUBLE_NEWLINE,methodName, elementName,elementName);

    }

    @Override
    public String getCheckBoxCheckMethod(String methodName, String elementName) {
        TestContext.getLogger().log(LogLevel.INFO,"Writing Check Method For CheckBox Element "+methodName);
        return String.format(TemplateConstants.SINGLE_TAB
                +"public void check%s(boolean check, String ... formatArgs){"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.DOUBLE_TAB+"check(check, %s,\"%s\", formatArgs);"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.SINGLE_TAB+"}"+ TemplateConstants.DOUBLE_NEWLINE,methodName,elementName, elementName);

    }

    @Override
    public String getAttributeMethod(String methodName, String elementName) {
        TestContext.getLogger().log(LogLevel.INFO,"Writing Get Attribute Method For Element "+methodName);

        return String.format(TemplateConstants.SINGLE_TAB+
                "public String get%sAttribute(String attributeName, String... formatArgs){"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.DOUBLE_TAB+"return getAttribute(attributeName, %s,\"%s\", formatArgs);"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.SINGLE_TAB+"}"+ TemplateConstants.DOUBLE_NEWLINE,methodName,elementName, elementName);

    }

    @Override
    public String getCssValueMethod(String methodName, String elementName) {
        TestContext.getLogger().log(LogLevel.INFO,"Writing Get cssValue method for element " +methodName);

        return String.format(TemplateConstants.SINGLE_TAB
                +"public String get%sCssValue(String propertyName, String... formatArgs){"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.DOUBLE_TAB+"return getCssValue(propertyName, %s,\"%s\", formatArgs);"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.SINGLE_TAB+"}"+ TemplateConstants.DOUBLE_NEWLINE,methodName,elementName, elementName);

    }

    @Override
    public String getTagNameMethod(String methodName, String elementName) {
        TestContext.getLogger().log(LogLevel.INFO,"Writing Get tagName method for element " +methodName);

        return String.format(TemplateConstants.SINGLE_TAB
                +"public String get%sTagName(String... formatArgs){"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.DOUBLE_TAB+"return getTagName(%s, formatArgs);"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.SINGLE_TAB+"}"+ TemplateConstants.DOUBLE_NEWLINE,elementName, elementName);

    }

    @Override
    public String getTextMethod(String methodName, String elementName) {
        TestContext.getLogger().log(LogLevel.INFO,"Writing Get Text Method For Label Element "+methodName);

        return String.format(TemplateConstants.SINGLE_TAB
                +"public String get%sText(String... formatArgs){"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.DOUBLE_TAB+"return getText(%s,\"%s\", formatArgs);"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.SINGLE_TAB+"}"+ TemplateConstants.DOUBLE_NEWLINE,methodName,elementName, elementName);

    }


    //get select method for select elements


    @Override
    public String getSelectByIndexMethod(String methodName, String elementName) {
        TestContext.getLogger().log(LogLevel.INFO,"Writing select by index Method For Select Element "+methodName);

        return String.format(TemplateConstants.SINGLE_TAB
                + "public void select%sByIndex(int index, String... formatArgs){"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.DOUBLE_TAB+"selectItemFromDropdownByIndex(index, %s,\"%s\", formatArgs);"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.SINGLE_TAB+"}"+ TemplateConstants.DOUBLE_NEWLINE,methodName,elementName, elementName);
    }


    @Override
    public String getSelectByValueMethod(String methodName, String elementName) {
        TestContext.getLogger().log(LogLevel.INFO,"Writing select by value Method For Select Element "+methodName);

        return String.format(TemplateConstants.SINGLE_TAB
                + "public void select%sByValue(String optionValue, String... formatArgs){"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.DOUBLE_TAB+"selectItemFromDropdownByValue(optionValue, %s,\"%s\", formatArgs);"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.SINGLE_TAB+"}"+ TemplateConstants.DOUBLE_NEWLINE,methodName,elementName, elementName);
    }

    @Override
    public String getSelectByVisibleTextMethod(String methodName, String elementName) {
        TestContext.getLogger().log(LogLevel.INFO,"Writing select by text Method For Select Element "+methodName);

        return String.format(TemplateConstants.SINGLE_TAB
                + "public void select%sByVisibleText(String optionText, String... formatArgs){"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.DOUBLE_TAB+"selectItemFromDropdownByVisibleText(optionText, %s,\"%s\", formatArgs);"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.SINGLE_TAB+"}"+ TemplateConstants.DOUBLE_NEWLINE,methodName,elementName, elementName);
    }

    @Override
    public String getDeselectByIndexMethod(String methodName, String elementName) {
        TestContext.getLogger().log(LogLevel.INFO,"Writing deselect by index Method For Select Element "+methodName);

        return String.format(TemplateConstants.SINGLE_TAB
                + "public void deselect%sByIndex(int index, String... formatArgs){"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.DOUBLE_TAB+"deSelectItemFromDropdownByIndex(index, %s,\"%s\", formatArgs);"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.SINGLE_TAB+"}"+ TemplateConstants.DOUBLE_NEWLINE,methodName,elementName, elementName);
    }


    @Override
    public String getDeselectByValueMethod(String methodName, String elementName) {
        TestContext.getLogger().log(LogLevel.INFO,"Writing deselect by value Method For Select Element "+methodName);

        return String.format(TemplateConstants.SINGLE_TAB
                + "public void deselect%sByValue(String optionValue, String... formatArgs){"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.DOUBLE_TAB+"deSelectItemFromDropdownByValue(optionValue, %s,\"%s\", formatArgs);"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.SINGLE_TAB+"}"+ TemplateConstants.DOUBLE_NEWLINE,methodName,elementName, elementName);
    }

    @Override
    public String getDeselectByVisibleTextMethod(String methodName, String elementName) {
        TestContext.getLogger().log(LogLevel.INFO,"Writing deselect by Text Method For Select Element "+methodName);

        return String.format(TemplateConstants.SINGLE_TAB
                + "public void deselect%sByVisibleText(String optionText, String... formatArgs){"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.DOUBLE_TAB+"deSelectItemFromDropdownByVisibleText(optionText, %s,\"%s\", formatArgs);"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.SINGLE_TAB+"}"+ TemplateConstants.DOUBLE_NEWLINE,methodName,elementName, elementName);
    }

    @Override
    public String getDeselectAllMethod(String methodName, String elementName) {
        TestContext.getLogger().log(LogLevel.INFO,"Writing deselect all For Select Element "+methodName);

        return String.format(TemplateConstants.SINGLE_TAB
                + "public void deselect%sAll(String optionText, String... formatArgs){"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.DOUBLE_TAB+"deSelectAllItemFromDropdown(optionText, %s, formatArgs);"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.SINGLE_TAB+"}"+ TemplateConstants.DOUBLE_NEWLINE,elementName, elementName);
    }

    @Override
    public String getSelectIsMultipleMethod(String methodName, String elementName) {
        TestContext.getLogger().log(LogLevel.INFO,"Writing is multiple all For Select Element "+methodName);

        return String.format(TemplateConstants.SINGLE_TAB
                + "public boolean check%sIsMultiple(String... formatArgs){"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.DOUBLE_TAB+"return checkDropdownIsMultiple(%s, formatArgs);"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.SINGLE_TAB+"}"+ TemplateConstants.DOUBLE_NEWLINE,elementName, elementName);
    }

    //combo box
    @Override
    public String getEnterTextInComboBoxMethod(String methodName, String elementName) {
        TestContext.getLogger().log(LogLevel.INFO,"Writing enter text in comboBox element "+methodName);

        return String.format(TemplateConstants.SINGLE_TAB
                    + "public void enterTextIn%sComboBox(String... formatArgs){"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.DOUBLE_TAB+"enterTextInComboBox(%s,\"%s\", formatArgs);"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.SINGLE_TAB+"}"+ TemplateConstants.DOUBLE_NEWLINE,methodName,elementName, elementName);
    }

    @Override
    public String getComboBoxValueMethod(String methodName, String elementName) {
        TestContext.getLogger().log(LogLevel.INFO,"Writing get comboBox value for combBox element "+methodName);

        return String.format(TemplateConstants.SINGLE_TAB
                + "public String get%sComboBoxValue(String... formatArgs){"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.DOUBLE_TAB+"return getComboBoxValue(%s,\"%s\", formatArgs);"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.SINGLE_TAB+"}"+ TemplateConstants.DOUBLE_NEWLINE,methodName,elementName, elementName);
    }

    @Override
    public String getValidateComboBoxListMethod(String methodName, String elementName) {
        TestContext.getLogger().log(LogLevel.INFO,"Writing get validate ComboBox List method for "+methodName);

        return String.format(TemplateConstants.SINGLE_TAB
                + "public boolean validate%sComboBoxList(List<WebElement> expectedOptions, String... formatArgs){"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.DOUBLE_TAB+"return validateComboBoxList(List<WebElement> expectedOptions, %s,\"%s\", formatArgs);"
                + TemplateConstants.SINGLE_NEWLINE
                + TemplateConstants.SINGLE_TAB+"}"+ TemplateConstants.DOUBLE_NEWLINE,methodName,elementName, elementName);
    }





    @Override
    public String getLocator(String methodName, String elementName) {
        return "";
    }

    @Override
    public String getSingleTab() {
        TestContext.getLogger().log(LogLevel.INFO,"Writing Closure Bracket");
        return TemplateConstants.SINGLE_TAB;
    }

    private boolean isDynamicLocator(String locator)
    {
        return locator.contains("%");
    }

    @Override
    public String getClosureBracket() {
        TestContext.getLogger().log(LogLevel.INFO,"Writing Closure Bracket");
        return "}\n";
    }
}



