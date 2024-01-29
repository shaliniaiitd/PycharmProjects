package com.epam.utility.gitclonefilecopy.services;

import com.epam.utility.gitclonefilecopy.models.ToolConfigBean;
import org.springframework.core.io.Resource;

public interface CloneGitRepo {

    String getProjectFromCloud(ToolConfigBean toolConfig);

    Resource getProject(ToolConfigBean toolConfig);
}
