import os
import json

OUTPUT_DIR = r"C:\Users\joshu\Downloads\fn-project\data\output"
SITE_DIR = r"C:\Users\joshu\Downloads\fn-site"

def build():
    nations = []
    skipped = 0
    
    for filename in sorted(os.listdir(OUTPUT_DIR)):
        if not filename.endswith(".json"):
            continue
        path = os.path.join(OUTPUT_DIR, filename)
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            # Skip empty or invalid records
            if not data.get("nation") or data.get("revenue", 0) == 0:
                skipped += 1
                continue
            # Keep only fields needed for the site
            nations.append({
                "nation": data.get("nation"),
                "fiscal_year": data.get("fiscal_year"),
                "province": data.get("province", ""),
                "auditor": data.get("auditor", ""),
                "revenue": data.get("revenue", 0),
                "expenses": data.get("expenses", 0),
                "annual_surplus": data.get("annual_surplus", 0),
                "accumulated_surplus": data.get("accumulated_surplus", 0),
                "isc_funding": data.get("isc_funding", 0),
                "total_government_transfers": data.get("total_government_transfers", 0),
                "osr": data.get("osr", 0),
                "cash": data.get("cash", 0),
                "long_term_debt": data.get("long_term_debt", 0),
                "tangible_capital_assets": data.get("tangible_capital_assets", 0),
                "net_financial_assets": data.get("net_financial_assets", 0),
                "amortization": data.get("amortization", 0),
                "annual_debt_service": data.get("annual_debt_service", 0),
                "population_on_reserve": data.get("population_on_reserve", 0),
                "population_total": data.get("population_total", 0),
                "num_employees": data.get("num_employees", 0),
                "num_subsidiaries": data.get("num_subsidiaries", 0),
                "expenses_health": data.get("expenses_health", 0),
                "expenses_education": data.get("expenses_education", 0),
                "expenses_housing": data.get("expenses_housing", 0),
                "expenses_social": data.get("expenses_social", 0),
                "expenses_administration": data.get("expenses_administration", 0),
                "expenses_salaries_total": data.get("expenses_salaries_total", 0),
                "audit_qualified": data.get("audit_qualified", False),
                "going_concern": data.get("going_concern", False),
                "one_time_items": data.get("one_time_items", False),
                "one_time_description": data.get("one_time_description", ""),
                "health_score": data.get("health_score", 0),
                "isc_dependency_pct": data.get("isc_dependency_pct", 0),
                "osr_pct": data.get("osr_pct", 0),
                "notes": data.get("notes", ""),
                "economic_notes": data.get("economic_notes", ""),
                "revenue_lines": data.get("revenue_lines", {}),
            })
        except Exception as e:
            print(f"  Error reading {filename}: {e}")
            skipped += 1

    # Write single consolidated file
    out_path = os.path.join(SITE_DIR, "data", "nations.json")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(nations, f)

    print(f"Built dataset: {len(nations)} records ({skipped} skipped)")
    print(f"Saved to: {out_path}")

if __name__ == "__main__":
    build()