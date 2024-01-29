package com.epam.utility.gitclonefilecopy.utils;

import org.apache.log4j.Logger;
import org.eclipse.jgit.api.Git;
import org.eclipse.jgit.api.TransportConfigCallback;
import org.eclipse.jgit.api.errors.GitAPIException;
import org.eclipse.jgit.transport.CredentialsProvider;
import org.eclipse.jgit.transport.UsernamePasswordCredentialsProvider;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

import java.io.File;
import java.util.function.Function;

@Component
public class GitUtilities {

    private static final Logger logger = Logger.getLogger(GitUtilities.class);

    @Value("${collab.git.user.name}")
    private String gitUsername;

    @Value("${collab.git.user.password}")
    private String gitPassword;

    @Value("${collab.git.repo.https.url}")
    private String gitRepoHttpsUrl;

    @Value("${collab.git.repo.ssh.url}")
    private String gitRepoSshUrl;

    @Value("${collab.git.repo.branch.name}")
    private String gitBranchName;

    @Autowired
    private FileUtilities fileUtilities;

    public void cloneMasterBranchWithHttps() {
        logger.info("Trying to clone master branch from git with Https");
        logger.info("username: " + gitUsername);
        try {
            CredentialsProvider cp = new UsernamePasswordCredentialsProvider(gitUsername, gitPassword);
            Git.cloneRepository()
                    .setURI(getUrlEncodedWithGitlabAccessToken(gitRepoHttpsUrl))
                    .setCredentialsProvider(cp)
                    .setDirectory(new File(fileUtilities.getTempDirectoryPath()))
                    .setBranch(gitBranchName)
                    .call().getRepository()
                    .close();

            logger.info("Cloned master branch from git - using HTTPS");
        } catch (GitAPIException e) {
            logger.error("Unable to clone the repository", e);
        }
    }

    public void cloneMasterBranchWithSSH() {
        logger.info("Trying to clone master branch from git with SSH");
        TransportConfigCallback transportConfigCallback = new SshTransportConfigCallback();
        try {
            Git.cloneRepository()
                    .setURI(gitRepoSshUrl)
                    .setTransportConfigCallback(transportConfigCallback)
                    .setDirectory(new File(fileUtilities.getTempDirectoryPath()))
                    .setBranch(gitBranchName)
                    .call().getRepository()
                    .close();

            logger.info("Cloned master branch from git - using SSH");
        } catch (GitAPIException e) {
            logger.error("Unable to clone the repository", e);
        }
    }

    private String getUrlEncodedWithGitlabAccessToken(String originalHttpsUrl) {
        String httpsLiteral = "https://";
        Function<String, String> replaceHttps =
                s -> s.startsWith(httpsLiteral) ? s.replace(httpsLiteral, "") : s;

        String accessTokenLiteral = "gitlab-ci-token:" + gitPassword.trim() + "@";
        String trimmedUrl = replaceHttps.apply(originalHttpsUrl);
        return httpsLiteral + accessTokenLiteral + trimmedUrl;
    }
}
