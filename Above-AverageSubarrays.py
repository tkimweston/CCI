"""
Above-Average Subarrays
You are given an array A containing N integers. Your task is to find all subarrays whose average sum is greater than the average sum of the remaining array elements. You must return the start and end index of each subarray in sorted order.
A subarray that starts at position L1 and ends at position R1 comes before a subarray that starts at L2 and ends at R2 if L1 < L2, or if L1 = L2 and R1 ≤ R2.
Note that we'll define the average sum of an empty array to be 0, and we'll define the indicies of the array (for the purpose of output) to be 1 through N. A subarray that contains a single element will have L1 = R1.
Signature
Subarray[] aboveAverageSubarrays(int[] A)
Input
1 ≤ N ≤ 2,000
1 ≤ A[i] ≤ 1,000,000
Output
A Subarray is an object with two integer fields, left and right, defining the range that a given subarray covers. Return a list of all above-average subarrays sorted as explained above.
Example 1
A = [3, 4, 2]
output = [[1, 2], [1, 3], [2, 2]]
The above-average subarrays are [3, 4], [3, 4, 2], and [4].
"""

"""
A[0...N] integers

 Subarray[] aboveAverageSubarrays(int[] arr) {

    List<Subarray> resultList = new ArrayList<>();

    int totalSum = 0;

    for (int k : arr) {
      totalSum += k;
    }

    for (int i = 0; i < arr.length; i++) {

      int sumCurrent = 0;

      for (int j = i; j < arr.length; j++) {

        sumCurrent += arr[j];

        if (sumCurrent / (j - i + 1) > (totalSum - sumCurrent) / (arr.length - (j - i + 1))) {
          resultList.add(new Subarray(i + 1, j + 1));
        }
      }
    }

    return resultList.toArray(new Subarray[0]);

  }
"""
def aboveAverageSubarrays(a):
  result = []
  sum = 0
  for num in a:
    sum += num
    
  for i in range(len(a)):
    currentSum = 0
    for j in range(i, len(a)):
      currentSum += a[j]
      if (len(a) - (j - i + 1)) == 0 or (currentSum / (j - i + 1)) > ((sum - currentSum) / (len(a) - (j - i + 1))):
        result.append([i + 1, j + 1])
  
  return result

def aboveAverageSubarrays2(a):
    result = []
    totalSum = sum(a)
    for i in range(len(a)):
        currentSum = 0
        for j in range(i, len(a)):
            count = j - i + 1
            othercount = len(a) - (j - i + 1)
            currentSum += a[j]
            if othercount == 0 or currentSum / count > (totalSum - currentSum) / othercount:
                result.append([i + 1, j + 1])

    return result

a = [3, 4, 2]
print(aboveAverageSubarrays(a))
print(aboveAverageSubarrays2(a))
b = [[1, 2], [2, 3], [3, 3]]
print(b.sort())