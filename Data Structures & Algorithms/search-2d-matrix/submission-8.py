class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Function that takes in a matrix with a target
        and returns a Boolean if the target exists in there
        Parameters: A Matrix and a Target integer
        Returns: A Boolean 
        """
       
        #Use pointers and check the highest val in frst list, and lowest val in last list
        #Once we find something in it we can return True or False
        #Once the length of the matrix is one, we can just check

        Left, Right = 0, len(matrix)-1
        Middle = (Left + Right)//2
                
        while Left <= Right:
            if len(matrix) == 1:
                break
            Middle = (Left+Right)//2
            if matrix[Middle][len(matrix[Middle])-1] < target:
                Left = Middle + 1
            elif matrix[Middle][0] > target:
                Right = Middle -1 
            else:
                if target in matrix[Middle]:
                    return True
                else:
                    return False

        if target in matrix[0]:
            return True
        else: 
            return False

        