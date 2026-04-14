import pytest
from src.reports.reports import generate_report, export_report, get_report_status


async def test_generate_report():
    result = await generate_report("sales", {"period": "monthly"})
    assert result["type"] == "sales"


async def test_export_report():
    result = await export_report(1, "pdf")
    assert result["format"] == "pdf"


async def test_get_report_status():
    result = await get_report_status(1)
    assert result["status"] == "completed"
