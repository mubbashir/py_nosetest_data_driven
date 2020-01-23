def test_dirs():
    for data in test_data():
        yield check_dir, data[0], data[1]

def check_dir(dir_ref, dir_new_gen):
    assert len(dir_ref) > 1
    assert len(dir_new_gen) > 1

def test_data():
    return [["dir1_ref", "dir1_gen"], ["dir2_ref", "dir2_gen"]]
