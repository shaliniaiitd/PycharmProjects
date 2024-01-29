package com.epam.utility.gitclonefilecopy.services.impl;

import com.azure.storage.blob.BlobClient;
import com.azure.storage.blob.BlobContainerClient;
import com.azure.storage.blob.BlobServiceClient;
import com.azure.storage.blob.BlobServiceClientBuilder;
import com.epam.utility.gitclonefilecopy.models.ToolConfigBean;
import com.epam.utility.gitclonefilecopy.services.CloneGitRepo;
import com.epam.utility.gitclonefilecopy.structure.factory.FolderFactory;
import com.epam.utility.gitclonefilecopy.utils.FileUtilities;
import com.epam.utility.gitclonefilecopy.utils.GitUtilities;
import com.epam.utility.gitclonefilecopy.utils.ZipUtilities;
import org.apache.log4j.Logger;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.core.io.Resource;
import org.springframework.core.io.UrlResource;
import org.springframework.stereotype.Service;
import java.io.File;
import java.net.MalformedURLException;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Objects;

@Service
public class CloneGitRepoImpl implements CloneGitRepo {

    private static final Logger logger = Logger.getLogger(CloneGitRepoImpl.class);

    @Value("${collab.azure.blob.container.name}")
    private String containerName;

    @Value("${collab.azure.blob.connection.string}")
    private String connectionString;

    @Autowired
    private GitUtilities gitUtilities;

    @Autowired
    private FileUtilities fileUtilities;

    @Autowired
    private ZipUtilities zipUtilities;

    @Autowired
    private FolderFactory folderFactory;

    @Override
    public String getProjectFromCloud(ToolConfigBean toolConfig) {
        this.createProjectZipFile(toolConfig);
        String fileUrl = this.uploadFileToCloudStorage();
        fileUtilities.removeDirectories();
        return fileUrl;
    }

    @Override
    public Resource getProject(ToolConfigBean toolConfig) {
        this.createProjectZipFile(toolConfig);
        Resource resource = this.getResource();
        fileUtilities.removeDirectories();
        return resource;
    }

    private void createProjectZipFile(ToolConfigBean toolConfig) {
        String language = toolConfig.getLanguage();
        String downloadFolderPath = fileUtilities.getDownloadFolderPath();
        fileUtilities.updateSourcePathBasedOnLanguage(language);
        fileUtilities.setupDirectories(downloadFolderPath);
        gitUtilities.cloneMasterBranchWithHttps();
        folderFactory.moveRequiredFiles(toolConfig);
        fileUtilities.removeTempDirectory();
        zipUtilities.createZipFile(downloadFolderPath);
    }

    private Resource getResource() {
        Path path = Paths.get(fileUtilities.getDownloadFileName());
        Resource resource = null;
        try {
            logger.info("creating a URL resource for the zip file");
            resource = new UrlResource(path.toUri());
        } catch (MalformedURLException e) {
            e.printStackTrace();
        }
        return resource;
    }

    private String uploadFileToCloudStorage() {
        BlobServiceClient blobServiceClient = new BlobServiceClientBuilder().connectionString(connectionString).buildClient();
        BlobContainerClient containerClient = blobServiceClient.getBlobContainerClient(containerName);
        File originalFile = new File(fileUtilities.getDownloadFileName());
        File uniqueFile = fileUtilities.getRandomFileName();

        boolean isRenameSuccess = originalFile.renameTo(uniqueFile);
        BlobClient blobClient = null;
        if (isRenameSuccess) {
            blobClient = containerClient.getBlobClient(uniqueFile.getName());
            blobClient.uploadFromFile(uniqueFile.getName());
        }
        return Objects.requireNonNull(blobClient).getBlobUrl();
    }


}
