package com.epam.framework.core.utils;

import com.google.common.primitives.Ints;

import java.security.SecureRandom;
import java.util.Optional;

public class NumberUtils {

    private NumberUtils(){

    }

    public static boolean isNumber(String number) {
        return org.apache.commons.lang3.math.NumberUtils.isDigits(number);
    }

    public static int min(int[] array) {
        return org.apache.commons.lang3.math.NumberUtils.min(array);
    }

    public static int max(int[] array) {
        return org.apache.commons.lang3.math.NumberUtils.max(array);
    }

    public static int generateRandomNumber(final int min, final int max) {
        SecureRandom ranGen = new SecureRandom();
        byte[] rno = new byte[4];
        ranGen.nextBytes(rno);
        return (rno[0] * max + min);
    }

    public static int getInt(String value) {
        return Optional.ofNullable(value)
                .map(Ints::tryParse)
                .orElse(0);
    }


}
