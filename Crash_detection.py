# Crash Detection Logic
# Grand-Terris | Google Solution Challenge 2026

# Thresholds based on typical crash force values
ACCEL_THRESHOLD = 20  # m/s² (sudden jolt)
GYRO_THRESHOLD = 10   # rad/s (sudden rotation)

def is_crash(accel_value, gyro_value):
    """
    Returns True if sensor values indicate a crash
    """
    if accel_value > ACCEL_THRESHOLD and gyro_value > GYRO_THRESHOLD:
        return True
    return False

# ---- Test it ----
print("Test 1 - Should be CRASH:")
print(is_crash(25, 12))   # True

print("Test 2 - Should be SAFE:")
print(is_crash(5, 2))     # False

print("Test 3 - Should be SAFE:")
print(is_crash(25, 3))    # False - only accel spike, no gyro