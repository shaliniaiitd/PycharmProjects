package com.epam.utility.gitclonefilecopy.models;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class ToolConfigBean {

    private String language;
    private String platform;
    private String engine;
    private String testModel;
    private String logger;
    private String reporter;
    private String db;
}
