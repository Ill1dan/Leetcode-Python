class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        merged_list = sorted(nums1 + nums2) 
        length = len(merged_list)
        mid = length // 2
        return float(merged_list[mid] if length % 2 else (merged_list[mid-1] + merged_list[mid]) / 2.0)
        