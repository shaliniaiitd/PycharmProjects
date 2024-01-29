package com.epam.framework.core.utils;

import com.epam.framework.core.constants.MessageConstants;

import java.text.SimpleDateFormat;
import java.time.*;
import java.time.format.DateTimeFormatter;
import java.util.Calendar;
import java.util.Date;
import java.util.TimeZone;

public class DateUtils {

    private DateUtils(){

    }

    public static LocalTime getTime() {
        return LocalTime.now();
    }

    public static LocalDate getCurrentDate() {
        return LocalDate.now();
    }

    public static LocalDateTime getCurrentDateTime() {
        return LocalDateTime.now();
    }

    public static long currentTimeMillis() {
        return System.nanoTime() / 1000000;
    }

    public static String getDateStringFormat(Date date) {
        if (date != null) {
            return new SimpleDateFormat("yyyy-MM-dd HH:mm:ss").format(date);
        } else {
            return "0000-00-00 00:00:00";
        }
    }

    public static String getDateStringFormat(LocalDate date) {
        if (date != null) {
            return date.format(DateTimeFormatter.ofPattern("dd/MM/yyyy"));
        } else {
            return "0000-00-00 00:00:00";
        }
    }

    public static boolean isSameDay(LocalDate date1, LocalDate date2) {
        if (date1 == null || date2 == null) {
            throw new IllegalArgumentException(MessageConstants.DATE_NULL_ERROR_MESSAGE);
        }
        return date1.isEqual(date2);
    }


    public static boolean isSameDay(Date date1, Date date2) {
        if (date1 == null || date2 == null) {
            throw new IllegalArgumentException(MessageConstants.DATE_NULL_ERROR_MESSAGE);
        }
        Calendar cal1 = Calendar.getInstance();
        cal1.setTime(date1);
        Calendar cal2 = Calendar.getInstance();
        cal2.setTime(date2);
        return isSameDay(cal1, cal2);
    }

    public static boolean isSameDay(Calendar cal1, Calendar cal2) {
        if (cal1 == null || cal2 == null) {
            throw new IllegalArgumentException(MessageConstants.DATE_NULL_ERROR_MESSAGE);
        }
        return (cal1.get(Calendar.ERA) == cal2.get(Calendar.ERA)
                && cal1.get(Calendar.YEAR) == cal2.get(Calendar.YEAR) && cal1
                .get(Calendar.DAY_OF_YEAR) == cal2
                .get(Calendar.DAY_OF_YEAR));
    }

    public static Date max(Date d1, Date d2) {
        if (d1 == null && d2 == null)
            return null;
        if (d1 == null)
            return d2;
        if (d2 == null)
            return d1;
        return (d1.after(d2)) ? d1 : d2;
    }

    public static LocalDate max(LocalDate d1, LocalDate d2) {
        if (d1 == null && d2 == null)
            return null;
        if (d1 == null)
            return d2;
        if (d2 == null)
            return d1;
        return (d1.isAfter(d2)) ? d1 : d2;
    }

    public static LocalDate min(LocalDate d1, LocalDate d2) {
        if (d1 == null && d2 == null)
            return null;
        if (d1 == null)
            return d2;
        if (d2 == null)
            return d1;
        return (d1.isBefore(d2)) ? d1 : d2;
    }


    public static Date min(Date d1, Date d2) {
        if (d1 == null && d2 == null)
            return null;
        if (d1 == null)
            return d2;
        if (d2 == null)
            return d1;
        return (d1.before(d2)) ? d1 : d2;
    }

    public static String getCurrentTime() {
        Calendar calendar = Calendar.getInstance();
        SimpleDateFormat simpleDateFormat = new SimpleDateFormat("HH:mm:ss yyyy-MM-dd");
        return simpleDateFormat.format(calendar.getTime());
    }

    public static String addDays(int days) {
        SimpleDateFormat simpleDateFormat = new SimpleDateFormat("dd/MM/yyyy");
        Calendar calendar = Calendar.getInstance();
        calendar.setTime(new Date());
        calendar.add(Calendar.DATE, days);
        return simpleDateFormat.format(calendar.getTime());
    }

    public static ZonedDateTime zonedDateTime(String date) {
        LocalDate localDate = LocalDate.parse(date);
        return localDate.atStartOfDay(ZoneId.systemDefault());
    }

    public static TimeZone timeZone() {
        Calendar now = Calendar.getInstance();
        return now.getTimeZone();
    }

    public static String timeZoneName() {
     return timeZone().getDisplayName();
    }

    public static String timeZoneId() {
        return timeZone().getID();
    }

    public static LocalDate localDate(ZoneId zoneId) {
        return LocalDate.now( zoneId );
    }




}
