class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ar = []
        for i in range(len(arr2)):
            for j in range(len(arr1)):
                if arr2[i] == arr1[j]:
                    ar.append(arr1[j])
                    arr1[j] = -2
        for numb in sorted(arr1):
            if numb != -2:
                ar.append(numb)

        return ar



                

        