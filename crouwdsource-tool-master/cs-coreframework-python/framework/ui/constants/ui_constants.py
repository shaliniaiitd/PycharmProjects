"""
Module to contain all constants of framework
"""
import os


class Generic:
    LOCATOR_BY_VALUE_SEPARATOR = "|"


class WaitConst:
    WAIT_TIMEOUT_DEFAULT = 10
    WAIT_TIMEOUT_LONG = 20
    WAIT_TIMEOUT_SHORT = 5
    POLL_FREQUENCY = .5
    MAX_EXPLICIT_WAIT = 120


class ErrorMessages:
    wait_msg_element_is_not_visible = "Element is not visible after waiting for {} seconds and polling frequency {} second(s)"
    wait_msg_element_is_not_present = "Element is not present after waiting for {} seconds and polling frequency {} second(s)"
    wait_msg_element_is_not_clickable = "Element is not clickable after waiting for {} seconds and polling frequency {} second(s)"
    wait_msg_page_is_not_fully_loaded = "Exception occurred, page fails to load after waiting for {} seconds"

    GENERAL_ELEMENT_NOT_FOUND = "Element not found"