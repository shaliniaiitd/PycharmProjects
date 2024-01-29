package com.epam.framework.ui.pageobjectgenerator.pojo;

public class Records {

    private String[] pageObjectNames;

    public Records() {}

    public Records(String[] records) {
        this.pageObjectNames = records;
    }

    public String[] getPageObjectNames() {
        return pageObjectNames;
    }

    public void setPageObjectNames(String[] pageObjectNames) {
        this.pageObjectNames = pageObjectNames;
    }
}
