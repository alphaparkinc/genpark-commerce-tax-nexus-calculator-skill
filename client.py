from typing import Dict, Any

class TaxNexusCalculatorClient:
    def calculate_tax(self, subtotal: float, destination_state: str) -> Dict[str, Any]:
        # Nexus state rates
        rates = {
            "CA": 0.0825,
            "NY": 0.08875,
            "TX": 0.0625,
            "WA": 0.065
        }
        rate = rates.get(destination_state.upper(), 0.0)
        tax = round(subtotal * rate, 2)
        return {
            "has_nexus": rate > 0,
            "tax_rate": rate,
            "calculated_tax": tax,
            "total_with_tax": round(subtotal + tax, 2)
        }
