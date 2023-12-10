#Count Tested Devices After Test Operations
#time complexity - O(n^2), where n is the length of the batteryPercentages list.

def countTestedDevices(batteryPercentages) -> int:
    n = len(batteryPercentages)
    tested_devices = 0

    for i in range(n):
        if batteryPercentages[i] > 0:
            tested_devices += 1
            for j in range(i + 1, n):
                batteryPercentages[j] = max(0, batteryPercentages[j] - 1)

    return tested_devices

if __name__ == "__main__":
    batteryPercentages = [1,1,2,1,3]
    print(countTestedDevices(batteryPercentages))