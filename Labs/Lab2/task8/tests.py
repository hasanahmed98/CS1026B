from test_helper import run_common_tests, failed, passed, get_answer_placeholders, test_is_not_empty, \
    test_answer_placeholders_text_deleted


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[0]
    if placeholder == "":  # TODO: your condition here
        passed()
    else:
        failed()


if __name__ == '__main__':
    test_is_not_empty()
    test_answer_placeholders_text_deleted()
    # test_answer_placeholders()       # TODO: uncomment test call
