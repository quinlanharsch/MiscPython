import numpy as np
import itertools
import sys
np.set_printoptions(threshold=sys.maxsize)

dim = 5

def main():
    # [1+1d] child_pulls
    # every possible combination of candy pulls
    # works only because the number of children = the number of candies taken
    child_pulls = [list(i) for i in itertools.combinations_with_replacement(list(range(dim)), dim)]

    # (iter) group_pulls & [1+2d] valid_group_pulls
    # every possible combination of combination of candy pulls taking into account there can only be dim candies
    valid_group_pulls = []
    for group_pull in itertools.combinations_with_replacement(child_pulls, dim):
        group_pull = np.array(group_pull)
        count = np.bincount(group_pull.ravel())
        if all([True if c == dim else False for c in count]):  # each count == dim
            valid_group_pulls.append(group_pull)
        # group_pull_counts.append(dict(zip(candy, count)))
    valid_group_pulls = np.array(valid_group_pulls)  # np array

    # [1+2d] valid_major_pulls
    # applies the constraint each child need a strict majority of some candy
    valid_major_pulls = []
    for valid_pull in valid_group_pulls:
        # print("valid_pull: \n", valid_pull)  # TODO delete debugs
        # [1+2d] counts_matrix
        # how many (val) of each candy (col) each child has (row)
        counts_matrix = np.apply_along_axis(np.bincount,
                                            axis=1,
                                            arr=valid_pull,
                                            minlength=np.max(valid_pull) + 1)
        # print("counts_matrix: \n", counts_matrix)  # TODO
        # [1+1d] counts_max
        # the candy(s) that child has most of; unique if valid 'major'
        # "must be strictly GREATER THAN (>, but unintentionally =) other max counts"
        counts_max = np.apply_along_axis(is_dist_max_fix,
                                         axis=0,  # cols / candy types
                                         arr=counts_matrix)
        # print("counts_max: \n", counts_max)  # TODO

        # if theres one maxima for every child AND each child has a different max candy type
        valid_total = -1 not in counts_max and len(set(counts_max)) == len(counts_max)
        if valid_total:
            valid_major_pulls.append(valid_pull)
    valid_major_pulls = np.array(valid_major_pulls)

    # PRINT SOLUTION
    print('=VALID===================')
    print(valid_group_pulls)
    print('=VALID=W/=MAJORITY=======')
    print(valid_major_pulls)
    print('=FRACTION================')

    print(len(valid_major_pulls), "/", len(valid_group_pulls))


def is_dist_max_fix(arr):
    n = list(np.argwhere(arr == np.amax(arr)).flatten())
    return -1 if len(n) > 1 else n[0]


if __name__ == '__main__':
    main()
