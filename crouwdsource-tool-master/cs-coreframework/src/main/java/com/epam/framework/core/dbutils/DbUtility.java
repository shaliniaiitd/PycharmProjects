package com.epam.framework.core.dbutils;

import com.epam.framework.core.TestContext;
import com.epam.framework.core.exceptions.DBUtilityException;
import com.epam.framework.core.exceptions.UnSupportedDBDriverException;
import com.epam.framework.core.logging.logger.CSLogger;
import com.epam.framework.core.logging.logger.LogLevel;
import org.apache.commons.dbutils.DbUtils;
import org.apache.commons.dbutils.QueryRunner;
import org.apache.commons.dbutils.handlers.ArrayListHandler;
import org.apache.commons.dbutils.handlers.MapListHandler;
import org.apache.commons.dbutils.handlers.ScalarHandler;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.Collections;
import java.util.List;
import java.util.Map;

public class DbUtility {
    CSLogger logger = TestContext.getLogger();
    
    private DBProperties dbProperties = new DBProperties();
    private Connection connection = getDBConnection();
    private static DbUtility instance;

    QueryRunner queryRunner = null;
    

    private DbUtility() {
        queryRunner = new QueryRunner();
    }

    public static synchronized DbUtility getInstance() {
        if (instance == null) {
            instance = new DbUtility();
        }
        return instance;
    }

    private Connection getDBConnection() {
        try {
            DbUtils.loadDriver(dbProperties.getDbDriver());
            logger.log(LogLevel.INFO, "Connecting to database...");
            return DriverManager.getConnection(dbProperties.getDbURL(), dbProperties.getDbUserName(), dbProperties.getDbPassword());
        } catch (SQLException sqlException) {
            throw new UnSupportedDBDriverException(dbProperties.getDbDriver() + " is unsupported!", sqlException);
        }
    }

    public List<Map<String, Object>> getAllRecordsFromTable(String tableName) {
        try {
            List<Map<String, Object>> maps = queryRunner.query(connection,
                    String.format("SELECT * FROM %s", tableName),
                    new MapListHandler());
            logger.log(LogLevel.INFO, "Records are : " + maps.toString());
            return maps;
        } catch (SQLException sqlException) {
            handleSQLException(sqlException);
        }
        return Collections.emptyList();
    }

    public List<Object[]> getListOfRecordsFromTable(String tableName) {
        try {
            List<Object[]> lists = queryRunner.query(connection,
                    String.format("SELECT * FROM %s", tableName),
                    new ArrayListHandler());
            logger.log(LogLevel.INFO, "Records are : " + lists.toString());
            return lists;
        } catch (SQLException sqlException) {
            handleSQLException(sqlException);
        }
        return Collections.emptyList();
    }

    public void updateRecordsInTable(String updateQuery) throws SQLException {
        int numRowsUpdated = queryRunner.update(connection, updateQuery);
        logger.log(LogLevel.INFO, "Records updated : " + numRowsUpdated);
    }

    public void deleteRecordsInTable(String deleteQuery) throws SQLException {
        int numRowsDeleted = queryRunner.update(connection, deleteQuery);
        logger.log(LogLevel.INFO, "Records deleted : " + numRowsDeleted);
    }

    public long findTableRecordsCount(String tableName) throws SQLException {
        ScalarHandler<Long> scalarHandler = new ScalarHandler<>();
        String query = "SELECT COUNT(*) FROM " + tableName;
        long count = queryRunner.query(connection, query, scalarHandler);
        logger.log(LogLevel.INFO, "No of records in table : " + count);
        return count;
    }

    public void insertTableRecords(String insertQuery) throws SQLException {
        int numRowsInserted = queryRunner.update(connection, insertQuery);
        logger.log(LogLevel.INFO, "Records inserted : " + numRowsInserted);
    }

    private void handleSQLException(SQLException sqlException) {
        throw new DBUtilityException(sqlException.getMessage(), sqlException);
    }
}
