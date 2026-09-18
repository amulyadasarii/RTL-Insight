
import re
from pathlib import Path


def extract_rtl_features(verilog_file):
    """Extract basic structural features from a Verilog RTL file."""

    verilog_code = Path(verilog_file).read_text(encoding="utf-8")

    verilog_code = re.sub(
        r"//.*|/\*.*?\*/",
        "",
        verilog_code,
        flags=re.DOTALL
    )

    features = {}

    features["modules"] = len(
        re.findall(r"\bmodule\s+\w+", verilog_code)
    )

    features["inputs"] = len(
        re.findall(r"\binput\b", verilog_code)
    )

    features["outputs"] = len(
        re.findall(r"\boutput\b", verilog_code)
    )

    features["registers"] = len(
        re.findall(r"\breg\b", verilog_code)
    )

    features["wires"] = len(
        re.findall(r"\bwire\b", verilog_code)
    )

    features["always_blocks"] = len(
        re.findall(r"\balways\b", verilog_code)
    )

    features["case_statements"] = len(
        re.findall(r"\bcase\b", verilog_code)
    )

    features["adders"] = len(
        re.findall(r"\+", verilog_code)
    )

    features["subtractors"] = len(
        re.findall(r"-", verilog_code)
    )

    features["and_operations"] = len(
        re.findall(r"&", verilog_code)
    )

    features["or_operations"] = len(
        re.findall(r"\|", verilog_code)
    )

    return features


if __name__ == "__main__":

    rtl_file = Path(__file__).parent.parent / "rtl" / "sample_alu.v"

    features = extract_rtl_features(rtl_file)

    print("\nRTL FEATURE EXTRACTION RESULTS")
    print("-" * 35)

    for feature, value in features.items():
        print(f"{feature}: {value}")