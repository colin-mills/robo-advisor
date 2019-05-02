from app.functions import to_USD, compile_URL, os
from dotenv import load_dotenv

def test_to_USD():
    assert to_USD(4) == "$4.00" #should have two decimal points
    assert to_USD(57.9999) == "$58.00" #test rounding 
    assert to_USD(99999.99) == "$99,999.99" #test commas 
    assert to_USD(100000) == "$100,000.00" #test commas and decimals 
    assert to_USD(8.00000000001) == "$8.00" #Should round down

def test_compile_URL():
    load_dotenv()
    API_KEY = os.environ.get("ALPHAVANTAGE_API_KEY")
    request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AMZN&apikey={}".format(API_KEY)
    
    assert compile_URL("AMZN") == request_url