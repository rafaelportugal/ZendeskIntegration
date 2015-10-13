from zendesk.helper import separete_into_groups
from random import random


def test_separate_into_groups_with_size_default():
    list_objs = [x for x in range(1000)]
    groups = separete_into_groups(list_objs)
    for group in groups:
        assert len(group) == 100
    assert len(groups) == 10


def test_separate_into_groups_with_size_dinamic():
    list_objs = [x for x in range(1000)]
    number_per_group = int(random()*100)
    groups = separete_into_groups(list_objs, size_group=number_per_group)
    rest = len(list_objs) % number_per_group
    if rest != 0:
        group = groups.pop(-1)
        assert len(group) == rest
    for group in groups:
        assert len(group) == number_per_group
    assert len(groups) == len(list_objs) / number_per_group
