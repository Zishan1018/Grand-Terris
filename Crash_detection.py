ACCEL_THRESHOLD = 20
GYRO_THRESHOLD = 10

def is_crash(accel_value, gyro_value):
    return accel_value > ACCEL_THRESHOLD and gyro_value > GYRO_THRESHOLD