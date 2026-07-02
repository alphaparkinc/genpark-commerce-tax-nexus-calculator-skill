from client import TaxNexusCalculatorClient
def main():
    c = TaxNexusCalculatorClient()
    print(c.calculate_tax(100.0, "NY"))
if __name__ == '__main__':
    main()
