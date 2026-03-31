import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def load_product_shell():
    with open(ROOT / "docs" / "PRODUCT_SHELL.json", "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    shell = load_product_shell()

    print("\n=== BINDU GUARDIAN ===")
    print(json.dumps({
        "product_name": shell["product_name"],
        "version": shell["version"],
        "purpose": shell["purpose"],
        "target_domains": shell["target_domains"],
        "module_count": len(shell["core_modules"]),
        "north_star": shell["north_star"]
    }, indent=2))

if __name__ == "__main__":
    main()
