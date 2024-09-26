def determine_progress3(hits, spins):
    if spins == 0:
        return "Get going!"
    
    hits_spins_ratio = hits / spins
    
    if hits_spins_ratio == 0:
        return "Get going!"
    elif hits_spins_ratio >= 0.5 and hits < spins:
        return "You win!"
    elif hits_spins_ratio >= 0.25:
        return "Almost there!"
    elif hits_spins_ratio > 0:
        return "On your way!"
    
    return "Get going!"

def test_determine_progress(progress_function):
    # Test case 1: spins = 0 returns "Get going!"
    assert progress_function(0, 0) == "Get going!", "Test case 1 failed"
    
    # Test case 2: hits_spins_ratio >= 0.5 and hits < spins should return "You win!"
    assert progress_function(1, 2) == "You win!", "Test case 2 failed"
    
    # Test case 3: hits_spins_ratio >= 0.25 should return "Almost there!"
    assert progress_function(1, 4) == "Almost there!", "Test case 3 failed"
    
    # Test case 4: hits_spins_ratio > 0 should return "On your way!"
    assert progress_function(1, 8) == "On your way!", "Test case 4 failed"
    
    print("All test cases passed!")

# Run the test
test_determine_progress(determine_progress3)




