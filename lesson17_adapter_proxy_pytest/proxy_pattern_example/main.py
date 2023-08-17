from lesson17_adapter_proxy_pytest.proxy_pattern_example.csv_reader import CsvReader
from lesson17_adapter_proxy_pytest.proxy_pattern_example.csv_proxy_reader import CsvProxyReader

csv_reader = CsvReader('users.csv')
proxy_reader = CsvProxyReader(csv_reader)
print(proxy_reader.read())
print(proxy_reader.read())