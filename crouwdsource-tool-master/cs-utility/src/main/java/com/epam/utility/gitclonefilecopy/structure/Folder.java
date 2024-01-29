package com.epam.utility.gitclonefilecopy.structure;

import com.epam.utility.gitclonefilecopy.models.ToolConfigBean;
import com.epam.utility.gitclonefilecopy.utils.FileUtilities;

import java.util.function.BiPredicate;

public interface Folder {

	BiPredicate<String, String> validate = String::equalsIgnoreCase;

	void moveFilesAndDirectories(FileUtilities fileUtilities, ToolConfigBean toolConfig);
}
