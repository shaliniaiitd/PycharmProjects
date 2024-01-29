package com.epam.framework.ui.pageobjectgenerator.pageObjectWriter;

/**
 * Page Object Writer Interface. Contains the methods
 * to write the Page Object Model (POM).
 *
 */

public interface PageObjectWriter {

    void writeClass(String pageObjectsPath, String packageName);

    void writeVerifications(String verificationPath, String packageName);
}
