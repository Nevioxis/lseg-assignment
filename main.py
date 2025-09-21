def extractKeyValue(dictionary: dict, result: dict = None) -> dict[str:list]:
    """
    Extract dictionary keys and values into dictionary of list of keys and values

    Parameters:
    - dictionary (dict): dictionary to be extracted
    - result (dict[str,list]): dictionary of list of keys and values to be included in actual output

    Returns:
    dict[str,list]: dictionary of list of keys and values
    
    Raises:
    - ValueError: if non-dictionary object being used as a parameter
    """
    
    # Prevent non-dictionary object to be a parameter
    if not isinstance(dictionary, dict): raise ValueError("Only dictionary object allowed")
    
    
    # Set initialize object
    if result is None: result = {"key": [], "value": []}
    
    for dict_key in dictionary:
        
        result["key"].append(dict_key)
        
        if isinstance(dictionary[dict_key], dict): extractKeyValue(dictionary[dict_key],result) #Recurse function to travel into the object
            
        else:
            result["value"].append(dictionary[dict_key])
    
    return result


test_cases = [
    ({"a":{"b":{"c":"d"}}}, {'key': ["a","b","c"], 'value': ["d"]}), #Example 1
    ({"x":{"y":{"z":"a"}}}, {'key': ["x","y","z"], 'value': ["a"]}), #Example 2
    ({},{'key': [], 'value': []}), #Empty Dictionary
    ({"a": "1", "b": {"c": "2"}}, {'key': ["a","b","c"], 'value': ["1","2"]}), #Same level keys
    ({"a": 1, "b": {"c": True, "d": None}}, {'key': ["a","b","c","d"], 'value': [1,True,None]}), #Multiple data types
    ({"a": "b"}, {'key': ["a"], 'value': ["b"]}) #Simple dictionary
]

#Function Unit testing

failed_cases = []
for test_no, test_case in enumerate(test_cases):
    try: 
        test_result = extractKeyValue(test_case[0])
        assert test_result == test_case[1], "Incorrect test"
    except:
        print(f"Incorrect test case #{test_no + 1}")
        print(f"Input: {test_case[0]}")
        print(f"Expected: {test_case[1]}")
        print(f"Actual: {test_result}\n")
        failed_cases.append(test_no + 1)

if len(failed_cases) > 0: raise AssertionError(f"Incorrect test case(s) including case {failed_cases}")
else: print("All test passed!")
