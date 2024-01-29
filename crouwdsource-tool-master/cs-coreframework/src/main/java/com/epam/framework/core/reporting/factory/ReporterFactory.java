package com.epam.framework.core.reporting.factory;

import com.epam.framework.core.logging.logger.exceptions.ArgumentNotSupportedException;
import com.epam.framework.core.reporting.HTMLReportObserver;
import com.epam.framework.core.reporting.extent.ExtentHTMLReportObserver;
import com.epam.framework.core.reporting.reportportal.ReportPortalObserver;

public class ReporterFactory {

	private static HTMLReportObserver reporter = null;

	private ReporterFactory() {
	}

	public static HTMLReportObserver getReporter(ReporterType reporterType) {
		if (reporter == null) {
			createReporter(reporterType);
		}
		return reporter;
	}

	private static void createReporter(ReporterType reporterType) {
		switch (reporterType) {
		case EXTENTREPORT:
			reporter = new ExtentHTMLReportObserver();
			break;
		case REPORTPORTAL:
			reporter = new ReportPortalObserver();
			break;
		default:
			throw new ArgumentNotSupportedException("Currently Supported  Reporters - Extent  and  ReportPortal");
		}
	}
}
