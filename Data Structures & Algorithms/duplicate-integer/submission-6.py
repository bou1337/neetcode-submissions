class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        st  =set()
        st.update(nums)
        return len(st)!=len(nums)
        