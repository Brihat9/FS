'''
    Fuzzy Systems Relation Composition Example
    Brihat Ratna Bajracharya (CRN: 19/075)
    CDCSIT
'''


from fs_basics import BTuple, Bset, Brelation
import numpy as np


def compute_relational_matrix(rela, seta, setb):
    ''' returns membership functional value matrix from relation
        of seta to setb in form of numpy array
    '''
    lena = len(seta)
    lenb = len(setb)

    wt_matrix = np.zeros((lena, lenb))

    for indexa in range(len(seta)):
        for indexb in range(len(setb)):
            for member in rela.members:
                if member[0].element == seta.elements[indexa].element and \
                   member[1].element == setb.elements[indexb].element:
                    wt_matrix[indexa, indexb] = \
                        min(seta.elements[indexa].value,
                            setb.elements[indexb].value)

    # print(wt_matrix)
    return wt_matrix


def max_min(deg_strength_1, deg_strength_2):
    ''' calculates MAX-MIN Composition between two numpy arrays '''
    result_max_min = np.zeros((deg_strength_1.shape[0],
                               deg_strength_2.shape[1]))
    temp_list = []
    n_row_1 = len(deg_strength_1)
    n_column_1 = len(deg_strength_1[0])
    n_row_2 = len(deg_strength_2)

    for i in range(n_row_1):
        for k in range(n_column_1):
            for j in range(n_row_2):
                temp_list.append(min(deg_strength_1[i, j],
                                     deg_strength_2[j, k]))
            result_max_min[i, k] = max(temp_list)
            temp_list = []

    return result_max_min


def max_product(deg_strength_1, deg_strength_2):
    ''' calculates MAX-Product Composition between two numpy arrays '''
    max_product_result = np.zeros((deg_strength_1.shape[0],
                                   deg_strength_2.shape[1]))
    temp_list = []
    n_row_1 = len(deg_strength_1)
    n_column_1 = len(deg_strength_1[0])
    n_row_2 = len(deg_strength_2)

    for i in range(n_row_1):
        for k in range(n_column_1):
            for j in range(n_row_2):
                temp_list.append(deg_strength_1[i, j] * deg_strength_2[j, k])
            max_product_result[i, k] = max(temp_list)
            temp_list = []

    return max_product_result


def main():
    """ Main Function """

    print("\nFS Example (Fuzzy Set Relation Composition)")
    print("Brihat Ratna Bajracharya\n19/075\n---------\n")

    ''' testing purpose '''
    # elema = BTuple('a', 1)
    # elemb = BTuple('b', 0)
    #
    # elemc = BTuple('c', 0)
    # elemd = BTuple('d', 1)
    #
    # eleme = BTuple('e', 1)
    # elemf = BTuple('f', 0)
    #
    # seta = Bset()
    # setb = Bset()
    # setc = Bset()
    #
    # seta.add_element(elema)
    # seta.add_element(elemb)
    #
    # setb.add_element(elemc)
    # setb.add_element(elemd)
    #
    # setc.add_element(eleme)
    # setc.add_element(elemf)
    #
    # new_rel_a = Brelation()
    # new_rel_a.add_member([elema, elemc])      # a -> c
    # new_rel_a.add_member([elema, elemd])      # a -> d
    # new_rel_a.add_member([elemb, elemd])      # b -> d
    #
    # print(new_rel_a)
    #
    # new_rel_b = Brelation()
    # new_rel_b.add_member([elemc, eleme])      # c -> e
    # new_rel_b.add_member([elemd, eleme])      # d -> e
    # new_rel_b.add_member([elemd, elemf])      # d -> f
    #
    # print(new_rel_b)
    #
    # compute_relational_matrix(new_rel_a, seta, setb)
    # compute_relational_matrix(new_rel_b, setb, setc)

    ''' actual example from class note '''

    # creating elements
    fast = BTuple('fast', 0.6)
    medium = BTuple('medium', 0.8)
    spin = BTuple('spin', 0.9)

    good = BTuple('good', 0.4)
    fair = BTuple('fair', 0.5)
    rough = BTuple('rough', 0.2)

    low = BTuple('low', 0.9)
    avg = BTuple('avg', 1.0)
    high = BTuple('high', 0.7)

    # initialize sets
    set_speed = Bset()
    set_pitch = Bset()
    set_run = Bset()

    # adding elements to set_speed
    set_speed.add_element(fast)
    set_speed.add_element(medium)
    set_speed.add_element(spin)

    print("Set Speed")
    print(set_speed, end="\n\n")

    # adding elements to set_pitch
    set_pitch.add_element(good)
    set_pitch.add_element(fair)
    set_pitch.add_element(rough)

    print("Set Pitch")
    print(set_pitch, end="\n\n")

    # adding elements to set_run
    set_run.add_element(low)
    set_run.add_element(avg)
    set_run.add_element(high)

    print("Set Run")
    print(set_run, end="\n\n")

    # new relation from set_speed to set_pitch
    rel_speed_pitch = Brelation()
    rel_speed_pitch.add_member([fast, good])
    rel_speed_pitch.add_member([fast, fair])
    rel_speed_pitch.add_member([fast, rough])
    rel_speed_pitch.add_member([medium, good])
    rel_speed_pitch.add_member([medium, fair])
    rel_speed_pitch.add_member([medium, rough])
    rel_speed_pitch.add_member([spin, good])
    rel_speed_pitch.add_member([spin, fair])
    rel_speed_pitch.add_member([spin, rough])

    print("Relation Speed -> Pitch")
    print(rel_speed_pitch)

    # new relation from set_pitch to set_run
    rel_pitch_run = Brelation()
    rel_pitch_run.add_member([good, low])
    rel_pitch_run.add_member([good, avg])
    rel_pitch_run.add_member([good, high])
    rel_pitch_run.add_member([fair, low])
    rel_pitch_run.add_member([fair, avg])
    rel_pitch_run.add_member([fair, high])
    rel_pitch_run.add_member([rough, low])
    rel_pitch_run.add_member([rough, avg])
    rel_pitch_run.add_member([rough, high])

    print("Relation Pitch -> Run")
    print(rel_pitch_run)

    # calculate membership functional values
    deg_strength_speed_pitch = compute_relational_matrix(rel_speed_pitch,
                                                         set_speed, set_pitch)
    deg_strength_pitch_run = compute_relational_matrix(rel_pitch_run,
                                                       set_pitch, set_run)

    print("Functional Value for Relation Speed -> Pitch")
    print(deg_strength_speed_pitch, end="\n\n")

    print("Functional Value for Relation Pitch -> Run")
    print(deg_strength_pitch_run, end="\n\n")

    # calculate MAX-MIN composition values
    max_min_result = max_min(deg_strength_speed_pitch, deg_strength_pitch_run)

    print("Resultant Functional Value for Relation Speed -> Run")
    print("    based on Relation Speed -> Pitch, Pitch -> Run")
    print("    using MAX-MIN composition algorithm")
    print(max_min_result, end="\n\n")

    # calculate MAX-Product composition values
    max_prod = max_product(deg_strength_speed_pitch, deg_strength_pitch_run)

    print("Resultant Functional Value for Relation Speed -> Run")
    print("    based on Relation Speed -> Pitch, Pitch -> Run")
    print("    using MAX-Product composition algorithm")
    print(max_prod, end="\n\n")


if __name__ == "__main__":
    main()
    print("DONE.")
