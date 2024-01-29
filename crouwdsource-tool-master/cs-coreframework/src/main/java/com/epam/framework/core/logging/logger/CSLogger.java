package com.epam.framework.core.logging.logger;

public interface CSLogger {

    public void log(String message);

    public void log(Object object);

    public void log(LogLevel level, String message);

    public void log(LogLevel level, Object object);


}
