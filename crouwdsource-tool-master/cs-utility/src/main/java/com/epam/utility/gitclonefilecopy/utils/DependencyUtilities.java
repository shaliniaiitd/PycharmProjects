package com.epam.utility.gitclonefilecopy.utils;

import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import org.apache.log4j.Logger;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import java.io.FileReader;
import java.util.Arrays;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import static com.epam.utility.gitclonefilecopy.constant.Constants.*;

@Component
public class DependencyUtilities {

    private static final Logger logger = Logger.getLogger(DependencyUtilities.class);
    private static final int NO_KEY = 0;

    private JsonObject languageObject;
    private JsonObject supportedTypesObject;

    @Autowired
    private FileUtilities fileUtilities;

    public void readDependencyConfigFile(String language) {
        JsonParser jsonParser;
        Object parserObjectVal;
        JsonObject supportedConfigObject;
        try (FileReader jsonReader = new FileReader(fileUtilities.getDependencyConfigFilePath())) {
            logger.info("Started reading dependency configuration json file!!");
            jsonParser = new JsonParser();
            parserObjectVal = jsonParser.parse(jsonReader);
            supportedConfigObject = (JsonObject) parserObjectVal;
            languageObject = (JsonObject) supportedConfigObject.get(language.toLowerCase().trim());
            logger.info("Dependency configuration read successfully!!");
        } catch (Exception e) {
            logger.fatal("Error while reading dependency configuration file: " + e.getMessage());
        }
    }

    public JsonObject getLanguageObject() {
        return languageObject;
    }

    public List<String> getSupportedTypesAsList(String type, JsonObject object) {
        Stream<String> supportedTypes = Arrays.stream(getSupportedTypes(type, object).split(COMMA_SEPARATOR));
        return supportedTypes.collect(Collectors.toList());
    }

    public JsonObject getObjectForSupportedElement(JsonObject object, String type) {
        JsonArray elementArrayForType = object.get(type).getAsJsonArray();
        JsonElement supportedTypeWithDependenciesElement = elementArrayForType.get(SECOND_ELEMENT);
        return supportedTypeWithDependenciesElement.getAsJsonObject();
    }

    public Map<String, List<String>> fetchArtifactIDWithRelatedNodes(JsonObject object, String category,
                                                                     String dependency) {
        String[] artifactIDAndNodeList;
        Map<String, List<String>> artifactWithNodeList = new LinkedHashMap<>();
        Map<String, JsonArray> dependenciesWithType = fetchDefaultAndSupportedTypeDependencies(object, category);
        if (!dependenciesWithType.isEmpty()) {
            JsonArray dependencyType = dependenciesWithType.get(dependency);
            if (dependencyType.size() > NO_ELEMENT) {
                for (int count = 0; count < dependencyType.size(); count++) {
                    artifactIDAndNodeList = splitArtifactIDAndRelatedNodes(dependencyType.get(count));
                    artifactWithNodeList.putAll(putArtifactIDWithRelatedNodes(artifactIDAndNodeList));
                }
            } else {
                logger.info("No Dependency type is available for Category: " + category + " and dependency: " + dependency);
            }
        }
        return artifactWithNodeList;
    }

    private JsonArray getJsonArrayFromJsonObject(JsonObject obj, String key) {
        return obj.get(key).getAsJsonArray();
    }

    private boolean isKeyExist(JsonObject object, String key) {
        long matchedKey = object.keySet().stream().filter(eachKey -> eachKey.equalsIgnoreCase(key)).count();
        return (matchedKey > NO_KEY);
    }

    private Map<String, JsonArray> putTypeWithDependenciesArray(JsonObject object, String type) {
        JsonObject dependenciesObject;
        JsonArray dependenciesArray;
        Map<String, JsonArray> dependency = new LinkedHashMap<>();
        dependenciesObject = getJsonArrayFromJsonObject(object, type).get(FIRST_ELEMENT).getAsJsonObject();
        dependenciesArray = dependenciesObject.get(TAG_DEPENDENCIES).getAsJsonArray();
        dependency.put(type, dependenciesArray);
        return dependency;
    }

    private Map<String, JsonArray> putEachTypeWithDependenciesArray(JsonObject object, String supportedType) {
        Map<String, JsonArray> dependency = new LinkedHashMap<>();
        String[] supportedList = supportedType.split(COMMA_SEPARATOR);
        int jsonArraySizeForType;
        for (String type : supportedList) {
            jsonArraySizeForType = getJsonArrayFromJsonObject(object, type).size();
            if (jsonArraySizeForType > NO_ELEMENT) {
                dependency.putAll(putTypeWithDependenciesArray(object, type));
            } else {
                logger.info("Please make sure " + type.toUpperCase() + " dependency is available!!");
            }
        }
        return dependency;
    }

    private Map<String, JsonArray> fetchDefaultAndSupportedTypeDependencies(JsonObject object, String type) {
        String supportedTypesAsString;
        Map<String, JsonArray> dependency = new LinkedHashMap<>();
        int jsonArraySizeForType;
        if (isKeyExist(object, type)) {
            jsonArraySizeForType = getJsonArrayFromJsonObject(object, type).size();
            if (jsonArraySizeForType > NO_ELEMENT) {
                dependency.putAll(putTypeWithDependenciesArray(object, type));
                if (jsonArraySizeForType > DEPENDENCY_ELEMENT) {
                    supportedTypesObject = getJsonArrayFromJsonObject(object, type).get(SECOND_ELEMENT).getAsJsonObject();
                    supportedTypesAsString = supportedTypesObject.get(TAG_SUPPORTED_LIST).getAsString();
                    dependency.putAll(putEachTypeWithDependenciesArray(supportedTypesObject, supportedTypesAsString));
                }
            } else {
                logger.warn("Please make sure platform dependencies and supported platform both are available!!");
            }
        } else {
            logger.info("Key " + type + " not present under object keys: " + object.keySet());
        }
        return dependency;
    }

    private String getSupportedTypes(String type, JsonObject object) {
        String supportedTypes = "";
        JsonArray objectArrayForType = getJsonArrayFromJsonObject(object, type);
        if (objectArrayForType.size() == OBJECT_SIZE_WITH_CHILD_AND_DEPENDENCY) {
            supportedTypesObject = objectArrayForType.get(SECOND_ELEMENT).getAsJsonObject();
            supportedTypes = supportedTypesObject.get(TAG_SUPPORTED_LIST).getAsString();
        } else {
            logger.warn("Please make sure for " + type + ", dependency and supported category both are available!!");
        }
        return supportedTypes;
    }

    private String getDependencyTagInnerText(JsonElement element) {
        // artifactId: json-simple, dependencyChildNodeList: groupId - artifactId -
        // version
        return element.getAsJsonObject().get(TAG_DEPENDENCY).getAsString();
    }

    private String[] splitArtifactIDAndRelatedNodes(JsonElement element) {
        return getDependencyTagInnerText(element).split(COMMA_SEPARATOR);
    }

    private Map<String, List<String>> putArtifactIDWithRelatedNodes(String[] childDependencyNodes) {
        Map<String, List<String>> artifactAndNodeMap = new LinkedHashMap<>();
        if (isChildDependencyNodeAvailable(childDependencyNodes)) {
            String artifactID = childDependencyNodes[FIRST_ELEMENT].split(COLON_SEPARATOR)[SECOND_ELEMENT];
            String childDependencyNodeDetail = childDependencyNodes[SECOND_ELEMENT].split(COLON_SEPARATOR)[SECOND_ELEMENT];
            String[] childDependencyNodeList = childDependencyNodeDetail.split(DASH_SEPARATOR);
            Stream<String> childNodes = Arrays.stream(childDependencyNodeList);
            List<String> childNodeList = childNodes.collect(Collectors.toList());
            artifactAndNodeMap.put(artifactID, childNodeList);
        }
        return artifactAndNodeMap;
    }

    private boolean isChildDependencyNodeAvailable(String[] childDependencyNodes) {
        return childDependencyNodes.length > EMPTY_STRING_ARRAY && !childDependencyNodes[FIRST_ELEMENT].isEmpty();
    }
}
