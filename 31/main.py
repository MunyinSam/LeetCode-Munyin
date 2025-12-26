

def permute(nums):

        perms = [[]]

        sorted_nums = sorted(nums)

        for n in sorted_nums:
            new_perms = []
            for p in perms:
                for i in range(len(p) + 1):
                    p_copy = p.copy()
                    p_copy.insert(i , n)
                    new_perms.append(p_copy)

            perms = new_perms

        sorted_perm = sorted(perms)
        index = sorted_perm.index(nums)
        return sorted_perm[(index + 1) % len(perms)]

print(permute([3, 2, 1]))