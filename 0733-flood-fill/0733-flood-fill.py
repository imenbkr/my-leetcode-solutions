class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        #check if source pixel has the new color or image is null
        if (image == None) or (image[sr][sc]== color):
            return image

        #start_color = image[sr][sc]
        self.depth_first(image, sr, sc, color,  image[sr][sc])

        return image 

    #depth first algorithm
    def depth_first(self, image, sr, sc, color, initial):
        #check sr and sc 
        #len(image) == length of rows , len(image[0]) == length of columns
        #if pixel()sc, sr) doesn't have the same color as the starting pixel
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]) or image[sr][sc] != initial:
            return

        #else
        #append value of new color to that pixel
        image[sr][sc] = color
        #right call : do the same to the pixel on the right
        self.depth_first(image, sr+1, sc, color, initial)
        #left call
        self.depth_first(image, sr-1, sc, color, initial)
        #down call
        self.depth_first(image, sr, sc+1, color, initial)
        #top call
        self.depth_first(image, sr, sc-1, color, initial)