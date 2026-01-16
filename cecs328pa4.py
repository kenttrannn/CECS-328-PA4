#Kent Tran

def aircraft_max_revenue(cargo, capacity):
    n = len(cargo)
    
    if capacity == 0 or n == 0:
        return 0
    
    prev = [0] * (capacity + 1)
    
    for i in range(n):
        weight, price = cargo[i]
        curr = [0] * (capacity + 1)
        
        for w in range(capacity + 1):
            curr[w] = prev[w]
            
            if weight <= w:
                curr[w] = max(curr[w], prev[w - weight] + price)
        
        prev = curr
    
    return prev[capacity]