def determine_progress2(hits, spins):
    if spins == 0:
        return "Get going!"
    
    hits_spins_ratio = hits / spins
    
    if hits_spins_ratio == 0:
        return "Get going!"
    
    if hits_spins_ratio >= 0.5:
        if hits < spins:
            return "You win!"
    
    if hits_spins_ratio >= 0.25:
        return "Almost there!"
    
    if hits_spins_ratio > 0:
        return "On your way!"
    
    return "Get going!"


def test_determine_progress(progress_function):
   # Test case 1: spins = 0 returns “Get going!”
    assert progress_function(1, 10) == "Get going!", "Test case 1 failed"
test_determine_progress(determine_progress2)




