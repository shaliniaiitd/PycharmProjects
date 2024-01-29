package com.epam.framework.ui.pageobjectgenerator;

/*
 * This class calls helper to read a file and write objects based on language from config properties.
 * languageType java or python.
 */

import com.epam.framework.ui.pageobjectgenerator.helper.HelperReadJsonAndCreateClass;

public class Runner {
    public static void main(String[] strings) {
        HelperReadJsonAndCreateClass helperReadJsonAndCreateClass = new HelperReadJsonAndCreateClass();
        helperReadJsonAndCreateClass.cleanRecordDirectory();
        helperReadJsonAndCreateClass.readJSON();
    }
}