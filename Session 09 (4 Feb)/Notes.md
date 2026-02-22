# Session 9

Contents of this session:
- Vector spaces
  - The definition of a vector space
  - Collinearity, linear independence, span and related concepts
  - Kernels and images
- A look at the Object-Oriented Programming and Algorithms papers


## Addendum: Finding the floor and ceiling of a key in a binary search tree

### Finding the floor

To find the floor of a key $k$, traverse the tree while keeping track of the best candidate found so far.

Start at the root and compare the search key with the current node's key.

- If the search key equals the current node's key, this exact match must be the floor.
- If the search key is less than the current node's key, the floor cannot be in the right subtree since all values there are even larger. Move to the left child and continue searching.
- If the search key is greater than the current node's key, the current node becomes a candidate for the floor. However, there might be an even larger key that's still smaller than the search key in the right subtree. Therefore, we update our candidate and move to the right child to see if we can find something closer to the search key.

Continue this process until a null child is reached. The last candidate saved is the floor.

If a candidate is never found, the floor doesn't exist because all keys in the tree are larger than the search key.



### Finding the ceiling

The process of locating the ceiling follows a similar logic. We start at the root and compare keys.

- If the search key equals the current node's key, that node is the ceiling.
- If the search key is greater than the current node's key, the ceiling must be in the right subtree since all values in the left subtree are smaller. We move right and continue.
- If the search key is less than the current node's key, the current node becomes a candidate for the ceiling. However, there might be a smaller key that's still larger than the search key in the left subtree. We update our candidate and move left to check for a closer match.

When a null child is reached, we return the last candidate. If no candidate was found, the ceiling doesn't exist because all keys are smaller than the search key.