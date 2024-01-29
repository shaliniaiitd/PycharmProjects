package com.epam.framework.core.utils;

import org.apache.commons.lang3.RandomStringUtils;

import java.security.SecureRandom;
import java.util.Base64;

public class StringUtils {

    private StringUtils(){

    }

    public static boolean isBlank(String input) {

        return (isEmpty(input) || input.matches("^\\s*$"));
    }

    public static boolean isNotEmpty(String input) {
        return ((input != null) && (input.length() > 0));
    }

    public static boolean isEmpty(String input) {
        return (input == null || input.isEmpty());
    }

    public static String toSnakeCase(String input) {
        return isBlank(input) ? input : input.replaceAll(" ", "_");
    }

    public static int length(String input) {
        return input != null ? input.length() : -1;
    }

    public static String reverse(String input) {
        return isBlank(input) ? input : new StringBuilder().append(input).reverse().toString();
    }

    public static String toKebabCase(String input) {
        return isBlank(input) ? input : input.replaceAll(" ", "-");
    }

    public static boolean contains(String input, String searchStr, boolean ignoreCase) {
        if (input == null || searchStr == null) {
            return false;
        }
        return ignoreCase ? input.toLowerCase().contains(searchStr.toLowerCase())
                : input.contains(searchStr);
    }

    public static String getFileExtension(String path) {
        int lastDot = path.lastIndexOf('.');
        if (lastDot > -1) {
            return path.substring(lastDot + 1);
        }
        return "";
    }

    public static int countLines(String input) {
        if (isEmpty(input)) {
            return 0;
        }
        return input.split("\n").length;
    }

    public static String upperCase(String input) {
        if (isEmpty(input)) {
            return null;
        }
        return input.toUpperCase();
    }

    public static String lowerCase(String input) {
        if (isEmpty(input)) {
            return null;
        }
        return input.toLowerCase();
    }

    public static String rightPad(String input, int length, char pad) {
        if (input.length() < length) {
            StringBuilder sb = new StringBuilder();
            sb.append(input);
            for (int i = 0, len = length - input.length(); i < len; i++) {
                sb.append(pad);
            }
            return sb.toString();
        }
        return input;
    }

    public static String leftPad(String input, int length, char pad) {
        if (input.length() < length) {
            StringBuilder sb = new StringBuilder();
            for (int i = 0, len = length - input.length(); i < len; i++) {
                sb.append(pad);
            }
            sb.append(input);
            return sb.toString();
        }
        return input;
    }

    public static String arrayToString(String[] input) {
        if (input.length == 0) {
            return "";
        }
        StringBuilder sb = new StringBuilder();
        sb.append(input[0]);
        for (int i = 1; i < input.length; i++) {
            sb.append(",");
            sb.append(input[i]);
        }
        return sb.toString();
    }

    public static String randomAlphaNumericString(int length) {
        return RandomStringUtils.random(length,0,0,true,true,null,new SecureRandom());
    }

    public static String randomAlphabeticString(int length) {
        return RandomStringUtils.random(length,0,0,true,false,null,new SecureRandom());
    }

    public static String base64Encode(String input) {
        if (input == null) {
            return null;
        }
        return Base64.getEncoder().encodeToString(input.getBytes());
    }

    public static String base64Decode(String encoded) {
        if (encoded == null) {
            return null;
        }
        return new String(Base64.getDecoder().decode(encoded.getBytes()));
    }

    public static String replaceAll(String input, String target, String replacement) {
        if (target == null || replacement == null)
            return null;
        return input != null ? input.replace(target, replacement) : null;
    }

    public static String toCamelCase(String input, String regex) {
        if (input == null || regex == null)
            return null;
        return toCamelCase(input, regex, false);
    }

    public static String toCamelCase(String input, String regex, boolean capitalizeFirst) {
        String[] split = input.split(regex);
        StringBuilder builder = new StringBuilder();
        for (String current : split) {
            String first = current.substring(0, 1);
            String last = current.substring(1).toLowerCase();
            builder.append(capitalizeFirst ? first.toUpperCase() : first.toLowerCase());
            builder.append(last);
            capitalizeFirst = true;
        }
        return builder.toString();
    }


}
