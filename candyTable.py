import numpy as np
import itertools
import sys
np.set_printoptions(threshold=255)

# =GLOBALS===============
# (I'm not writing args for one int variable)
dim = 3
# Note: works only because the number of children = the number of candies taken


# Note: the [1+Nd] means it's an Nd array with another dimension representing each possibility. TODO Space inefficient?
def main():
    # [1+1d] child_pulls
    # every possible combination of any given child's candy pulls
    child_pulls = [list(i) for i in itertools.combinations_with_replacement(list(range(dim)), dim)]
    # TODO ** should be moved here in the iter..., too bad. I already got my answer
    # TODO holy god, that's why it takes 3 hours for dim > 5

    # (iter) group_pulls & [1+2d] valid_group_pulls
    # every possible combination of candy pulls with filter taking into account there can only be dim candies
    valid_group_pulls = []
    for group_pull in itertools.combinations_with_replacement(child_pulls, dim):
        group_pull = np.array(group_pull)
        count = np.bincount(group_pull.ravel())
        # TODO **
        if all([True if c == dim else False for c in count]):  # each count == dim
            valid_group_pulls.append(group_pull)
    valid_group_pulls = np.array(valid_group_pulls)  # np array

    # [1+2d] valid_major_pulls
    # applies the constraint each child need a strict majority of some candy
    valid_major_pulls = []
    for valid_pull in valid_group_pulls:

        # [2d] counts_matrix
        # how many (val) of each candy (col) each child has (row)
        counts_matrix = np.apply_along_axis(np.bincount,
                                            axis=1,
                                            arr=valid_pull,
                                            minlength=np.max(valid_pull) + 1)

        # [1d] counts_max
        # the candy(s) that child has most of; unique if valid 'major'
        # "must be strictly GREATER THAN (>, but unintentionally =) other max counts"
        counts_max = np.apply_along_axis(is_dist_max_fix,
                                         axis=0,  # cols / candy types
                                         arr=counts_matrix)

        # if theres one maxima for every child AND each child has a different max candy type
        if -1 not in counts_max and len(set(counts_max)) == len(counts_max):
            valid_major_pulls.append(valid_pull)
    valid_major_pulls = np.array(valid_major_pulls)

    # PRINT SOLUTION
    print('=VALID===================')
    print(valid_group_pulls)
    print('\n=VALID=W/=MAJORITY=======')
    print(valid_major_pulls)
    print('\n=FRACTION================')
    print(len(valid_major_pulls), "/", len(valid_group_pulls))


def is_dist_max_fix(arr):
    n = list(np.argwhere(arr == np.amax(arr)).flatten())  # loc of all instances of max
    return -1 if len(n) > 1 else n[0]  # -1 if more than one location of max (not strictly >)


if __name__ == '__main__':
    main()
