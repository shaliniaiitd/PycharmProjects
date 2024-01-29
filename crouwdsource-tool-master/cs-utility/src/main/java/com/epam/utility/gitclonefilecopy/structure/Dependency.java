package com.epam.utility.gitclonefilecopy.structure;

import com.epam.utility.gitclonefilecopy.models.ToolConfigBean;
import org.w3c.dom.Document;

import java.util.ArrayList;

public interface Dependency {

	ArrayList<Integer> fetchDeletedPlatformChildDependencySequence(ToolConfigBean toolConfigBean, Document document);

	ArrayList<Integer> fetchDeletedTestModelChildDependencySequence(ToolConfigBean toolConfigBean, Document document);

	ArrayList<Integer> fetchDeletedEngineChildDependencySequence(ToolConfigBean toolConfigBean, Document document);
	
	ArrayList<Integer> fetchDeletedDbChildDependencySequence(ToolConfigBean toolConfigBean, Document document);

	void createPomFile(Document document, String newFilePath);

	void removeFutileDependencies(Document document, ArrayList<Integer> dependencySequence);
}
