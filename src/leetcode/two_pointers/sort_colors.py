def sort_colors(nums: list[int]) -> None:
   """ Sorts an array of 0, 1, and 2, so that all zeroes are first, then ones, and finally zeros

   Example:

    [1, 1, 0, 0, 2, 2, 0] -> [0, 0, 0, 1, 1, 2, 2]

   """
   left = 0
   middle = 0
   right = len(nums) - 1

   while middle <= right:
       if nums[middle] == 0:
           nums[left], nums[middle] = nums[middle], nums[left]
           left += 1
           middle += 1

       elif nums[middle] == 1:
           middle += 1

       else:
           nums[right], nums[middle] = nums[middle], nums[right]
           right -= 1
