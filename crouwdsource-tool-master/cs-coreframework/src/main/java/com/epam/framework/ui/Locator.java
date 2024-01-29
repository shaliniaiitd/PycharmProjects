package com.epam.framework.ui;

import org.openqa.selenium.By;


/**
 * This is wrapper for Selenium By selector.
 *
 *
 */
public abstract class Locator {
    private final By by;
    private final String locatorString;

    public Locator(By by, String locatorString) {
        this.by = by;
        this.locatorString = locatorString;
    }

    public static Locator byXpath(String locator) {
        return new XpathLocator(By.xpath(locator), locator);
    }

    public static Locator byClassName(String locator) {
        return new ClassNameLocator(By.className(locator), locator);
    }

    public static Locator byCssSelector(String locator) {
        return new CssSelectorLocator(By.cssSelector(locator), locator);
    }

    public static Locator byId(String locator) {
        return new IdLocator(By.id(locator), locator);
    }

    public static Locator byName(String locator) {
        return new NameLocator(By.name(locator), locator);
    }

    public static Locator byPartialLinkText(String locator) {
        return new PartialLinkTextLocator(By.partialLinkText(locator), locator);
    }

    public static Locator byLinkText(String locator) {
        return new LinkTextLocator(By.linkText(locator), locator);
    }

    public static Locator byTagName(String locator) {
        return new TagNameLocator(By.tagName(locator), locator);
    }

    public By getBy() {
        return this.by;
    }

    public String getLocatorString() {
        return this.locatorString;
    }

    public abstract Locator format(String... args);

    @Override
    public String toString() {
        return "Locator{" +
                "by=" + by +
                ", locator='" + locatorString + '\'' +
                '}';
    }

    public static class XpathLocator extends Locator {

        public XpathLocator(By by, String locator) {
            super(by, locator);
        }

        @Override
        public Locator format(String... args) {
            String dynamicLocator = String.format(getLocatorString(), args);
            return new XpathLocator(By.xpath(dynamicLocator), dynamicLocator);
        }
    }

    public static class ClassNameLocator extends Locator {

        public ClassNameLocator(By by, String locator) {
            super(by, locator);
        }

        @Override
        public Locator format(String... args) {
            String dynamicLocator = String.format(getLocatorString(), args);
            return new ClassNameLocator(By.className(dynamicLocator), dynamicLocator);
        }
    }

    public static class CssSelectorLocator extends Locator {

        public CssSelectorLocator(By by, String locator) {
            super(by, locator);
        }

        @Override
        public Locator format(String... args) {
            String dynamicLocator = String.format(getLocatorString(), args);
            return new CssSelectorLocator(By.cssSelector(dynamicLocator), dynamicLocator);
        }
    }

    public static class IdLocator extends Locator {

        public IdLocator(By by, String locator) {
            super(by, locator);
        }

        @Override
        public Locator format(String... args) {
            String dynamicLocator = String.format(getLocatorString(), args);
            return new IdLocator(By.id(dynamicLocator), dynamicLocator);
        }
    }

    public static class NameLocator extends Locator {

        public NameLocator(By by, String locator) {
            super(by, locator);
        }

        @Override
        public Locator format(String... args) {
            String dynamicLocator = String.format(getLocatorString(), args);
            return new NameLocator(By.name(dynamicLocator), dynamicLocator);
        }
    }

    public static class PartialLinkTextLocator extends Locator {

        public PartialLinkTextLocator(By by, String locator) {
            super(by, locator);
        }

        @Override
        public Locator format(String... args) {
            String dynamicLocator = String.format(getLocatorString(), args);
            return new PartialLinkTextLocator(By.partialLinkText(dynamicLocator), dynamicLocator);
        }
    }

    public static class LinkTextLocator extends Locator {

        public LinkTextLocator(By by, String locator) {
            super(by, locator);
        }

        @Override
        public Locator format(String... args) {
            String dynamicLocator = String.format(getLocatorString(), args);
            return new LinkTextLocator(By.linkText(dynamicLocator), dynamicLocator);
        }
    }

    public static class TagNameLocator extends Locator {

        public TagNameLocator(By by, String locator) {
            super(by, locator);
        }

        @Override
        public Locator format(String... args) {
            String dynamicLocator = String.format(getLocatorString(), args);
            return new TagNameLocator(By.tagName(dynamicLocator), dynamicLocator);
        }
    }

}
