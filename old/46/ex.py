def permute(nums):
        perms = [[]]
        for n in nums:
            new_perms = []
            for p in perms: 
                for i in range(len(p) + 1):
                    p_copy = p.copy()
                    p_copy.insert(i, n)
                    new_perms.append(p_copy)
            perms = new_perms

            print(perms, n)       
        return perms

print(permute([1, 2, 3]))