package com.epam.framework.ui;

import com.epam.framework.ui.pageobjectgenerator.exceptions.InvalidElementIdentificationTypeException;
import org.apache.commons.lang3.StringUtils;
import org.openqa.selenium.By;

import java.util.Optional;

public class LocatorFormatter {
    private LocatorFormatter(){

    }

    public static By getElementIdentifier(String ... selector) {

        String[] selectorTypeNVal = selector[0].split(" -> ", 2);
        return getByElement(selectorTypeNVal[0].trim().toLowerCase(), selectorTypeNVal[1].trim());

    }

    public static int getNumberOfFormatters(String selector)
    {
        String stringFormatter = "%s";
        return StringUtils.countMatches(selector, stringFormatter);
    }


    private static By getByElement(String selectorType, String webElementSelector) {

        By elementBy = null;
        switch(selectorType)
        {
            case "id":
                elementBy = By.id(webElementSelector);
                break;
            case "name":
                elementBy = By.name(webElementSelector);
                break;
            case "className":
                elementBy = By.className(webElementSelector);
                break;
            case "tagName":
                elementBy = By.tagName(webElementSelector);
                break;
            case "partialLinkText":
                elementBy = By.partialLinkText(webElementSelector);
                break;
            case "linkText":
                elementBy = By.linkText(webElementSelector);
                break;
            case "cssSelector":
                elementBy = By.cssSelector(webElementSelector);
                break;
            case "xpath":
                elementBy = By.xpath(webElementSelector);
                break;
            default:
                throw new InvalidElementIdentificationTypeException("You have selected Invalid Element Identification Type");
        }
        return Optional.ofNullable(elementBy).orElseThrow(InvalidElementIdentificationTypeException::new);
    }
}
