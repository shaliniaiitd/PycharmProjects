package com.epam.utility.gitclonefilecopy.controllers;

import com.epam.utility.gitclonefilecopy.models.ToolConfigBean;
import com.epam.utility.gitclonefilecopy.services.CloneGitRepo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.io.Resource;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import java.util.HashMap;
import java.util.Map;

@RestController
public class CollabController {

    @Autowired()
    private CloneGitRepo cloneGitRepo;

    @PostMapping(value = "/download", produces = MediaType.APPLICATION_JSON_VALUE)
    public ResponseEntity<Object> getProjectDataFromCloud(@RequestBody ToolConfigBean toolConfig) {
        String response = cloneGitRepo.getProjectFromCloud(toolConfig);
        Map<String, String> map = new HashMap<>();
        if (response != null) {
            map.put("fileUrl", response);
            return new ResponseEntity<>(map, HttpStatus.OK);
        }
        return null;
    }

    @PostMapping(value = "/download/v2", produces = MediaType.APPLICATION_OCTET_STREAM_VALUE)
    public ResponseEntity<Object> getProjectData(@RequestBody ToolConfigBean toolConfig) {
        Resource response = cloneGitRepo.getProject(toolConfig);
        if (response != null) {
            return ResponseEntity.ok()
                    .contentType(MediaType.parseMediaType(MediaType.APPLICATION_OCTET_STREAM_VALUE))
                    .header(HttpHeaders.CONTENT_DISPOSITION, "attachment; filename=\"" + response.getFilename() + "\"")
                    .body(response);
        }
        return null;
    }
}
