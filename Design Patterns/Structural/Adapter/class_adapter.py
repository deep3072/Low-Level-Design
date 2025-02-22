class StockDataProvider:
    """
    Adaptee: returns stocks data in XML format.
    """
    def get_stock_data(self):
        return """<stock><symbol>AAPL</symbol><price>250.00</price></stock>
                <stock><symbol>GOOGL</symbol><price>150.00</price></stock>"""
    
class StockAnalyticsLibrary:
    """
    Target: 3rd Party library that processes JSON format data.
    """
    def analyze_stock_data(self, json_data):
        print(f"Analyzing stock data: {json_data}")

class StockDataAdapter(StockDataProvider): # inherts adaptee
    """
    Class Adapter: converts XML data to JSON format using inheritance.
    """
    def get_stock_data_as_json(self):
        xml_data = super().get_stock_data()
        # Converting XML to JSON..
        json_data = self.convert_xml_to_json(xml_data)
        return json_data

    def convert_xml_to_json(self, xml_data):
        # Mock conversion logic
        return '{"stocks": [{"symbol": "AAPL", "price": 250.00}, {"symbol": "GOOGL", "price": 150.00}]}'
    
stock_data_adapter = StockDataAdapter()
stock_data_json = stock_data_adapter.get_stock_data_as_json()

stock_analytics = StockAnalyticsLibrary()
stock_analytics.analyze_stock_data(stock_data_json) # get analyzed data