
sample_fares = [8.60, 5.75, 13.25, 21.21]


for fare in sample_fares:
    if fare > 12:
        print(f"{fare}: This fare is high!")
    else:
        print(f"{fare}: This fare is low.")



def classify_fares(fares):
    results = []  
    for fare in fares:
        if fare > 12:
            message = f"{fare}: This fare is high!"
        else:
            message = f"{fare}: This fare is low."
        print(message)
        results.append(message)  
    return results

def test_classify_fares():
    # Test case 1: Basic list with different fares
    sample_fares = [8.60, 5.75, 13.25, 21.21]
    expected_output = [
        "8.6: This fare is low.",
        "5.75: This fare is low.",
        "13.25: This fare is high!",
        "21.21: This fare is high!"
    ]
    assert classify_fares(sample_fares) == expected_output, "Test case 1 failed"
    
    # Test case 2: List with all low fares
    low_fares = [5.00, 2.50, 11.99]
    expected_output = [
        "5.0: This fare is low.",
        "2.5: This fare is low.",
        "11.99: This fare is low."
    ]
    assert classify_fares(low_fares) == expected_output, "Test case 2 failed"
    
    # Test case 3: List with all high fares
    high_fares = [15.00, 20.50, 50.25]
    expected_output = [
        "15.0: This fare is high!",
        "20.5: This fare is high!",
        "50.25: This fare is high!"
    ]
    assert classify_fares(high_fares) == expected_output, "Test case 3 failed"
    
    # Test case 4: List with a single fare
    single_fare = [12.50]
    expected_output = [
        "12.5: This fare is high!"
    ]
    assert classify_fares(single_fare) == expected_output, "Test case 4 failed"
    
    # Test case 5
    empty_list = []
    expected_output = []
    assert classify_fares(empty_list) == expected_output, "Test case 5 failed"

    print("All test cases passed!")


test_classify_fares()
