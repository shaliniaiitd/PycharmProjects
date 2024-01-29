package com.epam.utility.gitclonefilecopy.structure;

import org.apache.log4j.Logger;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;

import javax.xml.XMLConstants;
import javax.xml.transform.OutputKeys;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;
import java.io.File;
import java.util.*;
import java.util.function.BiConsumer;
import java.util.function.BiPredicate;
import java.util.stream.Collectors;
import static com.epam.utility.gitclonefilecopy.constant.Constants.*;

public abstract class DependencyManager implements Dependency {

    private static final Logger logger = Logger.getLogger(DependencyManager.class);

    @Override
    public void removeFutileDependencies(Document document, ArrayList<Integer> dependencySequence) {
        if (Optional.ofNullable(dependencySequence).isPresent()) {
            sortArrayList(dependencySequence);
            Node dependenciesNode = getNodeObjectFromDocument(document, TAG_DEPENDENCIES, FIRST_ELEMENT);
            removeDependencyTagsIfEmpty(dependenciesNode, dependencySequence);
        }
    }

    @Override
    public void createPomFile(Document document, String newFilePath) {
        try {
            document.getDocumentElement().normalize();
            TransformerFactory transformerFactory = TransformerFactory.newInstance();
            transformerFactory.setAttribute(XMLConstants.ACCESS_EXTERNAL_DTD, "");
            transformerFactory.setAttribute(XMLConstants.ACCESS_EXTERNAL_STYLESHEET, "");
            Transformer transformer = transformerFactory.newTransformer();
            DOMSource sourceFile = new DOMSource(document);
            StreamResult destinationFile = new StreamResult(new File(newFilePath));
            transformer.setOutputProperty(OutputKeys.INDENT, "yes");
            transformer.transform(sourceFile, destinationFile);
        } catch (Exception e) {
            logger.fatal("Error while POM File creation: " + e.getMessage());
        }
    }

    private void sortArrayList(ArrayList<Integer> dependencySequence) {
        dependencySequence.sort(Comparator.reverseOrder());
    }

    private NodeList getNodeListFromDocument(Document document, String tagName) {
        return document.getElementsByTagName(tagName);
    }

    private Node getNodeObjectFromDocument(Document document, String tagName, int number) {
        NodeList nodeList = getNodeListFromDocument(document, tagName);
        return nodeList.item(number);
    }

    private Node getNodeObjectFromElement(Element element, String tagName, int number) {
        return element.getElementsByTagName(tagName).item(number);
    }

    private String getInnerTextOfNode(Node node) {
        return node.getTextContent();
    }

    private String getInnerTextOfElement(Element element) {
        return element.getTextContent();
    }

    private void removeDependencyTagsIfEmpty(Node node, ArrayList<Integer> dependencySequence) {
        if (node.getNodeType() == Node.ELEMENT_NODE) {
            Element dependencyAsChildElement = (Element) node;
            for (int count : dependencySequence) {
                Node dependencyNodeWithNoBody = getNodeObjectFromElement(dependencyAsChildElement, TAG_DEPENDENCY, count);
                String nodeInnerText = getInnerTextOfNode(dependencyNodeWithNoBody).trim();
                if (nodeInnerText.equalsIgnoreCase("")) {
                    dependencyAsChildElement.removeChild(dependencyNodeWithNoBody);
                }
            }
        }
    }

    private final BiConsumer<Element, List<String>> removeChildNodes = (element, chileNodeList) -> {
        for (String chileNode : chileNodeList) {
            Node node = element.getElementsByTagName(chileNode.trim()).item(FIRST_ELEMENT);
            element.removeChild(node);
        }
    };

    protected BiPredicate<Element, String> isChildNodeExist = (element, artifactIDValue) -> {
        boolean textNotEmpty = !getInnerTextOfElement(element).trim().isEmpty();
        boolean compareText = false;
        Node node = getNodeObjectFromElement(element, TAG_VALUE_ARTIFACT_ID, FIRST_ELEMENT);
        if(textNotEmpty){
            compareText = getInnerTextOfNode(node).trim().equalsIgnoreCase(artifactIDValue.trim());
        }
        return textNotEmpty && compareText;
    };


    private List<String> getArtifactIDInList(Set<Map.Entry<String, List<String>>> artifactSet) {
        return artifactSet.stream().map(Map.Entry::getKey).collect(Collectors.toList());
    }

    private List<List<String>> getListOfChildNodesInList(Set<Map.Entry<String, List<String>>> artifactSet) {
        return artifactSet.stream().map(Map.Entry::getValue).collect(Collectors.toList());
    }

    private ArrayList<Integer> removeChildNodeForDependencyTag(Node node, int nodeNumber, List<String> artifactList,
                                                               List<List<String>> chileNodeList) {
        ArrayList<Integer> sequence = new ArrayList<>();
        Element dependencyElement = (Element) node;
        for (int i = 0; i < artifactList.size(); i++) {
            if (isChildNodeExist.test(dependencyElement, artifactList.get(i))) {
                removeChildNodes.accept(dependencyElement, chileNodeList.get(i));
            } else {
                continue;
            }
            sequence.add(nodeNumber);
        }
        return sequence;
    }

    protected ArrayList<Integer> removeNode(NodeList dependencyNodeList, Map<String, List<String>> artifactMap) {

        ArrayList<Integer> dependencySequence = new ArrayList<>();
        if (!artifactMap.isEmpty()) {
            Set<Map.Entry<String, List<String>>> artifactSet = artifactMap.entrySet();
            List<String> artifactList = getArtifactIDInList(artifactSet);
            List<List<String>> chileNodeList = getListOfChildNodesInList(artifactSet);
            for (int count = 0; count < dependencyNodeList.getLength(); count++) {
                Node dependencyNode = dependencyNodeList.item(count);
                if (dependencyNode.getNodeType() == Node.ELEMENT_NODE) {
                    dependencySequence.addAll(removeChildNodeForDependencyTag(dependencyNode, count, artifactList, chileNodeList));
                }
            }
        }
        return dependencySequence;
    }
}
