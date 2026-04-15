import pytest
from src.reports.reports import generate_report, export_report, get_report_status


def test_generate_report():
    result = generate_report("sales", {"period": "monthly"})
    assert result["type"] == "sales"


def test_export_report():
    result = export_report(1, "pdf")
    assert result["format"] == "pdf"


def test_get_report_status():
    result = get_report_status(1)
    assert result["status"] == "completed"
