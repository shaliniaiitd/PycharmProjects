package com.epam.framework.ui.driver;

import org.openqa.selenium.WebDriver;

import java.util.Objects;


public class DriverDTO {

    private WebDriver driver;

    public DriverDTO() {
    }

    public DriverDTO(WebDriver driver) {
        this.driver = driver;
    }

    public WebDriver getDriver() {
        return driver;
    }

    public void setDriver(WebDriver driver) {
        this.driver = driver;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof DriverDTO)) return false;
        DriverDTO driver1 = (DriverDTO) o;
        return Objects.equals(driver, driver1.driver);
    }

    @Override
    public int hashCode() {
        return Objects.hash(driver);
    }
}
