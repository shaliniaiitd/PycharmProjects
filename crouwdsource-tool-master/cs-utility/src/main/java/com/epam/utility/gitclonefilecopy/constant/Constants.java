package com.epam.utility.gitclonefilecopy.constant;

import com.epam.utility.gitclonefilecopy.structure.exceptions.NoObjectException;

import java.io.File;

public class Constants {

	private Constants(){
		throw new NoObjectException("Not allowed to create object for Constants class");
	}

	public static final String COMMAND_CHANGE_DIRECTORY = "cd ";
	public static final String COMMAND_MAVEN_BUILD = "mvn clean compile";

	public static final String POM_FILE = "pom.xml";
	public static final String TEMP_FOLDER_FOR_POM = "temppom";
	public static final String NEW_FOLDER_WITH_POM_FILE = TEMP_FOLDER_FOR_POM + File.separator + POM_FILE;

	public static final String COLON_SEPARATOR = ":";
	public static final String DASH_SEPARATOR = "-";
	public static final String COMMA_SEPARATOR = ",";
	public static final String DOT_SIGN = ".";
	public static final String NEW_LINE = "\n";
	public static final int FIRST_ELEMENT = 0;
	public static final int SECOND_ELEMENT = 1;
	public static final int NO_ELEMENT = 0;
	public static final int DEPENDENCY_ELEMENT = 1;
	public static final int OBJECT_SIZE_WITH_CHILD_AND_DEPENDENCY = 2;
	public static final int EMPTY_STRING_ARRAY = 0;

	public static final String TAG_JAVA = "java";
	public static final String TAG_DEFAULT_FOLDER = "defaultFolder";
	public static final String TAG_UI = "ui";
	public static final String TAG_UI_DEFAULT_FOLDER = "uiDefaultFolder";
	public static final String TAG_SELENIUM = "selenium";
	public static final String TAG_API = "api";
	public static final String TAG_API_DEFAULT_FOLDER = "apiDefaultFolder";
	public static final String TAG_HTTPCLIENT = "httpclient";
	public static final String TAG_MOBILE = "mobile";
	public static final String TAG_MOBILE_DEFAULT_FOLDER = "mobileDefaultFolder";
	public static final String TAG_APPIUM = "appium";
	public static final String TAG_TEST_MODEL = "testmodel";
	public static final String TAG_DB = "db";
	public static final String TAG_DB_UTILITY = "dbUtils";
	public static final String TAG_TESTNG = "testng";
	public static final String TAG_CUCUMBER = "cucumber";
	public static final String TAG_REPORTING = "logging";
	public static final String TAG_LOGGING = "reporting";
	public static final String TAG_PYTHON = "python";
	public static final String TAG_DOTNET = "dotnet";

	public static final String TAG_PLATFORM = "platform";
	public static final String TAG_DEPENDENCIES = "dependencies";
	public static final String TAG_DEPENDENCY = "dependency";
	public static final String TAG_SUPPORTED_LIST = "supportedlist";
	public static final String TAG_VALUE_ARTIFACT_ID = "artifactId";
	public static final String TAG_ENGINE = "engine";

	public static final String LANGUAGE_JAVA = "java";
	public static final String LANGUAGE_PYTHON = "python";
	public static final String LANGUAGE_DOTNET = "dotnet";
	public static final String PLATFORM_UI = "ui";
	public static final String PLATFORM_API = "api";
	public static final String PLATFORM_MOBILE = "mobile";
	public static final String ENGINE_SELENIUM = "selenium";
	public static final String ENGINE_HTTPCLIENT = "httpclient";
	public static final String ENGINE_APPIUM = "appium";
	public static final String TESTMODEL_TESTNG = "testng";
	public static final String TESTMODEL_CUCUMBER = "cucumber";
	public static final String LOGGER_LOG4J = "log4j";
	public static final String LOGGER_SLF4J = "slf4j";
	public static final String REPORTER_EXTENT_REPORT = "extentreport";
	public static final String REPORTER_REPORT_PORTAL = "portalreport";

	public static final String DIRECTORY_CREATE = "create directory";
	public static final String DIRECTORY_CLONE = "clone directory";
	public static final String DIRECTORY_DELETE = "delete directory";

	public static final String CLONING_BRANCH_MASTER = "master";
}
