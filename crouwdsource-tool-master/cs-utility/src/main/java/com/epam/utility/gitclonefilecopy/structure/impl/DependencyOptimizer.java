package com.epam.utility.gitclonefilecopy.structure.impl;

import com.epam.utility.gitclonefilecopy.structure.DependencyManager;
import com.epam.utility.gitclonefilecopy.utils.DependencyUtilities;
import com.epam.utility.gitclonefilecopy.models.ToolConfigBean;
import com.google.gson.JsonObject;
import org.apache.log4j.Logger;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import org.w3c.dom.Document;
import org.w3c.dom.NodeList;

import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import static com.epam.utility.gitclonefilecopy.constant.Constants.*;

@Component
public class DependencyOptimizer extends DependencyManager {

    private static final Logger logger = Logger.getLogger(DependencyOptimizer.class);
    private JsonObject languageObject;

    @Autowired
    private DependencyUtilities dependencyUtilities;

    @Override
    public ArrayList<Integer> fetchDeletedPlatformChildDependencySequence(ToolConfigBean toolConfigBean, Document document) {
        languageObject = dependencyUtilities.getLanguageObject();
        String userDefinedPlatforms = toolConfigBean.getPlatform();
        return deleteChildNodesOfDependency(document, userDefinedPlatforms, fetchSupportedPlatformList(), TAG_PLATFORM);
    }

    @Override
    public ArrayList<Integer> fetchDeletedTestModelChildDependencySequence(ToolConfigBean toolConfigBean, Document document) {
        String userDefinedTestModel = toolConfigBean.getTestModel();
        return deleteChildNodesOfDependency(document, userDefinedTestModel, fetchSupportedTestModelList(), TAG_TEST_MODEL);
    }

    @Override
    public ArrayList<Integer> fetchDeletedEngineChildDependencySequence(ToolConfigBean toolConfigBean, Document document) {
        String userDefinedEngine = toolConfigBean.getEngine();
        return deleteChildNodesOfDependency(document, userDefinedEngine, fetchSupportedEngineList(), TAG_ENGINE);
    }
    
    @Override
	public ArrayList<Integer> fetchDeletedDbChildDependencySequence(ToolConfigBean toolConfigBean, Document document) {
    	 String userDefinedDb= toolConfigBean.getDb();
         return deleteChildNodesOfDependency(document, userDefinedDb, fetchSupportedDbList(), TAG_DB);
	}

    public List<String> fetchSupportedDbList() {
        return dependencyUtilities.getSupportedTypesAsList(TAG_DB, languageObject);
    }
    
    public List<String> fetchSupportedPlatformList() {
        return dependencyUtilities.getSupportedTypesAsList(TAG_PLATFORM, languageObject);
    }

    public List<String> fetchSupportedTestModelList() {
        return dependencyUtilities.getSupportedTypesAsList(TAG_TEST_MODEL, languageObject);
    }

    public List<String> fetchSupportedEngineList() {
        JsonObject platformObject = dependencyUtilities.getObjectForSupportedElement(languageObject, TAG_PLATFORM);
        List<String> supportedTypeForUI = dependencyUtilities.getSupportedTypesAsList(TAG_UI, platformObject);
        List<String> supportedTypeForAPI = dependencyUtilities.getSupportedTypesAsList(TAG_API, platformObject);
        List<String> supportedTypeForMobile = dependencyUtilities.getSupportedTypesAsList(TAG_MOBILE, platformObject);

        List<String> supportedEngineList = new ArrayList<>();
        supportedEngineList.addAll(supportedTypeForUI);
        supportedEngineList.addAll(supportedTypeForAPI);
        supportedEngineList.addAll(supportedTypeForMobile);
        return supportedEngineList;
    }

    private ArrayList<Integer> deleteChildNodesOfDependency(Document document, String userSelectedTypes, List<String> defaultSupportedList, String type) {
        Stream<String> userSelectedTypesInLowerCase = Arrays.stream(userSelectedTypes.split(COMMA_SEPARATOR)).map(String::toLowerCase);
        List<String> userSelectedList = userSelectedTypesInLowerCase.collect(Collectors.toList());
        defaultSupportedList.removeAll(userSelectedList);
        return type.equalsIgnoreCase(TAG_ENGINE) ?
                deleteFutileNodesByType(document, defaultSupportedList, null, TAG_PLATFORM) :
                deleteFutileNodesByType(document, defaultSupportedList, userSelectedList, type);
    }

    private ArrayList<Integer> deleteFutileNodesByType(Document document, List<String> futileSupportedList,
                                                       List<String> userDefinedList, String category) {
        ArrayList<Integer> dependencySequence = new ArrayList<>();
        if (!futileSupportedList.isEmpty()) {
            NodeList dependencyNodeList = document.getElementsByTagName(TAG_DEPENDENCY);
            ArrayList<Integer> deletedNodeSequence;
            if (Optional.ofNullable(userDefinedList).isPresent()) { //Refactoring required as validating with Null
                if (userDefinedList.isEmpty()) {
                    deletedNodeSequence = deleteAllNodeUnderCategory(dependencyNodeList, category);
                } else {
                    deletedNodeSequence = deleteNodeFromFutileList(futileSupportedList, dependencyNodeList, category);
                }
            } else {
                deletedNodeSequence = deleteNodesForSupportedTypeOfCategory(futileSupportedList, dependencyNodeList, category);
            }
            dependencySequence.addAll(deletedNodeSequence);
        } else {
            logger.warn("User selected all type of " + category + "!!");
        }
        return dependencySequence;
    }

    private ArrayList<Integer> deleteNodeFromFutileList(List<String> futileSupportedList, NodeList dependencyNodeList, String category) {
        ArrayList<Integer> dependencySequence = new ArrayList<>();
        Map<String, List<String>> artifactIDWithNodeList;
        for (String type : futileSupportedList) {
            artifactIDWithNodeList = dependencyUtilities.fetchArtifactIDWithRelatedNodes(languageObject, category, type);
            dependencySequence.addAll(removeNode(dependencyNodeList, artifactIDWithNodeList));
        }
        return dependencySequence;
    }

    private ArrayList<Integer> deleteAllNodeUnderCategory(NodeList nodeList, String category) {
        ArrayList<Integer> dependencySequence;
        Map<String, List<String>> artifactIDWithNodeList = dependencyUtilities.fetchArtifactIDWithRelatedNodes(languageObject, category, category);
        dependencySequence = removeNode(nodeList, artifactIDWithNodeList);
        return dependencySequence;
    }

    private ArrayList<Integer> deleteNodesForSupportedTypeOfCategory(List<String> futileSupportedList, NodeList dependencyNodeList, String category) {
        ArrayList<Integer> dependencySequence = new ArrayList<>();
        JsonObject categoryObject;
        JsonObject childOfCategoryObject;
        Map<String, List<String>> artifactIDWithNodeList;
        List<String> defaultSupportedList = dependencyUtilities.getSupportedTypesAsList(category, languageObject);
        for (String supportedType : defaultSupportedList) {
            for (String futileType : futileSupportedList) {
                categoryObject = dependencyUtilities.getObjectForSupportedElement(languageObject, category);
                childOfCategoryObject = dependencyUtilities.getObjectForSupportedElement(categoryObject, supportedType);
                artifactIDWithNodeList = dependencyUtilities.fetchArtifactIDWithRelatedNodes(childOfCategoryObject, futileType, futileType);
                dependencySequence.addAll(removeNode(dependencyNodeList, artifactIDWithNodeList));
            }
        }
        return dependencySequence;
    }
}
